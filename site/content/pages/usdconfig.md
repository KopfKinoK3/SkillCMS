---
title: "USDconfig: 3D-Konfiguration & AR für B2B-Produkte"
slug: usdconfig
status: published
meta_title: "USDconfig: 3D-Produktkonfigurator & AR für B2B | viSales NRW"
meta_description: "USDconfig macht Produktvarianten in AR erlebbar – ohne App, ohne Plattformgebühren, ohne Vendor Lock-in. Von viSales in Bochum/NRW."
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-03-01T17:36:44.000Z"
type: page
template: post
---

## Auf einen Blick

> USDconfig macht Produktvarianten, Optionen und Konfigurationslogiken direkt im Browser und in Augmented Reality erlebbar – auf Basis einer einzigen USDZ-Datei, ohne App, ohne laufende Plattformgebühren, ohne Parallelproduktion für verschiedene Kanäle.  
>   
> Der Ausgangspunkt ist kein technisches Problem, sondern ein Vertriebsproblem: Wer Produkte mit vielen Varianten verkauft, erklärt diese heute meist mit Tabellen, PDFs oder wechselnden Bildern. **USDconfig ermöglicht es, Varianten zu erleben – nicht nur zu lesen.**

&nbsp;

&nbsp;

## Das Problem: Varianten lassen sich nicht zeigen, nur beschreiben

Viele Produkte existieren in Varianten: Farben, Größen, Sets, Zubehör, Materialien. Im Vertrieb landet das meist als Tabelle in einer PDF oder als Bildergalerie auf der Website. Wer wissen will, wie Variante A im Vergleich zu Variante B aussieht, muss es sich vorstellen.

**Das ist das eigentliche Problem:** Nicht die Zahl der Varianten, sondern die fehlende Möglichkeit, sie direkt zu vergleichen – und das Produkt im eigenen Raum zu sehen, bevor eine Entscheidung getroffen wird.

Klassische Produktkonfiguratoren lösen das nur halb. Viele sind plattformgebunden, erfordern Abo-Modelle oder liefern AR als Zusatz mit separatem Dateiformat. Das Ergebnis: ein Tool für die Website, ein anderes für die Messe, ein drittes für das Kundengespräch. Und jeder Kanal braucht eine eigene Datei.

USDconfig basiert auf einem anderen Ansatz: einer einzigen USDZ-Datei, die in allen Kontexten funktioniert.

## Vorher. Nachher. Eine Datei.

**Vorher:**  
Produkt mit 8 Farben, 3 Sets, 2 Zubehöroptionen → PDF mit Tabelle → Bilder für die Website → separate App für AR → eigene Datei für die Messe → unterschiedliche Datenstände überall.

**Nachher:**  
Eine USDZ-Datei → interaktiver Konfigurator im Browser → AR auf iPhone, iPad und Apple Vision Pro → Keynote und Freeform → ohne App-Installation, ohne laufende Gebühren.

Einmal aufbereitet. In allen relevanten Vertriebskontexten einsetzbar.

## Was USDconfig konkret leistet

Eine USDZ-Datei, die kanalübergreifend genutzt wird:

