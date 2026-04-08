---
title: "ConfigXR: AR-Produktkonfigurator mit Apple AR Quick Look"
slug: usdz-ar-produktkonfigurator-arql-configxr
status: published
primary_tag: openusd
tags: [openusd, produktkonfigurator, usdz, augmented-reality]
meta_title: "ConfigXR – AR-Produktkonfiguratoren mit AR Quick Look"
meta_description: "ConfigXR erstellt interaktive AR-Produktkonfiguratoren mit Apple AR Quick Look und USDZ. Ohne App-Download, direkt im Browser. Open Source."
feature_image: /assets/images/2026/03/Verkaufen_Stuhl_Header.jpg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-04-01T07:01:08.000Z"
type: post
template: post
faq_heading: "Typische Entscheiderfragen"
faq:
  - q: "Was ist ein interaktives USDZ und wie unterscheidet es sich von einem normalen USDZ?"
    a: "Ein normales USDZ ist ein statisches 3D-Archiv – es zeigt ein einzelnes Modell in Augmented Reality, ohne Interaktion. Ein interaktives USDZ (interactiveUSDZ) hingegen enthält mehrere Assets, Nutzerinteraktionen, Physik-Simulation und sogar szenenübergreifende Logik. Apple hat dieses erweiterte Format ab iOS 13.1 eingeführt. AR Quick Look fungiert dabei als vorinstallierte AR-Game-Engine, die diese interaktiven Szenen direkt abspielen kann – ohne App-Download, ohne Installation."
  - q: "Braucht der Kunde eine App, um den AR-Konfigurator zu nutzen?"
    a: "Nein. Apple AR Quick Look ist auf jedem iPhone und iPad ab iOS 12 vorinstalliert. Der Kunde öffnet einfach einen Link auf der Produktseite – die AR-Szene startet sofort im Browser, ohne App Store, ohne Download, ohne Wartezeit. Das senkt die Einstiegshürde im Vertrieb erheblich. Mehr dazu im Artikel AR Quick Look mit Banner – Apple baut die AR-Kauftaste in Safari."
  - q: "Welche 3D-Formate und CAD-Daten lassen sich in AR-Konfiguratoren umwandeln?"
    a: "Die Pipeline unterstützt den Export aus Blender (via Python-Skript) in das USDZ-Format. Geometrie, Materialien, UV-Maps und Texturen werden automatisch übernommen. Für die Konvertierung von CAD-Daten aus gängigen Maschinenbau-Formaten (STEP, IGES, JT) in AR-fähige Assets bietet viSales mit USDbridge eine eigene Lösung, die den gesamten Konvertierungsprozess automatisiert."
  - q: "Was ist der Unterschied zwischen ConfigXR und USDconfig?"
    a: "ConfigXR war das Open-Source-Pionierprojekt (2022 auf GitHub veröffentlicht), mit dem viSales die Grundlagen für interaktive AR-Produktkonfiguratoren per USDZ geschaffen hat. USDconfig ist die professionelle Weiterentwicklung für B2B-Kunden: optimierte Pipeline, breitere Format-Unterstützung, einfachere Integration in bestehende Webshops und Vertriebsprozesse. ConfigXR bleibt als Referenz und Lernressource verfügbar."
  - q: "Funktioniert AR Quick Look auch auf Android-Geräten?"
    a: "AR Quick Look ist eine Apple-Technologie und läuft ausschließlich auf iOS und iPadOS. Für Android-Geräte gibt es WebXR als Alternative, die über den Chrome-Browser funktioniert – allerdings mit anderen technischen Anforderungen. Eine detaillierte Gegenüberstellung beider Plattformen findest du im Artikel Apple vs. Android: Augmented Reality Unterschiede erklärt."
---

