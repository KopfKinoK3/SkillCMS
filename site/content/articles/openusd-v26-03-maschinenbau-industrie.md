---
title: "OpenUSD v26.03: Was das Release für Maschinenbau & Industrie bedeutet"
slug: openusd-v26-03-maschinenbau-industrie
status: published
primary_tag: impuls
tags: [impuls]
meta_title: "OpenUSD v26.03: WebAssembly & Gaussian Splats für Industrie"
meta_description: "OpenUSD v26.03 bringt WebAssembly Build Support und 3D Gaussian Splats. Was das für Produktkonfiguratoren und 3D-Workflows im Maschinenbau bedeutet."
feature_image: /assets/images/2026/04/OpenUSD.jpeg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-04-07T18:21:22.000Z"
type: post
template: post
faq:
  - q: "Was bedeutet WebAssembly-Support für OpenUSD?"
    a: "USD-Dateien können künftig ohne Konvertierung in GLB oder andere Formate direkt im Webbrowser geladen werden. Für Produktkonfiguratoren heißt das: Die Masterdatei aus der Konstruktion wird dieselbe Datei, die der Vertrieb im Browser zeigt — inklusive nativer Auswertung von VariantSets."
  - q: "Was sind 3D Gaussian Splats in OpenUSD?"
    a: "Gaussian Splatting ist eine Methode, reale Umgebungen aus Fotos oder Scans als photorealistische 3D-Szene zu rekonstruieren. Mit v26.03 wird diese Technologie offiziell in den USD-Standard aufgenommen, sodass Showrooms, Produktionsumgebungen oder Messestände als begehbare 3D-Assets in bestehende USD-Workflows integriert werden können."
  - q: "Welche Vorteile hat OpenUSD für den Maschinenbau?"
    a: "OpenUSD ermöglicht einen durchgängigen Workflow, in dem CAD-Daten, photorealistische Umgebungsscans und interaktive Produktkonfiguration in einem einzigen Format koexistieren. Die Konstruktionsdatei wird zur Vertriebsdatei — ohne Konvertierungsschritte, ohne Qualitätsverlust, ohne separate Konfigurations-Layer."
  - q: "Realitätscheck"
    a: "WebAssembly-Support heißt nicht, dass morgen jeder USD-Viewer im Browser läuft. Die Laufzeitumgebung existiert jetzt — aber performante Player, die komplexe Szenen mit VariantSets und Materialien flüssig rendern, müssen erst gebaut werden. Gaussian Splatting als Schema ist ein Standard-Vorschlag, kein fertiges Ökosystem. Die Capture-Tools sind teuer, die Datenmengen groß, und die meisten Maschinenbau-Unternehmen haben aktuell weder die Pipeline noch das Know-how dafür.Was v26.03 liefert, ist eine Architekturentscheidung, kein fertiges Produkt. Zwischen ‘technisch möglich’ und ‘im Vertrieb einsetzbar’ liegen erfahrungsgemäß zwei bis drei Jahre. Wer jetzt investiert, investiert in eine Wette — eine gut begründete, aber eben eine Wette."
ki_text: true
---

Nun hat die Alliance for OpenUSD die Version 26.03 veröffentlicht. Normalerweise sind Versionsnummern nichts, worüber man einen Beitrag schreibt. Diesmal schon, denn zwei Features sind drin, die das verändern, was wir in der B2B-Produktkommunikation technisch für möglich halten.

&nbsp;

&nbsp;

