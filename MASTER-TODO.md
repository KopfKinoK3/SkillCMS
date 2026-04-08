# SkillCMS — Master ToDo
> Konsolidiert aus: `todo-skill-cms.md`, `KI-ToDo.md`, `TODO-fediverse-push.md`
> Stand: 2026-04-08

---

## ✅ Erledigt — Build-System & Skills

- Build-Pipeline: Markdown → HTML (`build.py`)
- Ghost Source Theme + CSS-Overrides
- Nav responsive (Desktop / Mobile)
- Tag-Listings, RSS 2.0, sitemap.xml, robots.txt
- llms.txt (KI-Crawler-Standard)
- Dev-Tooling: `--serve`, `--watch`
- GitHub Pages Deployment via Actions
- Brevo Newsletter-Form (einheitlich in allen Seiten)
- GA4 + Google Ads + Cookie Consent Mode v2
- Footer: 4 Spalten, responsive, Brevo-Form, first-child margin-fix
- Grounding Pages: viSales GmbH ✅, Gerhard Schröder ✅, 5 Kern-Themen ✅
- **Render-Skill Phase 1** (lokaler Build) ✅
- **Render-Skill Phase 2** (+ Git commit + GitHub Push) ✅
- FAQ-Konvention Ghost-Exporter: `post-faq`-Wrapper → `faq:` Frontmatter ✅
- D0.2 Kategorie-Badge über Titelbild ✅
- D0.3 Titelbild im Post-Header ✅
- D0.4 Autor-Block (Name, Bild, Bio, Datum) ✅
- D0.5 Bilder Broken Links via GitHub Pages gelöst ✅

---

## 🗂️ Aktive Chats & Zuständigkeiten

| Chat | Zuständig für | Status |
|---|---|---|
| **Dieser Chat** (Render/Build) | build.py, Render-Skill, MASTER-TODO | aktiv |
| **Ghost-Export** | ghost_exporter.py, MD-Migration aus Ghost | aktiv |
| **Template** | build.py Templates: post, home, grounding | aktiv |
| **KI-Website** | Grounding Pages, llms.txt, KI-Readiness | aktiv |
| **Newsletter** | Brevo-Kampagnen, Newsletter-Content | aktiv |
| **Leistungen** | Leistungs-Seiten als MD-Content | aktiv |
| **Fediverse** | Mastodon-Push, Publish-Flow | on hold |
| **Homepage 2.0** | type:home Template, Hero, Grids | aktiv |

---

## 🔜 Block A — Render-Skill

### A1 · `skillcms-render` — Phasen
| Phase | Inhalt | Status |
|---|---|---|
| Phase 1 | Local Render: `build.py` ausführen, Output prüfen | ✅ fertig |
| Phase 2 | + git add/commit/push, GitHub Actions Status | ✅ fertig |
| Phase 3 | + FTP/SSH Hetzner, RSS-Ping, Mastodon-Post | 🔜 wenn live |

**Offen:**
- [ ] Render-Skill: `template: post` → `type: post` Migrations-Warnung einbauen (warnt beim Build wenn altes Schema erkannt wird)

---

## 🔜 Block B — KI-Readiness
> Chat: **KI-Website**

### B1 · Grounding-Template
- [ ] MD-Template mit fester Frontmatter-Struktur dokumentieren
- [ ] Prüfen: rendert build.py JSON-LD + `<dl>` korrekt aus MD?

### B2 · llms.txt erweitern
- [ ] Grounding Pages in `llms.txt` referenzieren (Identität zuerst)
- [ ] Build: MD-Quelldateien zusätzlich nach `/content/[slug].md` ausgeben
- [ ] `llms-full.txt` generieren (alle Artikel gebündelt)
- [ ] Bestand nachziehen: alle bisherigen Artikel als MD

### B3 · Artikel verknüpfen
- [ ] Artikel 2025: Fußnote „Seit 2026 setzen wir das selbst um → /llms.txt"
- [ ] Artikel 2026: Links zu /llms.txt + Spatial-Demo
- [ ] Interlinking als SEO-Cluster

---