> Diese Seite ist die archivierte deutsche Dokumentation zum GitHub-Projekt **ConfigXR**, welches wir 2022 OpenSource gegeben haben: [github.com/.../ConfigXRBuilder](https://github.com/KopfKinoK3/ConfigXRBuilder?ref=visales.de) Mehr dazu unter [Verkaufen mit dem Augmented Reality-Stuhl-Konfigurator: AR mit *.usdz und *.reality](https://visales.de/verkaufen-mit-dem-augmented-reality-stuhl-konfigurator-ar-mit-usdz-reality/) Unser Nachfolgeprodukt ist [USDconfig](https://visales.de/usdconfig/).

## Was erstellt ConfigXR?

Dieser Workflow erstellt den kompletten HTML/JS-Code (in Elm) für eine mehrsprachige Landingpage – eine produktspezifische WebApp – sowie passende interaktive AR-Szenen (eine pro Sprache), die sich per Apple [AR Quick Look](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/) (ARQL) direkt von dieser Landingpage starten lassen. Eine WebXR-Version für Android-Geräte ist in der Roadmap.

Dieselbe WebApp kann auch mit einem URL-Parameter aufgerufen werden, der die in AR vorgenommenen Konfigurationsänderungen abbildet – oder den Nutzer direkt in den Webshop weiterleitet, inklusive passender Query-Parameter oder Shop-ID.

### Warum wird das gebraucht?

Viele Webshop-Frameworks erlauben zwar Produktanpassungen, laden dabei aber bei jeder Änderung die Seite vom Server neu. Das ist mit keiner bekannten WebAR/WebXR-Lösung kompatibel, um ein Produkt per CMS-Plugin zu konfigurieren. Nur eine dedizierte WebApp mit einem Headless CMS oder einer vergleichbaren Lösung kann dieses Problem lösen.

![](/assets/images/2026/03/AR-Produktkonfigurator_viSales.png)

![](/assets/images/2026/03/ConfigXR-Demo-AR-USDZ-Konfigurator.png)

![](/assets/images/2026/03/productpage3.png)

![](/assets/images/2026/03/Swivel_Snapshot.PNG)
***Webshop-Weiterleitung***

## Apple AR Quick Look und RealityOS

### Getroffene Entscheidungen

Als Pixar auf der SIGGRAPH 2015 USD (Universal Scene Description) als Open-Source-Framework vorstellte – die fünfte Generation ihres hauseigenen Systems für riesige Filmszenen mit Tausenden 3D-Assets, an denen Hunderte Künstler gleichzeitig arbeiten – war das Staunen groß.

Pixar nutzte High-End-GPUs von NVIDIA für das Realtime-Viewport. NVIDIA warb daraufhin viele Pixar-Entwickler ab, um an Omniverse zu arbeiten – heute genutzt, um High-End RTX-Karten und Server an Enterprise-Kunden zu verkaufen.

Apple entschied sich, seine geheimen VR/MR-Bemühungen umzubauen und USD zu einem zentralen Bestandteil seiner Strategie zu machen. Auch Unternehmen wie Adobe/Substance, Autodesk und diverse VFX-Anbieter wechselten zu USD.

### AR Quick Look ab iOS 12

2018 kündigte Apple USDZ-AR-Unterstützung für iPhones und iPads mit iOS 12 an. Geräte, die auf iOS 12 blieben, können nur einzelne AR-Assets darstellen.

### Interaktive USDZ ab iOS 13.1

Mit iOS 13.1 veröffentlichte Apple ein erweitertes AR Quick Look – eine AR-fokussierte Game Engine Runtime mit Nutzerinteraktionen und Physik-Simulation, vorinstalliert auf allen iOS-Geräten. Dazu den Reality Composer als Editor für interaktive Szenen. Das erweiterte USDZ-Format speichert nicht nur ein, sondern viele Assets in mehreren interaktiven Szenen – interactiveUSDZ.

Apple ermöglichte sogar das gleichzeitige Laden mehrerer (auch interaktiver) USDZ-Dateien, die individuell im Raum platziert werden können.

### Der Weg zu RealityOS

Apple bereitete intern bereits eine Stereo-AR-Version für iPhones vor. Die Hardware-Vorbereitung umfasste: mehr RAM, GPU-Leistung für Multi-View-Rendering, Metal-API für bis zu 16 Kamera-Views parallel, UltraWide-Kamera für Hand-/Fingertracking, U1-Chip für präzises Device-Tracking, und AirTags als MR-Tracking-Anker.

Auf der Software-Seite: Hand-/Fingertracking (ab iOS 14), Metal 3 (ab iOS 16 für iPhone 11+), SharePlay, RealityKit und RealityOS.

## Revolution für XR

Während alle auf Apples nächstes großes Ding warteten, haben einige den Köder geschluckt: Apple exportiert interactiveUSDZ in einem Open-Source-Format aus dem Reality Composer. Der Tech-Stack wurde reverse-engineered – so entstand eine eigene Pipeline für den Export von interactiveUSDZ, angefangen mit Produktkonfiguratoren (ConfigXR).

Das Revolutionäre an Apples Konzept: Es hat das Potenzial, die meisten kosten- und zeitintensiven Schritte zu eliminieren, die eine XR-Experience heute durchlaufen muss.

### Der alte Weg vs. der neue Weg

**Bisher:** 3D-Daten an Spezialisten übergeben → Game-Engine-Team baut dutzende App-Varianten → Monate warten → Rechtliche Freigabe pro Variante → App-Store-Einreichung → Erneut Monate warten auf Freigabe → OTA-Updates.

**Jetzt:** Geometrie, Materialien und Game-Logik in eine USDZ-Datei exportieren → Auf der Website hosten → Vertrieb bettet Link in Produktseite ein → Kunde öffnet AR Quick Look direkt → USDZ auf dem Server aktualisieren = Kunde bekommt immer die neueste Version.

## USD – Universal Scene Description

USD ist das universelle Szenen-Beschreibungsformat, ursprünglich von Pixar entwickelt. Weitere Informationen unter openUSD.org.

### Apples AR-Erweiterungen für USD

Das Framework nutzt Apples "preliminary_"-Schemas für: 3D-Text in AR Quick Look (reduziert Dateigrößen drastisch), Interaktionen und Physik auf 3D-Modellen im AR-Raum, sowie Animationen, die per Handgeste ausgelöst werden.

## Technische Basis

### Elm – Funktionale Frontend-Sprache

ConfigXR nutzt die funktionale Programmiersprache Elm. Vorteile: einfaches Refactoring, Garantie gegen Runtime-Fehler, striktes Typing. Für die Erstellung eines interaktiven Konfigurators muss man Elm nicht lernen – es reicht, ein produktbezogenes Modul anzulegen und Varianten als Datenstruktur zu deklarieren.

### Tauri – Leichtgewichtige Alternative zu Electron

Tauri ist in Rust geschrieben und eine schlanke Alternative zu Electron. Das gesamte App-Bundle ist unter 3 MB groß – verglichen mit Electron-Bundles, die leicht über 100 MB erreichen.

### USD Command Line Tools

Die Pipeline erstellt eine menschenlesbare USD-Datei (.usda), die dann mit usdcat in das Binärformat (.usdc) konvertiert und mit usdzip zusammen mit Texturen und Sounddateien in ein USDZ-Archiv verpackt wird – fertig für Apple AR Quick Look.

### Reality Composer

Apples offizielles 3D-Tool für interaktive USDZ-Experiences, verfügbar für macOS und iPadOS. Reality Composer exportierte früher im .reality-Format (umbenennen zu .usdz nötig), neuere Versionen exportieren direkt als USDZ.

## Produktseite erstellen

### Internationalisierung (i18n)

Alle nutzersichtbaren Texte – Landingpage, Editor-UI und AR-Interface – sind mehrsprachige Dictionaries. Standardmäßig mit Fallback auf Englisch. Weitere Sprachen lassen sich einfach ergänzen.

### Unternehmensbezogene Anpassungen

Der Ordner Intro enthält den Großteil des Landingpage-Codes. Pro Unternehmen wird eine eigene Datei angelegt mit Akzentfarbe, E-Mail, Impressum-URL, DSGVO-URL und weiteren Parametern.

### Export aus Blender

Ein Python-Skript (b3d/export-elm.py) exportiert einzelne Meshes aus Blender als Elm-Quellcode-Snippets. Diese werden dann als Modul eingebunden oder in den produktbezogenen Code eingefügt.

### Farben, Texturen und UV-Maps

Materialien müssen vor dem Export korrekt zugewiesen sein, UV-Maps sauber entfaltet. Texturdateien werden im USDZ-Archiv eingebettet. Mehrere Textur-Sets für verschiedene Varianten und Material-Eigenschaften wie Metallic und Roughness werden übernommen.

### Produktvarianten definieren

Jeder Produktkonfigurator erfordert die Definition von Varianten in Elm: Farbe, Größe, Material, Stil-Optionen, zugeordnete 3D-Modelle, interaktive Elemente und Preisinformationen. Produktmodule sind eigenständig und unabhängig aktualisierbar.

### Build-Zyklus

Der typische Build-Zyklus: 3D-Modelle in Blender vorbereiten → Geometrie und Texturen exportieren → Produktvarianten in Elm definieren → Anwendung kompilieren → Interaktive USDZ-Szene generieren → In AR Quick Look auf dem Gerät testen → USDZ-Dateien auf Webserver deployen. Jeder Schritt kann über bereitgestellte Skripte automatisiert werden.

## Erweiterte Funktionen

### HTML-Einbettung

AR Quick Look Experiences lassen sich per einfachem HTML-Link einbetten: Ein &lt;a&gt;-Tag mit rel="ar" und href auf die USDZ-Datei. Voraussetzungen: USDZ auf Webserver gehostet, CORS-Header konfiguriert, Content-Type model/vnd.usdz+zip, iOS-Gerät mit AR Quick Look.

### Mehrere Assets in einer AR-Session

AR Quick Look unterstützt komplexe Szenen mit mehreren Assets: Mehrere USDZ-Dateien in einer Session laden, jedes Asset individuell positionieren und skalieren, verschiedene Materialien und Interaktionen pro Asset, Multi-Produkt-Konfigurationen, Produktvergleiche und Raumplanungs-Anwendungen.

### Verbesserte IBL-Beleuchtung ab iOS 16

iOS 16 brachte Verbesserungen für Image-Based Lighting in AR Quick Look: präzisere Umgebungslicht-Schätzung, verbesserte Spiegelungen, besseres Schatten- und Occlusion-Handling, realistischere Materialdarstellung und überzeugendere Integration der Produkte in die physische Umgebung.

### Vordefinierte Farben

ConfigXR enthält vordefinierte Farbsysteme für Produktvarianten: Standard-Farbpaletten, Material-Finish-Presets (matt, glänzend, metallisch), branchenübliche Farbdefinitionen, Custom-Farbraum-Unterstützung und Varianten-Farbkombinationen.

## Roadmap und Community

Geplante Erweiterungen: Erweiterte Animations-Unterstützung, verbesserte Physik-Simulation, breitere USDZ-Schema-Unterstützung, bessere Integration mit weiteren DCC-Tools, Performance-Optimierungen und erweiterte Plattform-Unterstützung.

Das Projekt ist Open Source auf GitHub. Beiträge sind willkommen – Bug-Reports, Feature-Requests, Pull Requests, Dokumentations-Verbesserungen und Use-Case-Sharing.
