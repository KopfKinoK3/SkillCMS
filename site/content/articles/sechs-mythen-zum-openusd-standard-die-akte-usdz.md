---
title: "Sechs Mythen zum OpenUSD-Standard: Die USD-Z-Akte"
slug: sechs-mythen-zum-openusd-standard-die-akte-usdz
status: published
primary_tag: visual-sales
tags: [visual-sales, openusd, usdz]
meta_title: "6 USDZ-Mythen im Faktencheck: Was wirklich stimmt"
meta_description: "Ist USDZ nur ein Apple-Format? Braucht man glTF statt OpenUSD? Sechs verbreitete Irrtümer — mit Einordnung aus 15 Jahren 3D-Praxis für Industrie und B2B."
feature_image: /assets/images/2025/12/usdzfiles.png
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2025-11-14T15:17:59.000Z"
type: post
template: post
faq:
  - q: "Stimmt es, dass OpenUSD nur mit NVIDIA-Grafikkarten funktioniert?"
    a: "Nein. Python-OpenUSD läuft nur im NVIDIA Omniverse auf NVIDIA-Grafikkarten. Viele 3D-Assets in OpenUSD funktionieren aber direkt mit Pixar-Animationssoftware oder über Apple-AR-Lösungen – ohne NVIDIA-Hardware. Diese Fehlinformation wird von NVIDIA-Dienstleistern gerne verschwiegen, da teuere Hardware und Lock-In-Effekte das Geschäft fördern."
  - q: "Funktioniert USDZ nur im Apple-Ökosystem?"
    a: "Nein. USDZ ist kein proprietäres Apple-Format, sondern ein standardisierter Container innerhalb des offenen OpenUSD-Ökosystems. Was zu diesem Mythos führt, ist AR Quick Look (ARQL) – ein in iOS integrierter Player, der USDZ ohne App-Installation abspielt. Viele Industrieunternehmen wie Siemens, BMW oder NVIDIA unterstützen OpenUSD und USDZ in ihren eigenen Plattformen."
  - q: "Ist USDZ schlechter komprimiert als glTF?"
    a: "Nein, eher umgekehrt. glTF basiert ausschließlich auf Polygonen (Dreiecken). USDZ kennt auch Vierecke, Vielecke und USD-Primitive wie Kugel oder Würfel, die als vier Datenpunkte statt 36 Datenpunkten beschrieben werden. Die Aussage stammt aus dem glTF-Marketing und ist technisch falsch. Die eigentliche Qualität hängt vom jeweiligen Export ab."
  - q: "Kann USDZ keine Interaktionen?"
    a: "Falsch. Apple hat den OpenUSD-Standard um Interaktionen erweitert (Native-OpenUSD). Auf iPhone, iPad, Mac und Apple Vision Pro kann eine einzige USDZ-Datei statisch, animiert und interaktiv genutzt werden – direkt via AR Quick Look ohne App. glTF kann Interaktionen nur über zusätzliche Browser-Software, was bei echtem interaktiven AR mit monatlichen Lizenzkosten verbunden ist."
  - q: "Sind USDZ-Dateien verschlüsselt und nicht auslesbar?"
    a: "Nein. USDZ ist ein ZIP-Container und kann von fast jeder modernen 3D-Software gelesen und geschrieben werden, darunter Siemens NX. Die Verwechslung entsteht durch das Apple-Format *.reality, eine optional versiegelte Version, die bewusst nicht mehr editierbar ist – ähnlich einem digital signierten PDF. Das betrifft aber nicht den USDZ-Standard selbst."
---

- **Viele verbreitete Aussagen über OpenUSD und USDZ sind Fehlinformationen, kein neutraler Konsens, und behindern strategische Entscheidungen. **
- **OpenUSD ist nicht einfach ein Austauschformat, sondern eine Masterstruktur, die redundante Datenaufbereitungen in 3D-Prozessen überflüssig machen kann. **
- **USDZ wird oft technisch überhöht, obwohl sein Wert im gemeinsamen Datenverständnis und der Wiederverwendung für verschiedene Anwendungen liegt. **

