#!/usr/bin/env python3
"""
SkillCMS Build Script
=====================
Liest Markdown-Dateien aus content/, rendert sie zu HTML
und injiziert sie in das page-Template.

Konfiguration: site.yaml (im selben Verzeichnis)

Usage:
    python3 build.py                    # Baut alle published Seiten
    python3 build.py kontakt            # Baut nur kontakt.html
    python3 build.py --include-drafts   # Baut alle inkl. Entwürfe
    python3 build.py --drafts-only      # Nur Entwürfe bauen (Preview)

Generierte Dateien (bei build_all):
    sitemap.xml   — alle published Seiten
    robots.txt    — Suchmaschinen-Direktiven

Struktur:
    content/kontakt.md     →  kontakt.html
    content/posts/*.md     →  posts/*.html  (zukünftig)
"""

import os
import sys
import re
import json
import time
import threading
import subprocess
import http.server
import socketserver
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Pfade
# ---------------------------------------------------------------------------
SITE_DIR     = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR  = os.path.join(SITE_DIR, "content")
CONFIG_PATH  = os.path.join(SITE_DIR, "site.yaml")
OUTPUT_DIR   = SITE_DIR   # HTML-Dateien landen im site/-Root


# ---------------------------------------------------------------------------
# Abhängigkeiten sicherstellen
# ---------------------------------------------------------------------------
def ensure_deps():
    """Installiert markdown + PyYAML falls nötig."""
    missing = []
    try:
        import markdown  # noqa
    except ImportError:
        missing.append("markdown")
    try:
        import yaml  # noqa
    except ImportError:
        missing.append("PyYAML")

    if missing:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--break-system-packages", "-q"] + missing
        )

ensure_deps()

import markdown as md_lib   # noqa: E402
import yaml                  # noqa: E402


# ---------------------------------------------------------------------------
# Site-Config laden
# ---------------------------------------------------------------------------
def load_config():
    """Liest site.yaml und gibt das Config-Dict zurück."""
    if not os.path.exists(CONFIG_PATH):
        print(f"  ⚠  site.yaml nicht gefunden ({CONFIG_PATH})")
        return {}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

CONFIG = load_config()


def cfg(*keys, default=""):
    """Greift sicher auf verschachtelte Config-Werte zu."""
    val = CONFIG
    for k in keys:
        if not isinstance(val, dict):
            return default
        val = val.get(k, default)
    return val if val is not None else default


# ---------------------------------------------------------------------------
# Frontmatter-Parsing
# ---------------------------------------------------------------------------
def parse_frontmatter(text):
    """Extrahiert YAML-artiges Frontmatter aus Markdown."""
    meta = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    meta[key.strip()] = val.strip().strip('"').strip("'")
            text = parts[2]
    return meta, text.strip()


# ---------------------------------------------------------------------------
# Toggle-Card Konvertierung
# ---------------------------------------------------------------------------
TOGGLE_ICON_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2.5" stroke-linecap="round" '
    'stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>'
)


def convert_toggles(html):
    """Wandelt <details><summary>...</summary>...</details> in Ghost kg-toggle-card um."""
    def replace_toggle(match):
        summary_text = match.group(1).strip()
        summary_text = re.sub(r'</?(?:strong|em)>', '', summary_text)
        content_raw = match.group(2).strip()
        # Markdown inside <details> is not processed by the main md pass → do it here
        content_inner = md_lib.markdown(
            content_raw,
            extensions=["extra", "meta", "smarty"],
            output_format="html5",
        )
        return (
            f'<div class="kg-card kg-toggle-card" data-kg-toggle-state="close">\n'
            f'  <div class="kg-toggle-heading">\n'
            f'    <button class="kg-toggle-card-icon" aria-label="Inhalt einblenden">{TOGGLE_ICON_SVG}</button>\n'
            f'    <h4 class="kg-toggle-heading-text">{summary_text}</h4>\n'
            f'  </div>\n'
            f'  <div class="kg-toggle-content">\n'
            f'    {content_inner}\n'
            f'  </div>\n'
            f'</div>'
        )

    return re.sub(
        r'<details>\s*<summary>(.*?)</summary>(.*?)</details>',
        replace_toggle,
        html,
        flags=re.DOTALL,
    )


# ---------------------------------------------------------------------------
# Markdown → HTML
# ---------------------------------------------------------------------------
def md_to_html(md_text):
    """Konvertiert Markdown zu HTML (Spacer, Blockquote-Flatten, Toggles)."""
    # Spacer-Divs einfügen (Doppel-/Dreifach-Leerzeilen)
    lines = md_text.split('\n')
    protected = []
    in_blockquote = False
    for line in lines:
        if line.startswith('>'):
            in_blockquote = True
        elif in_blockquote and line.strip() == '':
            in_blockquote = False
        protected.append(line)
    md_text = '\n'.join(protected)

    md_text = re.sub(r'\n{4,}', '\n\n<div class="vs-spacer-lg"></div>\n\n', md_text)
    md_text = re.sub(r'\n{3}',  '\n\n<div class="vs-spacer"></div>\n\n',    md_text)

    html = md_lib.markdown(
        md_text,
        extensions=["extra", "meta", "smarty"],
        output_format="html5",
    )

    # Blockquotes wie Ghost: <p>-Tags → inline mit <br><br>
    def flatten_blockquote(match):
        inner = match.group(1)
        inner = re.sub(r'<p>(.*?)</p>', r'\1<br><br>', inner, flags=re.DOTALL)
        inner = re.sub(r'(<br>\s*)+$', '', inner.strip())
        inner = re.sub(r'\n', '<br>\n', inner)
        inner = re.sub(r'(<br>\s*){3,}', '<br><br>\n', inner)
        return f'<blockquote>\n{inner}\n</blockquote>'

    html = re.sub(
        r'<blockquote>\s*(.*?)\s*</blockquote>',
        flatten_blockquote,
        html,
        flags=re.DOTALL,
    )

    html = convert_toggles(html)
    return html


# ---------------------------------------------------------------------------
# Navigation aus Config generieren
# ---------------------------------------------------------------------------
def build_nav_html(active_slug=""):
    """Generiert <li>-Einträge aus site.yaml navigation."""
    nav_items = cfg("navigation", default=[])
    if not nav_items:
        return ""

    items_html = []
    for item in nav_items:
        label = item.get("label", "")
        slug  = item.get("slug", "")
        url   = item.get("url", f"/{slug}/")

        css_class = f"nav-{slug}"
        if slug == active_slug:
            css_class += " nav-current"

        items_html.append(f'<li class="{css_class}"><a href="{url}">{label}</a></li>')

    return "\n                    ".join(items_html)


