---
title: "USDbridge"
slug: usdbridge
status: published
meta_title: "USDbridge: Omniverse Assets in USDZ konvertieren für AR & Web"
meta_description: "Konvertieren Sie NVIDIA Omniverse Assets automatisch in USDZ, ohne Nachbearbeitung. Nutzen Sie 3D-Inhalte direkt im Browser, auf iPhone & Apple Vision Pro für effektivere Verkaufsgespräche."
og_image: /assets/images/2026/03/USDbridge_Apple_NVIDIA_Omniverse_Gabelstapler-1.jpg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-03-01T17:03:29.000Z"
type: post
template: post
---

## Auf einen Blick

> USDbridge konvertiert bestehende NVIDIA Omniverse-Assets in plattformübergreifende USDZ-Dateien – so dass dieselben 3D-Inhalte nativ auf iPhone, iPad und Apple Vision Pro laufen, ohne Streaming, ohne Parallelproduktion, ohne neue Dienstleister.  
>   
> Der Ausgangspunkt ist kein technisches Problem, sondern ein Vertriebsproblem: Wer in Omniverse investiert hat, kann diese Inhalte im Kundengespräch bisher nur schwer direkt einsetzen. **USDbridge schließt genau diese Lücke. **

&nbsp;

&nbsp;

## Zeitersparnis direkt im Kundengespräch

Der Kunde wünscht eine andere Farbe, ein 3D-Bauteil soll kleiner werden. Klassischerweise bedeutet das: Vertriebsgespräch unterbrechen, zurück an den Rechner, neu exportieren, neu übertragen, neu öffnen.

Mit USDbridge läuft die Konvertierung schnell auf dem Mac, direkt mit Apple Quick Look prüfen, fertig. Keine Unterbrechung, die den Gesprächsfluss kostet. Kein "ich schick Ihnen das dann später." **Das ist kein großes Feature. Aber im Vertrieb ist es der Unterschied zwischen Momentum und Warteschleife.**

## Das Problem: Omniverse und Apple sprechen nicht dieselbe Sprache

Viele Unternehmen haben in NVIDIA Omniverse investiert – und ihre 3D-Inhalte sehen dort beeindruckend aus. Doch sobald der Vertrieb dieselben Inhalte auf dem iPhone, iPad oder der Apple Vision Pro zeigen soll, passiert: nichts. Oder eine aufwändige Parallelproduktion beginnt.

