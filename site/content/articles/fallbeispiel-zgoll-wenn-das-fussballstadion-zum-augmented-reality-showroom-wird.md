---
title: "Fallbeispiel Zgoll: Wenn das Fußballstadion zum Augmented Reality-Showroom wird"
slug: fallbeispiel-zgoll-wenn-das-fussballstadion-zum-augmented-reality-showroom-wird
status: published
primary_tag: visual-sales
tags: [visual-sales, augmented-reality, vertriebskommunikation, case-study]
feature_image: /assets/images/2025/12/ZgollAR.png
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2025-09-10T08:30:00.000Z"
type: post
template: post
faq:
  - q: "Wie wurde eine 2,8-GB-3D-Datei auf 46 MB für die Apple Vision Pro reduziert?"
    a: "In mehreren Schritten: Single-Room-Konzept statt zweier Vollräume, Instancing statt doppelter Geometrie, Mesh-Reduktion und Baking (30+ Einzel-Meshes zu einem), Echtzeitbeleuchtung via OpenUSD und Konvertierung aller Texturen von JPEG/PNG in das AVIF-Format (bis zu 90 % kleiner). Ergebnis: 46 MB bei stabilen 90 fps auf der Apple Vision Pro, iPhone und iPad."
  - q: "Kann man Augmented Reality auch ohne App auf dem iPhone nutzen?"
    a: "Ja. Mit OpenUSD und USDZ-Dateien lässt sich AR direkt über AR Quick Look starten – ohne App-Installation. Ein QR-Code genügt. Das Fallbeispiel Zgoll zeigt, wie Konferenzraum-Varianten per iPhone oder iPad in 1:1-Realgröße erlebbar gemacht wurden, inklusive interaktiver Buttons zum Durchschalten von Produktvarianten."
  - q: "Wie funktioniert ein VR-Videocall mit mehreren Personen über Apple Vision Pro?"
    a: "Bis zu fünf Personen können sich per Apple FaceTime in einem gemeinsamen virtuellen Raum treffen – als neue Funktion in visionOS. Dabei werden USDZ-Inhalte live geteilt und können direkt im Call interaktiv gesteuert werden. Im Fallbeispiel Zgoll wurden so Konferenzraum-Szenarien live im Stadion vorgestellt, ohne App und ohne zusätzliche Installation."
  - q: "Was ist der Vorteil von AR-Präsentationen gegenüber PowerPoint im Vertrieb?"
    a: "AR-Präsentationen machen Produkte erlebbar statt nur erklärbar: Maßstab, Varianten und Raumsituationen werden direkt sichtbar. Im Fallbeispiel Zgoll konnten Teilnehmende vier verschiedene Videokonferenz-Setups live im 1:1-Maßstab vergleichen – ein Erlebnis, das jede Folie ersetzt. Entscheidungen werden dadurch beschleunigt und Missverständnisse reduziert."
  - q: "Was bedeutet ProduktNUTZENvisualisierung?"
    a: "ProduktNUTZENvisualisierung zeigt nicht nur, was ein Produkt ist, sondern welchen konkreten Nutzen es für den Kunden hat. Mit Formaten wie AR, VR und OpenUSD werden erklärungsbedürftige Produkte greifbar und verständlich. Ziel ist es, aus einem interessierten Lead einen informierten Entscheider zu machen – und damit den Verkaufsprozess im B2B-Vertrieb zu beschleunigen."
ki_text: true
---

**Heute geht es um die praktische Anwendung der neuen *****Virtual-Reality-Teamcall-Funktionen***** einer Apple Vision Pro (AVP). Wir von viSales GmbH** **setzen ja schon seit einigen Monaten mehrere Projekte für das neue (Beta-)Betriebssystem visionOS26 von **Apple **um. Nun, *****nach der gestrigen Keynote*****: Bereit für ein Fallbeispiel dazu? **

**Tasse Tee *****-oder Kaffee-***** zur Hand für meine neuen Inspirationszeilen?**

## Ein Stadion wird zum Besprechungsraum

