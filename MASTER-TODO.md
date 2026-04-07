# SkillCMS — Master ToDo
> Konsolidiert aus: `todo-skill-cms.md`, `KI-ToDo.md`, `TODO-fediverse-push.md`
> Stand: 2026-04-06

---

## ✅ Erledigt — Build-System

- Build-Pipeline: Markdown → HTML (`build.py`)
- Ghost Source Theme + CSS-Overrides
- Nav responsive (Desktop / Mobile)
- Tag-Listings, RSS 2.0, sitemap.xml, robots.txt
- llms.txt (KI-Crawler-Standard)
- Dev-Tooling: `--serve`, `--watch`
- GitHub Pages Deployment via Actions
- Brevo Newsletter-Form (einheitlich in allen Seiten)
- GA4 + Google Ads + Cookie Consent Mode v2
- Footer: 4 Spalten, responsive, Brevo-Form
- Grounding Pages: viSales GmbH ✅, Gerhard Schröder ✅, 5 Kern-Themen ✅

---

## 🔜 Block A — Cowork-Skills (nächster Schritt)

### A1 · Render-Skill `skillcms-render`
| Phase | Inhalt | Wann |
|---|---|---|
| **Phase 1** | Local Render: `build.py` ausführen, Output prüfen | **jetzt** |
| **Phase 2** | + git add/commit/push, GitHub Actions Status | nach Phase 1 |
| **Phase 3** | + FTP/SSH Hetzner, RSS-Ping, Mastodon-Post | wenn live |

→ Ablage: `.claude/skills/skillcms-render/SKILL.md`

---

## 🔜 Block B — KI-Readiness (parallel möglich)

### B1 · Grounding-Template (Phase 0.4)
- MD-Template mit fester Frontmatter-Struktur (`type: grounding`, `grounding_entity`, `faq`)
- Prüfen: rendert build.py JSON-LD + `<dl>` korrekt aus MD?
- `site/templates/` ist leer — aus bestehendem 0.1/0.2 ableiten

### B2 · llms.txt erweitern (Phase 1)
- Grounding Pages in `llms.txt` referenzieren (Identität zuerst)
- Build erweitern: MD-Quelldateien zusätzlich nach `/content/artikel-slug.md` ausgeben
- `llms-full.txt` generieren (alle Artikel gebündelt, optional)
- Bestand nachziehen: alle bisherigen Artikel als MD bereitstellen

### B3 · Artikel verknüpfen (Phase 2)
- Artikel 2025 updaten: Fußnote „Seit 2026 setzen wir das selbst um → /llms.txt"
- Artikel 2026 updaten: konkrete Links zu /llms.txt + Spatial-Demo
- Interlinking als Content-Cluster: 2025 (Warum) ↔ 2026 (Wie) ↔ Grounding (Was)

---

## 🔜 Block C — Spatial-Demo (wenn Assets bereit)

- **C1** Stufe 1: AR Quick Look Button (USDZ-Asset auswählen)
- **C2** Stufe 2: Spatial Foto prüfen + einbetten (falls Asset vorhanden)
- **C3** Stufe 3: `<model>`-Tag mit GLB einbetten
- **C4** Stufe 4: USDconfig-Konfigurator iframe einbauen ✅ Asset vorhanden
- **C5** Stufe 5: Videos bereits eingebunden — Begleittext prüfen
- **C6** Standalone-URL: `visales.de/demo` → USDconfig-Demo-Player
- **C7** Cross-Linking: `/spatial-website/` ↔ `/usdconfig-demo/` + Drei-Türen-Artikel

---

## 🔜 Block D — Content-Migration & Deploy

### D0 · Ghost-Exporter — Template-Fixes (Prio 1, Phase 1) 🆕

Erkannt beim Testlauf mit Tolkien-2 + Bildergalerie (2026-04-06):

