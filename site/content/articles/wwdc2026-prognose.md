---
title: "WWDC26: Prognosen* zum Thema 3D & AR von viSales"
slug: wwdc2026-prognose
status: published
primary_tag: apple
tags: [apple, augmented-reality, 3d-visualisierung]
feature_image: /assets/images/2026/03/wwdc26-visales-prognose.jpg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-03-24T23:42:30.000Z"
type: post
template: post
faq_heading: "Typische Entscheiderfragen"
faq:
  - q: "Was kann Apple AR Quick Look heute, was Android nicht kann?"
    a: "Apple AR Quick Look läuft seit iOS 12 auf jedem iPhone ohne App-Download. Es unterstützt interaktive Konfiguration via VariantSets, Audiounterstützung, prozedurale Materialien und Multi-User über SharePlay. Googles SceneViewer wurde seit fünf Jahren nicht aktualisiert und unterstützt nur 4 von 40 KHR-Extensions – kein Audio, keine prozeduralen Materialien, kein Multi-User. → Apple vs. Android AR: Unterschiede erklärt"
  - q: "Warum ist OpenUSD besser als glTF&nbsp;2.0 für B2B-Produktkonfiguration?"
    a: "OpenUSD bietet native VariantSets für Geometrie und Materialien, volle Audiounterstützung, prozedurale Materialien über OpenPBR/MaterialX sowie Multi-User über SharePlay. glTF&nbsp;2.0 unterstützt kein Audio, keine prozeduralen Materialien und keine native Konfiguration. glTF&nbsp;2.1 soll einige Lücken schließen – frühestens 2027.→ OpenUSD – Was ist das?→ OpenUSD: Geschichte &amp; Strategie"
  - q: "Was bringt iOS&nbsp;27 für B2B-Produktkommunikation?"
    a: "iOS&nbsp;27 (Mitte 2026) bringt OpenPBR &amp; MaterialX für industriekonforme Materialien, Gaussian Splats als native USD-Assets, SubD Patch Geometry für effiziente 3D-Assets sowie PCM-Kompression mit 42&nbsp;% kleineren Dateien gegenüber DRACO. Entscheidend für große Produktkataloge."
  - q: "Kann ich AR Quick Look ohne App-Download nutzen?"
    a: "Ja. AR Quick Look läuft direkt in der nativen Kamera-App auf jedem iPhone seit dem 6S (iOS&nbsp;12). Kein Download, kein Account, kein Login. Ein QR-Code reicht – das Produkt erscheint direkt im Raum des Kunden."
ki_text: true
---