Ich verfolge [OpenUSD](https://visales.de/tag/openusd/) seit Jahren, bin Mitglied der [Alliance for OpenUSD](https://aousd.org) und mein Team arbeitet täglich mit dem Format [USDZ](https://visales.de/tag/usdz/). Die meisten Releases bringen inkrementelle Verbesserungen: Performance hier, eine neue API dort. v26.03 ist anders. Nicht wegen der Menge an Changes, sondern weil zwei Entscheidungen drin stecken, die eine klare Richtung setzen.

## WebAssembly Build Support

Die erste - *WebAssembly Build Support* - USD lässt sich jetzt nativ für den Browser kompilieren. Das klingt technisch, hat aber eine direkte Konsequenz: USD-Dateien können künftig ohne Konvertierung im Webbrowser geladen werden. Kein Zwischenschritt über GLB, kein Export-Pipeline-Workaround, kein Qualitätsverlust durch Formatwechsel. Die 3D-Masterdatei geht direkt ins Web.

Für den Maschinenbau heißt das: Der [Produktkonfigurator der Zukunft](https://visales.de/usdconfig-demo/) liest die gleiche Datei, die auch in der Konstruktion liegt. VariantSets — *also die Logik, die Produktvarianten beschreibt* — werden nativ ausgewertet, nicht über einen separaten Konfigurations-Layer nachgebaut. Das ist ein Unterschied, nicht nur technisch sauberer, sondern auch wartbar.

**Ausblick dazu gefällig?**

→ [USDconfig](https://visales.de/usdconfig-demo/), unser neuer Produktkonfigurator auf OpenUSD-Basis

### Was WebAssembly & Gaussian Splatting für industrielle 3D-Workflows bedeuten

Die zweite Entscheidung: 3D Gaussian Splats als offizielles Schema. Gaussian Splatting ist eine Methode, mit der sich reale Umgebungen aus Fotos oder Scans photorealistisch als 3D-Szene rekonstruieren lassen. Bisher war das ein Forschungsthema, jetzt hat es einen Platz im USD-Standard.

Für Industrie und Maschinenbau öffnet das eine konkrete Tür: Produktionsumgebungen, Showrooms oder [Messeaufbauten](https://visales.de/messen/) lassen sich als begehbare 3D-Szenen erfassen — und als USD-Asset in bestehende Workflows einbetten. Nicht als separates Tool, sondern als Teil der gleichen Pipeline, die auch CAD-Daten und Konfiguratoren bedient.

### Schon heute...

Beide Features haben etwas gemeinsam: Sie machen USD breiter einsetzbar, ohne die Tiefe aufzugeben. WebAssembly bringt USD in den Browser. Gaussian Splats bringen die reale Welt in USD. Zusammen entsteht ein Workflow, in dem CAD-Daten, photorealistische Umgebungsscans und interaktive Produktkonfiguration in einem einzigen Format koexistieren — zugänglich über jeden Webbrowser.

> Das ist kein Science-Fiction-Szenario. Das ist eine Architektur, die jetzt technisch möglich wird. Was oft noch fehlt, sind die Player und Tools, die das ausnutzen. Aber die Richtung ist gesetzt.

→ [USDbridge](https://visales.de/usdbridge/), unser Übersetzer von NVIDIA Omniverse zu Apple USDZ

Für Unternehmen im Maschinenbau, die heute mit 3D-Visualisierung arbeiten oder darüber nachdenken: v26.03 ist das Release, ab dem es sich lohnt, USD nicht nur als Austauschformat zu betrachten, sondern als Laufzeitformat. Die Datei, die in der Konstruktion entsteht, wird die gleiche sein, die der Vertrieb im Browser zeigt.

Quelle:* *[Alliance for OpenUSD — OpenUSD v26.03 Release](https://aousd.org/blog/openusd-v26-03/)

&nbsp;

&nbsp;

## Typische Fragen zu OpenUSD v26.03

<details>
<summary><strong>Was ist neu in OpenUSD v26.03?</strong></summary>

Die Version 26.03 bringt zwei wesentliche Neuerungen: WebAssembly Build Support, der USD nativ im Browser lauffähig macht, und ein offizielles Schema für 3D Gaussian Splats, mit dem sich photorealistische Umgebungsscans als USD-Asset einbetten lassen.

</details>


