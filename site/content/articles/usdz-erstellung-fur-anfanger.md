---
title: "USDZ-Erstellung für Anfänger"
slug: usdz-erstellung-fur-anfanger
status: published
meta_title: "USDZ erstellen ohne Programmierung: Tools & Anleitung 2026"
meta_description: "USDZ-Dateien erstellen als Einsteiger — kostenlose Tools wie Reality Composer Pro, passende Hardware ab 700 € und Schritt-für-Schritt-Workflow für AR-Inhalte."
feature_image: /assets/images/2026/03/OpenUSD-USDZ-Erstellung-f--r-Anf--nger.001.jpeg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-03-23T15:22:18.000Z"
type: post
template: post
faq_heading: "Häufige Fragen zu USDZ"
faq:
  - q: "Kann man eine USDZ-Datei bearbeiten?"
    a: "Nicht direkt. Eine USDZ ist ein gepacktes Archiv (ZIP ohne Kompression). Um Änderungen vorzunehmen, arbeitet man am Quellformat (.usda oder .usd) und exportiert anschließend erneut als USDZ. Tools wie Reality Composer Pro oder Blender übernehmen diesen Schritt automatisch."
  - q: "Welche Software brauche ich, um USDZ-Dateien zu erstellen?"
    a: "Für den Einstieg ohne Programmierkenntnisse eignen sich Reality Composer Pro (kostenlos von Apple, benötigt einen Mac mit M1 oder neuer) und das Open-Source-Projekt Deconstructed. Beide sind Point-and-Click-Werkzeuge. Fortgeschrittene nutzen Blender mit USDZ-Export."
  - q: "Brauche ich einen Mac, um USDZ-Dateien zu erstellen?"
    a: "Für die meisten No-Code-Tools ja — Reality Composer Pro läuft nur auf macOS. Einen gebrauchten Mac Mini mit M1-Chip gibt es ab ca. 300 Euro. Auf Windows bleibt aktuell der Weg über NVIDIA Omniverse oder Blender mit USDZ-Export-Plugin."
  - q: "Was ist der Unterschied zwischen USD und USDZ?"
    a: "USD (Universal Scene Description) ist das offene 3D-Austauschformat von Pixar. USDZ ist die gepackte Variante: Alle Texturen, Materialien und Geometrien in einer einzigen Datei — optimiert für AR-Anwendungen auf iPhone und iPad. USDZ ist also das Endprodukt, USD das Arbeitsformat."
ki_text: true
ki_bild: true
---

Du interessiert Dich für OpenUSD und dem Dateiformat USDZ? Du bist kein Programmierer, vielleicht eher ein Grafiker oder einfach ein interessierter Mensch, der selbst mal solche AR-Inhalte erstellen will? Da gibt es No-Code / Low-Code-Tools zum ausprobieren.

Dann ist dieser Ratgeber genau für Dich gedacht.

<details>
<summary><strong>Du bist Programmierer?</strong></summary>

**Wunderbar:** Du kannst Dir gern die [USDZ-Apple Developer-Doku](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/usdz) anschauen. Das ist eher unser Weg...

