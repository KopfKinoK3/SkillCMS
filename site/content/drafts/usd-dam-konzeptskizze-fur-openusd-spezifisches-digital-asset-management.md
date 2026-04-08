---
title: "USD-DAM: Konzeptskizze für OpenUSD-spezifisches Digital Asset Management"
slug: usd-dam-konzeptskizze-fur-openusd-spezifisches-digital-asset-management
status: draft
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
type: post
template: post
---

**viSales GmbH | Gerhard Schröder | März 2026**

## Ausgangssituation

Unternehmen, die OpenUSD-basierte 3D-Workflows einsetzen, stehen ab einer bestimmten Asset-Menge vor einem strukturellen Problem: Generische DAM-Systeme verwalten Bilder, Videos und Dokumente – aber sie verstehen keine USD-spezifischen Zustände.

Die Fragen, die in der Praxis entstehen, sind nicht "wo liegt die Datei?" sondern:

- Welche Assets liegen als Omniverse-Original vor – und welche wurden bereits nach USDZ konvertiert?
- Ist die USDZ-Version noch aktuell, oder wurde das Original in Omniverse verändert?
- Welche Assets sind für welchen Kanal freigegeben – Vertrieb, Messe, Web, Vision Pro?
- Wer darf was sehen – 3D-Team, Marketing, Außendienst, Kunde?

Kein generisches DAM beantwortet diese Fragen ohne erhebliche Anpassung.

## Der spezifische Bedarf: Was ein USD-DAM leisten muss

### 1. USD-spezifische Metadaten

Jedes Asset braucht mindestens diese zusätzlichen Felder:

| Metadatenfeld | Beschreibung |
| --- | --- |
| Quellformat | Omniverse USD, CAD-Export, nativer USD |
| Shader-Typ | OmniPBR/MDL, OpenPBR, RealityKit-kompatibel |
| Konversionsstatus | Original only / USDZ vorhanden / USDZ veraltet |
| Letzte Konversion | Datum der letzten USDbridge-Konvertierung |
| Zielplattformen | Apple Vision Pro, iPhone/iPad, Browser, Omniverse |
| Freigabestatus | In Arbeit / Intern freigegeben / Extern freigegeben |
| Textur-Typ | Standard / UDIM (relevant für Konversionsprozess) |

### 2. Konversionsstatus-Tracking

Das Kernproblem bei wachsenden USD-Bibliotheken: Das Omniverse-Original wird aktualisiert, aber die USDZ-Version nicht. Im Vertrieb landet dann eine veraltete AR-Darstellung.

Ein USD-DAM muss erkennen:

- **Original aktueller als USDZ** → Konversion notwendig, Asset markieren
- **USDZ aktuell** → freigegeben für Vertriebskanäle
- **Keine USDZ vorhanden** → noch nicht konvertiert

### 3. Rollenbasierter Zugriff

Drei typische Nutzergruppen mit unterschiedlichen Bedürfnissen:

**3D-Team:** Vollzugriff auf Originaldaten, Konversionsstatus, technische Metadaten  
**Marketing/Vertrieb:** Zugriff nur auf freigegebene USDZ-Assets, keine Rohdaten  
**Außendienst:** Lesezugriff auf vertriebsfertige Assets, optimiert für mobile Nutzung

### 4. Kanalspezifische Ausgabe

Dasselbe Asset wird je nach Kanal unterschiedlich bereitgestellt:

- **Web:** USDZ-Link mit korrektem MIME-Typ für AR Quick Look
- **Messe/Außendienst:** Download auf Gerät für Offline-Nutzung
- **Omniverse:** Referenz auf Originaldatei im Nucleus

## Technologische Basis: AtroDAM als Ausgangspunkt

AtroDAM (AtroCore GmbH, Deutschland) ist ein Open-Source-DAM-System unter GPLv3-Lizenz mit API-zentrischer Architektur und flexiblem Datenmodell. Es ist erweiterbar über eigene Entitäten, Relationen und Metadatenfelder – ohne den Core anzufassen.

