---
title: "USDZ vs. glTF: Welches 3D-Format eignet sich für AR?"
slug: usdz-vs-gltf
status: draft
primary_tag: openusd
tags: [openusd, usdz, 3d-visualisierung]
meta_title: "USDZ vs. glTF: Welches 3D-Format eignet sich für AR?"
meta_description: "USDZ und glTF im direkten Vergleich: Wann welches Format für Augmented Reality sinnvoll ist — für Apple, Android und den Vertriebsalltag erklärt."
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
type: post
template: post
faq_heading: "Schnelle Antworten: USDZ vs. GLB"
faq:
  - q: "Was ist der Unterschied zwischen USDZ und glTF?"
    a: "USDZ basiert auf dem OpenUSD-Standard und ist tief im Apple-Ökosystem verankert – es läuft nativ in Safari und AR Quick Look. glTF ist ein offener Web-3D-Standard des Khronos-Konsortiums, unterstützt von Chrome, Firefox und Android. Für Apple-zentrierte Vertriebsumgebungen ist USDZ die unkompliziertere Wahl, für plattformübergreifende Lösungen glb/glTF."
  - q: "Was ist GLB — und wie hängt es mit glTF zusammen?"
    a: "glTF und GLB beschreiben dasselbe Format in unterschiedlicher Verpackung. glTF ist die textbasierte Version (JSON + externe Dateien), GLB ist die Binär-Version – alles in einer Datei. Für AR und Web wird meist GLB verwendet. Die Bezeichnungen werden oft synonym genutzt."
  - q: "Welches 3D-Format eignet sich für Augmented Reality im Vertrieb?"
    a: "Für Apple-geräte-basierte Demos: USDZ – AR Quick Look startet direkt, kein App-Download. Für Android oder plattformübergreifend: GLB mit Google Scene Viewer oder model-viewer. USDconfig kombiniert beide Pfade automatisch: Safari bekommt USDZ, alle anderen Browser GLB."
  - q: "Kann man USDZ auf Android verwenden?"
    a: "Nicht nativ. USDZ ist bisher an das Apple-Ökosystem geknüpft. Android-Geräte benötigen GLB und Google Scene Viewer für AR. Ein dual-format Ansatz – wie in USDconfig implementiert – liefert automatisch das richtige Format je nach Gerät."
  - q: "Welches Format ist besser für B2B-Marketing und Vertrieb?"
    a: "Für schnelle, planbare Einsätze im Vertriebsgespräch mit iPhone/iPad-Nutzern: USDZ. Für Webseiten mit gemischtem Gerätemix: GLB als Basis mit USDZ-Fallback für Safari. Beide Formate schließen sich nicht aus – eine sauber aufgebaute Pipeline liefert beide aus derselben Quelldatei."
---

- **USDZ und glTF sind die zwei wichtigsten 3D-Formate für Augmented Reality auf mobilen Geräten: USDZ basiert auf dem OpenUSD-Standard und ist tief im Apple-Ökosystem verankert. glb/glTF ist ein offener Standard der Khronos Group und läuft plattformübergreifend auf Android, Web und Apple-Geräten.**
- **USDZ ermöglicht auf Apple-Geräten Augmented Reality ohne App: Über AR Quick Look lassen sich USDZ-Inhalte direkt aus dem Browser, aus E-Mails oder Präsentationen starten. glb/glTF erfordert auf Apple- & Android-Geräten in der Regel einen Web-Viewer.**
- **Die Formatwahl hängt vom Einsatzkontext ab, nicht von der technischen Qualität: Für schnelle, planbare AR im Apple-Umfeld ist USDZ die unkompliziertere Wahl. Wer Android und Apple gleichzeitig bedienen muss, arbeitet mit beiden Formaten.**

## 

&nbsp;

Im folgenden Video werden USDZ/OpenUSD und glb/glTF aus der Praxisperspektive gegenübergestellt: Nicht als technischer Formatvergleich, sondern mit Blick auf Alltagstauglichkeit, Plattformunterstützung und Einsatz im Vertrieb.