# ---------------------------------------------------------------------------
# Footer aus Config generieren
# ---------------------------------------------------------------------------
def build_footer_html():
    """Generiert den kompletten Footer aus site.yaml."""

    # Trust Bar
    trust_clients = cfg("trust_clients", default="")
    memberships   = cfg("memberships", default=[])
    membership_links = " &amp; ".join(
        f'<a href="{m["url"]}" target="_blank" rel="noopener">{m["label"]}</a>'
        for m in memberships
    )
    trust_html = ""
    if trust_clients or membership_links:
        trust_html = f"""
            <div class="vs-footer-trust">
                {trust_clients}
                <span class="vs-footer-trust-sep">—</span>
                Mitglied der {membership_links}
            </div>"""

    # Spalten
    columns     = cfg("footer", "columns", default=[])
    contact_cfg = cfg("contact", default={})
    social_cfg  = cfg("social", default={})
    cols_html   = []

    for col in columns:
        col_type = col.get("type", "links")
        title    = col.get("title", "")
        h4       = f'<h4>{title}</h4>'

        if col_type == "contact":
            contact_links = [
                f'<li><a href="/kontakt/"><strong>Erstgespräch vereinbaren</strong></a></li>',
                f'<li><a href="mailto:{contact_cfg.get("email", "")}">{contact_cfg.get("email", "")}</a></li>',
                f'<li><a href="tel:{contact_cfg.get("phone", "")}">{contact_cfg.get("phone_display", contact_cfg.get("phone", ""))}</a></li>',
            ]
            if social_cfg.get("linkedin"):
                contact_links.append(f'<li><a href="{social_cfg["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a></li>')
            if social_cfg.get("youtube"):
                contact_links.append(f'<li><a href="{social_cfg["youtube"]}" target="_blank" rel="noopener">YouTube</a></li>')
            if social_cfg.get("mastodon"):
                rel = social_cfg.get("mastodon_rel", "me")
                contact_links.append(f'<li><a href="{social_cfg["mastodon"]}" target="_blank" rel="noopener {rel}">Mastodon</a></li>')
            cols_html.append(
                f'<div class="vs-footer-col">{h4}<ul>{"".join(contact_links)}</ul></div>'
            )

        elif col_type == "newsletter":
            teaser      = col.get("teaser", "")
            form_action = col.get("form_action", "#")
            archive_url = col.get("archive_url", "/newsletter/")
            archive_lbl = col.get("archive_label", "Alle Ausgaben →")
            cols_html.append(
                f'<div class="vs-footer-col vs-footer-newsletter">\n'
                f'                    {h4}\n'
                f'                    <p>{teaser}</p>\n'
                f'                    <form class="vs-newsletter-form" action="{form_action}" method="post">\n'
                f'                        <input type="email" placeholder="E-Mail-Adresse" required aria-label="E-Mail-Adresse">\n'
                f'                        <button type="submit" class="gh-button">Anmelden</button>\n'
                f'                    </form>\n'
                f'                    <a href="{archive_url}" class="vs-footer-podcast-link">{archive_lbl}</a>\n'
                f'                </div>'
            )

        else:
            links    = col.get("links", [])
            li_items = "".join(
                f'<li><a href="{lnk["url"]}">{lnk["label"]}</a></li>'
                for lnk in links
            )
            cols_html.append(
                f'<div class="vs-footer-col">{h4}<ul>{li_items}</ul></div>'
            )

    cols_joined = "\n                ".join(cols_html)

    # Bottom Bar
    year    = cfg("site", "copyright_year", default="2026")
    company = cfg("site", "company", default="")
    loc     = cfg("site", "location", default="")
    claim   = cfg("site", "claim", default="")
    legal   = cfg("legal", default=[])
    legal_links = "".join(
        f'<a href="{l["url"]}">{l["label"]}</a>'
        for l in legal
    )

    return f"""
        <footer class="gh-footer gh-outer">
            <div class="gh-footer-inner gh-inner">
                {trust_html}
                <div class="vs-footer-grid">
                    {cols_joined}
                </div>
                <div class="vs-footer-bottom">
                    <div class="vs-footer-copy">
                        &copy; {year} {company} &middot; {loc} &middot; {claim}
                    </div>
                    <div class="vs-footer-legal">
                        {legal_links}
                    </div>
                </div>
            </div>
        </footer>"""