| # | Problem | Lösung |
|---|---|---|
| D0.1 | **Bildergalerie fehlt** — Ghost `gallery`-Node wird als einzelne `![]()`-Liste gerendert, keine echte Galerie-Darstellung | Template: CSS-Grid-Galerie in `screen.css` + HTML-Wrapper im `build.py` für `gallery`-Blöcke |
| D0.2 | **Kategorie-Slug über Titelbild fehlt** | Template: `primary_tag` aus Frontmatter als Chip/Badge über dem Artikel-Header rendern |
| D0.3 | **Titelbild im Artikel-Header fehlt** | Template: `feature_image` als Hero-Bild im Post-Header rendern |
| D0.4 | **Autor-Block fehlt** (Name + Profilbild + Bio + Datum) | Template: Autor-Block unter dem Artikel-Header aus Frontmatter-Feldern `author`, `author_image`, `author_bio`, `published_at` |
| D0.5 | **Bilder als Broken Link** auf GitHub Pages (lokaler CORS-Block gelöst, GitHub live ✅) | Erledigt via GitHub Pages Deploy |
| D0.6 | **Homepage braucht eigenes Template `type: home`** — keine Artikel-Struktur (kein feature_image-Header, kein Autor-Block, kein Tag-Badge), stattdessen: Hero-Block, 3-Spalten-Grids, Kunden-Logo-Band, Leistungs-Grid, Fallbeispiel-Grid, volle Breite (`width: 100vw`). HTML-Nodes der Startseite werden 1:1 durchgereicht, nicht in Markdown konvertiert. MD liegt als `content/pages/home.md` mit `type: home` | Template-Chat: `home.html` Template in `build.py` + CSS für Fullwidth-Sections |

### D0.7 · FAQ-Konvention im Ghost-Exporter ✅ (2026-04-07)

- Ghost-Artikel nutzen `<details>/<summary>` für zwei Zwecke: Content-Toggles (Exkurse) und FAQ (Q&A am Ende)
- **Konvention:** FAQ-Toggles in Ghost mit `<div class="post-faq">` wrappen
- **Exporter:** erkennt `post-faq`-Wrapper → extrahiert als `faq:` Liste ins Frontmatter → entfernt Block aus Content
- **Content-Toggles** ohne Wrapper bleiben unverändert im Content
- `ghost_exporter.py`: `extract_faq_from_content()` implementiert und getestet
- Skill-Abo-Artikel: alle 4 Toggles sind Content-Toggles → kein `faq:` nötig ✅

### D1 · Content-Migration
- Ghost-Seiten als Dummy-MDs: Leistungen, Fallbeispiele, Über Uns, …
- Skeleton-Snapshot: ZIP als `SkillCMS-v1.0-skeleton`
- Ziel: ~51 Pages + ~200 Posts aus Ghost exportieren

### D2 · Hetzner Deploy (wenn live)
- FTP-Zugangsdaten klären
- Deploy-Workflow in Render-Skill Phase 3 integrieren
- URL-Schema prüfen (1:1 zu aktuellem Ghost-Schema?)

### D3 · Fediverse Push — Mastodon
- Mastodon-Account `@visales@mastodon.social` prüfen/einrichten
- Token testen (liegt in `TODO-fediverse-push.md`)
- Publish-Flow: HTML → RSS → Mastodon-Vorschlag → Review → POST → FTP
- In Render-Skill Phase 3 integrieren

---

## 🔜 Block E — Kommunikation (erst wenn Phase A–B live)

- Case-Study-Artikel: „Wie wir unsere Website KI-ready gemacht haben"
- „Drei-Türen-Check" als Lead-Magnet / Infografik
- LinkedIn-Post: Referenzimplementierung
- Newsletter via Brevo: beide KI-Artikel + Spatial-Demo

---

## Offene Fragen

- FTP-Zugangsdaten Hetzner: vorhanden?
- URL-Schema: 1:1 zu Ghost oder neu strukturieren?
- Mastodon-Account `@visales`: schon aktiv?

---

## Empfohlene Reihenfolge

1. **A1 Phase 1** — Render-Skill lokal bauen
2. **B1** — Grounding-Template finalisieren
3. **B2/B3** — llms.txt + Artikel-Verlinkung
4. **A1 Phase 2** — Render + GitHub im Skill
5. **D1** — Content-Migration starten
6. **C** — Spatial-Demo (parallel, wenn Assets bereit)
7. **D2/D3** — Deploy + Mastodon (= A1 Phase 3)
8. **E** — Kommunikation

---
*Zusammengeführt: 2026-04-06 | Duke Jera / viSales*