[Embed: https://www.youtube.com/watch?v=cN8boqmD8Tc](https://www.youtube.com/watch?v=cN8boqmD8Tc)

Die wichtigsten Aspekte aus dem Video sind im Folgenden als Fragen und Antworten zusammengefasst und ergänzt.

## Typische Fragen

- Was ist der Unterschied zwischen USDZ und glTF?
- Was ist glb — und wie hängt es mit glTF zusammen?
- Welches Format eignet sich für Augmented Reality?
- Kann man USDZ auf Android verwenden?
- Kann man glTF auf Apple-Geräten verwenden?
- Welches Format ist besser für Marketing und Vertrieb?
- Kann man USDZ in glTF konvertieren — und umgekehrt?

## Tabellenvergleich

| Aspekt | USDZ (OpenUSD) | glb / glTF |
| --- | --- | --- |
| Hersteller | AOUSD | Khronos Group |
| AR ohne App auf iPhone | ✔ direkt via AR Quick Look | ✗ Web-Viewer nötig |
| AR auf Android | ✗ nicht nativ | ✗ Web-Viewer nötig |
| Dateiformat | .usdz (Container) | .glb (binär) / .gltf (JSON) |
| Produktionslogik | Ausgangsbasis (USDZ-first) | Derivat aus USDZ |
| Einsatz im Vertrieb | Apple-Umgebungen, planbar | Ergänzung für Android/Web |
| Konvertierung | → glb möglich | → USDZ mit Einschränkungen |

## FAQ-Abschnitt

### Was ist der Unterschied zwischen USDZ und glTF?

USDZ basiert auf dem OpenUSD-Standard und ist tief im Apple-Ökosystem verankert. glTF ist ein offener Standard der Khronos Group und gilt als das „JPEG der 3D-Welt" — plattformübergreifend, weit verbreitet, browserkompatibel.

Der entscheidende Unterschied liegt nicht im Format selbst, sondern im Einsatzkontext: USDZ ist für Apple-Geräte optimiert und ermöglicht AR ohne App. glTF ist für maximale Offenheit ausgelegt, erfordert aber oft mehr technische Absicherung im Alltag.

### Was ist glb — und wie hängt es mit glTF zusammen?

glb und glTF beschreiben dasselbe Format — nur in unterschiedlicher Verpackung. glTF ist die textbasierte Variante (JSON), die alle Teile einer 3D-Szene in separaten Dateien ablegt. glb ist die binäre Version: alles in einer einzigen Datei gebündelt, was den Einsatz in der Praxis einfacher macht.

Für AR und Web wird meist glb verwendet. Die Bezeichnungen werden oft synonym genutzt, technisch sind sie aber nicht identisch.

### Welches 3D-Format eignet sich für Augmented Reality?

Das kommt auf die Zielplattform an. USDZ funktioniert auf Apple-Geräten direkt — ohne App, ohne Umwege. glb funktioniert plattformübergreifend, erfordert auf Apple- und Android-Geräten jedoch in der Regel eine Web-Viewer-Lösung (z.B. model-viewer im Browser).

Für Apple-zentrierte Vertriebsumgebungen ist USDZ die unkompliziertere Wahl. Wer Android und Apple gleichzeitig bedienen muss, braucht entweder beide Formate oder eine technische Lösung, die konvertiert.

### Kann man USDZ auf Android verwenden?

Nicht nativ. USDZ ist bisher an das Apple-Ökosystem geknüpft und wird auf Android-Geräten standardmäßig noch nicht unterstützt. Es gibt technische Umwege — etwa über WebGL-basierte Viewer im Browser — aber das ist kein direkter, einfacher Einstieg wie [AR Quick Look](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/) auf dem iPhone.

Wer Android-Geräte einbinden möchte, arbeitet in der Regel mit glb/glTF und einem geeigneten Web-Viewer. viSales liefert für beide Plattformen eine Lösung.

### Kann man glTF auf Apple-Geräten verwenden?

Ja, aber nicht mit AR Quick Look. Apple unterstützt nativ nur USDZ für den direkten AR-Einsatz ohne App. glb-Dateien lassen sich auf Apple-Geräten in Browsern über model-viewer oder ähnliche Lösungen darstellen — allerdings ohne die nahtlose Integration, die USDZ mit AR Quick Look bietet.

### Welches Format ist besser für Marketing und Vertrieb?

Kommt auf den Kontext an — aber für einen schnellen, planbaren Einsatz im Vertriebsgespräch hat USDZ auf Apple-Geräten klare Vorteile. AR Quick Look lässt sich direkt aus E-Mails, Präsentationen oder Websites starten, ohne dass Kunden etwas installieren müssen.

Für Kampagnen oder Produktseiten, die sowohl Apple- als auch Android-Nutzer erreichen sollen, ist glb/glTF die einfachere Basis, in der Regel liefert man beide Formate aus.

→ Wie AR im Vertrieb konkret eingesetzt wird: [Augmented Reality im Vertrieb](https://visales.de/augmented-reality/)

### Kann man USDZ in glTF konvertieren — und umgekehrt?

Ja, Konvertierungen sind möglich — aber nicht verlustfrei. Einfache 3D-Objekte lassen sich zwischen den Formaten übertragen. Komplexere Materialien, Animationen oder physikbasierte Eigenschaften können dabei verloren gehen oder anders dargestellt werden.

In der Praxis empfiehlt sich die Konvertierung aus einer gemeinsamen Ausgangsbasis — idealerweise aus dem OpenUSD-Workflow. Wer USDZ und glb parallel benötigt, ist mit einer Produktionspipeline besser bedient als mit nachträglicher Konvertierung.

→ Wie viSales mit USDZ und OpenUSD arbeitet: [OpenUSD Dienstleister](https://visales.de/openusd-dienstleister-in-deutschland-visales-aus-bochum/)

<details>
<summary><strong>**ARKit vs. ARCore – kurz eingeordnet**</strong></summary>

ARKit ist Apples AR-Framework, ARCore das von Google. Beide steuern, wie das Gerät Flächen erkennt, Licht einschätzt und Objekte im Raum platziert.

Für den praktischen Einsatz im Vertrieb ist diese Unterscheidung meist zweitrangig. Entscheidender ist das Dateiformat: USDZ für Apple, glb/glTF für Android – und welcher Einstieg ohne App möglich ist. Wer AR-Inhalte plant, denkt besser in Formaten und Plattformen als in Frameworks.

</details>

## Fazit

USDZ und glTF schließen sich nicht aus — sie bedienen unterschiedliche Szenarien. Für schnelle, planbare AR-Einsätze auf Apple-Geräten ist USDZ die pragmatischere Wahl. Für plattformübergreifende Anforderungen bietet USDZ-first, dann glb/glTF mehr Flexibilität.

Die Formatfrage ist letztlich eine Kontextfrage: Wer nutzt die Inhalte, auf welchen Geräten, und wie direkt soll der Einstieg sein? Wer diese drei Fragen beantwortet hat, weiß welches Format — oder welche Kombination — sinnvoll ist.

→ Apple vs. Android: Wie sich die Plattformen bei AR unterscheiden
