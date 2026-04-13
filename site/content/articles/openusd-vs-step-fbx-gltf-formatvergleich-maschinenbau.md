---
title: "OpenUSD vs. STEP, FBX und glTF: Welches Format gehört in Ihren Vertrieb?"
slug: openusd-vs-step-fbx-gltf-formatvergleich-maschinenbau
status: published
primary_tag: openusd
tags: [openusd, 3d-visualisierung, augmented-reality, glossar, usdz]
meta_title: "OpenUSD vs. STEP, FBX, glTF – Formatvergleich für den Vertrieb"
meta_description: "STEP bleibt in der Konstruktion – aber im Vertrieb gewinnt OpenUSD. Ein ehrlicher Vergleich der wichtigsten 3D-Formate für Maschinenbau und Industrie."
feature_image: /assets/images/2026/04/CAD_usdz_industrial_metaverse_openUSD.jpg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-04-13T00:00:00.000Z"
type: post
template: post
text_credit: "Kopf & KI"
image_credit: "Kopf & KI"
faq_heading: "Typische Entscheiderfragen"
faq:
  - q: "Muss ich STEP aufgeben, um OpenUSD zu nutzen?"
    a: "Nein. STEP und OpenUSD schließen sich nicht aus. STEP bleibt der Standard in der Konstruktion und im Datenaustausch zwischen Ingenieuren. OpenUSD ist eine zusätzliche Schicht – speziell für Vertrieb, Visualisierung und interaktive Anwendungen."
  - q: "Kann mein CAD-Tool OpenUSD exportieren?"
    a: "Sehr wahrscheinlich. Siemens NX, Autodesk-Produkte und viele andere CAD-Tools haben OpenUSD-Export bereits integriert. Einfach in den Exporteinstellungen nachschauen – der Export ist oft schon vorhanden."
  - q: "Was ist der Unterschied zwischen OpenUSD und USDZ?"
    a: "USDZ ist eine gepackte, schreibgeschützte Version von OpenUSD – optimiert für mobile Geräte und WebAR. OpenUSD ist das offene Basis-Format, USDZ ist das Auslieferungsformat für den Endnutzer auf iPhone und iPad."
  - q: "Was kostet der Einstieg in OpenUSD für den Vertrieb?"
    a: "Der Export aus dem CAD-Tool ist in der Regel kostenlos. Die Investition liegt in der Aufbereitung: Materialdefinition, Variantenlogik, Integration in Konfigurator oder WebAR. Das hängt stark vom Produkt und den gewünschten Anwendungsfällen ab."
  - q: "Warum nicht einfach glTF nutzen?"
    a: "glTF ist eine gute Wahl für einfache Web-Darstellungen. Sobald Varianten, Szenenkomposition oder Materialkonfiguration ins Spiel kommen, stößt glTF an Grenzen. OpenUSD wurde genau für diese Komplexität entwickelt – und ist mittlerweile von Apple, NVIDIA und Autodesk als Standard gesetzt."
---

- **STEP bleibt Standard in der Konstruktion, aber im Vertrieb ist es blind: keine Interaktivität, keine Varianten, kein WebAR.**
- **OpenUSD kann heute schon aus Siemens NX und Autocad exportiert werden, statisch, aber als Einstieg in eine neue Pipeline.**
- **Der relevante Schritt ist nicht der Export, sondern die weitere Verarbeitung: Konfiguratoren, WebAR und digitale Zwillinge aus einer Datei.**

&nbsp;

&nbsp;

## Die Formate, aus Vertriebssicht erklärt

**STEP** gibt es seit über 30 Jahren. Es ist präzise, kompatibel mit fast allem und in jedem CAD-Tool exportierbar. Genau deswegen ist es der Datenaustausch-Standard in der Konstruktion – und wird es wegen der Beharrungskräfte im Markt noch eine Weile bleiben. Aber STEP ist statisch: Es überträgt Geometrie, keine Erlebnisse.

**FBX** kam aus der Filmbranche. Es kann Animationen und Materialdaten transportieren, ist aber proprietär und verliert bei jedem Formatwechsel strukturelle Informationen. Für Vertriebsanwendungen ist es eine Übergangslösung, keine Grundlage.

**glTF** ist leichtgewichtig und für das Web optimiert. Es funktioniert gut für einfache Produktdarstellungen, aber ohne Variantenlogik, ohne Szenen-Komposition, ohne Konfiguration. Für erklärungsintensive Industrieprodukte reicht das selten.