Genau das hat [Michael Zgoll](https://www.linkedin.com/in/michael-zgoll-47b3913a/) erst vor 6 Tagen, am **03. September 2025, **in Madrid ausprobiert. Aus organisatorischen Gründen nicht am Spielfeldrand des bekannten Santiago Bernabéu - sondern in der Tiefgarage - setzt er seine Vision Pro von Apple auf und Gruppen von je vier weitere Teilnehmer folgen seinem Beispiel. Eigentlich wollen sie sich nur das neue Cisco-Videokonferenzsystem in seinen Varianten ansehen. 

![](/assets/images/2025/12/Zgoll_Mobile_Office.png)

Doch anstatt auf klassische PowerPoint-Folien zu starren, stehen sie plötzlich gemeinsam in einem virtuellen Videokonferenzraum, der mitten im Raum existiert und sich mit einem Blick- und Handgriff in verschiedene Raum-Szenarien verwandelt.

![Artikelinhalte](/assets/images/2025/12/Zgoll_Mobile_Office_Innen.png)

So wird aus einer Produktdemo ein echtes Erlebnis: Die Teilnehmenden sind nicht nur Zuschauer, sondern mittendrin im Raum. Michael Zgoll führt sie Schritt für Schritt herum und durch die **Spatial Präsentation**, ein interaktives Kennenlernen der technischen Lösungen und Alternativen, das greifbarer und eindrücklicher ist als jede Powerpoint-Folie.

![Artikelinhalte](/assets/images/2025/12/Apple_Vision_Pro_Mobile_Office.png)

Wie sich diese Erfahrung selbst anfühlt? Weiter unten im Newsletter befindet sich QR-Codes, mit dem die Demo direkt in Augmented Reality ausprobieren werden kann. Im Tischformat und in 1:1-Realgröße, je nach Platzangebot.

## 8 Tage davor, ein Anruf von Firma zgoll: GmbH 

Für Zgoll war es nicht das erste gemeinsame Projekt mit uns und doch ein typisches Beispiel für viele unserer Kunden: Ein spontaner Anruf mit den Worten „Ich habe da eine Idee, könnt ihr kurzfristig…?“

**Die Kundenvision: **Zwei Besprechungsräume mit unterschiedlicher Videokonferenztechnik zum durchwandern für 5 Personen, als VR-Lösung. Fünf Apple Vision Pro sind beim Kunden vorhanden. Fertigstellung im Zeitraum von 5 Tagen, inklusive Wochenende...

**Unsere echte Herausforderung:** Aus einer branchenüblichen Inneneinrichtungsplanungs-Software kamen 2,8 Gigabyte an 3D-Rohdaten. Für den Einsatz im Videocall - über Apple FaceTime - musste das Material jedoch auf *unter 100 Megabyte* reduziert werden, damit es live und ohne technische Hürden funktioniert. Viele Anbieter hätten hier sofort zu einer teuren App-Lösung geraten.

Wir zeigen, dass es einfacher geht: Mit den nativen Funktionen von Apple visionOS 26 und interaktiven OpenUSD-Inhalten im USDZ-Format wird aus schwerfälligen 3D-Daten eine leicht zugängliche, erlebbare Präsentation… ohne App-Programmierung, ohne zusätzliche Installationen. Am Ende stand ein schlankes Modell mit nur noch rund 46 MB , termingerecht auf den Punkt geliefert.

**Vorteil für Marketing und Vertrieb:** Lösungen lassen sich spontan, live und ortsunabhängig präsentieren, ob im Besprechungsraum, im Videocall oder, wie im aktuellen Fall, mitten im Stadion. So wird selbst komplexe Technologie zum unmittelbaren Kundenerlebnis.

**Technik:** Solche Facetime-Videocalls mit Augmented Reality-Inhalten **gehen bei Apple schon seit einer ganzen Weile**. Von mir vorgestellt in [AR im eCommerce, ein Überblick](https://visales.de/augmented-reality-im-ecommerce-ein-uberblick/). Neu ist diese Funktion nun jedoch im „Virtual-Reality-Modus“ für die AVP mit bis zu fünf Personen an einem oder mehreren Orten.

## Zum Ausprobieren: Augmented Reality mit dem iPhone & iPad

Nicht jeder hat schon eine Apple Vision Pro auf der Nase, darum haben wir das Erlebnis für unterschiedliche Endgeräte zugänglich gemacht. Das neue Besprechungsraum-Modell von viSales gibt es in zwei Varianten:

1. Als handliches Tischmodell auf einem AR-Sockel, mit iPhone oder iPad direkt aufrufen und überall in Sekunden erlebbar machen
2. Als lebensgroßes VR-Modell, ebenfalls für iPhone und iPad, um Produkte im Maßstab 1:1 mitten in den Raum zu stellen und real zu erfahren

Beide Versionen lassen sich ohne zusätzliche App per QR-Code starten, ideal für Vertriebsgespräche, Kundentermine oder interne Präsentationen.

Und für alle, die (*noch*) kein iPhone oder iPad nutzen: Wir haben zusätzlich eine kompakte Videofassung als YouTube-Shorts in Vorbereitung. So wird das Prinzip der **ProduktNUTZENvisualisierung** auch plattformübergreifend anschaulich.

## Zwei Modelle mit angepassten Funktionen

Für diesen Newsletter haben wir das große Modell noch weiterentwickelt: Es wurde im Maßstab angepasst und auf einen virtuellen Sockel gestellt. Das macht den Einblick in den Konferenzraum deutlich intuitiver und erleichtert die Präsentation.

![Artikelinhalte](/assets/images/2025/12/TischmodellQRCode.png)

Auf dem Sockel befindet sich ein auffälliger oranger Interaktions-Button, damit lassen sich verschiedene Konferenztechnik-Setups direkt durchwechseln. So können Entscheider auf einen Blick vergleichen, wie unterschiedliche Lösungen im Raum wirken.

![Artikelinhalte](/assets/images/2025/12/QRCode_IPhone_IPad.png)

In der lebensgroßen Variante geht das noch einen Schritt weiter: Hier lässt sich nicht nur die Technik, sondern auch das gesamte Besprechungstisch-Setup anpassen. So entsteht eine echte ProduktNUTZENvisualisierung im Maßstab 1:1 – mit maximaler Relevanz für Marketing und Vertrieb, weil Produkte nicht erklärt, sondern erlebt werden.

[Embed: https://www.youtube.com/watch?v=K0u44ylyP0o](https://www.youtube.com/watch?v=K0u44ylyP0o)

## Von 2,8 GB zu 46 MB: Fast 99 % kleiner

Wie schaffen es Unternehmen, komplexe Produkte digital erlebbar zu machen – und dabei gleichzeitig technische Ressourcen zu schonen? Die folgende Beschreibung zeigt einige Arbeitsschritte und den erreichten Einsparungseffekt in diesem Projekt und verdeutlicht, was wir in der Praxis umsetzen und welche Effizienzgewinne auch für Ihr Unternehmen möglich sind.

Firma Zgoll konnte in seiner Planungssoftware verschiedene Konferenzraum-Szenarien zusammenstellen: Tische in zwei Größen, unterschiedliche Bestuhlungen sowie vier Varianten von Videomöbeln. Der direkte USDZ-Export für iPhone, iPad und Apple Vision Pro erzeugte jedoch 2,8 GB an Daten - unstrukturiert und für mobile Geräte ungeeignet, da jedes Detailobjekt einzeln exportiert wurde.

In mehreren Schritten haben wir die Datenmenge und die geometrische Komplexität massiv reduziert:

- **Single-Room-Konzept:** Anstelle zweier kompletter Räume (für 12er- und 16er-Setup) gibt es einen optimierten Konferenzraum, in dem nur die Tischvariante gewechselt wird. Das entlastet die GPU der Apple Vision Pro, verhindert unsichtbare, aber rechenintensive Geometrie im Hintergrund und ermöglicht stabile 90 fps.
- **Instancing statt Duplikate:** Statt 12 oder 16 einzelne Stühle zu exportieren, wird ein optimiertes Modell als Instanz vielfach referenziert.
- **Mesh-Reduktion & Baking:** Ein Bürostuhl bestand ursprünglich aus über 30 Einzel-Meshes mit separaten Materialien. Nach dem Zusammenfassen und Baken entstand ein einziges Mesh mit einer effizienten PBR-Textur.
- **Echtzeitbeleuchtung: **Statt wie vor über drei Jahren Lichtstimmung in die Wände einzuarbeiten - *Siehe unser preisgeköntes* Somfy*-Projekt* ([Augmented Virtuality im Digitalen Musterhaus](https://www.youtube.com/watch?v=ELAIrRXOQeQ)) - haben wir hier die neue Echtzeitbeleuchtungsfunktion von OpenUSD genutzt. Hatten wir zuerst gezeigt in unserer [2024er-Weihn-AR-chtskarte](https://visales.de/weihnachten_postkarte_augmented_reality/).
- **Interaktive Bedien-Panels:** In der VR-Szene können zwei Panels direkt im Raum anvisiert werden - eines schaltet zwischen den vier Videomöbel-Varianten, das andere zwischen den beiden Tischgrößen. Die Steuerung erfolgt so intuitiv und ohne Menüwechsel.
- **Modernes Texturformat:** Alle Texturen wurden von JPEG/PNG in das neue **AVIF-Format** konvertiert, wodurch manche Dateien um bis zu 90 % kleiner wurden – ohne sichtbare Qualitätseinbußen. Dazu wurde am Samstag mit KI-Code-Unterstützung eine neue Funktion unserer Toolbox entwickelt. *Allein dieser Schritt sparte am Ende nochmals 20 MB ein!*
- **Asset-Wiederverwendung:** Jedes optimierte Objekt ist nun modular und kann in künftigen Projekten direkt erneut eingesetzt werden, ohne erneute Aufbereitung.

**Das Ergebnis:** Aus 2,8 GB wurden knapp 46 MB, performant genug für Apple Vision Pro, iPhone und iPad, und kompakt genug, um per (Video-)**SharePlay** mit mehreren Nutzern gleichzeitig geteilt zu werden.

**Der Nutzen für Marketing & Vertrieb:** Varianten lassen sich live durchschalten und sofort vergleichen. Entscheider erleben unterschiedliche Raum- und Technik-Setups direkt im Maßstab 1:1 – ohne Wartezeiten, ohne Ruckeln, ohne App-Installation. So werden Entscheidungsprozesse beschleunigt und komplexe Technik zu einem verständlichen, begeisternden Kundenerlebnis.

*Wenn Sie neugierig geworden sind und tiefer in die Hintergründe einsteigen möchten: Wir teilen unsere Erfahrungen auch in individuellen Schulungen und Intial-Projektrunden. Melden Sie sich gern, wenn Sie mehr über die Chancen für Ihr Marketing erfahren möchten.*

## Vertiefung: Vier Artikel und ein Livestream zu Spatial Content & AR im Marketing

Welche Entwicklungen treiben den Wandel vom 2D-Web hin zu immersiven 3D-Erlebnissen? Wie lässt sich Augmented Reality bereits heute im eCommerce einsetzen – und welche Rolle spielt FaceTime dabei? Diese und weitere Aspekte beleuchten diese vier Beiträge aus dem Archiv:

- [Von 2D zu 3D: Wie das Web spatial wird und was Unternehmen davon haben](https://visales.de/spatial-website_enviroments_apple_vision_pro_model_tag/): Wir haben inzwischen mehrere Website-spezifische "Enviroments" erstellt. Erklär-Video folgt bald!
- [Einstieg: Spatial Content im Marketing:](https://visales.de/einstieg-spatial-content-im-marketing/) Mit einem Überblick über die 3D-Formate inkl. Foto & Video
- [AR im eCommerce, ein Überblick](https://visales.de/augmented-reality-im-ecommerce-ein-uberblick/)
- [HowTo iPhone-Facetime mit Augmented Reality:](https://www.linkedin.com/feed/update/urn:li:activity:7322145513057800192/) Aufbereitung als Slideshow 
- Dazu eine Ankündigung für den nächsten Livestream: „**Rückblick auf die Apple Keynote**“ mit dem Experten [Thomas Riedel](https://www.linkedin.com/in/triedel/) ([Spatial Realities Podcast](https://metaverse-podcast.de/)) und die Gastgeber [Kai Heddergott](https://www.linkedin.com/in/kaiheddergott/) & [Gerhard Schröder](https://www.linkedin.com/in/gerhardschroeder/) am **16. September um 12 Uhr** ([LinkedIn](https://www.linkedin.com/events/7368169728927797249/) & [YouTube](https://youtube.com/live/FmMcwfl_WH8))

## Zum Schluss: Ein Tee, ein Kaffee und ein Gedanke für Marketing & Vertrieb

Verkaufen ist am Ende immer eine Zahl, denn Umsatz lässt sich messen. Doch der Weg dorthin läuft über Leads zu Erlebnissen. Wenn meine Kunden durch ein visuelles Aha-Erlebnis mehr verkauft wird, habe ich mein Ziel erreicht.

Wir sind weder klassische „Verkaufstrainer“ noch eine „normale“ Werbeagentur und auch keine Lead-Beschaffungsagentur. Die Generierung neuer Kontakte ist Aufgabe anderer.

Unser Ansatz setzt dort an, wo im B2B-Marketing und -Vertrieb die größten Hürden entstehen: beim** Lead-Nurturing** und in der **Sales-Enablement-Phase**. Gerade bei erklärungsbedürftigen Produkten bremsen unklare Botschaften, lange Erklärschleifen und fehlende Visualisierung häufig den Verkaufsprozess.

Deshalb setzen wir auf *ProduktNUTZENvisualisierung*: Inhalte, die nicht nur zeigen, was ein Produkt ist, sondern vor allem, **welchen Nutzen es für den Kunden hat**. Mit Formaten wie (2D/3D-)Foto/Grafik, Video oder AR&VR (OpenUSD) werden komplexe Lösungen anschaulich, greifbar und verkaufsstark inszeniert. So entsteht aus einem interessierten Lead ein informierter Entscheider und am Ende ein Kunde. **Wir machen Leads verkaufsbereit, mit Visual Sales.**

Als viSales arbeiten wir, ein reguläres Grafik-, Video- und dazu Hardcore-Code-Spezialistenteam für OpenUSD, aber immer mit einem klaren Sales-Mindset. Ja, KI-Tools sind im Backend längst Standard. Aber komplexe Produkte und Dienstleistungen werden (noch) von Menschen an Menschen verkauft. Und Menschen sind visuell erreichbar. Genau deshalb dieser Weg: viSales = Visual Sales.

Nicht ohne Grund hören wir von führenden Apple-Vision-Pro-Experten Feedback wie: „**Bin wirklich begeistert, was Ihr mit USDZ only auf die Beine stellt – das ist echt eure Kompetenz, die ihresgleichen sucht. 🙇**“ (Mark Zimmermann, Mobile Technology Expert @EnBW &gt; [Workshop-Bericht](https://www.linkedin.com/posts/gerhardschroeder_visionos26-environment-webenvironments-activity-7370376494776213504-Zu7X?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAKaaIkBCS8zGNs-1btUP3WES7BQ3Vf6uzc))

Und falls bei einem Tee *oder Kaffee* der Gedanke aufkommt, ob sich auch die eigene Produktwelt so inszenieren ließe… einfach melden. Ich freue mich über Austausch, gern ganz unkompliziert.

Viele Grüße aus Velbert,

Gerhard Schröder

&nbsp;

&nbsp;

&nbsp;

&nbsp;

### **Ihr Produkt in AR — wann können wir starten?**

AR-Visualisierung für Ihr Produkt ist in wenigen Wochen umsetzbar. Zeigen Sie uns Ihr Produkt — wir zeigen Ihnen wie es in AR aussieht. **Siemens, Somfy und Rheingas vertrauen viSales.**

[Projekt anfragen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

&nbsp;



