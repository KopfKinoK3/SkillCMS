---
title: "Augmented Reality für Produkte — Eine Roadmap für B2B"
slug: augmented-reality-produkte-roadmap-b2b
status: draft
meta_title: "AR für B2B-Produkte: OpenUSD vs. glTF — Roadmap 2025–2027"
meta_description: "Apple AR Quick Look vs. Android, OpenUSD vs. glTF 2.0, iOS 27-Features und drei Use Cases für AR-Produktkonfiguration im B2B-Vertrieb."
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
type: post
template: post
---

- **Apple AR Quick Look ist heute die leistungsfähigste Plattform für interaktive Produkterlebnisse — und die einzige, die ohne App-Download funktioniert.**
- **OpenUSD schlägt glTF 2.0 in jeder Kategorie, die für B2B-Produktkonfiguration relevant ist: VariantSets, Audiounterstützung, prozedurale Materialien, Multi-User.**
- **Mit iOS 27 (Mitte 2026) kommen Gaussian Splats, OpenPBR-Materialien und PCM-Kompression — der technische Vorsprung gegenüber dem Web-Standard wächst weiter.**


Du kennst das vermutlich: Du willst ein erklärungsintensives Produkt im Vertrieb zeigen — eine Maschine, ein Möbelstück, eine industrielle Komponente. Und irgendwann fällt der Satz: „Können wir das nicht in AR zeigen?“

Die Antwort ist ja. Aber die Frage, die danach kommt, ist entscheidend: Auf welcher Plattform? Denn was nach außen wie ein einheitliches Thema wirkt — „Augmented Reality“ — ist technisch eine Landschaft mit massiven Unterschieden.

Ich habe gerade ein internes Strategie-Briefing fertiggestellt, das diese Landschaft aufarbeitet. Nicht als Meinung, sondern als technischen Vergleich: Was kann Apple heute, was kann Android, was kommt als Nächstes — und was davon ist für B2B-Produkte tatsächlich relevant?

Die Ergebnisse sind eindeutig genug, dass ich sie hier teilen will.


Auf der Apple-Seite steht AR Quick Look, betrieben von RealityKit. Das ist seit dem iPhone 6S (iOS 12, 2018) verfügbar und wurde seitdem kontinuierlich ausgebaut. Interaktive Konfiguration über VariantSets gibt es seit iOS 14, prozedurale Materialien seit iOS 18. Auf der Vision Pro kommt mit SharePlay sogar ein Multi-User-Modus dazu, in dem bis zu fünf Personen gemeinsam ein Produkt in AR betrachten.

Auf der Android-Seite gibt es zwei Wege: Googles SceneViewer und WebXR. Der SceneViewer wurde vor rund fünf Jahren hinzugefügt und seitdem nie aktualisiert. Er unterstützt 4 von über 40 KHR-Extensions, kein Audio, keine prozeduralen Materialien, kein Multi-User. WebXR ist technisch leistungsfähiger, erfordert aber eine vollständige WebApp (PlayCanvas, BabylonJS oder ThreeJS), läuft nur auf High-End-Geräten performant und hat keinen nativen Multi-User.

Wenn du im B2B-Vertrieb ein Produkt zeigen willst, das der Kunde konfigurieren, in den Raum stellen und mit Kollegen besprechen soll — dann gibt es heute genau eine Plattform, die das ohne App-Download und ohne WebApp-Infrastruktur kann.


Das Dateiformat bestimmt, was möglich ist. glTF 2.0 ist der Web-First-Standard: Rendering über WebGL/WebGPU, Kompression via DRACO, Interaktivität nur über KHR-Extensions in einer WebApp. Kein Audio, keine prozeduralen Materialien, kein Multi-User, und die Konfigurierbarkeit beschränkt sich auf einzelne Material-Swaps.

OpenUSD — in Apples Ökosystem als USDZ verpackt — läuft auf RealityKit und bietet: native VariantSets für Geometrie, Materialien und ganze Szenen, volle Audiounterstützung, prozedurale Materialien über OpenPBR/MaterialX (ab iOS 18), und Multi-User über SharePlay auf der Vision Pro. Die Geometriekompression via PCM ist 42% effizienter als DRACO.

glTF 2.1 wird einige dieser Lücken schließen — geschätzte Verfügbarkeit: um 2027. Bis dahin ist der technische Abstand groß.


Mitte 2026 steht das nächste große Apple-Update an. iOS 27 bringt fünf Features, die direkt in die B2B-Produktkommunikation einzahlen:

OpenPBR und MaterialX liefern industrie-standardkonforme Materialien, die in professionellen Render-Pipelines genauso aussehen wie auf dem iPhone. SubD Patch Geometry mit Displacement Maps ersetzt klassische LOD-Strategien — ein einziges Asset funktioniert auf allen Distanzen. Gaussian Splats ermöglichen photorealistische Umgebungsscans als native USD-Assets. Mesh Instances rendern tausende identische Bauteile (Schrauben, Fliesen, Blätter) mit minimalem Speicherverbrauch. Und PCM-Kompression reduziert die Dateigröße um 42% gegenüber DRACO — entscheidend für große Kataloge.


Was in dem Briefing am meisten Eindruck macht, sind nicht die Specs — sondern die konkreten Anwendungen, die heute bereits laufen:

Ein Produktkonfigurator in AR Quick Look. Der Kunde scannt einen QR-Code, das Produkt steht in seinem Raum, und er konfiguriert Stoffe, Oberflächen und Armlehnen direkt in der nativen Kamera-App. Kein Download, kein Account, kein Login. Funktioniert auf jedem iPhone seit dem 6S.

Kollaborative AR auf der Vision Pro. Bis zu fünf Personen — lokal oder remote — betrachten das gleiche Produkt gleichzeitig in AR. Position, Skalierung, Rotation und Konfiguration werden über SharePlay synchronisiert. Kaufentscheidungen im Team, ohne dass jemand in einen Showroom fahren muss.

Und der dritte: Ein Besprechungsraum wird in AR eingerichtet, bevor die Möbel bestellt werden. Ein komplettes Raumlayout wird im Vorfeld zusammengestellt, die Gruppe steht gemeinsam im virtuellen Raum und diskutiert die Auswahl. Die Entscheidung fällt, bevor ein einziges Stück physisch bewegt wird.


Wir konzentrieren uns bewusst auf B2B-Branchen, in denen Apple-Geräte bereits dominieren — Architektur, Inneneinrichtung, Maschinenbau. Der Grund ist einfach: Unsere Kunden und deren Kunden nutzen bereits iPhones und iPads. Die Hardware ist da, die Plattform ist ausgereift, und der Technologievorsprung gegenüber dem Web-Standard beträgt aktuell zwei bis drei Jahre.

Wir warten nicht auf glTF 2.1. Wenn der Web-Standard 2027 soweit ist, haben wir produktionserprobte Assets, die sich auf WebApps und WebXR erweitern lassen. Die Investition in OpenUSD ist keine Sackgasse — sie ist ein Vorsprung.

Viele Grüße aus Velbert,

Gerhard Schröder

PS: Wenn es zu dem Thema Gesprächsbedarf bei einer Tasse Remote-Tee oder -Kaffee gibt, [einfach melden](https://visales.de/kontakt).

Überblick AR im Vertrieb: [Augmented Reality im B2B-Vertrieb](https://visales.de/augmented-reality/)

Tool für AR-Produktkonfiguration: [USDconfig](https://visales.de/usdconfig/)
