---
title: "LiTo: 3D-Rekonstruktion mit realistischen Licht- und Materialeffekten"
slug: lito-3d-rekonstruktion-mit-realistischen-licht-und-materialeffekten
status: draft
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
type: post
template: post
---

Apple hat am 11. März ein neues Forschungsergebnis veröffentlicht: [LiTo: Surface Light Field Tokenization](https://apple.github.io/ml-lito/) und ich bin beeindruckt was das Forscherteam gelang:

Stell dir vor, du siehst ein Produkt auf deinem Bildschirm, und es wirkt fast greifbar: [LiTo](https://arxiv.org/abs/2603.11047) macht genau das möglich. Aus einem einzigen Bild entsteht ein 3D-Modell, das nicht nur die Form zeigt, sondern auch **Licht, Glanzlichter und Materialeigenschaften realistisch abbildet**. Plötzlich wirken digitale Produktpräsentationen wie echte Objekte, und jede Blickrichtung offenbart neue Details.

Die Technologie kombiniert **präzise Geometrie** mit **optischer Authentizität**, sodass digitale Prototypen in AR, VR oder 3D-Showrooms überzeugen. Marketing- und Vertriebsteams können Produkte erlebbar machen, ohne dass Kunden vor Ort sein müssen. Designentscheidungen lassen sich schneller treffen, Diskussionen werden klarer, Präsentationen eindrucksvoller.

### Neue Maßstäbe für AR- und VR-Visualisierung

Für virtuelle Produktpräsentationen bedeutet LiTo: Oberflächen wirken echt, Materialien sprechen für sich, und jede digitale Interaktion wird zum immersiven Erlebnis. Ob [Online-Produktkonfigurator](https://visales.de/produktkonfigurator/), [virtueller Messestand](https://visales.de/messen/) oder 3D-Produktvideo, LiTo schafft visuelle Qualität, die Entscheidungen erleichtert und Kunden beeindruckt.

<details>
<summary><strong>Wie LiTo funktioniert: KI trifft 3D</strong></summary>

Stell dir vor, du hast viele Bilder eines Objekts mit Tiefeninformationen (RGB + Depth). Die ForscherInnen sehen diese Bilder als Samples eines „Surface Light Field“ – das beschreibt, wie Licht von jeder Stelle der Oberfläche in jede Richtung abgestrahlt wird.

LiTo entwickelt daraus ein Modell, das:

* Einen kompakten latenten Raum lernt – eine interne Repräsentation, die Form und Aussehen zusammenfasst.
* Diesen latenten Raum so trainiert, dass realistische Blickwinkel-Effekte entstehen, z. B. Glanzlichter und Reflexionen.
* Ein weiteres Modell erlaubt, aus nur einem einzelnen Bild ein vollständiges 3D-Modell inklusive Licht- und Materialeffekten zu generieren.

Die Technik nutzt latente Vektoren zur komprimierten Repräsentation des Surface Light Field und arbeitet mit Latent Flow Matching, um diese Darstellungen zu lernen und zu erzeugen. Der Fokus liegt auf view-dependent Erscheinungen, also Effekten, die sich je nach Blickwinkel ändern.

Fazit: LiTo erzeugt 3D-Modelle, die nicht nur die Form eines Objekts erfassen, sondern auch realistische optische Eigenschaften, basierend auf Einzelbildern oder Multiview-Daten.

</details>

<details>
<summary><strong>Realitätscheck</strong></summary>

Ja, das ist eine ganz neue Forschung von Apple und die Möglichkeiten sind schlicht wunderbar. Bisherige KI-Ansätze erzeugten zwar „schönes 3D“, aber kein Modell, das leichtgewichtige AR-Anwendungen via AR Quick Look gut unterstützt. Die Polygon-Anzahl dieser bisherigen Modelle war meist zu hoch oder unpraktisch für schnelle, mobile AR-Visualisierungen.

Mit dem neuen Ansatz lassen sich hoffentlich effiziente, realistische 3D-Modelle erzeugen, die für AR, VR und digitale Präsentationen optimal nutzbar sind. Wir werden die mit LiTo erzeugten Dateien bald selbst testen, sowohl für Apple als auch für sonstige leichte AR-Anwendungen.

</details>

&nbsp;