- **Browser (Web-Player):** Interaktiver Konfigurator – Farben, Varianten, Sets direkt ansteuerbar, optional mit Schnittstelle zu Shop-Systemen
- **iPhone & iPad:** AR via Apple Quick Look, ohne App-Installation 
- **Android:** Fallback-Lösung mit Android-Kompatiblen *.glb-dateien für AR
- **Apple Vision Pro:** Lokales Rendering, ohne Streaming-Abhängigkeit
- **Apple Keynote & Freeform:** Dieselbe Datei direkt in Apple-Präsentationen nutzbar
- **Messe & Beratungsgespräch:** Auf dem iPad zur [Messe](https://visales.de/messen/) mitgenommen, sofort einsatzbereit

<details>
<summary><strong>Technische Details (für alle, die es genau wissen wollen)</strong></summary>

USDconfig umfasst zwei Dinge: einen Webplayer und eine interne Toolchain.

**Der Player** lädt eine einzelne USDZ-Datei live im Browser und stellt sie als interaktiven Konfigurator dar. Variantenlogik, Abhängigkeiten und Darstellungsparameter werden über eine strukturierte Konfiguration gesteuert. Der Player gibt dieselbe Datei auch in AR aus – ohne Konvertierung, ohne Datenverlust.

**Die Toolchain** ist ein Set aus Branchenstandards und eigenentwickelten Werkzeugen, mit dem wir CAD-Daten, 3D-Grafiken und Animationssequenzen effizient in performante USDZ-Dateien überführen. Besonderer Fokus: große Industriedateien, die auch mobil ohne sichtbare Qualitätsverluste funktionieren.

Das Dateiformat [USDZ](https://visales.de/usdz/) basiert auf [OpenUSD](https://visales.de/openusd/) – einem offenen Standard, der von Apple, NVIDIA und der gesamten Industrie breit unterstützt wird. Kein proprietäres Format, keine Plattformbindung.

**Aktueller Reifegrad:** Der Player ist in Kundenprojekten produktiv im Einsatz. Einige Funktionen – **insbesondere Full-OpenUSD im Desktop-Browser** – befinden sich noch in Entwicklung. Das Fundament ist stabil, der Ausbau läuft aktiv weiter.

</details>

### Unterstützte Kontexte

| Kontext | Funktionsweise |
| --- | --- |
| Browser (Desktop & Mobile) | Web-Player mit interaktiver Konfigurationslogik |
| iPhone & iPad | AR Quick Look, nativ, ohne App |
| Apple Vision Pro | Lokales Rendering, ohne Streaming |
| Keynote & Freeform | Direkteinbindung der USDZ-Datei |
| Messe & Außendienst | Auf Gerät mitgenommen, offline nutzbar |

## Für wen USDconfig sinnvoll ist – und für wen nicht

USDconfig ist dort sinnvoll, wo Produkte in mehreren Varianten existieren und diese Varianten im Vertrieb bisher nicht direkt gezeigt werden können – weil ein statisches Bild keine Entscheidung ermöglicht und ein klassischer Konfigurator zu aufwändig, zu teuer oder zu plattformabhängig wäre.

**Besonders geeignet:** B2B-Produkte, bei denen Kunden Farben, Sets, Größen oder Ausstattungsoptionen vergleichen müssen – und bei denen ein räumliches Erleben ("Passt das in unsere Halle? Wie wirkt die Farbe vor Ort?") eine Kaufentscheidung erleichtert oder beschleunigt.

USDconfig ist kein ERP-Konfigurator, keine Preiskalkulation, kein Webshop-Ersatz. Das Produkt löst das Visualisierungsproblem – nicht die kaufmännische Logik. Wer einen vollautomatisierten Konfigurationsprozess mit tiefer Shop-Integration sucht, braucht eine ergänzende Lösung von viSales.

→ [Fallbeispiel RENZ: Verkauf beginnt mit Erleben](https://visales.de/renz-augmented-reality-produktkonfigurator-fallbeispiel/)  
→ Zur Einordnung: [Spatial Websites – USDconfig (Stufe 4)](https://visales.de/spatial-website/)

<details>
<summary><strong>Typische Fragen aus Marketing & Vertrieb</strong></summary>

**Brauchen unsere Kunden eine App, um die AR-Funktion zu nutzen?**

Nein. Die AR-Ansicht läuft über [Apple Quick Look](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/) direkt auf iPhone und iPad – kein Download, keine IT-Freigabe, keine Registrierung. Der Kunde öffnet einen Link und kann das Produkt sofort im eigenen Raum platzieren.

**Können wir USDconfig auf unserer eigenen Website einbinden?**

Ja. Der Player wird auf Wunsch auf der Website des Kunden installiert und mit den bereitgestellten USDZ-Dateien ausgeliefert. Danach läuft die Lösung ohne monatliche Gebühren gegenüber viSales.

**Was brauchen wir, um loszulegen – reicht eine vorhandene 3D-Datei?**

Meistens ja. Wir arbeiten uns von Ihrer vorhandenen Datei (CAD, GLB, FBX, OBJ oder bereits USDZ) vor. Was fehlt, entwickeln wir gemeinsam. Der einfachste Einstieg: ein konkretes Produkt, eine konkrete Variante, ein erster Test.

**Wie aufwendig ist die Umsetzung organisatorisch?**

Das hängt von der Komplexität der Variantenlogik und dem Zustand der Ausgangsdaten ab. Wir klären das am schnellsten anhand eines konkreten Produkts.

**Was ist der Unterschied zu USDconfig und ConfigXR?**

[ConfigXR](https://github.com/KopfKinoK3/ConfigXRBuilder) war ein frühes System für AR-Konfigurationslogiken von viSales – entwickelt zu einer Zeit, als AR-Anwendungen vor allem als Einzellösungen gedacht wurden. Wir haben die Arbeit Open Source gestellt. USDconfig ist kein direkter Nachfolger, aber trägt die Erkenntnisse daraus weiter – auf Basis heutiger Standards und Anforderungen.

</details>

## 30 Minuten.   
Ihr Produkt.   
Wir zeigen, wie es weitergehen kann.

Nicht jede Anfrage muss sofort ein Projekt sein. Oft ist es sinnvoller, gemeinsam ein konkretes Produkt einzuordnen, bevor eine Entscheidung getroffen wird.

**Ins Gespräch kommen:** Schicken Sie uns eine 3D-Datei oder beschreiben Sie, welche Varianten Sie heute nicht direkt zeigen können. Wir schauen gemeinsam, ob und wie USDconfig hilft. **Ohne Pitch, bei einer Tasse Tee oder Kaffee.**

→ [Kontakt aufnehmen](https://visales.de/kontakt/)

## Häufige Fragen zu USDconfig

<details>
<summary><strong>Was ist USDconfig und wofür wird es eingesetzt?</strong></summary>

USDconfig ist ein AR-basierter Produktkonfigurator auf Basis von OpenUSD. Er ermöglicht Produktvarianten, Farben und Optionen in Echtzeit in 3D und Augmented Reality – direkt im Browser, ohne App.

</details>

<details>
<summary><strong>Für welche Branchen eignet sich USDconfig?</strong></summary>

USDconfig eignet sich für Maschinenbau, Möbelhandel, Medizintechnik und alle Branchen mit variantenreichen Produkten – überall dort, wo Kunden Konfigurationen visuell erleben sollen.

</details>

<details>
<summary><strong>Braucht man eine App für USDconfig?</strong></summary>

Nein. USDconfig funktioniert direkt im Browser – auf iPhone, iPad, Mac und Android. Dank AR Quick Look von Apple und WebXR ist kein App-Download nötig.

</details>

<details>
<summary><strong>Wie unterscheidet sich USDconfig von klassischen Produktkonfiguratoren?</strong></summary>

Klassische Konfiguratoren zeigen 2D-Bilder. USDconfig nutzt OpenUSD und zeigt das konfigurierte Produkt in echter Augmented Reality – im Raum des Kunden, in Originalgröße.

</details>

→ Technische Architektur, Web-Player & Live Demo: USDconfig Version 1.1. Demo & Dokumentation (Folgt)
