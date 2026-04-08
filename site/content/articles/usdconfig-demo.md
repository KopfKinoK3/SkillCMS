---
title: "Vom 3D-Modell zum Web-Konfigurator: Was OpenUSD & USDZ im B2B-Vertrieb wirklich leisten: USDconfig 1.1"
slug: usdconfig-demo
status: published
primary_tag: vertriebskommunikation
tags: [vertriebskommunikation]
meta_title: "USDconfig – 3D-Produktkonfigurator auf Basis von OpenUSD | viSales"
meta_description: "USDconfig verwandelt USDZ-Masterdateien in vollständige Web-Konfiguratoren mit nativem OpenUSD-Rendering in Safari und AR für iOS und Android."
feature_image: /assets/images/2026/03/USDconfig_1_1_Stuhl_Konfigurator.jpg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: 2026-03-25T23:02:16.000Z
type: post
template: post
faq_heading: "Typische (Technik-) Entscheiderfragen"
faq:
  - q: "Welche 3D-Formate werden unterstützt?"
    a: "USDconfig arbeitet nativ mit USDZ (OpenUSD) und GLB (glTF 2.0). USDZ ist das Primärformat für Safari-Rendering und iOS-AR via Quick Look. GLB wird für alle anderen Browser sowie Android-AR via Scene Viewer genutzt. CAD-Daten aus gängigen Systemen (STEP, SolidWorks, CATIA) werden im Rahmen der viSales-Pipeline konvertiert."
  - q: "Brauche ich eine eigene App für die AR-Funktion?"
    a: "Nein. iOS-AR läuft über Apples Quick Look — direkt aus dem Browser, ohne App-Download. Android-AR nutzt Google Scene Viewer, der auf jedem modernen Android-Gerät vorinstalliert ist. Kein App Store, kein Update-Zwang auf Kundenseite."
  - q: "Wie viele Varianten-Kombinationen sind realistisch umsetzbar?"
    a: "USDconfig trennt strukturelle Varianten (Geometrieänderungen) von materiellen Varianten (Farben, Texturen). Strukturvarianten erzeugen separate Dateien — realistisch sind 4–12 Kombinationen. Materialvarianten laufen über KHR_materials_variants im GLB und verursachen keine zusätzlichen Dateien. Beispiel Bürostuhl: 3 Armlehnen × 2 Sitzformen = 6 GLB-Dateien, dazu beliebig viele Bezugfarben ohne Mehraufwand."
  - q: "Funktioniert der Player auch in Ghost CMS oder anderen CMS?"
    a: "Ja. Der Player wird als statische HTML-Datei auf einem Webserver oder GitHub Pages gehostet und per iframe in Ghost, WordPress, Webflow oder jedes andere CMS eingebunden. Der iframe-Snippet ist parametrisierbar — Produkt, Startvarianten und Asset-URLs werden als URL-Parameter übergeben."
  - q: "Was ist der Unterschied zu model-viewer alleine?"
    a: "Google model-viewer rendert GLB-Dateien über WebGL in allen Browsern — solide, aber ohne nativen OpenUSD-Support. USDconfig ergänzt einen Safari-Pfad über den HTML-&lt;model&gt;-Tag, der USDZ mit vollem OpenUSD-Fidelity direkt in WebKit rendert — inklusive Variant Sets aus dem USD-Schema, ohne Konvertierungsverluste. Beide Pfade werden vom selben Web-Player automatisch erkannt und genutzt."
  - q: "Warum nicht einfach three.js oder Babylon.js?"
    a: "three.js und Babylon.js sind leistungsstarke 3D-Engines für das Web — aber sie rendern über WebGL und kennen kein OpenUSD nativ. Das bedeutet: Alle USD-spezifischen Konzepte wie Variant Sets, Layering, Stage-Composition müssen entweder weggelassen oder manuell nachgebaut werden. Der Konvertierungsweg von USDZ → glTF → WebGL kostet Fidelity &amp; Qualität, vor allem bei Materialien und Texturauflösung.USDconfig nutzt model-viewer als WebGL-Fallback für Chrome, Firefox und Edge — und legt für Safari bewusst den nativen &lt;model&gt;-Pfad oben drauf. So bleibt OpenUSD-Fidelity erhalten, wo der Browser es unterstützt, ohne für alle anderen Geräte auf Kompatibilität zu verzichten."
---

