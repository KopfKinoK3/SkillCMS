---
title: "OpenUSD ohne Apple: Wer baut ein NoCode-Tool für Windows?"
slug: openusd-ohne-apple-wer-baut-ein-nocode-tool-fur-windows
status: published
primary_tag: impuls
tags: [impuls, apple, openusd]
meta_title: "OpenUSD NoCode-Tool für Windows: Wer baut die Alternative?"
meta_description: "Reality Composer Pro läuft nur auf macOS. Mit "Deconstructed" gibt es erstmals eine OpenSource-Alternative – und die Frage: Wann kommt ein NoCode-Tool für Windows?"
feature_image: /assets/images/2026/03/Reality-Composer-Pro-Alternative.jpg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-03-02T07:28:25.000Z"
type: post
template: post
---

[OpenUSD](https://visales.de/openusd/) ist ein offenes Format. Jeder kann es nutzen, jeder kann darauf aufbauen. **Genau das ist der Witz an Open Source:** Nicht ein Anbieter entscheidet, was möglich ist, sondern die Community. Mittlerweile steht fast die gesamte Industrie dahinter: Microsoft, Google, Apple, NVIDIA Omniverse.

Nur bei einem Schritt hört die Offenheit bisher auf, dem Authoring. Wer mit einem NoCode-Tool Szenen für Apples Spatial-Plattform bauen will, kommt an Apples "Reality Composer Pro" kaum vorbei. Ein Tool, ein Ökosystem, ein Betriebssystem.

Nun gibt es eine OpenSource-Alternative: [Deconstructed](https://github.com/elkraneo/Deconstructed). Noch macOS only, aber der Ansatz ist offen. Einfach von jemand, der verstehen wollte, wie das Dateiformat funktioniert und [dann angefangen hat, es nachzubauen](https://elkraneo.com/deconstructing-reality-composer-pro-inspector-components/).

→ Alle OpenUSD-Lösungen: [OpenUSD-Tools & Dienste von viSales](https://visales.de/openusd-dienstleister/)

<details>
<summary><strong>Was ist Reality Composer Pro?</strong></summary>

Reality Composer Pro ist Apples professionelles Entwicklerwerkzeug, um 3D-Szenen für visionOS und iOS zu bauen. Man importiert 3D-Modelle, ordnet sie im Raum an, verknüpft Animationen und exportiert das Ganze als USDZ-Datei, Apples AR-Format auf Basis von [OpenUSD](https://visales.de/tag/openusd-usdz/).

Das Exportformat ist offen und funktioniert auch -**in der Idee**- auf Android oder im Web, [dort Nativ bisher nur mit dem Safari-Browser](https://www.youtube.com/shorts/dhrUMZGwsZY) via Model-Tag.

Aber die Projektdatei davor, das `.realitycomposerpro`-Format, in dem die eigentliche Arbeit steckt, ist nicht dokumentiert und bisher an Apples eigene Xcode-Tools gebunden. Wer keine Apple-Hardware hat, schaut außen vor.

</details>

Das Tool erstellt keine 3D-Modelle. Das muss man woanders machen – mit Blender zum Beispiel, oder man lädt Dateien herunter. Weitere Wege zu 3D-Content hab ich [hier schon mal beschrieben](https://visales.de/der-weg-zur-3d-datei-fur-alle-zwecke-openusd-usdz/). Aber sobald die Geometrie da ist, braucht man einen Weg, sie in eine Szene zu bringen. Genau da setzt dieses Tool an.

[Microsoft ist 2025 der Alliance for OpenUSD beigetreten. Google auch.](https://visales.de/openusd-geschichte-strategie/) Das Signal ist klar: OpenUSD und das Dateiformat USDZ wird (früher oder später) in allen 3D-Bereichen ein zentrales Datenformat werden.

Auf Windows gibt es mit [NVIDIA Omniverse](https://visales.de/nvidia-omniverse-mittelstand/) bereits ein mächtiges OpenUSD-Werkzeug, aber es richtet sich an Profis. Was fehlt, ist ein LowCode-/NoCode-Einstieg: etwas, das auch Nicht-Programmierer in die Lage versetzt, interaktive AR-Szenen zu bauen. Genau das leistet Deconstructed – bisher nur für macOS.

**Vielleicht liest das gerade jemand, der sich dieser Aufgaben annehmen möchte?**

&nbsp;

&nbsp;

### **Du willst wissen ob OpenUSD für dein Unternehmen passt?**

In 30 Minuten sortieren wir gemeinsam, ob und wo OpenUSD in eurem Vertrieb konkret etwas bringt — ohne Pitch, ohne Angebot. Kein Verkaufsdruck, eine ehrliche Einordnung. **Rheingas und Somfy haben so angefangen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

<details>
<summary><strong>Realitätscheck</strong></summary>

Der nächste logische Schritt wäre eigentlich, dass interaktive Apple-USDZ-Dateien 1:1 in NVIDIA Omniverse laufen – und umgekehrt.

Unser Tool [USDbdridge](https://visales.de/usdbridge/) kann einzelne Omniverse-Assets Cross-Plattform zwischen Omniverse und dem Apple-Ökosystem überführen. Aber interaktive Apple-Assets in Omniverse wirklich zum Laufen zu bringen – das geht bisher nicht.

Auch das wäre ein Markt.   
Einer, auf den wir warten.

</details>

&nbsp;

&nbsp;

&nbsp;

Entdeckt via [Thomas Kumlehn](https://www.linkedin.com/in/thomas-kumlehn/), meinen Mitarbeiter, der in regelmäßigem Apple-Vision-Pro-Developer-Austausch mit [Christian Diaz](https://github.com/elkraneo) steht, dem Entwickler hinter Deconstructed.