**Warum AtroDAM als Basis:**

- Deutsches Unternehmen, DSGVO-konform, selbst hostbar
- Flexibles Datenmodell – USD-spezifische Felder lassen sich ohne Core-Änderung ergänzen
- API-First – Integration mit USDbridge und Omniverse Nucleus möglich
- Open Source – keine laufenden Lizenzkosten für die Grundlage
- Aktive Entwicklung und ansprechbarer Gründer (Alex Zinchenko)

**Was fehlt und ergänzt werden müsste:**

- USD-spezifische Metadatenfelder (Konversionsstatus, Shader-Typ, Zielplattformen)
- Statuslogik für Konversionspipeline (Original vs. USDZ-Aktualität)
- USDbridge-Integration: Konversion direkt aus dem DAM anstoßen
- Optionale Nucleus-Anbindung für automatisches Erkennen von Asset-Updates

## Realistischer Einstieg

Kein Unternehmen braucht von Tag eins ein vollständig ausgebautes USD-DAM. Der sinnvolle Einstieg ist schrittweise:

**Stufe 1 – Struktur schaffen (sofort umsetzbar):**  
AtroDAM installieren, USD-spezifische Metadatenfelder einrichten, bestehende Assets strukturiert einpflegen. Konversionsstatus manuell pflegen.

**Stufe 2 – Statustracking (nach erstem Betrieb):**  
Automatische Erkennung von veralteten USDZ-Versionen auf Basis von Dateidatum oder Prüfsumme. Benachrichtigung an 3D-Team bei Aktualisierungsbedarf.

**Stufe 3 – Pipeline-Integration (mittelfristig):**  
USDbridge-Konversion direkt aus dem DAM anstoßen. Optionale Nucleus-Anbindung für Teams mit zentralem Omniverse-Server.

## Relevanz für viSales-Kunden

Dieser Bedarf entsteht nicht sofort – sondern an einer konkreten Schwelle: wenn ein Unternehmen mehr als 20–30 USD-Assets aktiv im Vertrieb einsetzt und die manuelle Verwaltung (Ordnerstrukturen, E-Mail-Weitergabe, fehlende Versionskontrolle) zu Fehlern führt.

**Typische Signale, dass die Schwelle erreicht ist:**

- Vertrieb nutzt veraltete AR-Darstellungen ohne es zu merken
- 3D-Team verliert Überblick welche Assets konvertiert wurden
- Verschiedene Abteilungen haben unterschiedliche Dateistände
- Neuer Außendienstmitarbeiter findet nicht die richtigen Assets

viSales kann in diesem Moment eine strukturierte Lösung skizzieren – statt den Kunden mit generischen DAM-Empfehlungen allein zu lassen.

## Mögliche Zusammenarbeit mit AtroCore

Eine Partnerschaft mit AtroCore/AtroDAM könnte zwei Formen annehmen:

**Option A – Referenzimplementierung:**  
viSales entwickelt eine USD-Erweiterung für AtroDAM (Metadatenfelder, Statuslogik) und stellt sie als Open-Source-Modul zur Verfügung. AtroCore bewirbt die USD-Kompatibilität, viSales gewinnt Sichtbarkeit im DAM-Umfeld.

**Option B – gemeinsames Kundenprojekt:**  
Für einen konkreten Kunden wird AtroDAM mit USD-Erweiterung gemeinsam implementiert. AtroCore liefert die DAM-Basis, viSales die USD-Workflow-Expertise und USDbridge-Integration.

Beide Optionen setzen kein großes gemeinsames Produktprojekt voraus – sondern beginnen mit einem konkreten Fall.

*Dokument erstellt: März 2026 | viSales GmbH | Gerhard Schröder*  
*Kontakt: *[*https://visales.de/kontakt/*](https://visales.de/kontakt/)
