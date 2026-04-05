# SkillCMS — Entwicklungsplan

> Statischer Site-Generator für visales.de als Ghost-CMS-Ablösung.
> Basiert auf Ghost "Source" Theme v9, Python-Build-Pipeline, Markdown-Content.

---

## Status Quo (Stand: 05.04.2026)

### Was steht

| Feature | Status |
|---|---|
| Markdown → HTML Pipeline | ✅ fertig |
| Frontmatter-Parsing (title, slug, meta_description, template) | ✅ fertig |
| Ghost kg-toggle-card (aus `<details>/<summary>`) | ✅ fertig |
| CTA-Buttons (`.gh-button .cta-center`) | ✅ fertig |
| Spacer-System (Doppel-/Dreifach-Leerzeilen) | ✅ fertig |
| Blockquote-Flattening (Ghost-Stil) | ✅ fertig |
| 6-Spalten Footer (Trust Bar, Newsletter, responsive) | ✅ fertig |
| Ghost Source Theme Assets (CSS, Fonts, JS, Logo) | ✅ fertig |
| Single-Build (`build.py kontakt`) | ✅ fertig |
| Full-Build (`build.py`) | ✅ fertig |
| Testseite: kontakt.html | ✅ verifiziert |

### Bekannte Platzhalter

- Mastodon-URL: `mastodon.social/@visales` — echte URL einsetzen
- Newsletter-Form: `action="#"` — Backend/Endpoint klären
- Navigation: hardcoded in `build_page()` — muss aus Config kommen

---

## Architektur-Entscheidungen

### Flat URL-Struktur
Alle ~42 Seiten liegen auf Root-Level (kein `/leistungen/augmented-reality/`, sondern `/augmented-reality/`). Entspricht der bestehenden Ghost-Sitemap.

### Content-Ordner
```
site/
├── content/
│   ├── kontakt.md              # type: page
│   ├── augmented-reality.md    # type: leistung
│   ├── siemens-ddx.md          # type: fallbeispiel
│   ├── ar-agentur-bochum.md    # type: seo
│   └── posts/
│       ├── 2024-03-15-openusd-einstieg.md
│       └── ...
├── assets/
├── templates/                  # (zukünftig: externe Templates)
├── build.py
├── site.yaml                   # (neu: zentrale Config)
└── *.html                      # generierter Output
```

### Draft-Handling
Frontmatter-Feld `status: draft` (Default: `published`). Build überspringt Drafts. Preview-Modus via `--include-drafts` mit visuellem Banner.

### Frontmatter-Schema (erweitert)
```yaml
---
title: "Augmented Reality für B2B"
slug: augmented-reality
type: leistung                  # page | leistung | fallbeispiel | seo | post
status: published               # published | draft
meta_description: "..."
og_image: assets/images/ar-hero.webp
date: 2024-03-15               # nur für Posts
tags: [openusd, 3d]            # nur für Posts
author: Gerhard Schröder        # nur für Posts
template: page                  # page | post | listing | landing
---
```

---

## Roadmap: Features nach Priorität

### Phase 1 — Config & Grundstruktur
> Ziel: Mehrere Seiten sauber bauen, Navigation zentral steuern.

#### 1.1 Zentrale Site-Config (`site.yaml`)
- Site-Titel, URL-Basis, Beschreibung, Sprache
- Navigations-Einträge (Header-Menü)
- Social-Links, Footer-Inhalte
- Build-Optionen (include_drafts, base_url)

```yaml
# site.yaml
site:
  title: "viSales"
  url: "https://visales.de"
  language: "de"
  description: "B2B-Agentur für visuelle Vertriebskommunikation"

navigation:
  - label: "Leistungen"
    slug: leistungen
  - label: "Fallbeispiele"
    slug: fallbeispiele
  - label: "Praxis"
    slug: praxis
  - label: "Über Uns"
    slug: ueber-uns
  - label: "Kontakt"
    slug: kontakt

build:
  include_drafts: false
  base_url: "/"
```

#### 1.2 Navigation aus Config generieren
- Header-Nav liest `site.yaml` statt hardcoded HTML
- Aktive Seite automatisch via `nav-current` markieren
- Burger-Menü funktioniert weiterhin (Source-Theme JS)

#### 1.3 Draft-Handling implementieren
- `status: draft` in Frontmatter erkennen
- `build.py --include-drafts` Flag
- Draft-Banner: orangefarbener Balken oben "ENTWURF — nicht veröffentlicht"
- `build.py --drafts-only` für schnelle Vorschau

---

### Phase 2 — SEO & Meta
> Ziel: Jede Seite ist suchmaschinenoptimiert und social-sharing-ready.

#### 2.1 Erweiterter `<head>`
- `<title>` mit Site-Name: `{title} — viSales`
- `<meta name="description">`
- `<link rel="canonical" href="{base_url}/{slug}/">`
- `<meta name="robots" content="index, follow">` (bzw. `noindex` für Drafts)

#### 2.2 Open Graph & Twitter Cards
```html
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_description}">
<meta property="og:image" content="{og_image}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
```

#### 2.3 Strukturierte Daten (JSON-LD)
- `Organization` Schema für viSales
- `WebPage` Schema pro Seite
- `Article` Schema für Blog-Posts
- `FAQPage` Schema für Seiten mit Toggle-Cards

#### 2.4 Sitemap.xml generieren
- Alle published Pages + Posts
- `<lastmod>` aus Datei-Änderungsdatum oder Frontmatter
- `<changefreq>` und `<priority>` nach Typ

#### 2.5 robots.txt generieren
```
User-agent: *
Allow: /
Sitemap: https://visales.de/sitemap.xml
```

---

### Phase 3 — Template-System
> Ziel: Unterschiedliche Layouts für Pages, Posts, Listings.