## 🔜 Block C — Spatial-Demo
> Wartet auf Assets

- [ ] **C1** Stufe 1: AR Quick Look Button (USDZ wählen)
- [ ] **C2** Stufe 2: Spatial Foto (falls vorhanden)
- [ ] **C3** Stufe 3: `<model>`-Tag mit GLB
- [ ] **C4** Stufe 4: USDconfig-Konfigurator iframe ✅ Asset vorhanden
- [ ] **C5** Stufe 5: Videos eingebunden — Begleittext prüfen
- [ ] **C6** `visales.de/demo` → USDconfig-Demo-Player
- [ ] **C7** Cross-Linking + Drei-Türen-Artikel

---

## 🔜 Block D — Content-Migration & Deploy

### D0 · Ghost-Exporter Fixes
> Chat: **Ghost-Export** + **Template**

| # | Problem | Status |
|---|---|---|
| D0.1 | Bildergalerie: CSS-Grid + HTML-Wrapper in build.py | 🔜 offen |
| D0.2 | Kategorie-Badge über Titelbild | ✅ erledigt |
| D0.3 | Titelbild im Post-Header | ✅ erledigt |
| D0.4 | Autor-Block (Name, Bild, Bio, Datum) | ✅ erledigt |
| D0.5 | Bilder Broken Links | ✅ erledigt |
| D0.6 | Homepage `type: home` Template | 🔜 Chat: Homepage 2.0 |
| D0.7 | FAQ-Konvention im Exporter | ✅ erledigt |

**Frage an Ghost-Export-Chat:**
> „Welche Frontmatter-Felder gibt der Exporter aktuell aus? Nutzt er `type: post` oder noch `template: post`? Und: wird `date:` als String `"2026-03-26"` oder als datetime-Objekt exportiert?"

### D1 · Content-Migration
> Chat: **Leistungen** + **Ghost-Export**

- [ ] ~51 Ghost-Pages als MD (Leistungen, Fallbeispiele, Über Uns, …)
- [ ] ~200 Ghost-Posts exportieren + schema-fix (type: post, date als String)
- [ ] Skeleton-Snapshot: ZIP `SkillCMS-v1.0-skeleton`

### D2 · Hetzner Deploy
> Chat: **Dieser Chat** (Render-Skill Phase 3)

- [ ] FTP-Zugangsdaten klären
- [ ] URL-Schema 1:1 zu Ghost prüfen
- [ ] Render-Skill Phase 3 bauen

### D3 · Fediverse Push
> Chat: **Fediverse** (on hold bis live)

- [ ] Mastodon-Account `@visales@mastodon.social` prüfen
- [ ] Token testen (`TODO-fediverse-push.md`)
- [ ] In Render-Skill Phase 3 integrieren

---

## 🔜 Block E — Kommunikation
> Erst wenn Block B live ist

- [ ] Case-Study: „Wie wir unsere Website KI-ready gemacht haben"
- [ ] „Drei-Türen-Check" als Lead-Magnet
- [ ] LinkedIn-Post: Referenzimplementierung
- [ ] Newsletter via Brevo: KI-Artikel + Spatial-Demo

---

## Offene Fragen

- FTP-Zugangsdaten Hetzner: vorhanden?
- URL-Schema: 1:1 zu Ghost oder neu?
- Mastodon `@visales`: Account schon aktiv?
- author_image-Pfad `/assets/images/2025/10/1706254155883-1.jpeg` — liegt das Bild im Repo?

---

## Empfohlene Reihenfolge

1. ✅ A1 Phase 1+2 — Render-Skill fertig
2. **D0.1** — Bildergalerie-Fix (Template-Chat)
3. **D0.6** — Homepage-Template (Homepage-2.0-Chat)
4. **D1** — Ghost-Export + Content-Migration
5. **B2** — llms.txt erweitern (KI-Website-Chat)
6. **C** — Spatial-Demo (wenn Assets bereit)
7. **D2/D3** — Deploy + Mastodon → A1 Phase 3
8. **E** — Kommunikation

---
*Aktualisiert: 2026-04-08 | Duke Jera / viSales*