# ---------------------------------------------------------------------------
# CSS (inline im <head>)
# ---------------------------------------------------------------------------
INLINE_CSS = """
        :root {
            --background-color: #ffffff;
            --ghost-accent-color: #f2902a;
        }

        /* Spacers */
        .vs-spacer    { height: 1rem; }
        .vs-spacer-lg { height: 2rem; }
        .gh-content .vs-spacer + *,
        .gh-content .vs-spacer-lg + * { margin-top: 0 !important; }

        /* ===== Navigation — 828px, zweizeilig: Logo+CTA oben, Links unten ===== */
        .gh-navigation-inner {
            max-width: 828px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            flex-wrap: wrap !important;
            justify-content: space-between !important;
        }
        .gh-navigation-brand { order: 1 !important; }
        .gh-navigation-menu {
            order: 3 !important;
            flex: 0 0 100% !important;
            margin-top: 0.3rem;
        }
        .gh-navigation-actions {
            order: 2 !important;
            margin-left: auto !important;
        }
        .vs-nav-cta {
            display: inline-flex;
            align-items: center;
            padding: 0.55em 1.3em;
            background: var(--ghost-accent-color);
            color: #fff !important;
            font-size: 1.4rem;
            font-weight: 700;
            border-radius: 6px;
            text-decoration: none;
            white-space: nowrap;
            transition: background 0.2s ease, opacity 0.2s ease;
        }
        .vs-nav-cta:hover { background: #e07f20; opacity: 1; }

        /* Feature Image — max 828px (720px Textlaufbreite + 15%) */
        .gh-article-image {
            max-width: 828px;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 2.4rem;
        }
        .gh-article-image img {
            border-radius: 6px;
        }
        /* Mindestabstand Feature Image → erster Content-Block */
        .gh-article-image + .gh-content > *:first-child {
            margin-top: 1.6rem;
        }

        /* CTA Button Fix */
        .gh-content a.gh-button {
            color: #fff !important;
            text-decoration: none !important;
        }
        p:has(> .cta-center) { text-align: center; }

        /* ===== 6-Spalten Footer ===== */
        .gh-footer {
            background-color: #fff;
            color: var(--color-secondary-text);
            padding-top: 4rem;
            padding-bottom: 2rem;
            border-top: 1px solid var(--color-border);
        }
        .gh-footer a { color: var(--color-primary-text); }
        .gh-footer a:hover { color: var(--ghost-accent-color); opacity: 1; }

        .vs-footer-trust {
            text-align: center;
            font-size: 1.4rem;
            padding-bottom: 2.5rem;
            margin-bottom: 2.5rem;
            border-bottom: 1px solid var(--color-border);
            color: var(--color-secondary-text);
        }
        .vs-footer-trust a { color: var(--ghost-accent-color); }
        .vs-footer-trust-sep { margin: 0 0.6em; }

        .vs-footer-grid {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 2rem;
            padding-bottom: 3rem;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--color-border);
        }
        .vs-footer-col h4 {
            color: var(--color-primary-text);
            font-size: 1.5rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1.2em;
        }
        .vs-footer-col ul { list-style: none; padding: 0; margin: 0; }
        .vs-footer-col li { margin-bottom: 0.6em; }
        .vs-footer-col li a { font-size: 1.4rem; color: var(--color-secondary-text); }
        .vs-footer-col li a:hover { color: var(--ghost-accent-color); }
        .vs-footer-col ul li a strong { color: var(--ghost-accent-color); }

        .vs-footer-newsletter p {
            font-size: 1.3rem;
            margin-bottom: 1em;
            color: var(--color-secondary-text);
        }
        .vs-newsletter-form { display: flex; flex-direction: column; gap: 0.6em; }
        .vs-newsletter-form input {
            padding: 0.6em 0.8em;
            border: 1px solid var(--color-border);
            border-radius: 6px;
            background: var(--color-lighter-gray);
            color: var(--color-primary-text);
            font-size: 1.4rem;
        }
        .vs-newsletter-form input::placeholder { color: var(--color-secondary-text); }
        .vs-newsletter-form .gh-button {
            font-size: 1.3rem;
            padding: 0.6em 1em;
            color: #fff !important;
        }
        .vs-footer-podcast-link {
            display: inline-block;
            margin-top: 0.8em;
            font-size: 1.3rem;
            color: var(--ghost-accent-color) !important;
        }

        .vs-footer-bottom {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.3rem;
            color: var(--color-secondary-text);
        }
        .vs-footer-legal { display: flex; gap: 1.5em; }
        .vs-footer-legal a { color: var(--color-secondary-text); font-size: 1.3rem; }
        .vs-footer-copy { max-width: 60%; }

        @media (max-width: 1024px) {
            .vs-footer-grid { grid-template-columns: repeat(3, 1fr); }
        }
        @media (max-width: 640px) {
            .vs-footer-grid { grid-template-columns: 1fr; gap: 2.5rem; }
            .vs-footer-bottom { flex-direction: column; gap: 1em; text-align: center; }
            .vs-footer-copy { max-width: 100%; }
            .vs-footer-trust { font-size: 1.2rem; }
            .vs-footer-trust-sep { display: block; margin: 0.3em 0; }
        }

        /* ===== kg-toggle-card — Pfeil links ===== */
        .kg-toggle-card {
            background: transparent;
            border: 1px solid rgba(124, 139, 154, 0.4);
            border-radius: 4px;
            padding: 1.2em 1.4em;
        }
        .kg-toggle-heading {
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.8em;
            list-style: none;
            user-select: none;
        }
        .kg-toggle-card-icon {
            background: none;
            border: none;
            cursor: pointer;
            padding: 0;
            flex-shrink: 0;
            color: inherit;
            transition: transform 0.25s ease;
            display: flex;
            align-items: center;
        }
        .kg-toggle-card-icon svg { width: 20px; height: 20px; }
        .kg-toggle-card[data-kg-toggle-state="open"] .kg-toggle-card-icon {
            transform: rotate(90deg);
        }
        .kg-toggle-heading-text {
            font-size: 2rem;
            font-weight: 700;
            margin: 0;
            line-height: 1.3;
            font-family: var(--font-sans);
            color: var(--color-primary-text);
        }
        .kg-toggle-content {
            overflow: hidden;
            height: 0;
            transition: height 0.25s ease;
        }
        .kg-toggle-content > *              { margin-top: 1em; }
        .kg-toggle-content > *:first-child  { margin-top: 0.8em; }
        .kg-toggle-content > *:last-child   { margin-bottom: 0.2em; }

        /* ===== Praxis Card Grid ===== */
        .gh-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 4rem 2rem;
        }
        .gh-container.is-grid .gh-feed {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 3rem;
        }
        .gh-card-link {
            text-decoration: none;
            color: inherit;
            display: block;
        }
        .gh-card-link:hover .gh-card-title {
            color: var(--ghost-accent-color);
        }
        .gh-card-image {
            aspect-ratio: 16 / 9;
            overflow: hidden;
            border-radius: 6px;
            margin-bottom: 1.2rem;
            background: var(--color-lighter-gray);
        }
        .gh-card-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.3s ease;
        }
        .gh-card-link:hover .gh-card-image img {
            transform: scale(1.03);
        }
        .gh-card-tag {
            display: block !important;
            color: var(--ghost-accent-color);
            text-transform: uppercase;
            font-size: 1.2rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            margin-bottom: 0.5rem;
        }
        .gh-card-title {
            font-size: 2rem;
            font-weight: 700;
            margin: 0 0 0.8rem;
            line-height: 1.3;
            transition: color 0.2s ease;
        }
        .gh-card-meta {
            display: flex;
            align-items: center;
            gap: 0.5em;
            font-size: 1.3rem;
            color: var(--color-secondary-text);
            margin-top: 0.6rem;
        }
        .gh-card-author::after {
            content: "·";
            margin-left: 0.5em;
        }
        @media (max-width: 640px) {
            .gh-container.is-grid .gh-feed {
                grid-template-columns: 1fr;
                gap: 2rem;
            }
        }
"""


# ---------------------------------------------------------------------------
# JavaScript (inline am Ende des <body>)
# ---------------------------------------------------------------------------
INLINE_JS = """
    // kg-toggle-card interaktiv
    document.querySelectorAll('.kg-toggle-card').forEach(function(card) {
        var heading = card.querySelector('.kg-toggle-heading');
        var content = card.querySelector('.kg-toggle-content');
        if (!heading || !content) return;

        function openToggle() {
            card.setAttribute('data-kg-toggle-state', 'open');
            content.style.height = content.scrollHeight + 'px';
        }
        function closeToggle() {
            card.setAttribute('data-kg-toggle-state', 'close');
            content.style.height = '0';
        }

        heading.addEventListener('click', function() {
            card.getAttribute('data-kg-toggle-state') === 'open'
                ? closeToggle()
                : openToggle();
        });

        heading.setAttribute('tabindex', '0');
        heading.setAttribute('role', 'button');
        heading.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                heading.click();
            }
        });
    });
"""


# ---------------------------------------------------------------------------
# Draft-Banner
# ---------------------------------------------------------------------------
DRAFT_BANNER = """
    <div style="position:fixed;top:0;left:0;right:0;z-index:9999;
                background:#f2902a;color:#fff;text-align:center;
                padding:0.5em 1em;font-weight:700;font-size:1.4rem;
                letter-spacing:0.05em;">
        &#9888; ENTWURF &mdash; nicht ver&ouml;ffentlicht
    </div>
    <div style="height:2.5rem;"></div>"""


