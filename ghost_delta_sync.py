#!/usr/bin/env python3
"""
Ghost → SkillCMS Delta Sync
============================
Vergleicht die aktuell in Ghost publizierten Posts/Pages mit dem SkillCMS-Repo
und synchronisiert neue oder geänderte Inhalte.

Was das Skript tut:
  1. Alle publizierten Ghost-Posts/Pages per Admin API laden
  2. Slugs mit vorhandenen articles/ und pages/ vergleichen
  3. NEUE Items: exportieren → articles/ oder pages/
  4. GEÄNDERTE Items (--update-existing): neu exportieren → überschreiben
  5. DRAFTS bereinigen: wenn ein Slug in drafts/ liegt und jetzt published ist,
     wird der Draft gelöscht
  6. Neue Bilder lokal spiegeln (assets/images/)
  7. Optionaler Git-Commit + Push

Voraussetzungen:
  pip install requests markdownify pyyaml --break-system-packages

Konfiguration (Umgebungsvariablen oder direkt hier eintragen):
  GHOST_API_URL   = https://write.visales.de
  GHOST_ADMIN_KEY = <id>:<secret>

Aufruf:
  python3 ghost_delta_sync.py                   # Dry-run (zeigt was passieren würde)
  python3 ghost_delta_sync.py --apply            # Wendet Änderungen an
  python3 ghost_delta_sync.py --apply --commit   # + Git-Commit
  python3 ghost_delta_sync.py --apply --commit --push  # + Git-Push
  python3 ghost_delta_sync.py --apply --update-existing  # Auch geänderte überschreiben
  python3 ghost_delta_sync.py --pages            # Auch Pages synchronisieren (default: nur Posts)
"""

import os
import sys
import re
import time
import hmac
import hashlib
import json
import struct
import base64
import shutil
import argparse
import subprocess
from pathlib import Path
from datetime import datetime, timezone
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Konfiguration — hier oder per Umgebungsvariable
# ---------------------------------------------------------------------------
GHOST_API_URL   = os.environ.get("GHOST_API_URL",   "https://write.visales.de")
GHOST_ADMIN_KEY = os.environ.get("GHOST_ADMIN_KEY", "")   # id:secret

# Pfade (relativ zu diesem Skript)
SCRIPT_DIR   = Path(__file__).parent
ARTICLES_DIR = SCRIPT_DIR / "site" / "content" / "articles"
PAGES_DIR    = SCRIPT_DIR / "site" / "content" / "pages"
DRAFTS_DIR   = SCRIPT_DIR / "site" / "content" / "drafts"
ASSETS_DIR   = SCRIPT_DIR / "site" / "assets" / "images"

# ---------------------------------------------------------------------------
# JWT-Erzeugung für Ghost Admin API
# ---------------------------------------------------------------------------

def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

def make_ghost_jwt(admin_key: str) -> str:
    """Erzeugt ein kurzlebiges JWT für die Ghost Admin API."""
    key_id, secret = admin_key.split(":", 1)
    header  = _b64url(json.dumps({"alg": "HS256", "typ": "JWT", "kid": key_id}).encode())
    now     = int(time.time())
    payload = _b64url(json.dumps({"iat": now, "exp": now + 300, "aud": "/admin/"}).encode())
    signing = f"{header}.{payload}"
    secret_bytes = bytes.fromhex(secret)
    sig = _b64url(hmac.new(secret_bytes, signing.encode(), hashlib.sha256).digest())
    return f"{signing}.{sig}"

# ---------------------------------------------------------------------------
# Ghost API-Abruf
# ---------------------------------------------------------------------------

