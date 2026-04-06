# Footer-Struktur — viSales SkillCMS

Der Footer wird vollständig aus `site/site.yaml` generiert. Keine Änderungen im build.py nötig — alles über die YAML-Konfiguration steuerbar.

---

## Spalten (Stand: April 2026)

### 1. Kontakt
- Typ: `contact` (Spezial-Rendering aus Kontaktdaten in `site.yaml`)
- Unterabschnitt **KI & Daten**:
  - Grounding-Pages → `/ki/`
  - LLMs.txt → `/llms.txt`
  - Notebook LLM → extern (notebooklm.google.com)

### 2. Visual Sales
- Grafik & Visualisierung → `/grafik-2d-3d/`
- Interaktive Präsentationen → `/interaktive-prasentationen/`
- Video- & Fotoproduktion → `/video/`
- Produktkonfiguratoren (Web) → `/produktkonfigurator/`
- Website → `/website/`

### 3. Immersive Sales
- Produktkonfiguratoren (AR/VR) → `/ar-konfigurator/`
- Augmented Reality → `/augmented-reality/`
- Messe-Lösungen → `/messen/`
- Virtuelle Rundgänge → `/virtuelle-rundgange/`
- Immersive Video → `/immersive-video/`
- Spatial Websites → `/spatial-website/`
- Spatial Presentations → `/spatial-presentation/`
- OpenUSD / NVIDIA Omniverse → `/tag/openusd/`

### 4. Produkte & Feeds
- **Produkte:** USDconfig, USDbridge, SkillCMS
- **Feeds & Social:**
  - RSS Website → `/rss/`
  - RSS Visual Com-Podcast → https://visualcom.podcaster.de/visual-com.rss
  - Mastodon @visales
  - LinkedIn · Gerhard Schröder
  - YouTube · Gerhard Schröder
  - GitHub · Gerhard Schröder → https://github.com/KopfKinoK3

### 5. Newsletter
- Titel: **VISUAL SALES: 1x IM MONAT**
- Kein Teaser-Text
- Kein "E-Mail-Adresse"-Label
- Formular: Brevo-Embed aus `_brevo-form.html`
- Archiv-Link: Alle Ausgaben & Podcasts → `/newsletter/`

---

## Trust-Bar (über dem Footer)
- Kunden-Zeile aus `trust_clients:` in site.yaml
- Mitgliedschaften: Alliance for OpenUSD (AOUSD) · Metaverse Standards Forum

## Legal-Zeile
- Impressum → `/impressum/`
- Datenschutz → `/datenschutz/`

---

## Änderungen vornehmen

Alle Footer-Inhalte in `site/site.yaml` unter dem Schlüssel `footer:`.
Nach jeder Änderung: `python3 site/build.py` → `git push` → GitHub Actions baut automatisch.