- **Apple **[**AR Quick Look**](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/)** ist heute die leistungsfähigste Plattform für interaktive Produkterlebnisse und die einzige, die ohne App-Download funktioniert.**
- [**OpenUSD**](https://visales.de/openusd/)** schlägt glTF 2.0 in jeder Kategorie, die für B2B-Produktkonfiguration relevant ist: VariantSets, Audiounterstützung, prozedurale Materialien, Multi-User.**
- **Mit iOS 27 (Mitte 2026) kommen Gaussian Splats, OpenPBR-Materialien und PCM-Kompression = der technische Vorsprung gegenüber dem alten Web-Standard wächst weiter.**

&nbsp;

&nbsp;

> Apple hat vorgestern zur nächsten Entwicklerkonferenz [WWDC26](https://www.apple.com/de/newsroom/2026/03/apples-worldwide-developers-conference-returns-the-week-of-june-8/) ab dem 8. Juni eingeladen und wir werfen dazu einen Blick in die Betas / unter die Motorhaube der Apple-Software-Systeme.

## AR im B2B-Vertrieb: Zwei Welten, eine klare Entscheidung

Du kennst das vermutlich: Du willst ein erklärungsintensives Produkt im Vertrieb zeigen — eine Maschine, ein Möbelstück, eine industrielle Komponente. Und irgendwann fällt der Satz: „Können wir das nicht in AR zeigen?“

Die Antwort ist ja. Aber die Frage, die danach kommt, ist entscheidend: [Auf welcher Plattform](https://visales.de/apple-vs-android-augmented-reality-unterschiede-erklart/)? Denn was nach außen wie ein einheitliches Thema wirkt — „Augmented Reality“ — ist technisch eine Landschaft mit massiven Unterschieden.

Ich habe gerade ein internes Strategie-Briefing fertiggestellt, das diese Landschaft aufarbeitet. Nicht als Meinung, sondern als technischen Vergleich: [Was kann Apple heute, was kann Android](https://visales.de/apple-vs-android-augmented-reality-unterschiede-erklart/), was kommt als Nächstes — und was davon ist für B2B-Produkte tatsächlich relevant?

Die Ergebnisse sind eindeutig genug, dass ich sie hier teilen will.

<details>
<summary><strong>Apple vs. Android: Der Zustand, der nicht in der Presse steht</strong></summary>

Auf der Apple-Seite steht [AR Quick Look](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/), betrieben von Apples RealityKit. Das ist seit dem iPhone 6S (iOS 12, **2018**) verfügbar und wurde seitdem kontinuierlich ausgebaut. Interaktive Konfiguration über VariantSets gibt es seit iOS 14, prozedurale Materialien seit iOS 18. Auf der Vision Pro kommt mit SharePlay sogar ein Multi-User-Modus dazu, in dem bis zu fünf Personen gemeinsam ein Produkt in AR betrachten. Auf dem iPhone & iPad gehen via SharePlay gemeinsame AR-Sessions im Videocall (Bildschirmfreigabe).

**Auf der Android-Seite gibt es zwei Wege: Googles SceneViewer und WebXR.**

Der SceneViewer wurde vor rund fünf Jahren hinzugefügt und seitdem nie aktualisiert. Er unterstützt 4 von über 40 KHR-Extensions, kein Audio, keine prozeduralen Materialien, kein Multi-User. WebXR ist technisch leistungsfähiger, erfordert aber eine vollständige WebApp (PlayCanvas, BabylonJS oder ThreeJS), läuft nur auf High-End-Geräten performant und hat keinen nativen Multi-User.

Wenn du im B2B-Vertrieb ein Produkt zeigen willst, das der Kunde konfigurieren, in den Raum stellen und mit Kollegen besprechen soll — dann gibt es heute genau eine Plattform, die das ohne App-Download und ohne WebApp-Infrastruktur kann.

</details>

<details>
<summary><strong>glTF 2.0 vs. OpenUSD: Der Vergleich, den man kennen sollte</strong></summary>

Das Dateiformat bestimmt, was möglich ist. glTF 2.0 ist der Web-First-Standard: Rendering über WebGL/WebGPU, Kompression via DRACO, Interaktivität nur über KHR-Extensions in einer WebApp. Kein Audio, keine prozeduralen Materialien, kein Multi-User, und die Konfigurierbarkeit beschränkt sich auf einzelne Material-Swaps.

OpenUSD — in Apples Ökosystem als USDZ verpackt — läuft auf RealityKit und bietet: native VariantSets für Geometrie, Materialien und ganze Szenen, volle Audiounterstützung, prozedurale Materialien über OpenPBR/MaterialX (ab iOS 27 vollständig umgesetzt), und Multi-User über SharePlay auf der Vision Pro. Die Geometriekompression via PCM ist 42% effizienter als DRACO.

glTF 2.1 wird einige dieser Lücken schließen — geschätzte Verfügbarkeit: um 2027. Bis dahin ist der technische Abstand groß.

**Und Apple schläft nicht!**

</details>

## Was mit der WWDC 2026 & iOS 27 kommt und warum das für dich relevant ist

Mitte 2026 steht das nächste große Apple-Update an. iOS 27 bringt fünf Features, die direkt in die B2B-Produktkommunikation einzahlen:

- **OpenPBR & **[**MaterialX**](http://materialx.org) – Industrie-standardkonforme Materialien, die in professionellen Render-Pipelines genauso aussehen wie auf dem iPhone.
- **SubD Patch Geometry mit Displacement Maps** – Ersetzt klassische LOD-Strategien. Ein einziges Asset funktioniert auf allen Distanzen.
- **Gaussian Splats** – Photorealistische Umgebungsscans als native USD-Assets.
- **Mesh Instances** – Tausende identische Bauteile (Schrauben, Fliesen, Blätter) mit minimalem Speicherverbrauch rendern.
- **PCM-Kompression** – 42 % kleinere Dateien gegenüber DRACO. Entscheidend für große Kataloge.

## Drei Use Cases, die heute schon funktionieren

Was in dem Briefing* am meisten Eindruck macht, sind nicht die Specs — sondern die konkreten Anwendungen, die heute bereits laufen:

**Ein Produktkonfigurator in AR Quick Look**. Der Kunde scannt einen QR-Code, das Produkt steht in seinem Raum, und er konfiguriert Stoffe, Oberflächen und Armlehnen direkt in der nativen Kamera-App. Kein Download, kein Account, kein Login. Funktioniert auf jedem iPhone seit dem 6S.

→ [USDconfig](https://visales.de/usdconfig/)

**Kollaborative AR auf der Vision Pro**. Bis zu fünf Personen — lokal oder remote — betrachten das gleiche Produkt gleichzeitig in AR. Position, Skalierung, Rotation und Konfiguration werden über SharePlay synchronisiert. Kaufentscheidungen im Team, ohne dass jemand in einen Showroom fahren muss.

→ [Fallbeispiel zgoll](https://visales.de/fallbeispiel-zgoll-wenn-das-fussballstadion-zum-augmented-reality-showroom-wird/)

**Und der dritte**: Ein Besprechungsraum wird in AR eingerichtet, bevor die Möbel bestellt werden. Ein komplettes Raumlayout wird im Vorfeld zusammengestellt, die Gruppe steht gemeinsam im virtuellen Raum und diskutiert die Auswahl. Die Entscheidung fällt, bevor ein einziges Stück physisch bewegt wird.

## Die strategische Einordnung

Wir konzentrieren uns bewusst auf B2B-Branchen, in denen Apple-Geräte bereits dominieren — AeroSpace, Defence, Maschinenbau und Architektur / Inneneinrichtung. Der Grund ist einfach: Unsere Kunden und deren Kunden nutzen bereits iPhones und iPads. Die Hardware ist da, die Plattform ist ausgereift, und der **Technologievorsprung gegenüber dem Web-Standard beträgt aktuell zwei bis drei Jahre**.

Wir warten nicht auf glTF 2.1. Wenn der Web-Standard 2027 soweit ist, haben wir produktionserprobte Assets, die sich auf WebApps und WebXR erweitern lassen.

> **Die Investition in OpenUSD ist keine Sackgasse, sie ist ein Vorsprung.**

&nbsp;

&nbsp;

*) Wir haben für eine Kundenanalyse mal vor ein paar Tagen die aktuellen Fakten zusammengetragen und geben hier einen kleinen Teil an die Öffentlichkeit.

&nbsp;

&nbsp;

&nbsp;

&nbsp;

### **Du willst wissen ob AR im B2B-Vertrieb für dein Produkt passt?**

In 30 Minuten sortieren wir gemeinsam, ob und wo AR in eurem Vertrieb konkret etwas bringt — ohne Pitch, ohne Angebot. Kein Verkaufsdruck, eine ehrliche Einordnung. **Rheingas und Somfy haben so angefangen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;