def ghost_get(path: str, params: dict = None) -> dict:
    """GET-Request gegen Ghost Admin API, gibt geparsten JSON zurück."""
    token = make_ghost_jwt(GHOST_ADMIN_KEY)
    url = f"{GHOST_API_URL.rstrip('/')}/ghost/api/admin/{path.lstrip('/')}"
    if params:
        qs = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{qs}"
    req = urllib.request.Request(url, headers={"Authorization": f"Ghost {token}"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def fetch_all_published(resource: str) -> list:
    """
    Lädt alle publizierten Posts oder Pages (resource = 'posts' | 'pages').
    Paginiert automatisch durch alle Seiten.
    """
    items = []
    page  = 1
    limit = 100
    include = "tags,authors"
    while True:
        data = ghost_get(
            resource,
            params={
                "limit":   limit,
                "page":    page,
                "filter":  "status:published",
                "include": include,
                "fields":  "id,slug,title,status,published_at,updated_at,lexical,html,"
                           "meta_title,meta_description,custom_excerpt,feature_image,"
                           "og_image,primary_tag,tags,authors,type",
            },
        )
        batch = data.get(resource, [])
        items.extend(batch)
        meta = data.get("meta", {}).get("pagination", {})
        if page >= meta.get("pages", 1):
            break
        page += 1
    return items

# ---------------------------------------------------------------------------
# Lokalen Slug-Index aufbauen
# ---------------------------------------------------------------------------

def slug_from_filename(path: Path) -> str:
    return path.stem  # Dateiname ohne .md

def build_local_index(directory: Path) -> dict:
    """slug → Path für alle .md-Dateien in einem Verzeichnis."""
    if not directory.exists():
        return {}
    return {slug_from_filename(p): p for p in directory.glob("*.md")}

# ---------------------------------------------------------------------------
# Bild-Download (analog Full-Exporter)
# ---------------------------------------------------------------------------

def _image_local_path(url: str, assets_dir: Path) -> tuple:
    """
    Gibt (local_path, relative_path_for_md) zurück.
    Ghost-URLs wie https://write.visales.de/content/images/2025/10/foto.jpg
    → assets/images/2025/10/foto.jpg
    """
    if not url or not url.startswith("http"):
        return None, url

    # Pfad nach /content/images/ extrahieren
    match = re.search(r"/content/images/(.+)$", url)
    if match:
        rel = match.group(1)
        local = assets_dir / rel
        md_path = f"/assets/images/{rel}"
    else:
        # Fallback: nur Dateiname
        name = url.split("/")[-1].split("?")[0]
        local = assets_dir / name
        md_path = f"/assets/images/{name}"

    return local, md_path

def download_image(url: str, local_path: Path, dry_run: bool = False) -> bool:
    if local_path.exists():
        return False  # Bereits vorhanden
    if dry_run:
        print(f"    [DRY] Bild würde heruntergeladen: {url} → {local_path}")
        return True
    local_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            local_path.write_bytes(resp.read())
        return True
    except Exception as e:
        print(f"    ⚠️  Bild-Download fehlgeschlagen: {url} — {e}")
        return False

# ---------------------------------------------------------------------------
# Post → Markdown (importiert ghost_exporter aus gleichem Verzeichnis)
# ---------------------------------------------------------------------------

# ghost_exporter.py liegt im Sessions-Temp-Ordner — wir importieren es von dort.
# Damit das Skript auch standalone aus dem SkillCMS-Ordner aufrufbar ist,
# suchen wir es an mehreren Stellen.

def _find_and_import_exporter():
    """Sucht ghost_exporter.py und gibt das Modul zurück."""
    candidates = [
        Path(__file__).parent / "ghost_exporter.py",
        Path.home() / "ghost_exporter.py",
        Path("/sessions/determined-serene-johnson/ghost_exporter.py"),
    ]
    for p in candidates:
        if p.exists():
            import importlib.util
            spec = importlib.util.spec_from_file_location("ghost_exporter", p)
            mod  = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
    raise FileNotFoundError(
        "ghost_exporter.py nicht gefunden.\n"
        "Bitte in dasselbe Verzeichnis wie dieses Skript kopieren."
    )

def post_to_markdown(post: dict, exporter) -> str:
    """Konvertiert Ghost-Post-JSON in Markdown-String via ghost_exporter."""
    return exporter.page_to_markdown(post)

# ---------------------------------------------------------------------------
# Bildpfade im Markdown ersetzen
# ---------------------------------------------------------------------------

def rewrite_image_paths(md_text: str, post: dict, assets_dir: Path, dry_run: bool) -> str:
    """
    Findet alle Ghost-Image-URLs im Markdown und ersetzt sie durch lokale Pfade.
    Lädt Bilder herunter (außer bei dry_run).
    """
    ghost_base = GHOST_API_URL.rstrip("/")

    def replace_url(url: str) -> str:
        if not url:
            return url
        full_url = url if url.startswith("http") else f"{ghost_base}{url}"
        local, md_path = _image_local_path(full_url, assets_dir)
        if local:
            download_image(full_url, local, dry_run=dry_run)
            return md_path
        return url

    # Feature image in Frontmatter
    fi = post.get("feature_image", "")
    if fi:
        new_fi = replace_url(fi)
        md_text = md_text.replace(fi, new_fi, 1)

    # Bilder im Body (Markdown-Syntax ![alt](url) und HTML src="url")
    def replace_md_img(m):
        return f"![{m.group(1)}]({replace_url(m.group(2))})"

    def replace_html_src(m):
        return f'src="{replace_url(m.group(1))}"'

    md_text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_md_img, md_text)
    md_text = re.sub(r'src="(https?://[^"]+)"', replace_html_src, md_text)

    return md_text

# ---------------------------------------------------------------------------
# Git-Operationen
# ---------------------------------------------------------------------------

def git_run(args: list, cwd: Path) -> bool:
    result = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ⚠️  git {' '.join(args)}: {result.stderr.strip()}")
        return False
    return True

def git_commit_and_push(repo_dir: Path, message: str, push: bool = False) -> None:
    print("\n📦 Git-Commit …")
    git_run(["add", "-A"], cwd=repo_dir)
    git_run(["commit", "-m", message], cwd=repo_dir)
    if push:
        print("🚀 Git-Push …")
        git_run(["push"], cwd=repo_dir)

# ---------------------------------------------------------------------------
# Hauptlogik
# ---------------------------------------------------------------------------

def run_delta_sync(
    include_pages: bool     = False,
    dry_run: bool           = True,
    update_existing: bool   = False,
    do_commit: bool         = False,
    do_push: bool           = False,
) -> None:
    if not GHOST_ADMIN_KEY:
        print("❌ GHOST_ADMIN_KEY nicht gesetzt.")
        print("   export GHOST_ADMIN_KEY='id:secret'")
        sys.exit(1)

    # Exporter laden
    exporter = _find_and_import_exporter()

    print(f"\n{'🔍 DRY-RUN' if dry_run else '🚀 APPLY'} — Ghost Delta Sync")
    print(f"   Ghost: {GHOST_API_URL}")
    print(f"   Repo:  {SCRIPT_DIR}")
    print(f"   Pages: {'ja' if include_pages else 'nein (nur Posts)'}")
    print(f"   Update bestehende: {'ja' if update_existing else 'nein'}")
    print()

    # Lokale Indizes
    local_articles = build_local_index(ARTICLES_DIR)
    local_pages    = build_local_index(PAGES_DIR)
    local_drafts   = build_local_index(DRAFTS_DIR)

    print(f"📂 Lokal: {len(local_articles)} Artikel, {len(local_pages)} Pages, {len(local_drafts)} Drafts\n")

    # Ghost-Daten laden
    print("⬇️  Lade Ghost-Posts …")
    ghost_posts = fetch_all_published("posts")
    print(f"   → {len(ghost_posts)} publizierte Posts in Ghost")

    ghost_pages = []
    if include_pages:
        print("⬇️  Lade Ghost-Pages …")
        ghost_pages = fetch_all_published("pages")
        print(f"   → {len(ghost_pages)} publizierte Pages in Ghost")

    print()

    # Auswertung
    stats = {
        "new_articles": [],
        "updated_articles": [],
        "draft_removed": [],
        "new_pages": [],
        "updated_pages": [],
        "images_downloaded": 0,
    }

    # --- Posts ---
    for post in ghost_posts:
        slug = post.get("slug", "")
        if not slug:
            continue

        is_new     = slug not in local_articles
        is_changed = not is_new and update_existing

        if not is_new and not is_changed:
            # Bereits vorhanden, kein Update gewünscht
            continue

        label = "NEU" if is_new else "UPDATE"
        print(f"  [{label}] {slug}")

        if not dry_run:
            md = post_to_markdown(post, exporter)
            md = rewrite_image_paths(md, post, ASSETS_DIR, dry_run=False)
            out_path = ARTICLES_DIR / f"{slug}.md"
            out_path.write_text(md, encoding="utf-8")

        if is_new:
            stats["new_articles"].append(slug)
        else:
            stats["updated_articles"].append(slug)

        # Draft bereinigen?
        if slug in local_drafts:
            draft_path = local_drafts[slug]
            print(f"    🗑️  Draft löschen: {draft_path.name}")
            if not dry_run:
                draft_path.unlink()
            stats["draft_removed"].append(slug)

    # --- Pages ---
    for page in ghost_pages:
        slug = page.get("slug", "")
        if not slug:
            continue

        is_new     = slug not in local_pages
        is_changed = not is_new and update_existing

        if not is_new and not is_changed:
            continue

        label = "NEU" if is_new else "UPDATE"
        print(f"  [{label}][PAGE] {slug}")

        if not dry_run:
            md = post_to_markdown(page, exporter)
            md = rewrite_image_paths(md, page, ASSETS_DIR, dry_run=False)
            out_path = PAGES_DIR / f"{slug}.md"
            out_path.write_text(md, encoding="utf-8")

        if is_new:
            stats["new_pages"].append(slug)
        else:
            stats["updated_pages"].append(slug)

        # Draft bereinigen (Pages können auch als Draft vorliegen)
        if slug in local_drafts:
            draft_path = local_drafts[slug]
            print(f"    🗑️  Draft löschen: {draft_path.name}")
            if not dry_run:
                draft_path.unlink()
            stats["draft_removed"].append(slug)

    # --- Zusammenfassung ---
    print()
    print("=" * 60)
    print(f"✅ Neue Artikel:         {len(stats['new_articles'])}")
    if stats["new_articles"]:
        for s in stats["new_articles"]:
            print(f"   + {s}")
    print(f"✏️  Geänderte Artikel:    {len(stats['updated_articles'])}")
    if stats["updated_articles"]:
        for s in stats["updated_articles"]:
            print(f"   ~ {s}")
    print(f"📄 Neue Pages:           {len(stats['new_pages'])}")
    if stats["new_pages"]:
        for s in stats["new_pages"]:
            print(f"   + {s}")
    print(f"🗑️  Drafts entfernt:      {len(stats['draft_removed'])}")
    if stats["draft_removed"]:
        for s in stats["draft_removed"]:
            print(f"   - {s}")
    print("=" * 60)

    total_changes = (
        len(stats["new_articles"])
        + len(stats["updated_articles"])
        + len(stats["new_pages"])
        + len(stats["draft_removed"])
    )

    if dry_run:
        print("\n⚠️  DRY-RUN — keine Dateien wurden verändert.")
        print("   Für echte Ausführung: --apply")
        return

    if total_changes == 0:
        print("\n✅ Alles aktuell — keine Änderungen nötig.")
        return

    # Git
    if do_commit:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        msg = f"[delta-sync] {now} — +{len(stats['new_articles'])+len(stats['new_pages'])} neu, ~{len(stats['updated_articles'])} aktualisiert, -{len(stats['draft_removed'])} Drafts"
        git_commit_and_push(SCRIPT_DIR, msg, push=do_push)
    else:
        print("\nℹ️  Dateien geändert. Für Git-Commit: --commit")

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ghost → SkillCMS Delta Sync",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Änderungen wirklich anwenden (Standard: Dry-run)",
    )
    parser.add_argument(
        "--update-existing",
        action="store_true",
        help="Auch bereits vorhandene Artikel/Pages neu exportieren (überschreiben)",
    )
    parser.add_argument(
        "--pages",
        action="store_true",
        help="Pages zusätzlich synchronisieren (Standard: nur Posts)",
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        help="Nach dem Sync einen Git-Commit erstellen",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Nach dem Commit auch pushen (impliziert --commit)",
    )
    parser.add_argument(
        "--ghost-url",
        default=None,
        help="Ghost API URL überschreiben (z.B. https://write.visales.de)",
    )
    parser.add_argument(
        "--key",
        default=None,
        help="Ghost Admin API Key überschreiben (id:secret)",
    )

    args = parser.parse_args()

    if args.ghost_url:
        GHOST_API_URL = args.ghost_url
    if args.key:
        GHOST_ADMIN_KEY = args.key
    if args.push:
        args.commit = True

    run_delta_sync(
        include_pages=args.pages,
        dry_run=not args.apply,
        update_existing=args.update_existing,
        do_commit=args.commit,
        do_push=args.push,
    )