- **USDconfig liest OpenUSD-Variantensets direkt aus USDZ-Masterdateien, d.h. kein manuelles Setup, keine kombinatorische Datei-Explosion.**
- **Safari auf VisionOS** **rendert USDZ nativ über den &lt;model&gt;-Tag mit vollem OpenUSD-Fidelity, alle anderen Browser nutzen vorerst GLB via model-viewer. Beide Pfade, ein Player, kein Reload.**
- **iOS-AR startet direkt in Quick Look, Android-AR via Scene Viewer — aus demselben Web-Player heraus, ein einziger Button. **

&nbsp;

&nbsp;

## Was ist USDconfig 1.1?

USDconfig ist ein modulares Web-Framework für 3D-Produktkonfiguratoren auf Basis von OpenUSD & dem USDZ-Dateiformat. Es verbindet die native 3D-Rendering-Kompetenz von Apples OpenUSD-Standard mit dem offenen Web — und macht erklärungsintensive B2B-Produkte direkt im Browser und in Augmented Reality konfigurierbar.

Entstanden aus der Arbeit mit Industriekunden, die komplexe Produktvarianten in Vertriebsgesprächen zeigen müssen — ohne Musterkoffer, ohne Vor-Ort-Termin, ohne App-Installation auf Kundenseite.