# ---------------------------------------------------------------------------
# JSON-LD Schema
# ---------------------------------------------------------------------------
def build_jsonld(meta, is_draft=False):
    """Generiert JSON-LD structured data für Organization + WebPage/Article."""
    if is_draft:
        return ""   # Drafts nicht schema-markieren

    site_url    = cfg("site", "url",     default="https://visales.de").rstrip("/")
    site_title  = cfg("site", "title",   default="viSales")
    description = cfg("site", "description", default="")
    logo        = cfg("site", "logo",    default="assets/images/logo-visales.png")
    email       = cfg("contact", "email", default="")
    phone       = cfg("contact", "phone", default="")
    social_cfg  = cfg("social", default={})
    company     = cfg("site", "company", default="viSales GmbH")
    location    = cfg("site", "location", default="Bochum")

    slug        = meta.get("slug",  "page")
    title       = meta.get("title", site_title)
    page_desc   = meta.get("meta_description", description)
    page_type   = meta.get("type", "page")   # page | leistung | fallbeispiel | post
    date        = meta.get("date",  "")
    og_image    = meta.get("og_image", "")
    canonical   = f"{site_url}/{slug}/"

    # Social-Profile für sameAs
    same_as = []
    for key in ("linkedin", "youtube", "mastodon"):
        url = social_cfg.get(key, "")
        if url:
            same_as.append(url)
    same_as_json = json.dumps(same_as)

    # Organization Schema (auf jeder Seite)
    org_schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": company,
        "url": site_url,
        "logo": f"{site_url}/{logo}",
        "email": email,
        "telephone": phone,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": location,
            "addressCountry": "DE"
        },
        "sameAs": same_as
    }

    # WebPage / Article Schema
    if page_type == "post" and date:
        webpage_schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": page_desc,
            "url": canonical,
            "datePublished": date,
            "author": {
                "@type": "Person",
                "name": meta.get("author", "Gerhard Schröder"),
                "url": f"{site_url}/ueber-uns/"
            },
            "publisher": {
                "@type": "Organization",
                "name": company,
                "logo": {"@type": "ImageObject", "url": f"{site_url}/{logo}"}
            }
        }
        if og_image:
            webpage_schema["image"] = f"{site_url}/{og_image}"
    else:
        webpage_schema = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": title,
            "description": page_desc,
            "url": canonical,
            "isPartOf": {"@type": "WebSite", "name": site_title, "url": site_url}
        }

    org_json     = json.dumps(org_schema,     ensure_ascii=False, indent=2)
    webpage_json = json.dumps(webpage_schema, ensure_ascii=False, indent=2)

    return (
        f'    <script type="application/ld+json">\n{org_json}\n    </script>\n'
        f'    <script type="application/ld+json">\n{webpage_json}\n    </script>'
    )


# ---------------------------------------------------------------------------
# Seite zusammenbauen
# ---------------------------------------------------------------------------
def calc_reading_time(html_text, wpm=200):
    """Schätzt Lesezeit aus HTML-Text (~200 Wörter/Min)."""
    import re as _re
    plain = _re.sub(r'<[^>]+>', ' ', html_text)
    words = len(plain.split())
    minutes = max(1, round(words / wpm))
    return minutes


def format_date_de(date_str):
    """Formatiert ISO-Datum → '05 Apr. 2026'."""
    months = ["Jan.","Feb.","Mär.","Apr.","Mai","Jun.",
              "Jul.","Aug.","Sep.","Okt.","Nov.","Dez."]
    try:
        parts = str(date_str).split("-")
        d, m, y = int(parts[0][-2:]) if len(parts[0]) > 4 else int(parts[2]), int(parts[1]), int(parts[0][:4])
        # Handle YYYY-MM-DD
        if len(parts) == 3 and len(parts[0]) == 4:
            y, m, d = int(parts[0]), int(parts[1]), int(parts[2][:2])
        return f"{d:02d} {months[m-1]} {y}"
    except Exception:
        return str(date_str)


def build_post_article_html(meta, content_html, is_draft=False):
    """Baut den <article>-Block für type:post mit Header, Meta, Feature Image."""
    title         = meta.get("title", "")
    primary_tag   = meta.get("primary_tag", "")
    feature_image = meta.get("feature_image", "")
    date_raw      = meta.get("date", "")
    date_str      = str(date_raw).split("T")[0] if date_raw else ""

    # Author from site.yaml
    author_name   = cfg("author", "name",   default="Gerhard Schröder")
    author_url    = cfg("author", "url",    default="/author/gerhard/")
    author_avatar = cfg("author", "avatar", default="")

    date_display  = format_date_de(date_str) if date_str else ""
    reading_time  = calc_reading_time(content_html)
    tag_slug      = primary_tag.lower().replace(" ", "-") if primary_tag else ""
    article_class = f"gh-article post{' tag-' + tag_slug if tag_slug else ''}"

    # Tag label
    tag_html = ""
    if primary_tag:
        tag_html = f'<a class="gh-article-tag" href="/tag/{tag_slug}/">{primary_tag}</a>\n'

    # Author/date meta row
    avatar_html = ""
    if author_avatar:
        avatar_html = f"""<div class="gh-article-author-image instapaper_ignore">
                <a href="{author_url}">
                    <img class="author-profile-image" src="{author_avatar}" alt="{author_name}">
                </a>
            </div>"""

    meta_html = f"""
            <div class="gh-article-meta">
                {avatar_html}
                <div class="gh-article-meta-wrapper">
                    <h4 class="gh-article-author-name"><a href="{author_url}">{author_name}</a></h4>
                    <div class="gh-article-meta-content">
                        <time class="gh-article-meta-date" datetime="{date_str}">{date_display}</time>
                        <span class="gh-article-meta-length">&nbsp;&#8212; {reading_time} min read</span>
                    </div>
                </div>
            </div>"""

    # Feature image
    feature_html = ""
    if feature_image:
        feature_html = f"""
    <figure class="gh-article-image">
        <img src="{feature_image}" alt="{title}">
    </figure>"""

    draft_label = ' <span style="color:#f2902a">[DRAFT]</span>' if is_draft else ""

    return f"""        <article class="{article_class}">
            <header class="gh-article-header gh-canvas">
                {tag_html}<h1 class="gh-article-title is-title">{title}{draft_label}</h1>
                {meta_html}
            </header>
            {feature_html}
            <section class="gh-content gh-canvas is-body">
                {content_html}
            </section>
        </article>"""


