# KI-ToDo: Website der Zukunft — Drei Türen für visales.de

> **Projekt:** SkillCMS · KI-Readiness für visales.de
> **Erstellt:** 2026-04-05
> **Status:** In Planung
> **Kontext-Artikel:**
> - [Website der Zukunft](https://visales.de/website-zukunft-ki-agent-2d-openusd/) (2026)
> - [Was deine Website KI sagt](https://visales.de/was-deine-website-ki-sprachmodellen-sagt-und-warum-das-kunftig-wichtig-wird/) (2025)
> - [Grounding Page Standard v1.5](https://groundingpage.com/spec/technical-implementation/de/)

---

## Phase 0 — Identität: Grounding Pages

Ziel: KI-Systeme sollen viSales, Duke Jera und die Kern-Themen korrekt als Entitäten erkennen und zuordnen können. Basiert auf dem Grounding Page Standard v1.5.

- [ ] **0.1 Grounding Page: viSales GmbH**
  - Entitätstyp: Organization
  - H1: nur "viSales GmbH" (kein Marketing-Claim)
  - Lead-Definition: Ein Satz — wer, was, seit wann
  - Fact Grid als `<dl>`: Gründung, Standort, Segment, Leistungen, Kunden
  - Disambiguierung: "viSales ist NICHT eine klassische Werbeagentur / Filmproduktion / Softwarehaus"
  - JSON-LD: Organization-Schema, gespiegelt mit HTML
  - Human Notice + Verifiziert-Datum
  - FAQ mit Entitätsname in jeder Antwort

- [ ] **0.2 Grounding Page: Gerhard Schröder / Duke Jera**
  - Entitätstyp: Person
  - Disambiguierung besonders wichtig (Namens-Verwechslung!)
  - Rollen: Gründer viSales, Thought Leader OpenUSD, AOUSD-Mitglied, Konferenzsprecher
  - Verknüpfung zu viSales-Entität

- [ ] **0.3 Grounding Pages: Kern-Themen**
  - Entitätstyp: DefinedTerm (je Thema)
  - Themen: WebAR, OpenUSD im B2B, Digitaler Zwilling, Produktkonfigurator, Spatial Computing
  - Jeweils: Lead-Definition, Fact Grid, Disambiguierung, FAQ
  - Verknüpfung zu viSales als Anbieter

- [ ] **0.4 SkillCMS-Template: Grounding Page**
  - MD-Template mit fester Struktur (Lead, Fact Grid, Disambiguierung, FAQ)
  - Generation-Step: MD → HTML mit korrektem JSON-LD + `<dl>`-Tags
  - Wiederverwendbar für alle zukünftigen Entitäten

---

## Phase 1 — Content-Tür: llms.txt + MD-Dateien

Ziel: KI-Agenten finden strukturierten Content auf der eigenen Domain. Keine Plattform-Abhängigkeit (kein GitHub).

- [ ] **1.1 llms.txt erstellen**
  - Datei: `visales.de/llms.txt`
  - Inhalt: Firmen-Intro + Liste aller Artikel mit Titel, Beschreibung, Link zur MD-Version
  - Auch Grounding Pages hier referenzieren (Identität zuerst, dann Content)

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

Ziel: Eine erlebbare Demo, die zeigt was "Spatial Website" bedeutet. Einsetzbar im Artikel, auf Konferenzen und in Sales-Calls.

- [ ] **3.1 Konzept definieren**
  - Was zeigen? Optionen: Produkt im 3D-Raum + Voice-KI, begehbarer Showroom, interaktives Architektur-Modell
  - Muss in 30 Sekunden überzeugen
  - Zielgruppe: B2B-Entscheider, nicht 3D-Nerds

- [ ] **3.2 Spatial-Demo bauen**
  - Technologie: WebXR / Model-Viewer / OpenUSD-basiert
  - Einbettbar in Artikel (iframe/embed)
  - Standalone nutzbar für Konferenzen
  - Mobile-tauglich

- [ ] **3.3 In Artikel 2026 einbetten**
  - Interaktives Element direkt im Text
  - Leser lesen über Tür 3 und können sie sofort ausprobieren

---

## Phase 4 — Proof & Kommunikation

Ziel: Die Implementierung als Referenz nutzen — für Content, Leads und Positionierung.

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

## Notizen

- **Priorität:** Phase 0 + Phase 1 parallel starten — beides sind Quick Wins
- **Grounding Page viSales** ist eine einzelne Seite, machbar in einer Session
- **llms.txt** ist eine Textdatei + kleiner SkillCMS-Build-Erweiterung
- **Phase 3 (Spatial)** ist das Prestige-Projekt, braucht mehr Vorlauf
- **Phase 4** erst starten wenn Phase 0–2 live sind (sonst fehlt der Proof)