#### 3.1 Template-Varianten
- **page** (Default): Aktuelle Struktur, Titel + Content
- **post**: Datum, Autor, Tags, Lesezeit oben; verwandte Artikel unten
- **listing**: Grid/Liste von Unterseiten (z.B. /leistungen/, /fallbeispiele/)
- **landing**: Kein Artikel-Header, volle Breite, Hero-Bereich

#### 3.2 Template-Auswahl via Frontmatter
`template: post` → `build_page()` wählt entsprechendes Layout.

#### 3.3 Partials extrahieren
- Header (Navigation) → `_header.html` oder Python-Funktion
- Footer → `_footer.html` oder Python-Funktion
- `<head>` → `_head.html` oder Python-Funktion
- Wiederverwendbar für alle Templates

---

### Phase 4 — Blog-System
> Ziel: ~130 Posts migrieren und sauber darstellen.

#### 4.1 Post-Verarbeitung
- `content/posts/` Ordner mit Datums-Prefix (`2024-03-15-slug.md`)
- Datum, Autor, Tags aus Frontmatter
- Lesezeit berechnen (~200 Wörter/Min)
- Excerpt: Erste 160 Zeichen oder `excerpt:` Frontmatter-Feld

#### 4.2 Listing-Seite `/praxis/`
- Grid mit Post-Cards (Bild, Titel, Excerpt, Datum)
- Pagination (z.B. 12 Posts pro Seite)
- Sortierung: neueste zuerst

#### 4.3 Tag-System
- Tag-Seiten: `/tag/openusd/` mit gefilterten Posts
- Tag-Cloud oder Tag-Liste auf Listing-Seite

#### 4.4 Verwandte Artikel
- "Weitere Artikel" Block unter jedem Post
- Basierend auf gemeinsamen Tags

---

### Phase 5 — RSS & Feeds
> Ziel: Blog- und Podcast-Feeds automatisch generieren.

#### 5.1 RSS Blog-Feed (`/rss/index.xml`)
- Alle published Posts
- Titel, Excerpt, Datum, Link, Author
- Atom-Format oder RSS 2.0

#### 5.2 RSS Podcast-Feed (`/podcast/rss/index.xml`)
- Falls Podcast-Episoden als eigener Content-Typ kommen
- Oder: Weiterhin extern hosten, nur verlinken

---

### Phase 6 — Bild-Handling
> Ziel: Bilder sauber referenzieren, optional optimieren.

#### 6.1 Bild-Ordner
- `content/images/` → wird nach `site/content/images/` kopiert (oder symlinked)
- Markdown: `![Alt](images/hero.webp)`
- Build konvertiert Pfade korrekt

#### 6.2 Responsive Images (optional)
- `srcset` mit verschiedenen Größen
- Lazy Loading: `loading="lazy"`
- WebP-Konvertierung via Pillow (optional)

---

### Phase 7 — DX & Tooling
> Ziel: Angenehmer Workflow für Content-Erstellung.

#### 7.1 Watch-Mode
- `build.py --watch` mit `watchdog`-Library
- Bei Dateiänderung in `content/` automatisch neu bauen
- Nur geänderte Dateien rebuilden (incremental)

#### 7.2 Dev-Server
- `build.py --serve` startet lokalen HTTP-Server (Port 8000)
- Kombinierbar mit Watch: `build.py --watch --serve`
- Live-Reload (optional, via JS-Snippet)

#### 7.3 Validierung
- Tote Links erkennen (interne Links gegen bekannte Slugs prüfen)
- Fehlende Pflichtfelder in Frontmatter warnen
- Doppelte Slugs erkennen
- Build-Report: "42 Seiten, 130 Posts, 3 Drafts, 0 Fehler"

#### 7.4 404-Seite
- Statische `404.html` mit Navigation und Suchhinweis
- Webserver-Konfiguration (nginx/Apache) dokumentieren

---

## Migration Ghost → SkillCMS

### Schritt 1: Content exportieren
- Ghost Admin API: alle Pages + Posts als JSON
- Oder: Ghost Export (JSON) + HTML-zu-Markdown-Konvertierung
- Bilder aus Ghost `/content/images/` kopieren

### Schritt 2: Markdown-Dateien erstellen
- JSON → Markdown mit korrektem Frontmatter
- Bilder-Referenzen anpassen
- CTA-Buttons, Toggle-Cards, Spacer in Markdown-Syntax übersetzen

### Schritt 3: Seite für Seite verifizieren
- Visueller Abgleich mit Ghost-Version
- SEO-Meta prüfen
- Interne Links testen

### Schritt 4: DNS umschalten
- SkillCMS-Output auf Webserver deployen
- Redirects für geänderte URLs (falls nötig)
- Google Search Console: neue Sitemap einreichen

---

## Technische Eckdaten

| Eigenschaft | Wert |
|---|---|
| Sprache | Python 3 |
| Markdown-Library | `markdown` (extensions: extra, meta, smarty) |
| Theme | Ghost Source v9 (angepasst) |
| Schrift | Atkinson Hyperlegible (self-hosted woff2) |
| CSS-Framework | Ghost Theme CSS (`screen.css`) + Custom Overrides |
| JS | Ghost Source `source.js` + Custom Toggle-Script |
| Accent-Color | `#f2902a` (Orange/Amber) |
| URL-Struktur | Flat (alle Seiten auf Root-Level) |
| Seiten | ~42 statische + ~130 Blog-Posts |
| Config | `site.yaml` (YAML) |
| Hosting | Statisch (nginx, Netlify, o.ä.) |

---

## Nächster Schritt

→ **Phase 1.1**: `site.yaml` anlegen und Config-Parsing in `build.py` einbauen.
