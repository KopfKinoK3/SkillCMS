# SkillCMS — Claude Instructions

## Build

```bash
cd ~/Documents/Claude/Software_Dev/SkillCMS/site
python3 build.py
```

Output landet direkt in `site/` (gleicher Ordner). Danach committen und pushen:

```bash
git add -A && git commit -m "Beschreibung" && git push
```

GitHub Pages deployed automatisch von `main` — URL: https://kopfkinok3.github.io/SkillCMS/

---

## ⚠️ Kritische Regeln für alle Chats

### Wer was anfassen darf

| Was | Datei | Wann anfassen |
|-----|-------|---------------|
| Footer-Struktur, Spalten, Links | **`site/site.yaml`** → `footer:` | Für alle Inhaltsänderungen |
| Footer-Design, CSS, HTML-Logik | **`site/build.py`** → `build_footer_html()` | Nur wenn Layout-Änderung nötig |
| Cookie-Banner | **`site/build.py`** → `build_cookie_banner()` | Nur wenn Banner-Änderung nötig |
| Globale Config (Farben, Nav, Schema) | **`site/site.yaml`** | Für Config-Änderungen |
| Seiteninhalte | `site/content/**/*.md` | Immer ok |

### Niemals ohne Lesen anfassen

**`site/build.py`** ist die Masterdatei für das gesamte Template. Vor jeder Änderung:
1. Relevante Funktion lesen (`build_footer_html`, `build_cookie_banner`, `build_page`)
2. Keine Abschnitte löschen ohne zu prüfen ob sie aktiv genutzt werden
3. Immer komplett neu bauen (`python3 build.py`) und prüfen bevor commit

### Footer-Architektur (5 Spalten)

Konfiguration in `site.yaml` unter `footer.columns`:
1. **Kontakt** (`type: contact`) — Adresse, Button, E-Mail, Tel + KI & Daten sub
2. **Visual Sales** (`type: links`) — Leistungen + Strategie sub
3. **Immersive Sales** (`type: links`) — AR/VR Leistungen
4. **Strategie** (`type: links`) — Beratung, Produkte sub, Feeds & Social sub
5. **Newsletter** (`type: newsletter`) — Teaser + Anmeldung

Sub-Sektionen werden über Felder in `site.yaml` gesteuert:
- `ki_items` / `ki_title` — KI & Daten Sektion
- `products` / `products_url` / `products_title` — Produkte Sektion
- `feeds_items` / `feeds_title` — Feeds & Social Sektion

---

## Projekt-Struktur

```
site/
  build.py              # Build-Script — HTML-Template, CSS, JS, Footer-Logik
  site.yaml             # Globale Konfiguration, Schema.org, Navigation, Footer
  content/
    pages/              # Statische Seiten (kontakt, praxis, über-uns …)
    ki/                 # Grounding Pages für KI-Crawler (Entity-Seiten)
    posts/              # Blog-Posts (Dateiname: YYYY-MM-DD-slug.md)
  assets/
    css/screen.css      # Ghost-Theme Basis-CSS (nicht editieren)
    js/source.js        # Ghost-Theme Basis-JS (nicht editieren)
  *.html                # Build-Output (nicht committen — von build.py erzeugt)
```

---

## Frontmatter-Felder

| Feld | Bedeutung |
|---|---|
| `type: grounding` | Erzeugt AboutPage JSON-LD statt WebPage |
| `grounding_entity: organization\|person` | Welche Entität in mainEntity |
| `faq:` | Liste `[{q: "...", a: "..."}]` → FAQPage JSON-LD |
| `status: published` | Pflicht damit Seite gebaut wird |

---

## Grounding Pages (KI & Daten)

- `/visales-gmbh-grounding/` — Entitätsseite viSales GmbH
- `/gerhard-schroeder-grounding/` — Entitätsseite Gerhard Schröder
- `/llms.txt` — Maschinenlesbare Sitemap für KI-Crawler
- Notebook LLM: https://notebooklm.google.com/notebook/8214e4ca-dd3d-4420-9cc5-be74370ea3ed

---

## Wichtige Hinweise

- **API-Keys (Brevo etc.) NICHT in `site.yaml`** — GitHub Push Protection blockt den Push
- Stabiler lokaler Pfad: `~/Documents/Claude/Software_Dev/SkillCMS`
- Bei Konflikten zwischen Chats: `git pull` vor jeder Arbeitssitzung
- HTML-Dateien in `site/` sind Build-Output — die Quelle sind immer `.md` + `build.py` + `site.yaml`