→ [Produktübersicht: USDconfig für B2B-Vertrieb](https://visales.de/usdconfig/)

<details>
<summary><strong>Vorgeschichte: AR-Player, ConfigXR & USDconfig 1.0</strong></summary>

2021 begannen wir mit der Entwicklung unseres ersten [AR-Players](https://visales.de/ar-player-webbasierte-augmented-reality-jetzt-auch-vom-desktop-aus-moglich/), der dann von unsrem Produkt [ConfigXR](https://visales.de/verkaufen-mit-dem-augmented-reality-stuhl-konfigurator-ar-mit-usdz-reality/) (Builder) abgelöst wurde, inzwischen [OpenSource auf Github](https://github.com/KopfKinoK3/ConfigXRBuilder) zu finden.

Mit dem [Start der Apple Vision Pro](https://visales.de/vision-pro-apple-mittelstand/) kam ein neuer Bedarf auf und wir entwickelten ein neues Web-Player-Tool [USDconfig](https://visales.de/usdconfig/). Dazu gehörte schon ein neuer Konvertierungsansatz.

→ [Fallbeispiel RENZ: Verkauf beginnt mit Erleben](https://visales.de/renz-augmented-reality-produktkonfigurator-fallbeispiel/) (USDconfig 1.0)

**Neu mit Version 1.1. ist der automatische USDconfig-Analyzer, der direkt eine USDZ-Masterdatei analysiert und für die weiteren Schritte aufbereitet.**

</details>

## Welches Problem löst USDconfig?

3D-Produktkonfiguratoren im B2B scheitern meist nicht am 3D, sondern an der Infrastruktur dahinter. Varianten werden als separate Dateien verwaltet, AR erfordert App-Downloads, und was in Safari funktioniert, bricht in Chrome zusammen.

USDconfig trennt strukturelle Varianten — verschiedene Geometrien wie Armlehnen, Sockeltypen oder Gehäuseformen — von materiellen Varianten wie Farben, Oberflächen und Texturen. Strukturvarianten werden als separate Dateien generiert: überschaubar in der Anzahl. Materialvarianten leben als KHR_materials_variants-Extension direkt im GLB-File und werden ohne Datei-Reload live umgeschaltet. 

> Keine kombinatorische Explosion, keine 400 Einzeldateien pro Produkt.

## Live Demo — Vitra ID Chair (Konzeptansicht)

Der folgende Beta-Player zeigt den USDconfig-Konfigurator in Aktion — alle Assets sind live. 39 Bezugfarben, alle Strukturvarianten und die AR-Übergabe funktionieren vollständig.

<div style="width:100%;height:560px;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.10);">
  <iframe
    src="https://kopfkinok3.github.io/USDconfig-demo-player/"
    width="100%" height="100%" frameborder="0"
    allow="xr-spatial-tracking; camera" allowfullscreen loading="lazy"
    title="USDconfig 3D Konfigurator — Vitra ID Chair">
  </iframe>
</div>

**Dislaimer:** Wir haben von der Vitra-Website die Elemente übernommen und für USDZ mit Varianten und Top-Texturen optimiert. Dies war die Highend-Testdatei für unseren neuen Analyser.  
  
→ Alternativ: [Als Step-by-Step-Guide-Konfigurator / Wizard](https://kopfkinok3.github.io/USDconfig-demo-player/wizard.html)  
→ [Technik-Demo (Mobile) mit Web-Konfigurator & Apple-Pay-Button in AR](https://kopfkinok3.github.io/USDconfig-demo-player/apple-pay-cube/)

## Wie funktioniert das USDconfig-Produkt-Package?

Das System besteht aus vier Modulen — zwei Python-seitig (viSales-Lokal), zwei im Browser. Die Pipeline startet bei der USDZ-Masterdatei aus [Reality Composer Pro](https://visales.de/openusd-ohne-apple-wer-baut-ein-nocode-tool-fur-windows/) oder einem anderen USD-Workflow wie z.B. [NVIDIA Omniverse](https://visales.de/nvidia-omniverse-mittelstand/) via [USDbridge](https://visales.de/usdbridge/) und endet beim fertigen Web-[Produktkonfigurator](https://visales.de/produktkonfigurator/) mit AR-Button.

> Aktuell nutzen wir [&lt;model&gt;-Tag](https://youtube.com/shorts/dhrUMZGwsZY) nur für die Apple Vision Pro, sind aber für die weitere Apple-Zukunft vorbereitet. Sollte Apple für iOS, iPadOS oder macOS &lt;model&gt;-Tag aus der Beta herausholen, so können wir sehr kurzfristig das höhere Potential von nativem USDZ im Browser Rechnung tragen.

![USDconfig Architektur – 4 Module](/assets/images/2026/03/usdconfig-architektur-1.svg)

<details>
<summary><strong>Roadmap-Pläne</strong></summary>

**v1.2 — Quick Wins (kurzfristig)**

* Desktop AR → QR-Code-Flow: Wer am Desktop auf "In AR anzeigen" klickt, bekommt heute nichts Brauchbares. Besser: Modal mit QR-Code der direkt auf die aktuelle Konfiguration zeigt, daneben "Öffne diesen Link auf deinem iPhone → AR startet automatisch". Konfigurationslink via URL-Parameter übergeben. (So ca. wie USDconfig 1.0 es auch gelöst hat.)
* Wizard: Summary-Screen: Nach Bezug-Auswahl eine Zusammenfassung aller Choices zeigen, bevor AR/Teilen erscheint. Visueller Abschlussmoment, ggf. Kamerafahrt?

**v1.3 — Plattform-Ausbau (mittelfristig)**

* visionOS-Modus: User-Agent-Erkennung für visionOS → statt vollem 2D-Konfigurator: ein minimales Floating-Menu mit 3-4 Buttons + `<model>`-Tag mit der Masterdatei im Vordergrund. "Produkt in AR erleben — Variante wählen und starten." Der Headset-User soll nicht tippen, er soll schauen.
* media.visales.de als USDZ-Host: `.htaccess` mit korrektem MIME-Type → `<model>`-Tag läuft in Safari macOS. Dann: Safari-Badge wird zu "Safari · native USD" mit echter Funktion.
* Gestell-Farbvariante: Pulverbeschichtet (weiß/schwarz/RAL) als zweite KHR-Gruppe — ohne neue Dateien.

**v2.0 — OpenUSD-Native (langfristig, mit v26.03)**

* WebAssembly USD-Runtime: OpenUSD läuft direkt im Browser. USD-VariantSets live schalten ohne GLB-Konvertierung. Kein KHR\_materials\_variants mehr nötig. Die Masterdatei IS der Player.
* Konfigurator-Generator: URL-Builder als Tool — Kunde gibt Produkt-URL ein, bekommt Embed-Snippet für sein CMS.
* Analytics: Welche Variante wird am häufigsten gewählt? Heatmap der Bezugfarben. Abbruchpunkt im Wizard.

</details>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

### **Einstieg in den AR-Konfigurator — mit Unterstützung.**

Wir begleiten Unternehmen vom ersten USDZ-Modell bis zum vollständigen Web-Konfigurator im Vertrieb. Das erste Gespräch dauert 30 Minuten. Ohne Pitch, ohne Vorbereitungspflicht. **Rheingas, Somfy und Carl Hamm haben mit einem Produkt begonnen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;