&nbsp;

**Sie sind keine gewöhnlichen Ermittler: Eine rothaarige Frau, ruhig und skeptisch, rührt in ihrem Kaffee. Ein Mann, überzeugt, dass hinter jedem Dateiformat mehr steckt als nur Code, nippt an seinem Tee.**

**Zwischen ihnen liegen ausgedruckte Screenshots, Forenbeiträge, technische Spezifikationen ... Spuren eines Rätsels. Mythen, Fehlinformationen, widersprüchliche Wahrheiten. Mit jeder Zeile tauchen sie tiefer in ein digitales Labyrinth. **

**Die Akte trägt den Namen eines Dateiformats, das verspricht, Effizienz und Wahrheit zu verbinden und doch so oft missverstanden wird: Die "Akte USDZ".**

Passend zum Titelbild eine kleine Akte-X-Einstimmung in die heutige Ausgabe. Spaß beiseite ...

## Warum sollte sich jeder aus Marketing & Sales mit diesem 3D-Datenformat beschäftigen?

> Wäre eigentlich auch ein Mythos: "OpenUSD ist nur für Konzerne".   
>   
> Aber: Gerade im Mittelstand entfaltet OpenUSD seinen Nutzen, weil dort parallele Datenwege besonders schnell zu unnötiger Doppelarbeit führen.

**Effizienz, Kosteneinsparung **und** Datensouveränität**: Dies sind die drei zentralen Vorteile, warum ich mich seit Anfang 2017 in meiner Rolle als Verkaufsleiter / Geschäftsführer mit so einem "technischen" Thema zu beschäftigen begann.

**Effizienz** fängt damit an, dass Kunden nicht mehr mehrere Dienstleister für 3D-Werbegrafik, Software-Simulation vor der Inbetriebnahme, Website-3D und Augmented Reality benötigen. 

Unnötige, mehrfache Datenaufbereitung ist eine ***Kostenfalle für viele Mittelständler, die locker vermieden werden kann*** durch eine Vereinheitlichung der Aufbereitung (**Master-Dateiformat**) und ergibt somit eine **Kosteneinsparung**.

**Reales Fallbeispiel eines unserer Kunden vor Beginn unserer Zusammenarbeit: **Ein interner Mitarbeiter überarbeitet die CAD-Daten, erstellt daraus statische 3D-Renderings und einfache Kamerafahrten in Unreal. Ein externer Dienstleister nutzt dieselben Daten erneut, wandelt sie in Unity um, um eine SPS-Simulation der Anlage zu erstellen. Für die Website folgt eine weitere Aufbereitung, für Apple-AR ein zusätzliches Format. Spätestens beim „Digitalen Zwilling“ existieren mehrere Varianten desselben Datensatzes, jede einzeln aufbereitet, jede mit eigenem Aufwand. Fünf Dateiaufbereitungen statt einer Master-Datei für alle weiteren Zwecke.

Alternative / **Vorteil:** Mit einem einheitlichen Master-Dateiformat wie OpenUSD lässt sich dieser Prozess vereinfachen: Von CAD zu OpenUSD und von dort aus, falls nötig, in weitere Formate oder an verschiedene Dienstleister. Die Basisarbeit wird nur einmal erledigt, bleibt konsistent und erspart Zeit, Kosten und Abstimmungsfehler.

**Datensouveränität**: Viele Dienstleister erfordern eine Dateninkompatibilität oder ein Dienstleister-Lock-In-Effekt. Wir geben bei unseren Kunden die fertigen 3D-Daten heraus, denn nur so kann so ein Lock-In vermieden werden. Durch den Einsatz von offenen Standards können so Dienstleister und Software einfach gewechselt werden.

Noch weiter gedacht: Da es kein US-Software-Anbieter wie z.B. Unity oder Unreal sein muss, bei dem die Daten auch schnell in deren Cloud-Diensten landen könnten, ist auch hier eine rein nationale oder lokale Lösung möglich.