**OpenUSD** – *Universal Scene Description* – ist das Verbindungsformat. Entwickelt von Pixar, [heute von Apple, NVIDIA, Autodesk und Siemens weiterentwickelt](https://visales.de/openusd-geschichte-strategie/). Es kann Szenen, Varianten, Materialien, Animationen und Metadaten in einer einzigen Datei halten. Nicht als Alternative zu STEP – sondern als nächste Schicht darüber.

→ [OpenUSD für Entscheider](https://visales.de/openusd/) (Umfangreiche Einordnung)  
→ [Von CAD zu USDZ: Der Weg zur 3D-Datei für alle Zwecke](https://visales.de/der-weg-zur-3d-datei-fur-alle-zwecke-openusd-usdz/)

## OpenUSD kommt aus der CAD-Welt heraus, schneller als viele denken

Das ist der Teil, der viele überrascht: OpenUSD ist heute schon in vielen CAD-Tools integriert. Siemens NX kann OpenUSD exportieren. Autodesk-Produkte ebenfalls. Einfach in den Exporteinstellungen suchen – der Export ist oft schon da.

Das Ergebnis ist zunächst statisch: eine dreidimensionale Beschreibung des Produkts, geometrisch korrekt, mit Materialinformationen. Ein solider Ausgangspunkt.

Was dann kommt, ist die eigentliche Frage: Wer macht aus dieser statischen Datei einen [Konfigurator](https://visales.de/produktkonfigurator/)? Wer bringt sie ins WebAR? Wer baut daraus einen digitalen Zwilling?

→ [CAD-Daten für den Vertrieb: Einmal aufbereiten & überall nutzen](https://visales.de/openusd-maschinenbau-cad-daten/)  
→ [OpenUSD v26.03: Was das Release für Maschinenbau & Industrie bedeutet](https://visales.de/openusd-v26-03-maschinenbau-industrie/)

## Von statisch zu interaktiv, das ist der eigentliche Schritt

Der Export aus dem CAD-Tool ist nicht das Ziel, er ist erst der Anfang. Wer Vertrieb mit OpenUSD ernst nimmt, denkt von Anfang an in Anwendungsfällen: Welche Varianten soll der Konfigurator zeigen? Welche Materialien wählt der Kunde selbst? Soll das Produkt im Raum des Kunden erscheinen – auf dem Handy, ohne App-Download?

Diese Fragen lassen sich mit STEP, FBX oder glTF nicht beantworten. Mit OpenUSD schon – wenn die Pipeline stimmt und jemand weiß, wie er die Datei für den Vertrieb aufbereitet.

→  [Von CAD zu AR: 3D-Daten im Vertrieb einsetzen](https://visales.de/cad_usdz_openusd_augmented_reality_sales/)  
→  [Digital Twins im Mittelstand: Was mitgeliefert wird, spart später Zeit und Geld](https://visales.de/digital-twins-im-mittelstand-was-mitgeliefert-wird-spart-spater-zeit-und-geld/)

## Der ehrliche Vergleich

Kein Format ist universell besser. Aber für Vertrieb, Konfiguration und räumliche Präsentation hat OpenUSD heute die stärksten Argumente:

STEP bleibt in der Konstruktion. Das wird noch Jahre so bleiben – und das ist auch richtig so. Aber wer heute entscheidet, wie er 3D-Daten für den Vertrieb aufbereitet, sollte wissen, wohin die Reise geht.

## Was jetzt?

Euer CAD-Tool kann OpenUSD wahrscheinlich schon exportieren. Schaut einfach in den Exporteinstellungen nach: **USD, USDZ, USDC oder USDA**. Was ihr danach damit macht – Konfigurator, [WebAR](https://visales.de/tag/augmented-reality/), digitaler Zwilling – das ist die eigentliche Frage.

→  [viSales als OpenUSD-Dienstleister](https://visales.de/openusd-dienstleister/)  
→ [Spatial Sales Infrastructure: Der 3D-Markt 2026–2030](https://visales.de/spatial-sales-infrastructure/)

&nbsp;

&nbsp;

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

<details>
<summary><strong>Realitätscheck</strong></summary>

OpenUSD ist kein Allheilmittel – und STEP wird nicht von heute auf morgen verschwinden. Die Marktkräfte sind träge: ERP-Systeme, PDM-Workflows und Einkaufsabteilungen hängen seit Jahrzehnten an STEP.

Wer OpenUSD als Masterdateiformat einführt, kämpft intern oft gegen IT-Abteilungen, die keine neuen Formate wollen, und Agenturen, die noch keinen vernünftigen OpenUSD-Export hinbekommen.

Der Export aus Siemens NX oder Autocad klingt einfach – ist es auch, aber nur für statische Dateien. Wer dann Varianten, Materialien oder Interaktivität will, steht wieder vor einer Integrationsaufgabe.

**Die Frage ist also nicht ob OpenUSD kommt, sondern wer intern den ersten Schritt macht – und wer dabei begleitet.**

→ [viSales als OpenUSD-Beratung / Dienstleister](https://visales.de/openusd-dienstleister/)  
→ [Unverbindliches Erstgespräch](https://visales.de/kontakt/)

</details>

&nbsp;

&nbsp;