def build_page(meta, content_html, is_draft=False):
    """Baut eine komplette HTML-Seite aus Meta + Content + Config."""

    title         = meta.get("title",        cfg("site", "title",       default="viSales"))
    description   = meta.get("meta_description", cfg("site", "description", default=""))
    slug          = meta.get("slug",         "page")
    og_image      = meta.get("og_image",     "")
    feature_image = meta.get("feature_image","")
    page_type     = meta.get("type",         "page")

    site_title  = cfg("site", "title",  default="viSales")
    site_url    = cfg("site", "url",    default="https://visales.de").rstrip("/")
    logo        = cfg("site", "logo",   default="assets/images/logo-visales.png")

    # Relativer Basis-Pfad für Assets — je nach Slug-Tiefe (z.B. "tag/skill-abo" → "../")
    slug_depth = len([p for p in slug.split("/") if p]) - 1
    base       = "../" * max(0, slug_depth)

    canonical    = f"{site_url}/{slug}/"
    # og:image priority: feature_image > og_image > default logo
    og_img_src   = feature_image or og_image
    og_image_url = og_img_src if og_img_src.startswith("http") else (
                   f"{site_url}/{og_img_src}" if og_img_src else f"{site_url}/assets/images/logo-visales.png")
    og_type      = "article" if page_type == "post" else "website"
    robots       = "noindex, nofollow" if is_draft else "index, follow"
    full_title      = f"{title} \u2014 {site_title}" if title != site_title else title

    nav_html     = build_nav_html(active_slug=slug)
    footer_html  = build_footer_html()

    # CTA-Button aus site.yaml nav_cta
    nav_cta_cfg = cfg("nav_cta", default={})
    if nav_cta_cfg and isinstance(nav_cta_cfg, dict):
        cta_label = nav_cta_cfg.get("label", "Kontakt")
        cta_url   = nav_cta_cfg.get("url", "/kontakt/")
        nav_cta_html = f'<a class="vs-nav-cta" href="{cta_url}">{cta_label}</a>'
    else:
        nav_cta_html = ""
    draft_banner = DRAFT_BANNER if is_draft else ""
    jsonld       = build_jsonld(meta, is_draft=is_draft)

    # Article HTML block — post / listing / page template
    if page_type == "post":
        article_html = build_post_article_html(meta, content_html, is_draft)
    elif page_type == "listing":
        # Kein gh-canvas — Card-Grid steuert Breite selbst via gh-container
        article_html = (
            f'        <article class="gh-article">\n'
            f'            <section class="gh-content is-body">\n'
            f'                {content_html}\n'
            f'            </section>\n'
            f'        </article>'
        )
    else:
        draft_label = ' <span style="color:#f2902a">[DRAFT]</span>' if is_draft else ""
        article_html = (
            f'        <article class="gh-article">\n'
            f'            <header class="gh-article-header gh-canvas">\n'
            f'                <h1 class="gh-article-title is-title">{title}{draft_label}</h1>\n'
            f'            </header>\n'
            f'            <section class="gh-content gh-canvas is-body">\n'
            f'                {content_html}\n'
            f'            </section>\n'
            f'        </article>'
        )

    return f"""<!DOCTYPE html>
<html lang="de" class="has-dark-text">
<head>
    <title>{full_title}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <meta name="robots" content="{robots}">
    <link rel="canonical" href="{canonical}">

    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:image" content="{og_image_url}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{og_image_url}">

    <!-- Preload -->
    <link rel="preload" as="style" href="{base}assets/css/screen.css">
    <link rel="preload" as="font" type="font/woff2" href="{base}assets/fonts/atkinson-regular.woff2" crossorigin="anonymous">
    <link rel="preload" as="font" type="font/woff2" href="{base}assets/fonts/atkinson-bold.woff2" crossorigin="anonymous">

    <!-- Fonts -->
    <style>
        @font-face {{
            font-family: "Atkinson Hyperlegible";
            font-style: normal; font-weight: 400; font-display: swap;
            src: url({base}assets/fonts/atkinson-regular.woff2) format("woff2");
        }}
        @font-face {{
            font-family: "Atkinson Hyperlegible";
            font-style: italic; font-weight: 400; font-display: swap;
            src: url({base}assets/fonts/atkinson-italic.woff2) format("woff2");
        }}
        @font-face {{
            font-family: "Atkinson Hyperlegible";
            font-style: normal; font-weight: 700; font-display: swap;
            src: url({base}assets/fonts/atkinson-bold.woff2) format("woff2");
        }}
        @font-face {{
            font-family: "Atkinson Hyperlegible";
            font-style: italic; font-weight: 700; font-display: swap;
            src: url({base}assets/fonts/atkinson-bold-italic.woff2) format("woff2");
        }}
    </style>

    <!-- Theme CSS -->
    <link rel="stylesheet" type="text/css" href="{base}assets/css/screen.css">

    <!-- SkillCMS Custom Styles -->
    <style>{INLINE_CSS}
    </style>

    <!-- Structured Data -->
{jsonld}
</head>
<body class="{'post-template' if page_type == 'post' else 'page-template'} page-{slug} has-sans-title has-sans-body">
{draft_banner}
<div class="gh-viewport">

    <!-- NAVIGATION -->
    <header id="gh-navigation" class="gh-navigation is-left-logo gh-outer">
        <div class="gh-navigation-inner gh-inner">
            <div class="gh-navigation-brand">
                <a class="gh-navigation-logo is-title" href="/">
                    <img src="{base}{logo}" alt="{site_title}">
                </a>
                <button class="gh-burger gh-icon-button" aria-label="Menu">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <nav class="gh-navigation-menu">
                <ul class="nav">
                    {nav_html}
                </ul>
            </nav>
            <div class="gh-navigation-actions">{nav_cta_html}</div>
        </div>
    </header>

    <!-- MAIN CONTENT -->
    <main class="gh-main">
{article_html}
    </main>

    {footer_html}

</div>

<script src="{base}assets/js/source.js"></script>
<script>{INLINE_JS}
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Einzelne Datei bauen (intern — arbeitet mit absolutem Dateipfad)
# ---------------------------------------------------------------------------
def build_file(md_path, include_drafts=False, drafts_only=False):
    """
    Baut eine HTML-Seite aus einem absoluten Markdown-Dateipfad.
    Output-Slug kommt aus dem Frontmatter-Feld 'slug:' (flat URL-Struktur).
    Gibt (True, meta) | (False, {}) | (True, None/skipped) zurück.
    Seiten mit type:listing werden übersprungen — build_praxis_listing() übernimmt.
    """
    if not os.path.exists(md_path):
        print(f"  ✗ {md_path} nicht gefunden")
        return False, {}

    with open(md_path, "r", encoding="utf-8") as f:
        raw = f.read()

    meta, body = parse_frontmatter(raw)

    # Listing-Seiten werden von build_praxis_listing() gebaut, nicht hier
    if meta.get("type", "page").lower() == "listing":
        return True, None

    # Slug aus Frontmatter; Fallback: Dateiname ohne Datum-Präfix und .md
    filename = os.path.splitext(os.path.basename(md_path))[0]
    # Datum-Präfix entfernen (z.B. "2026-04-05-slug" → "slug")
    filename_clean = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename)
    slug = meta.get("slug", filename_clean)

    status   = meta.get("status", "published").lower()
    is_draft = (status == "draft")

    if is_draft and not include_drafts:
        print(f"  ○ {slug}.html übersprungen (Entwurf)")
        return True, None

    if not is_draft and drafts_only:
        return True, None

    content_html = md_to_html(body)
    page_html    = build_page(meta, content_html, is_draft=is_draft)

    out_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html)

    draft_marker = " [ENTWURF]" if is_draft else ""
    rel_path     = os.path.relpath(md_path, SITE_DIR)
    print(f"  ✓ {slug}.html{draft_marker} ← {rel_path} ({len(page_html):,} Bytes)")
    return True, {**meta, "slug": slug}


# ---------------------------------------------------------------------------
# Einzelne Seite bauen (CLI-Interface: nach Slug suchen)
# ---------------------------------------------------------------------------
def build_single(slug, include_drafts=False, drafts_only=False):
    """
    Sucht content/{slug}.md oder content/posts/*{slug}.md und baut die Seite.
    """
    # 1. Direkt in content/
    direct = os.path.join(CONTENT_DIR, f"{slug}.md")
    if os.path.exists(direct):
        return build_file(direct, include_drafts=include_drafts, drafts_only=drafts_only)

    # 2. In content/posts/ (mit optionalem Datum-Präfix)
    posts_dir = os.path.join(CONTENT_DIR, "posts")
    if os.path.isdir(posts_dir):
        for fname in os.listdir(posts_dir):
            if fname.endswith(".md") and slug in fname:
                return build_file(
                    os.path.join(posts_dir, fname),
                    include_drafts=include_drafts,
                    drafts_only=drafts_only,
                )

    print(f"  ✗ Keine Markdown-Datei für '{slug}' gefunden")
    return False, {}


# ---------------------------------------------------------------------------
# rss.xml generieren
# ---------------------------------------------------------------------------
def build_rss():
    """
    Erzeugt rss.xml (RSS 2.0) aus allen published Posts in content/posts/.
    Sortiert nach Datum absteigend. Inkl. Atom self-link und media:content für Feature Images.
    """
    site_url    = cfg("site", "url",         default="https://visales.de").rstrip("/")
    site_title  = cfg("site", "title",       default="viSales")
    site_desc   = cfg("site", "description", default="")
    email       = cfg("contact", "email",    default="")
    author_name = cfg("author",  "name",     default="Gerhard Schröder")
    author_tag  = f"{email} ({author_name})" if email else author_name

    posts_dir = os.path.join(CONTENT_DIR, "posts")
    items     = []

    if os.path.isdir(posts_dir):
        for fname in sorted(os.listdir(posts_dir)):
            if not fname.endswith(".md"):
                continue
            meta = read_post_meta_yaml(os.path.join(posts_dir, fname))
            if str(meta.get("status", "published")).lower() != "published":
                continue

            filename       = os.path.splitext(fname)[0]
            filename_clean = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename)
            slug           = str(meta.get("slug", filename_clean))
            date_raw       = meta.get("date", "")
            date_str       = str(date_raw).split("T")[0] if date_raw else ""
            title          = str(meta.get("title", "")).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            description    = str(meta.get("meta_description", "")).replace("&", "&amp;").replace("<", "&lt;")
            feature_image  = str(meta.get("feature_image", ""))
            link           = f"{site_url}/{slug}/"

            # pubDate im RFC-822-Format: "Sat, 05 Apr 2026 00:00:00 +0000"
            pub_date = ""
            if date_str:
                try:
                    parts   = date_str.split("-")
                    y, m, d = int(parts[0]), int(parts[1]), int(parts[2][:2])
                    dt      = datetime(y, m, d, tzinfo=timezone.utc)
                    pub_date = dt.strftime("%a, %d %b %Y %H:%M:%S +0000")
                except Exception:
                    pub_date = ""

            enclosure_tag = ""
            if feature_image:
                enclosure_tag = f'\n      <enclosure url="{feature_image}" type="image/jpeg" length="0"/>'

            items.append((date_str, (
                f'  <item>\n'
                f'    <title>{title}</title>\n'
                f'    <link>{link}</link>\n'
                f'    <guid isPermaLink="true">{link}</guid>\n'
                f'    <description>{description}</description>\n'
                f'    <pubDate>{pub_date}</pubDate>\n'
                f'    <author>{author_tag}</author>'
                f'{enclosure_tag}\n'
                f'  </item>'
            )))

    # Neueste zuerst
    items.sort(key=lambda x: x[0], reverse=True)
    items_xml = "\n".join(item for _, item in items)

    now_rfc822 = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

    rss = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"\n'
        '  xmlns:atom="http://www.w3.org/2005/Atom"\n'
        '  xmlns:content="http://purl.org/rss/1.0/modules/content/">\n'
        '  <channel>\n'
        f'    <title>{site_title}</title>\n'
        f'    <link>{site_url}/</link>\n'
        f'    <description>{site_desc}</description>\n'
        f'    <language>de</language>\n'
        f'    <lastBuildDate>{now_rfc822}</lastBuildDate>\n'
        f'    <atom:link href="{site_url}/rss.xml" rel="self" type="application/rss+xml"/>\n'
        f'{items_xml}\n'
        '  </channel>\n'
        '</rss>\n'
    )

    out_path = os.path.join(OUTPUT_DIR, "rss.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(rss)

    print(f"  ✓ rss.xml ({len(items)} Item(s))")


# ---------------------------------------------------------------------------
# sitemap.xml generieren
# ---------------------------------------------------------------------------
def build_sitemap(published_pages):
    """
    Erzeugt sitemap.xml aus einer Liste von Dicts mit keys:
        slug, type, date (optional)
    published_pages: nur published, keine Drafts.
    """
    site_url = cfg("site", "url", default="https://visales.de").rstrip("/")
    now      = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Priorität nach Seiten-Typ
    priority_map = {
        "page":        "0.8",
        "leistung":    "0.9",
        "fallbeispiel": "0.7",
        "seo":         "0.6",
        "post":        "0.6",
    }
    changefreq_map = {
        "page":        "monthly",
        "leistung":    "monthly",
        "fallbeispiel": "yearly",
        "seo":         "monthly",
        "post":        "yearly",
    }

    url_blocks = []
    for page in published_pages:
        slug       = page["slug"]
        page_type  = page.get("type", "page")
        lastmod    = page.get("date", "") or now   # Fallback: heutiges Build-Datum
        priority   = priority_map.get(page_type, "0.7")
        changefreq = changefreq_map.get(page_type, "monthly")

        url_blocks.append(
            f"  <url>\n"
            f"    <loc>{site_url}/{slug}/</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            f"    <changefreq>{changefreq}</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            f"  </url>"
        )

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(url_blocks)
        + "\n</urlset>\n"
    )

    out_path = os.path.join(OUTPUT_DIR, "sitemap.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"  ✓ sitemap.xml ({len(url_blocks)} URL(s))")


# ---------------------------------------------------------------------------
# robots.txt generieren
# ---------------------------------------------------------------------------
def build_robots():
    """Erzeugt robots.txt mit Sitemap-Verweis."""
    site_url = cfg("site", "url", default="https://visales.de").rstrip("/")

    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {site_url}/sitemap.xml\n"
    )

    out_path = os.path.join(OUTPUT_DIR, "robots.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("  ✓ robots.txt")


# ---------------------------------------------------------------------------
# Praxis-Listing /praxis/ bauen
# ---------------------------------------------------------------------------
def read_post_meta_yaml(md_path):
    """Liest Frontmatter einer Markdown-Datei via yaml.safe_load (vollständig)."""
    with open(md_path, "r", encoding="utf-8") as f:
        raw = f.read()
    if not raw.startswith("---"):
        return {}
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except Exception:
        return {}


def build_tag_listing(tag_slug):
    """
    Erzeugt tag/{tag_slug}.html — Card-Grid-Übersicht für einen Tag.
    Filtert published Posts nach primary_tag oder tags-Liste.
    Liest optionale Metadata aus content/tags/{tag_slug}.md.
    """
    posts_dir = os.path.join(CONTENT_DIR, "posts")

    # Optionale Tag-Metadata
    tag_md = os.path.join(CONTENT_DIR, "tags", f"{tag_slug}.md")
    if os.path.exists(tag_md):
        tag_meta_file = read_post_meta_yaml(tag_md)
        tag_label       = str(tag_meta_file.get("title", tag_slug.replace("-", " ").title()))
        tag_description = str(tag_meta_file.get("meta_description", ""))
    else:
        tag_label       = tag_slug.replace("-", " ").title()
        tag_description = ""

    # Posts mit diesem Tag sammeln
    post_data = []
    if os.path.isdir(posts_dir):
        for fname in sorted(os.listdir(posts_dir)):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(posts_dir, fname)
            meta  = read_post_meta_yaml(fpath)

            if str(meta.get("status", "published")).lower() != "published":
                continue

            primary_tag = str(meta.get("primary_tag", "")).strip()
            tags_raw    = meta.get("tags", [])
            if isinstance(tags_raw, str):
                tags_list = [t.strip() for t in tags_raw.split(",")]
            elif isinstance(tags_raw, list):
                tags_list = [str(t).strip() for t in tags_raw]
            else:
                tags_list = []

            if primary_tag != tag_slug and tag_slug not in tags_list:
                continue

            filename       = os.path.splitext(fname)[0]
            filename_clean = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename)
            slug           = str(meta.get("slug", filename_clean))
            date_raw       = meta.get("date", "")
            date_str       = str(date_raw).split("T")[0] if date_raw else ""

            post_data.append({
                "slug":          slug,
                "title":         str(meta.get("title", "")),
                "feature_image": str(meta.get("feature_image", "")),
                "primary_tag":   primary_tag,
                "date":          date_str,
            })

    # Neueste zuerst
    post_data.sort(key=lambda p: p.get("date", ""), reverse=True)

    author_name = cfg("author", "name", default="Gerhard Schröder")

    # Cards bauen
    cards_html = []
    for p in post_data:
        post_slug     = p["slug"]
        title         = p["title"]
        feature_image = p["feature_image"]
        pt            = p["primary_tag"]
        date_str      = p["date"]
        date_display  = format_date_de(date_str) if date_str else ""
        pt_slug       = pt.lower().replace(" ", "-") if pt else ""
        pt_label      = pt.upper() if pt else ""
        card_class    = f"gh-card post{' tag-' + pt_slug if pt_slug else ''}"

        img_html = ""
        if feature_image:
            img_html = (
                f'                <figure class="gh-card-image">'
                f'<img src="{feature_image}" alt="{title}" loading="lazy"></figure>\n'
            )

        tag_card_html = ""
        if pt_label:
            tag_card_html = f'                <p class="gh-card-tag">{pt_label}</p>\n'

        cards_html.append(
            f'            <article class="{card_class}">\n'
            f'                <a class="gh-card-link" href="/{post_slug}/">\n'
            f'{img_html}'
            f'{tag_card_html}'
            f'                    <h3 class="gh-card-title is-title">{title}</h3>\n'
            f'                    <footer class="gh-card-meta">\n'
            f'                        <span class="gh-card-author">{author_name}</span>\n'
            f'                        <time class="gh-card-date" datetime="{date_str}">{date_display}</time>\n'
            f'                    </footer>\n'
            f'                </a>\n'
            f'            </article>'
        )

    cards_joined = "\n".join(cards_html)
    content_html = (
        '<div class="gh-container is-grid">\n'
        '    <div class="gh-feed">\n'
        f'{cards_joined}\n'
        '    </div>\n'
        '</div>'
    )

    listing_meta = {
        "title":            tag_label,
        "slug":             f"tag/{tag_slug}",
        "type":             "listing",
        "meta_description": tag_description,
    }

    page_html = build_page(listing_meta, content_html)

    # Output: site/tag/{tag_slug}.html
    tag_dir  = os.path.join(OUTPUT_DIR, "tag")
    os.makedirs(tag_dir, exist_ok=True)
    out_path = os.path.join(tag_dir, f"{tag_slug}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html)

    print(f"  ✓ tag/{tag_slug}.html ({len(post_data)} Post(s), {len(page_html):,} Bytes)")


# ---------------------------------------------------------------------------
# Alle Seiten bauen
# ---------------------------------------------------------------------------
def collect_md_files():
    """Sammelt alle Markdown-Dateien aus content/ und content/posts/."""
    files = []

    # content/*.md (Seiten)
    for fname in sorted(os.listdir(CONTENT_DIR)):
        if fname.endswith(".md"):
            files.append(os.path.join(CONTENT_DIR, fname))

    # content/posts/*.md (Blog-Posts)
    posts_dir = os.path.join(CONTENT_DIR, "posts")
    if os.path.isdir(posts_dir):
        for fname in sorted(os.listdir(posts_dir)):
            if fname.endswith(".md"):
                files.append(os.path.join(posts_dir, fname))

    return files


def build_all(include_drafts=False, drafts_only=False):
    """Baut alle Markdown-Dateien in content/ und content/posts/ + sitemap.xml + robots.txt."""
    all_files = collect_md_files()
    if not all_files:
        print("Keine Markdown-Dateien in content/ gefunden.")
        return

    mode = ""
    if drafts_only:
        mode = " (nur Entwürfe)"
    elif include_drafts:
        mode = " (inkl. Entwürfe)"

    # Seiten vs. Posts für übersichtliche Ausgabe aufteilen
    page_files = [f for f in all_files if "/posts/" not in f]
    post_files = [f for f in all_files if "/posts/" in f]

    total = len(all_files)
    print(f"SkillCMS Build{mode} — {total} Datei(en) ({len(page_files)} Seiten, {len(post_files)} Posts)\n")

    published_pages = []

    if page_files:
        print("── Seiten ──────────────────────────")
        for fpath in page_files:
            ok, meta = build_file(fpath, include_drafts=include_drafts, drafts_only=drafts_only)
            if ok and meta:
                published_pages.append({
                    "slug": meta.get("slug", ""),
                    "type": meta.get("type", "page"),
                    "date": meta.get("date", ""),
                })

    if post_files:
        print("\n── Posts ───────────────────────────")
        for fpath in post_files:
            ok, meta = build_file(fpath, include_drafts=include_drafts, drafts_only=drafts_only)
            if ok and meta:
                published_pages.append({
                    "slug": meta.get("slug", ""),
                    "type": meta.get("type", "post"),
                    "date": meta.get("date", ""),
                })

    # Tag-Listings + sitemap.xml + robots.txt nur beim Full-Build
    if not drafts_only:
        # Alle einzigartigen Tags aus published Posts sammeln
        all_tags = set()
        posts_dir_scan = os.path.join(CONTENT_DIR, "posts")
        if os.path.isdir(posts_dir_scan):
            for fname in os.listdir(posts_dir_scan):
                if not fname.endswith(".md"):
                    continue
                meta = read_post_meta_yaml(os.path.join(posts_dir_scan, fname))
                if str(meta.get("status", "published")).lower() != "published":
                    continue
                pt = str(meta.get("primary_tag", "")).strip()
                if pt:
                    all_tags.add(pt)
                tags_raw = meta.get("tags", [])
                if isinstance(tags_raw, list):
                    for t in tags_raw:
                        ts = str(t).strip()
                        if ts:
                            all_tags.add(ts)
                elif isinstance(tags_raw, str):
                    for t in tags_raw.split(","):
                        ts = t.strip()
                        if ts:
                            all_tags.add(ts)

        if all_tags:
            print(f"\n── Tag-Listings ({len(all_tags)} Tags) ──────────")
            for tag in sorted(all_tags):
                build_tag_listing(tag)

        print()
        build_sitemap(published_pages)
        build_robots()
        build_rss()

    print("\n✓ Fertig.")


# ---------------------------------------------------------------------------
# Phase 6 — DX Tooling: Dev-Server + File-Watcher
# ---------------------------------------------------------------------------
DEV_PORT = 8765


class _SilentHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP-Handler der aus OUTPUT_DIR serviert — ohne Console-Spam."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=OUTPUT_DIR, **kwargs)

    def log_message(self, fmt, *args):  # noqa
        pass  # Stille Logs im Watch-Modus


def run_dev_server(port=DEV_PORT):
    """Startet einen simplen HTTP-Dev-Server in einem Daemon-Thread."""
    with socketserver.TCPServer(("", port), _SilentHandler) as httpd:
        httpd.serve_forever()


def _collect_mtimes():
    """Sammelt mtimes aller .md-Dateien in content/ + site.yaml."""
    mtimes = {}
    for root, _, files in os.walk(CONTENT_DIR):
        for fname in files:
            if fname.endswith(".md"):
                fpath = os.path.join(root, fname)
                mtimes[fpath] = os.path.getmtime(fpath)
    if os.path.exists(CONFIG_PATH):
        mtimes[CONFIG_PATH] = os.path.getmtime(CONFIG_PATH)
    return mtimes


def watch_and_rebuild(port=DEV_PORT, interval=0.8):
    """
    Beobachtet content/ + site.yaml auf Änderungen.
    Bei .md-Änderung: gezielter Einzelbuild + betroffene Tag-Listings.
    Bei site.yaml-Änderung: Full Build.
    """
    last_mtimes = _collect_mtimes()
    print(f"  Watching content/ … Ctrl+C zum Stoppen.\n")

    while True:
        time.sleep(interval)
        current_mtimes = _collect_mtimes()

        changed = [
            fpath for fpath, mtime in current_mtimes.items()
            if fpath not in last_mtimes or last_mtimes[fpath] != mtime
        ] + [
            fpath for fpath in last_mtimes
            if fpath not in current_mtimes   # gelöscht
        ]

        if not changed:
            continue

        last_mtimes = current_mtimes
        labels = [os.path.relpath(f, SITE_DIR) for f in changed]
        print(f"  Geändert: {labels}")

        # site.yaml → Full Build
        if any(f == CONFIG_PATH for f in changed):
            print("  ↺  site.yaml — Full Build …")
            global CONFIG
            CONFIG = load_config()
            build_all(include_drafts=True)
        else:
            for fpath in changed:
                if not fpath.endswith(".md"):
                    continue
                if "/posts/" in fpath:
                    # Post: Einzelbuild + betroffene Tags neu generieren
                    ok, meta = build_file(fpath, include_drafts=True)
                    if ok and meta:
                        pt = str(meta.get("primary_tag", "")).strip()
                        if pt:
                            build_tag_listing(pt)
                        tags_raw = meta.get("tags", [])
                        tag_list = (
                            [str(t).strip() for t in tags_raw]
                            if isinstance(tags_raw, list)
                            else [t.strip() for t in str(tags_raw).split(",")]
                        )
                        for t in tag_list:
                            if t and t != pt:
                                build_tag_listing(t)
                    build_rss()
                else:
                    # Normale Seite
                    build_file(fpath, include_drafts=True)

        print(f"  ✓  http://localhost:{port}/\n")


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    args = sys.argv[1:]

    include_drafts = "--include-drafts" in args
    drafts_only    = "--drafts-only"    in args
    serve_mode     = "--serve"          in args
    watch_mode     = "--watch"          in args

    # Port überschreiben: --port=9000
    port = DEV_PORT
    for a in args:
        if a.startswith("--port="):
            try:
                port = int(a.split("=", 1)[1])
            except ValueError:
                pass

    # Slug-Argumente (alles ohne --Flags)
    slugs = [a for a in args if not a.startswith("--")]

    if serve_mode or watch_mode:
        # Initialer Build (inkl. Drafts für Dev)
        build_all(include_drafts=True)

        if serve_mode:
            t = threading.Thread(target=run_dev_server, args=(port,), daemon=True)
            t.start()
            print(f"\n  Dev-Server: http://localhost:{port}/")

        if watch_mode:
            watch_and_rebuild(port=port)
        else:
            # Nur serve, kein watch → blockieren bis Ctrl+C
            print("  Ctrl+C zum Stoppen.")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n  Server gestoppt.")

    elif slugs:
        for slug in slugs:
            slug = slug.replace(".md", "").replace(".html", "")
            build_single(slug, include_drafts=include_drafts, drafts_only=drafts_only)
    else:
        build_all(include_drafts=include_drafts, drafts_only=drafts_only)