Grund genug sich als Marketing- & Sales-Verantwortliche Person mit diesem Thema zu beschäftigen. Wer nun eine knappe, technische Erklärung zu OpenUSD haben möchte, hier ein paar Zeilen bei einer Tasse Tee *oder Kaffee*. #TLDR

## **Was ist OpenUSD? **

OpenUSD ([Open-Universal Scene Discription](https://visales.de/404/)) mit dem Dateiformat USDZ ist ein Standard für 3D-Dateien mit Animation -*und Interaktion**- direkt in einer Datei. Ursprünglich „erfunden“ von der Animationsfirma Pixar ist es nun ein internationales Open-Source-Projekt der „Alliance of USD" ([AOSUD](https://aousd.org)) unter Verwaltung der Linux Foundation. 

Der AOUSD haben sich inzwischen viele deutsche Industrieunternehmen wie SIEMENS, VW, BMW und Co. angeschlossen. Natürlich gehören auch US-Konzerne wie z.B. Pixar, Apple, NVIDIA oder Google der AOUSD an. Die Liste umfasst weltweit über 2.000 Unternehmen. Keine kleine Nischenlösung, sondern eine breite Zukunftsallianz.

*Hinweis: Wir sind seit dem Start Mitglied in der AOUSD, im *[*Metaverse Standards Forum*](https://metaverse-standards.org)* und unterstützen seit 2017 die USDWG (USD Working Group).*

## **Ergänzung: Was unterscheidet USDZ von anderen 3D-Formaten wie zum Beispiel einer OBJ- oder STEP-Dateien?**

Viele herkömmliche Dateiformate beschreiben ein einzelnes Objekt. In diesem Beispiel beschreibe ich nun ein Bein: Fuß, Unterschenkel und Oberschenkel. Drei Teile, jeweils eine Datei. Wie dieses Elemente sich nun bewegen können (Animation) ist aber noch garnicht definiert. 

In einer USD-Z-Datei (das Z steht für das Datenkomprimierungsformat ZIP) befinden sich in diesem Beispiel also gleich drei Datenpakete (Fuß, Unterschenkel und Oberschenkel) und dazu die Beschreibung der Bewegung / Beweglichkeit. Also in Summe vier Datenpakete.

Außerdem kann durch eine Erweiterung des OpenUSD-Standards von Apple auch in dem Datenpaket die Programmierung (Interaktion) eingefügt werden: Stichwort "Digital Twin". Somit habe ich eine „programmierbare“ 3D-Datei. Wir von viSales sprechen da von **Native-OpenUSD**.  
  
NVIDIA unterstützt mit seinem [Omniverse](https://www.nvidia.com/de-de/omniverse/)-System auf Windows-Rechnern einen alternativen Ansatz für Interaktionen bei dem diese Programmierung in Zusatzdateien als Python-Skript abgelegt wird. In dem Fall sind also 2+ Dateien erforderlich für die Aufgabe. Wir von viSales sprechen da von **Python-OpenUSD**.

Simulationen (Digital Twins & Shadows) lassen sich auch via OpenUSD abbilden. Mehr dazu unter [Digital Twins im Mittelstand](https://visales.de/digital-twins-im-mittelstand-was-mitgeliefert-wird-spart-spater-zeit-und-geld/).

&nbsp;

&nbsp;

### **Einstieg in AR & USDZ — mit Unterstützung.**

Wir begleiten Unternehmen vom ersten USDZ-Modell bis zum eingebetteten AR-Erlebnis im Vertrieb. Das erste Gespräch dauert 30 Minuten. Ohne Pitch, ohne Vorbereitungspflicht. **Rheingas, Somfy und Carl Hamm haben mit einem Produkt begonnen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

## **Mythos 1: OpenUSD funktioniert nur mit NVIDIA-Grafikkarten**

Fehlinformation, gut gestreut von NVIDIA, welche ja gern High-End-Grafikkarten verkaufen wollen. Wie oben erklärt läuft Python-OpenUSD nur im NVIDIA Omniverse - auf NVIDIA-Grafikkarten - aber viele 3D-Assets laufen auch direkt mit Pixar-Animationssoftware oder via Apple Augmented-Reality-Lösungen... sofern man bei der Bearbeitung und Export der Dateien darauf Wert legt!

Omniverse-Dienstleister verschweigen gern diese kleine Besonderheit ... Ein Schelm wer da an teuere Hardwareverkäufe und Lock-In-Effekte denken mag, was ja gern Apple vorgeworfen wird. Aber auch andere Marktteilnehmer gehen gern diesen Weg.

Ergänzung: Wer nun den Weg Nvidia-Omniverse + Apple Vision Pro als AR-Headset testen mag: Es ist wie bei Radio Eriwan, im Prinzip geht es. Demos in Besprechungsräumen oder Design-Offices sind aber keine Umgebungen, die überall anzutreffen sind. Es kann schnell bei zu großer Latenz zu ruckelnden AR-Objekten in der Brille kommen, denn die von Omniverse-Anbietern gefeierte "Pixelstreaming-Technologie" ist sehr latenzanfällig. 

Der alternative Ansatz wäre "On-Device-Rendering", wie z.B. mit der Apple Vision Pro – was uns zu Mythos 2 führt...

**Kurz: USDZ ist kein proprietäres Apple-Format, sondern ein standardisierter Container innerhalb des offenen OpenUSD-Ökosystems – Apple nutzt ihn, kontrolliert ihn aber nicht.**

## **Mythos 2: USDZ funktioniert nur im Apple-Ökosystem**

Wie oben beschrieben gibt es viele Industrieunternehmen, die den OpenUSD-Standard (USDZ-Dateien) unterstützen. Was zu dem Irrglauben / Mythos 2 führt ist nicht USDZ, sondern ARQL (AR Quick Look), ein im Apple-Betriebssystem direkt integrierter Player von USDZ-Dateien, der ohne weitere Installation einer App funktioniert. Mehr dazu unter [Was ist AR Quick Look?](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/) Auf der AVP heisst ARQL hingegen 3DQL, ist aber 1:1 die gleiche Technologie.

Eine solche gute Integration von 3D & AR kann bis heute Android im System leider nicht bieten. Google plant in den nächsten Jahren mit AndroidXR eine in kleinen Schritten vergleichbare Funktion zu integrieren. Bis aber auf einem aktuellen Android-Handy eine solche Betriebssystemfunktion vorhanden ist, wird noch eine Weile (Jahre) dauern.

**Kurz: USDZ wird oft auf AR reduziert, obwohl sein eigentlicher Wert in der portablen Weitergabe strukturierter 3D-Inhalte über verschiedene Kontexte hinweg liegt.**

## **Mythos 3: USDZ ist schlechter komprimiert als das alternative glTF-Format von Google****

Auch wenn auf einigen Websites aus dem glTF-Umfeld diese falsche, klar dem Marketing geschuldete Aussage zu lesen ist, ist es doch genau umgekehrt. 

Kurze technische Erklärung dazu: glTF und viele weitere Datenformate basieren nur auf Polygonen, also vielen Dreiecken,  zur Darstellung eines 3D-Objekts. USDZ kennt hingegen auch Vierecke und Vielecke, Basisformen (Kugel, Kegel, Würfel & Co) und können sogar als **USD-Primitive** beschrieben werden. 

Ein Beispiel dazu: Ein Würfel besteht aus sechs Seiten. Dazu muss ich bei vielen Datenformaten jede Seite mit zwei Dreiecken beschreiben. Jedes Dreieck hat DREI Datenpunkte / Ecken im 3D-Raum. Ergibt in Summe 6 x 2 x 3 = 36 Datenpunkte. OpenUSD kann hingegen einfach „Würfel, Höhe, Breite, Tiefe“ verarbeiten, lediglich vier Datenpunkte für ein „USD-Primitiv“, ganz ohne weitere Komprimierung, denn DIES ist die datensparsamste Art der Objektbeschreibung. **Datensparsamkeit** ist eines der obersten Gebote dieses Formats.

![](/assets/images/2025/12/Polygone_Vierecke_Primitive.png)
*Meine Skizze hat Miranda dankenswerter Weise in diese Grafik umgesetzt. Wer dazu weitere Fragen hat, gern melden.*

Um diese Polygon-Schwäche auszugleichen gibt es bei glTF tatsächlich Komprimierungsverfahren. Doch wozu Polygone / Dreiecke komprimieren, wenn ich direkt Vielecke oder USDZ-Primitive verwenden kann?

Die Wahrheit ist also: Es hängt von dem genauen Export bei jeder Datei ab. Wenn ein USDZ-File nicht die Vorteile ausnutzt, sondern z.B. von einem Web-Dienstleister zuerst als glTF/glb exportiert wird und draus dann via Automatik eine USDZ-Datei erzeugt wird, dann ist ein gewisser "Datensalat" vorprogrammiert.

**) Der glTF-Standard ist von der Khronos-Group, wird von Entwicklern jedoch als der Standard von Google bezeichnet. Auch ein Web-Mythos ...

## **Mythos 4: USDZ kann keine Interaktionen*, glTF hingegen schon**

Auch dies ist eine klare Falschaussage: glb-Dateien (glTF-Standard) können von Haus aus *keine* Interaktionen, sondern zusätzliche Browser-Software-Lösungen erlauben es, einzelne glb-Elemente zu animieren, mit Interaktionen zu versehen und im Browser darzustellen. Läuft dann auf allen Geräten: Windows-PC, Mac, Android oder iOS, sofern diese Zusatz-Software vom Browser unterstützt wird.

Ich schreibe hier mit Absicht nur von **Browser-AR**. App-Lösungen sind ja eine ganze eigene Welt. Leider ist es aber ein großer Unterschied, ob ich auf einem Android-Handy nur ein statisches Objekt, zum Beispiel ein IKEA-Regal, ins Zimmer stellen möchte, oder ob ich ein Browser-AR-Produktkonfigurator umsetzen möchte. Dies geht technisch auch auf Android-glTF-Basis, jedoch hat für diesen Einsatzzweck (interaktive AR im Browser) ein US-Unternehmen ein Patent und wer somit echte interaktive AR-Anwendungen umgesetzt haben möchte - [haben wir zum Beispiel für die Firma SIEMENS neben einer USDZ-Lösung umgesetzt](https://visales.de/augmented_reality-data-driven-x-siemens-fallbeispiel/) - der muss monatliche Lizenzkosten zahlen. Bei Fragen dazu, bitte direkt bei mir melden - Danke!

Zur Wahrheit gehört auch: Bei USDZ-Dateien ist die Lage eine andere. Auf einem iPhone, iPad, Mac oder einer Apple Vision Pro kann eine einzige USDZ-Datei auf allen Geräten genutzt werden. Statisch, Animiert und Interaktiv, direkt in AR via AR Quick Look, ohne weitere App-Installation. Für Windows-PCs und Android-Handys muss zusätzlich eine glTF-Lösung erstellt werden. Diese Dateien zu erstellen ist aber oft ein einfacher Umwandlungsvorgang.

**Kurz: Der Vergleich zwischen glTF und OpenUSD verfehlt oft den Kern, weil beide unterschiedliche Probleme lösen: Übertragung auf der einen, Datenorganisation auf der anderen Seite.**

## **Mythos 5: USDZ ist ein Allzweck-3D-Format – für jede Anwendung die beste Wahl**

Fast. 

Es gibt Spezialthemen wie Building Information Modeling ([BIM](https://de.wikipedia.org/wiki/Building_Information_Modeling)) mit eigenen Datenanforderungen. Die oben erwähnte AOUSD erarbeitet zur Zeit entsprechende Datenbeschreibungsergänzungen. D.h. in einer USD**Z**(= Zip)-Datei, also einem gezippten Ordner mit weiteren Daten, können neben den 3D-Daten für eine Darstellung z.B. auf dem iPhone auch weitere Daten enthalten sein. Der "Player auf dem Handy" (ARQL) ignoriert zunächst solche Daten und stellt das 3D-Objekt wie gewohnt da. Somit werden im Prinzip nicht mehrere Dateien für eine Aufgabe benötigt.

Selbst absolute technische Neuerungen im 3D-Bereich wie **Gaussian Splats **sind via OpenUSD / USDZ abgedeckt. Die neuen Personas (3D-Gesichter für Videocalls) bei einer Apple Vision Pro sind schon 4D-Gauss-Splats.

Wie immer gilt natürlich: Erst den genauen Bedarf klären. OpenUSD ist aber eine Art 3D-HTML für das Internet der Gegenwart und Zukunft. Mehr dazu: [USDZ: So wichtig wie MP3 und HTML](https://visales.de/usdz-so-wichtig-wie-mp3-und-html/).

## Mythos 6: USDZ‑Dateien sind verschlüsselt und können nicht extrahiert werden

Völlige Fehlinformation.

Fast jede heutige 3D-Software kann inzwischen USDZ-Dateien lesen und speichern. Eine Software, die kein USDZ kann, ist inzwischen die Ausnahme. Selbst eine lange am Markt befindliche Industrie-CAD-Software wie [Siemens NX](https://plm.sw.siemens.com/en-US/nx/products/nx-x-manufacturing/) kann USDZ speichern, denn SIEMENS ist Teil der [AOUSD.](https://en.wikipedia.org/wiki/Alliance_for_OpenUSD)

**Der OpenUSD-Standard umfasst im Kern diese drei (plus eins) Teilformate:**

1. ***.USDZ**: Ein Zip-Container mit komprimierten Daten. *Hinweis: *****.usdz**** (Kleinbuchstaben) ist ein ZIP-Archiv mit allen benötigten Dateien: Es wird absichtlich keine ZIP-Kompression angewandt, weil die Inhalte selbst bereits komprimiert sind (png, jpeg, Audio, Binär-USD (USDC).*
2. ***.USDC**: C steht hier für binäre Inhalte. Diese Datei muss mit einem kostenlosen Tool aus dem Internet erst in eine USDZ umgewandelt werden. Dies ist kein Hexenwerk, genauso einfach wie einen Ordner mit einigen Dateien in ein Zip zu packen / entpacken. Es kann sein, dass "mit Absicht" in so einer Datei einige Abschnitte (z.B. aus Geheimhaltungsgründen) nicht weiter verarbeitet werden können. *Die im A wichtigste Eigenschaft von OpenUSD wird sogar von vielen in der AOUSD derzeit übersehen: Mehrschichtige Wiederverwendung von Daten.*
3. ***.USDA**: A steht für ASCII, diese Datei kann mit der gleichen Software umgewandelt werden. Die Datei ist dann eine reine Textdatei, die mit jedem Texteditor editiert werden kann. Diesen Weg gehen wir immer wieder, um dann mit unseren eigenen Programmierwerkzeugen oder Open-Source-Tools die Dateien zu bearbeiten.
4. ***.reality**: Dies ist eine Apple-spezifische Ergänzung des Standards, der *vermutlich* zu dem Mythos führte. Wenn das Projekt zur Veröffentlichung fertig ist, kann man optional ein Apple-Tool nutzen, um eine USDZ-Datei in eine Reality-Datei umzuwandeln: Kompiliert & versiegelt für das Publishing. Diese Datei ist dann nicht mehr einsehbar oder gar nachträglich veränderbar.  
  
Die Gründe dafür liegen auf der Hand: So wie ein digital signiertes PDF nicht mehr verändert werden kann / soll, so soll eine Reality-Datei MIT ABSICHT nur noch BETRACHTET, aber nicht mehr im Detail eingesehen oder gar editiert werden können.  
  
Ein Schelm, wer daran denkt eine solche Datei einsehen zu wollen: So verhindern zum Beispiel einige unserer Kunden, dass Konstruktionsdaten "einfach so" ins Netz gestellt und ausgelesen werden können. #Industriespionage

![](/assets/images/2025/12/PolarisQRCode.png)

**Hier eine solche Reality-Datei als Beispiel:** Sieht aus wie eine gewöhnliche OpenUSD-Datei, kann zwar mit Apple-Geräten betrachtet werden, jedoch nicht mehr editiert. Sie stammt aus meinem Artikel über unsere Non-NDA-Aerospace-Projekte: [Next-Level Aerospace Pitch-Fallbeispiele](https://visales.de/aerospace-augmented-reality_openusd_usdz/). Dort als Video eingebunden.

[Embed: https://www.youtube.com/watch?v=T5j-hLsDwv0](https://www.youtube.com/watch?v=T5j-hLsDwv0)

*Mitschnitt meines Vortrags am 25.11.2025 in Stuttgart im Rahmen der "XR-Tagung", circa 28 Minuten. *[*Weitere Vorträge und Interviews auf YouTube.*](https://www.youtube.com/playlist?list=PLIggDLmpuIxqVKu9rrX_wxd_tueBs0jGd)

> **OpenUSD und seine Containerformate wie USDZ werden häufig missverstanden, weil man sie als einzelne Formate statt als Teil einer gemeinsamen Datenstrategie begreift.**  
>   
> Die Debatte um OpenUSD und USDZ scheitert oft daran, dass Formate statt Datenstrukturen verglichen werden. Entscheidend ist nicht, wie 3D verteilt wird, sondern ob es einmal sauber aufgebaut und anschließend mehrfach genutzt werden kann.

## **Vorgeschichte: Testen eines KI-Browsers**

ChatGPT stellte vor ein paar Tagen seinen eigenen KI-Browser [ATLAS](https://chatgpt.com/de-DE/atlas/) vor, und ich nahm mir den kurzen Moment für den Download und hatte dann einen Browser mit „Agentenfunktion“. 

Erster Ego-Test: Wie gut wird mein Unternehmen viSales zum Thema AR in der Region gefunden? Platz zwei. Ok, der erste Platz wäre mir lieber … 

Zweiter Test, noch ohne Agentenmodus, in Vorbereitung für den heutigen Beitrag: "Nenn mir doch mal die Top-3-Mythen zu USDZ". Das Ergebnis stimmte mit meinen Erwartungen überein: Genug Fehlinformationen, um einen lesenswerten Drei-Mythen-Artikel zu verfassen.

Dann aktivierte ich den Agentenmodus und ließ eine Detailrecherche laufen. Was dabei raus kam, führte zu dem heutigen Sechs-Mythen-Artikel. So viele Fehlinformationen, mit Quellenangaben, da muss eine umfangreiche Klarstellung erfolgen.

Damit war klar: Bei so vielen Fehlinformationen, mit einer Veröffentlichung dieser  Zeilen im kalten und dunklen November, muss es eine Akte-X-Anspielung – *Alternative wäre *[*Aktenzeichen XYZ-Ungelöst*](https://www.zdf.de/magazine/aktenzeichen-xy-ungeloest-110)* gewesen –* als Titelbild geben. [Titelmelodie](https://www.youtube.com/watch?v=zTLyQ2xf82I) bitte selbst Pfeifen!

Viele Grüße aus dem Velberter Homeoffice,

Gerhard Schröder

PS: Wir bieten zu dem ganzen OpenUSD-Thema, ebenso wie zu Apple (Vision Pro), Inhouse-Workshops an und setzen natürlich auch komplette Projekte im 3D- / AR- / VR-Bereich um. Wer mag, hier der Link zur [Terminvereinbarung](https://visales.de/kontakt/).

&nbsp;

&nbsp;

&nbsp;


→ Alle Einsatzszenarien: [AR-Lösungen für Messen & Events](https://visales.de/augmented-reality/)

→ OpenUSD in der Praxis: [OpenUSD-Dienstleister viSales](https://visales.de/openusd-dienstleister/)


