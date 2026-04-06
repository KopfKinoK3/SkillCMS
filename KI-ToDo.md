# KI-ToDo: Website der Zukunft — Drei Türen für visales.de

> **Projekt:** SkillCMS · KI-Readiness für visales.de
> **Erstellt:** 2026-04-05
> **Zuletzt aktualisiert:** 2026-04-05
> **Status:** In Arbeit
> **Kontext-Artikel:**
> - [Website der Zukunft](https://visales.de/website-zukunft-ki-agent-2d-openusd/) (2026)
> - [Was deine Website KI sagt](https://visales.de/was-deine-website-ki-sprachmodellen-sagt-und-warum-das-kunftig-wichtig-wird/) (2025)
> - [Grounding Page Standard v1.5](https://groundingpage.com/spec/technical-implementation/de/)

---

## Phase 0 — Identität: Grounding Pages

Ziel: KI-Systeme sollen viSales, Duke Jera und die Kern-Themen korrekt als Entitäten erkennen und zuordnen können. Basiert auf dem Grounding Page Standard v1.5.

- [x] **0.1 Grounding Page: viSales GmbH** ✅
  - Dateien: `site/content/visales-gmbh-grounding.md` + `site/visales-gmbh-grounding.html`
  - Organization-Entität, Fact Grid `<dl>`, Disambiguierung, FAQ, Human Notice, Verifiziert-Datum

- [x] **0.2 Grounding Page: Gerhard Schröder / Duke Jera** ✅
  - Dateien: `site/content/gerhard-schroeder-grounding.md` + `site/gerhard-schroeder-grounding.html`
  - Person-Entität, Bundeskanzler-Disambiguierung explizit gelöst, vollständige Berufslaufbahn

- [x] **0.3 Grounding Pages: Kern-Themen** ✅
  - `site/content/webar-grounding.md`
  - `site/content/openusd-b2b-grounding.md`
  - `site/content/digitaler-zwilling-grounding.md`
  - `site/content/produktkonfigurator-grounding.md`
  - `site/content/spatial-computing-grounding.md`
  - Alle mit: Lead-Definition, Fact Grid `<dl>`, Disambiguierung, FAQ, Human Notice, Verknüpfung zu viSales
  - HTML noch zu generieren via SkillCMS-Build

- [ ] **0.4 SkillCMS-Template: Grounding Page**
  - `site/templates/` ist noch leer — Template aus 0.1/0.2 ableiten
  - MD-Template mit fester Frontmatter-Struktur (type: grounding, grounding_entity, faq)
  - Generation-Step prüfen: rendert er JSON-LD + `<dl>` korrekt aus dem MD?

---

## Phase 1 — Content-Tür: llms.txt + MD-Dateien

Ziel: KI-Agenten finden strukturierten Content auf der eigenen Domain. Keine Plattform-Abhängigkeit (kein GitHub).

- [ ] **1.1 llms.txt erstellen**
  - Datei: `visales.de/llms.txt`
  - Inhalt: Firmen-Intro + Liste aller Artikel mit Titel, Beschreibung, Link zur MD-Version
  - Grounding Pages ebenfalls referenzieren (Identität zuerst, dann Content)

- [ ] **1.2 SkillCMS-Generation erweitern**
  - Bestehender Build: MD → HTML → FTP-Push
  - Neuer Output: MD-Quelldatei zusätzlich nach `/content/artikel-slug.md` hochladen
  - llms.txt automatisch aktualisieren bei jedem neuen Artikel

- [ ] **1.3 llms-full.txt generieren (optional)**
  - Alle Artikel-MDs in einer Datei gebündelt
  - Für Agenten, die den kompletten Content auf einmal lesen wollen
  - Automatisch generiert durch SkillCMS-Build

- [ ] **1.4 Bestand nachziehen**
  - Alle bisherigen Ghost-/SkillCMS-Artikel als MD hochladen
  - Sicherstellen, dass der Content-Bestand von Tag 1 vollständig ist

---

## Phase 2 — Verknüpfung: Artikel-Story schließen

Ziel: Die beiden bestehenden Artikel aktualisieren, damit sie die Live-Implementierung referenzieren. Narrativen Bogen schließen.

- [ ] **2.1 Artikel 2025 updaten (llms.txt)**
  - Absatz oder Fußnote ergänzen: "Seit 2026 setzen wir das selbst um → /llms.txt"
  - Verlinkung zum 2026er-Artikel

- [ ] **2.2 Artikel 2026 updaten (Drei Türen)**
  - Konkreten Hinweis: "Diese Website hat alle drei Türen"
  - Tür 2 → Link zu /llms.txt
  - Tür 3 → Link zur Spatial-Demo (sobald fertig)
  - Verlinkung zum 2025er-Artikel als Vorgeschichte

- [ ] **2.3 Interlinking als Content-Cluster**
  - 2025er = "Warum" (Awareness)
  - 2026er = "Wie" (Strategie)
  - Grounding Pages = "Was" (Fakten)
  - Gegenseitige Verlinkung für SEO-Cluster "KI-ready Website"

---

## Phase 3 — Spatial-Demo: Die dritte Tür

Ziel: Die bestehende `/spatial-website/`-Seite wird zur lebenden Demo — jede der 5 Stufen erlebbar statt nur beschrieben. Bestehende Assets (USDconfig-Demo, Videos) einbetten, nichts neu bauen.

> **Assets vorhanden:**
> - USDconfig Demo-Konfigurator (iframe → `kopfkinok3.github.io/USDconfig-demo-player/`) → Stufe 4
> - 2 Videos bereits eingebunden auf der Seite → Stufe 5 ✅

- [ ] **3.1 Stufe 1 einbetten: AR Quick Look**
  - Ein bestehendes USDZ-Asset aus dem viSales-Fundus wählen
  - AR Quick Look Button direkt unter der Stufe-1-Beschreibung einbauen
  - Funktioniert ohne App auf iPhone/iPad

- [ ] **3.2 Stufe 2 einbetten: Spatial Foto**
  - Prüfen ob ein Spatial Foto aus bestehenden Assets vorhanden ist
  - Falls ja: einbetten unter Stufe-2-Beschreibung
  - Falls nein: Todo zurückstellen bis Asset erstellt

- [ ] **3.3 Stufe 3 einbetten: `<model>`-Tag**
  - Ein GLB-Asset wählen (Fallback für Android/Desktop)
  - `<model>`-Tag mit GLB unter Stufe-3-Beschreibung einbauen

- [ ] **3.4 Stufe 4 einbetten: USDconfig-Konfigurator**
  - iframe `kopfkinok3.github.io/USDconfig-demo-player/` unter Stufe-4-Beschreibung einbauen
  - Kurze Einleitung: "Stufe 4 in Aktion — Vitra ID Chair, 39 Farben, AR-Übergabe"
  - Ghost-Edit der `/spatial-website/`-Seite

- [x] **3.5 Stufe 5: Videos** ✅
  - 2 Videos bereits eingebunden
  - [ ] Kontext/Beschriftung prüfen — ggf. Begleittext ergänzen

- [ ] **3.6 Standalone-URL für Konferenzen & Sales**
  - Weiterleitung `visales.de/demo` → USDconfig-Demo-Player einrichten
  - Kurze URL für Live-Demos auf der Bühne und in Sales-Calls

- [ ] **3.7 Cross-Linking schließen**
  - `/spatial-website/` ↔ `/usdconfig-demo/` gegenseitig verlinken
  - Im 2026er-Artikel "Drei Türen" → Tür 3 auf `/spatial-website/` verlinken

---

## Phase 4 — Proof & Kommunikation

Ziel: Die Implementierung als Referenz nutzen — für Content, Leads und Positionierung. Erst starten wenn Phase 0–2 live sind.

- [ ] **4.1 Case-Study-Artikel schreiben**
  - "Wie wir unsere Website KI-ready gemacht haben"
  - Grounding Pages + llms.txt + Spatial als dokumentierte Praxis
  - Ghost-Draft via SkillCMS

- [ ] **4.2 "Drei-Türen-Check" als Lead-Magnet**
  - Einfaches Assessment: "Welche Türen hat deine Website schon?"
  - Infografik oder interaktives Tool
  - Lead-Generierung über CTA

- [ ] **4.3 LinkedIn-Post: Referenzimplementierung**
  - "Wir haben unsere eigene These umgesetzt"
  - Screenshot llms.txt + Spatial-Demo
  - Thought-Leadership-Positioning

- [ ] **4.4 Newsletter via Brevo**
  - Beide Artikel + Live-Demo als Newsletter-Package
  - An bestehende Kontaktliste

---

## Fortschritt

| Phase | Offen | Erledigt |
|---|---|---|
| Phase 0 — Grounding Pages | 1 | 3 ✅ |
| Phase 1 — llms.txt + MD | 4 | 0 |
| Phase 2 — Verknüpfung | 3 | 0 |
| Phase 3 — Spatial-Demo | 6 | 1 ✅ |
| Phase 4 — Kommunikation | 4 | 0 |
| **Gesamt** | **19** | **3** |

## Notizen

- **Nächster Schritt:** 0.3 (Kern-Themen Grounding Pages) oder 0.4 (Template) oder direkt Phase 1
- **0.4 Template:** `site/templates/` ist leer — aus 0.1/0.2 ableiten
- **Phase 3:** Kein Neuaufbau nötig — alles einbetten was schon da ist
- **Phase 4** erst starten wenn Phase 0–2 live sind (sonst fehlt der Proof)