**Der Grund ist technisch, die Konsequenz ist praktisch:** Omniverse nutzt proprietäre Shader ([OmniPBR/MDL](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/materials.html)), die außerhalb der Omniverse-Umgebung nicht funktionieren. Die USDbridge konvertiert in [UsdPreviewSurface](https://openusd.org/release/spec_usdpreviewsurface.html) Materialien *-die offizielle *[*OpenUSD-Empfehlung*](https://aousd.org)* für photorealistische Shader*-, die auch von Apple-RealityKit in AR/XR auf Apple-Geräten funktionieren. Zukünftig werden vom Omniverse und Apple die OpenPBR/[MaterialX](https://materialx.org)-Lösung genutzt. 

<details>
<summary><strong>**Nicht zu verwechseln mit den NVIDIA Omniverse Bridges**</strong></summary>

NVIDIA selbst bietet unter dem Begriff „Bridges" Verbindungen zwischen Omniverse und anderen DCC-Anwendungen an – etwa Houdini, Substance 3D Painter oder Onshape. Diese Bridges führen Inhalte **in** Omniverse hinein oder synchronisieren Tools miteinander.

USDbridge löst das entgegengesetzte Problem: fertige Omniverse-Assets **heraus** auf Apple-Geräte bringen – ohne Cloud, ohne Streaming, mit korrekten Materialien.

Gleicher Wortlaut. Andere Richtung. Anderes Ziel.

</details>

Ein in Omniverse produziertes Asset lässt sich zwar als USDZ-Datei exportieren – Texturen und Materialien erscheinen auf Apple-Geräten aber entweder gar nicht oder fehlerhaft. Das Ergebnis ist ein klassisches Inselproblem: hochwertige 3D-Daten, die für einen einzigen Kontext produziert wurden und dort bleiben.

USDbridge löst genau das. 

## Vorher.   
Nachher.   
Einmal.

![](/assets/images/2026/03/USDbridge_Apple_NVIDIA_Omniverse_Gabelstapler.jpg)

**Vorher:** Omniverse-Asset → funktioniert nur in Omniverse → Vertrieb kann nicht damit arbeiten → neue Produktion, neues Budget, neuer Dienstleister.

**Nachher:** Omniverse-Asset → USDbridge → USDZ-Datei, die auf iPhone, iPad und Apple Vision Pro nativ läuft – und gleichzeitig rückwärtskompatibel in Omniverse bleibt.

Kein Server, kein Cloud-Abo, sondern eine Software die jederzeit Konvertieren kann.

## Was USDbridge konkret leistet

Ihr bestehendes Omniverse-Asset wird in eine plattformübergreifende USDZ-Datei konvertiert:

- **Apple Vision Pro**: Lokal gerendert *auf bis zu 5 Geräten*, ohne [Streaming-Abhängigkeit](https://visales.de/foveated-streaming-openusd-visualisierung-ohne-server-infrastruktur/)
- **iPhone & iPad**: nativ via AR Quick Look, ohne App-Installation
- **NVIDIA Omniverse**: weiterhin nutzbar, rückwärtskompatibel
- **Neu erstellte Omniverse-Assets**: von Anfang an kompatibel, kein nachträglicher Aufwand

Einmal aufbereitet. Überall einsetzbar.

<details>
<summary><strong>Technische Details (für alle, die es genau wissen wollen)</strong></summary>

USDbridge ist ein von der viSales GmbH entwickelter, lokaler Konvertierungsprozess – kein Cloud-Dienst, keine externe Datenübertragung:

1. **Einlesen** des Omniverse-Assets inklusive aller Texturen und Materialreferenzen
2. **Analyse** der OmniPBR/MDL-Shader-Parameter und Zuordnung zu RealityKit-kompatiblen Äquivalenten
3. **UDIM-Textur-Erkennung** – mehrteilige Textur-Layouts werden erkannt und als GeomSubsets für AR Quick Look vorbereitet
4. **Ausgabe** als kompaktes, selbstenthaltendes USDZ-Paket – optimiert für AR Quick Look auf iPhone/iPad und (lokales) Rendering auf der Apple Vision Pro
5. **Rückwärtskompatibilität** – die konvertierte Datei bleibt in Omniverse nutzbar!

</details>

### Unterstützte Standards und Plattformen

| Eingang | Ausgang |
| --- | --- |
| NVIDIA Omniverse USD (OmniPBR/MDL) | USDZ (Apple AR Quick Look) |
| OpenUSD mit proprietären Shadern | Apple Vision Pro (lokal, ohne Streaming) |
| UDIM-Textur-Layouts | iPhone & iPad (nativ, ohne App) |
| Bestehende Omniverse-Projekte | NVIDIA Omniverse (rückwärtskompatibel) |

<details>
<summary><strong>Warum kein Cloud-Streaming?</strong></summary>

Cloud-Streaming (z.B. NVIDIA Omniverse Cloud / Pixel Streaming) ist technisch möglich – scheitert in der Praxis aber häufig an banalen Voraussetzungen: instabiles WLAN auf Messen, keine Netzanbindung beim Kunden, sensible CAD-Daten, die das Unternehmen nicht verlassen sollen.

USDbridge ermöglicht [lokales Rendering](https://visales.de/foveated-streaming-openusd-visualisierung-ohne-server-infrastruktur/): Das USDZ-Asset liegt auf dem Gerät, läuft ohne Verbindung, ohne Latenz, ohne Infrastruktur-Abhängigkeit. Für Vertriebssituationen – Messe, Kundentermin, spontane Demo – ist das der zuverlässigere Weg.

</details>

<details>
<summary><strong>Läuft auf dem Mac – nah am Apple-Ökosystem</strong></summary>

USDbridge ist eine macOS-Applikation, optimiert für Apple Silicon (M-Chip). Das ist kein Zufall, sondern Prinzip: Die direkte Nähe zur Apple-Hardware ermöglicht präzise Konvertierung, sofortige Vorschau via Quick Look, und zuverlässige Ergebnisse für iPhone, iPad und Apple Vision Pro – ohne Umweg über Windows-Tools oder externe Dienste.

**Der typische Workflow:** Szene in Omniverse auf der Windows-Workstation fertigstellen, USDbridge auf dem Mac konvertieren, Ergebnis sofort prüfen und verteilen.

Für Teams, die bereits NVIDIA Nucleus im Einsatz haben, sprechen wir gern über weiterführende Workflow-Anbindungen.

</details>

### Zwei Wege zur Zusammenarbeit

**1: Als Dienstleistung:** Sie schicken uns Ihre Omniverse-Assets. Wir konvertieren, optimieren und liefern fertige USDZ-Dateien zurück – bereit für Vertrieb, Messe und Kundengespräch.

**2: Als wiederkehrender Workflow:** Für Teams, die regelmäßig neue Assets produzieren, richten wir einen strukturierten Konvertierungsprozess auf Ihrer Hardware ein. Ihre OpenUSD-Masterdatei bleibt in Omniverse. Die Ausgabe ist immer überall kompatibel.

## Für wen USDbridge sinnvoll ist – und für wen nicht

USDbridge ist dort sinnvoll, wo bereits in NVIDIA Omniverse produziert wird und diese Inhalte im Vertrieb auf Apple-Geräten eingesetzt werden sollen. Besonders wenn Außendienst oder Messeteams mit iPhone und iPad arbeiten und keine App-Installationen oder Server-Infrastruktur einsetzen können.

USDbridge ist kein Ersatz für eine durchdachte OpenUSD-Masterdaten-Strategie. Wer noch keine Omniverse-Inhalte hat oder neu in die 3D-Produktion einsteigt, profitiert stärker von einem OpenUSD-First-Workflow, der Kompatibilität von Anfang an einplant – nicht erst nachträglich herstellt.

→ [Mehr zu unserem OpenUSD-Ansatz](https://visales.de/5-warum-wir-bei-visales-konsequent-auf-openusd-first-setzen/)

<details>
<summary><strong>Typische Fragen aus Marketing & Vertrieb</strong></summary>

**Brauchen wir dafür neue Hardware oder Software auf unserer Seite?**

Nein. USDbridge läuft lokal bei uns – Sie schicken uns Ihre Assets, wir liefern fertige USDZ-Dateien zurück. Für einen wiederkehrenden Workflow richten wir den Prozess auf Ihrer vorhandenen mac-Hardware ein.

**Was passiert mit unseren CAD- und Konstruktionsdaten – verlassen sie unser Haus?**

Bei der Dienstleistungsvariante werden Assets für die Konvertierung übermittelt. Wer das vermeiden möchte, kann den Workflow direkt auf der eigenen Hardware betreiben. Das ist einer der Gründe, warum wir bewusst auf Cloud-Dienste verzichten.

**Wie aufwendig ist die erste Konvertierung?**

Das hängt vom Asset ab – Materialstruktur, Textur-Komplexität und Dateigröße spielen eine Rolle. Wir klären das am schnellsten anhand eines konkreten Beispiel-Assets.

**Können unsere Vertriebsmitarbeiter die USDZ-Dateien direkt einsetzen?**

Ja. Die Dateien laufen über Apple [AR Quick Look](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/) direkt auf iPhone und iPad – kein App-Download, keine IT-Freigabe notwendig. Starten, platzieren, erklären.

**Eignet sich USDbridge für jedes Omniverse-Asset?**

Nicht ohne Einschränkungen. Sehr komplexe Shader-Setups oder prozedural generierte Materialien erfordern manchmal Nacharbeit. Wir bewerten das anhand Ihrer konkreten Datei.

</details>

<details>
<summary><strong>Systemvoraussetzungen</strong></summary>

**Für die Konvertierung (USDbridge auf macOS):**

* Mac mit Apple Silicon (M1 oder neuer) empfohlen
* macOS aktuell
* USDZ-Quelldaten aus NVIDIA Omniverse (USD Composer oder vergleichbar)

**Für die Quell-Workstation (Windows/Linux):**

* NVIDIA Omniverse mit RTX-GPU
* Export als USD-Datei mit Texturen

**Für die Ausgabe:**

* Webserver mit MIME-Typ `model/vnd.usdz+zip` für direkte AR-Vorschau im Browser
* Alternativ dazu unseren AR-Web-Player oder unser Produkt [USDconfig](https://visales.de/usdconfig/)
* Oder direkte Übertragung auf Apple-Gerät via AirDrop, Mail oder eigene App

</details>

## 30 Minuten.   
Ihre Datei.   
Wir zeigen, wie es weitergehen kann

Nicht jede Anfrage muss sofort ein Projekt sein. Oft ist ein erstes gemeinsames Einordnen anhand eines konkreten Assets sinnvoller als eine schnelle Entscheidung.

**Ins Gespräch kommen:** Schicken Sie uns ein Beispiel-Asset oder beschreiben Sie, was Sie bisher nicht lösen konnten. Wir schauen gemeinsam, ob und wie USDbridge hilft. **Ohne Pitch, bei einer Tasse Tee oder Kaffee.**

**→** [Kontakt aufnehmen](https://visales.de/kontakt/)

&nbsp;

&nbsp;

## Häufige Fragen zu USDbridge

<details>
<summary><strong>Was ist USDbridge?</strong></summary>

USDbridge ist ein Konvertierungsdienst von viSales, der NVIDIA Omniverse-Assets automatisch in USDZ-Dateien umwandelt – plattformübergreifend nutzbar auf iPhone, iPad, Mac, im Browser und in der Apple Vision Pro.

</details>

<details>
<summary><strong>Welche Formate akzeptiert USDbridge als Eingabe?</strong></summary>

USDbridge verarbeitet primär OpenUSD- und Omniverse-Dateien. Auf Anfrage können auch FBX, OBJ oder STEP-Dateien aus CAD-Systemen als Ausgangsmaterial dienen.

</details>

<details>
<summary><strong>Wie lange dauert eine Konvertierung?</strong></summary>

Die Dauer hängt von der Komplexität des Assets ab – einfache Objekte in wenigen Stunden, komplexe Industrieanlagen mit Animationen in 1–3 Werktagen.

</details>

<details>
<summary><strong>Für wen ist USDbridge gedacht?</strong></summary>

USDbridge richtet sich an Industrieunternehmen, die 3D-Assets in NVIDIA Omniverse erstellt haben und diese nun für AR, Web und Apple Vision Pro nutzbar machen möchten.

</details>