**Oder:** Du kannst Dir die [kostenlosen Tutorials von NVIDIA](https://docs.omniverse.nvidia.com/dev-guide/latest/tutorials.html) anschauen, dazu benötigst Du jedoch einen Windows-PC mit einer NVIDIA Grafikkarten.

In dem Beitrag [NVIDIA Omniverse, eine Einordnung für den Mittelstand](https://visales.de/nvidia-omniverse-mittelstand/) gibt es auch Angaben zu den technischen Mindestspezifikationen an den Rechner.

</details>

## Hardware zum Start: MacMini & iPad/iPhone

Um im Apple-Ökosystem eine USDZ-Datei für AR erstellen zu können sollte man wenigstens ein MacMini benutzen können. [Modelle mit M1-Prozessor - *M2-M5 gehen auf jeden Fall auch* - gibt es bei Ebay ab ca. 300 Euro](https://www.ebay.de/sch/i.html?_nkw=macmini&_sacat=0&_from=R40&_trksid=p4624852.m570.l1313). Man kann sich dann die erstellten Inhalte mit der Quick-Look-Funktion am Mac anschauen, aber zum echten AR-Erlebnis sollte man ein günstiges iPad oder iPhone nutzen. Das iPhone sollte mindestens ein 6S sein, neuere Modelle sind hier immer besser, auch so ein Gerät bekommt man günstig bei Ebay.

<details>
<summary><strong>Was ist mit Windows-PCs?</strong></summary>

Bisher gibt es noch keinen [No-Code / Low-Code Editor für USDZ](https://visales.de/openusd-ohne-apple-wer-baut-ein-nocode-tool-fur-windows/) auf Windows-Basis. Da bleibt bisher nur der beschwerliche Weg via NVIDIA Omniverse > Siehe "Du bist Programmierer?"

</details>

## Software zum Start: Reality Composer Pro oder Deconstructed

Als Werkzeug zur Bearbeitung bietet sich das kostenlose Tool [Reality Composer Pro](https://developer.apple.com/augmented-reality/tools/) von Apple an, alternativ dazu gibt es auch das [OpenSource-Projekt Deconstructed](https://visales.de/openusd-ohne-apple-wer-baut-ein-nocode-tool-fur-windows/). Die Programme sind Point-n-Click-Werkzeuge und können ohne Programmierkenntnisse ausprobiert werden. 

<details>
<summary><strong>USDZ Datei bearbeiten — geht das überhaupt?</strong></summary>

Die häufigste Frage nach dem Erstellen: Kann ich eine USDZ-Datei nachträglich bearbeiten? Die kurze Antwort: Nicht direkt. Eine USDZ ist technisch ein **gepacktes ZIP-Archiv** ohne Kompression. Man kann sie nicht öffnen und verändern wie eine Word-Datei.

**Der Workflow in der Praxis:** Du arbeitest immer am Quellformat — also an der .usda, .usdc oder .usd Datei. Dort änderst Du Materialien, Positionen oder Geometrie. Danach exportierst Du erneut als USDZ. Tools wie Reality Composer Pro oder Blender machen das automatisch: Öffnen, bearbeiten, als USDZ speichern. Die USDZ selbst ist das Endprodukt — vergleichbar mit einem PDF.

**Praxistipp:** Behalte immer Deine Quelldateien (.usda/.usd). Wer nur die fertige USDZ aufhebt, steht bei Änderungen vor einem Problem. Für fortgeschrittene Nutzer: Mit dem Kommandozeilen-Tool `usdzconvert` von Apple lässt sich eine USDZ auch entpacken und neu zusammensetzen.

Bei B2B-Projekten mit vielen Produktvarianten übernehmen wir diesen Workflow komplett — von der CAD-Datei bis zur fertigen USDZ für AR.

→ [Mehr über unseren Ansatz](https://visales.de/openusd-dienstleister/)

</details>

&nbsp;

&nbsp;

### Du willst wissen ob USDZ für dein Produkt passt?

In 30 Minuten sortieren wir gemeinsam, ob und wo AR in eurem Vertrieb konkret etwas bringt — ohne Pitch, ohne Angebot. Kein Verkaufsdruck, eine ehrliche Einordnung.* ***Rheingas und Somfy haben so angefangen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

## Wie kommt man an die 3D-Dateien?

In [Der Weg zur 3D-Datei für alle Zwecke: OpenUSD & .usdz](https://visales.de/der-weg-zur-3d-datei-fur-alle-zwecke-openusd-usdz/) habe ich einige Wege ausgeführt, darunter 3D-Werkzeuge wie das kostenlose [Blender](https://www.blender.org). Für den absoluten Einsteiger hier noch weitere Wege:

**Kostenloser Download (1)** [Sketchfab](https://sketchfab.com/search?q=USDZ&type=models): Die Website bietet einige Modelle an, nicht alle sind Kostenlos: Ich rate - *keine Rechtsberatung* - von jeglicher kommerzieller Nutzung ohne genaues Studium der AGBs und des Lizenzvertrags ab. Für erste Experimente ist es aber ein Weg zu einer Datei. Zum Start schlage ich ein einfaches 3D-Objekt vor.

**Kostenloser Download (2) **[Turbosquit](https://www.turbosquid.com/de/Search/3D-Models?certification_id=7&max_poly=100K&min_poly=0K&file_type=1024): Bietet eine ganze Reihe guter Modelle an, größtenteils zu guten Preisen. Kostenlos ist zum Beispiel der [Golfball](https://www.turbosquid.com/de/3d-models/golfball-lowpoly-3d-model-2515171).

**Claude Code:** Ich habe selbst schon mit der KI von [Claude Code](https://claude.ai/) einfache 3D-Modelle als USDZ Dateien erzeugen können. Prompt-Vorschläge wie "Mach mir einen Würfel als USDZ-Datei" sollten gehen.

## Nächster Schritt: Reality Composer Pro (oder Deconstructed) ausprobieren

[Embed: https://www.youtube.com/watch?v=KaTqrRfvZkM](https://www.youtube.com/watch?v=KaTqrRfvZkM)

## Arbeitsergebnisse: USDZ & AR zum Ausprobieren

Apple bietet auf einer Demo-Seite einige Beispiele an. Direkt die Seite mit einem iPhone oder iPad starten: [Quick Look Gallery](https://developer.apple.com/augmented-reality/quick-look/). Von meiner Agentur hier ein Beispiel, welches man via QR Code ausprobieren kann, ist unser [Igus-Startprojekt ](https://www.youtube.com/watch?v=dDTESsqB8HI)gewesen.

![](/assets/images/2026/03/Produktspr--sentation.jpeg)

Viel Spaß beim Ausprobieren!

&nbsp;

&nbsp;

### Einstieg in USDZ — mit Unterstützung.

Wir begleiten Unternehmen vom ersten USDZ-Modell bis zum eingebetteten AR-Erlebnis im Vertrieb. Das erste Gespräch dauert 30 Minuten. Ohne Pitch, ohne Vorbereitungspflicht.* ***Rheingas, Somfy und Carl Hamm haben mit einem Produkt begonnen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

**Die Vorgeschichte:** Am 18. März 2026 habe ich im Rahmen des Heidelberger XR-Symposiums einen Vortrag über [OpenUSD für Entscheider](https://visales.de/openusd/) gehalten. Am Ende kam von einem der vielen Zuschauer die Frage:** **"**Wie kann ich denn nun mit OpenUSD anfangen?**" Das führte zu den heutigen Zeilen für die Blog-Kategorie [OpenUSD & USDZ](https://visales.de/tag/openusd-usdz/). Mehr unter...

→ Praxiseinsatz von AR: [AR im B2B-Vertrieb – der große Überblick](https://visales.de/augmented-reality/)  
→ OpenUSD im Einsatz: [USDZ & OpenUSD für den Vertrieb](https://visales.de/openusd-dienstleister/)

&nbsp;

&nbsp;
