---
title: "Fünf praktische Beispiele für USDZ"
slug: funf-beispiele-usdz-openusd
status: published
primary_tag: visual-sales
tags: [visual-sales, openusd, usdz]
feature_image: /assets/images/2025/11/usd_trees.jpeg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2022-10-25T06:00:00.000Z"
type: post
template: post
---

*Dieser Beitrag erschien ursprünglich 2022 als Blogbeitrag. Er richtet sich an Leserinnen und Leser, die einen Einstieg in das Thema suchen. Neuere Seiten und Artikel bauen inhaltlich darauf auf und gehen bewusst weiter in die Tiefe.*

&nbsp;

&nbsp;

**Nach meiner Newsletter-Ausgabe **[**USDZ: So wichtig wie MP3 und HTML**](https://visales.de/usdz-so-wichtig-wie-mp3-und-html/)** bekam ich einige Anfragen ala "*****...und was kann man nun mit diesem neuen Format machen?*****" Darum soll es in dieser Ausgabe gehen. Schnappt Euch eine Tasse Tee - oder Kaffee - und wir steigen ein in die kreative, bunte Welt von **[***.usdz & *.reality**](https://www.linkedin.com/pulse/usdz-so-wichtig-wie-mp3-und-html-gerhard-schr%25C3%25B6der/?trackingId=uQIj8VnuS0628Lv%2FLbyEYw%3D%3D)**.**

### ReCap, was steckt in einer USDZ-Datei?

Ich habe dazu meinen Kollegen [Thomas Kumlehn](https://www.linkedin.com/in/thomas-kumlehn/) gebeten einen Überblick zu verfassen. Die Vor- / Entstehungsgeschichte vom Dateiformat USDZ.

*"Seit iOS 12 kann man auf iPhones / iPads und später auch auf Macs ein Dateiformat namens USDZ (*.usdz) öffnen. Solche Dateien sind ZIP-Archive, die sowohl Dateien für 3D-Grafik Daten (*.usdc/*.usda), wie auch die benötigten *[*Texturen (*.jpg, *.png, *.heic)*](https://www.youtube.com/watch?v=bVmH3BxExqc)* und Töne (*.mp4) enthalten. Anfangs konnte nur ein einzelnes 3D-Object (Asset) je USDZ gespeichert / angezeigt werden.*

*Seit iOS 13.1 kann ein USDZ auch mehrere Game-Level, samt ihrer Assets (als *[*Tochter-Archive*](https://www.youtube.com/watch?v=UXBtPXEQ8RQ)*) und deren Game-Logik, Animationen und *[*rudimentärer Physics-Eigenschaften*](https://www.youtube.com/watch?v=ufolpQcS3gw)* enthalten und mit *[*AR Quick Look*](https://www.youtube.com/watch?v=9gVTg-ZizSs)* "gespielt" werden.*

*Seit Kurzem enthalten Assets auch Angaben über ihre Gewichtsverteilung, Bewegung-Freiheitsgrade - kurz, wie sie sich in einer hoch-realistischen Physics-Simulation verhalten. NVIDIA's Marketing nennt das "SimReady".*

*Und erste Anbieter nutzen bereits die mit USD möglichen, neuesten Oberflächen-Beschreibungen NURBS (CAD) und Subdivision Surface, und bald auch Displacement Textures beim Export der Assets.*

*Dabei ist das Dateiformat USD (*.usdc) nur eine von vielen Komponenten. Die Programmier-Bibliotheken (openSubD, openUSD, Pixar hydra) sind in C++ geschrieben und auf sowohl hoch-performante, wie auch -flexible Verwantung von 3D-Daten optimiert.*

*Das *[*Metavese Standards Forum*](https://metaverse-standards.org/)** hat USD dieses Jahr als zentrales Authoring Format für Assets empfohlen."*

***) Disclaimer: Meine Agentur***** *****viSales GmbH ist Teil dieser Organisation. Wir sind auch ständig Teilnehmer der **[**USD-User Group**](https://graphics.pixar.com/usd/release/index.html)**, die diesen USD-Standard weiter entwickelt. 😉**

Klammheimlich hat Apple in diesem Jahr weitere Umbauten/Ergänzungen mit und ohne Dokumentation oder Vortrag vorgenommen, die auf folgende Ergänzungen hindeuten:

- Geräte ab iOS14 können in USDZ kompaktere Textur-Formate verwenden mit den auch kurze Animationen möglich werden. Wir haben da sogar schon einen Weg gefunden GIF-artige Animationen umsetzen. 😎
- (Schnellere) Geräte ab iOS16 können nicht nur die übliche Vorderseite einer Oberfläche, sondern auch deren Rückseite darstellen (doublesided = 1)
- Ab iOS16 darf eine Oberfläche auch mehr als eine UV map speichern (bessere Textur-Nutzungen)
- Geschwungene Oberflächen müssen bald nicht mehr als speicherverschwendend feine Polygon-Netze sondern dürfen auch als NURBS (CAD) oder SubD (Animation) gespeichert werden. Diese werden dann dynamisch je nach Blickwinkel, Nähe des Betrachters in Polygone umgewandelt - eine Revolution und drastische Vereinfachung der Workflows sowie kompaktere Dateien!
- Das kombiniert mit sogenannten Displacement-Texturen (auch in realtime!) erlaubt sowohl total "smoothe" wie auch hoch-detaillierte, filigrane Oberflächen.
- Noch besserer Einbettung in existierende Web-Seiten (&lt;model&gt; - Siehe auch unseren [AR-Player als PlugIn](https://visales.de/ar-player-webbasierte-augmented-reality-jetzt-auch-vom-desktop-aus-moglich/).)

Wir erwarten diese Neuerungen zuerst auf **macOS** (Okt. / Nov. 2022)und später auf **realityOS** (Q1/2 '23) das sowohl auf dem sagenumwobenen, immer wieder verzögerten MixelReality headset (codename N301) wie auch auf iPhones ab dem Modell 11 laufen soll. [Video mit Infos zu dem Headset von Thomas Kumlehn und mir](https://www.youtube.com/watch?v=zp7IaL6BMrQ).

### **Anwendungen mit USDZ: Kleiner, schneller, ohne App.**

Nun kann man ja viel über solche Technologien schreiben, aber was hat ein User von dem neuen Format? Oder was hat ein Unternehmen davon dieses Format einzusetzen?

![Apps, Browser-Apps und Web-Apps](/assets/images/2025/11/AnwendungenUSDZ.png)

Dazu ein kurzer Exkurs in die Welt von Apple (Grafik aus dem Video zu [AR Quick Look](https://www.youtube.com/watch?v=9gVTg-ZizSs)):

- **APP**: Normalerweise installieren wir Apps auf unserem iPhone, sein es Spiele oder eine (AR) -App. Jede Installation belegt mehr Speicher vom Handy, denn jede App besteht aus einer neuen Game-Engine und den weiteren Daten für die App.
- **AR Quick Look**: Apple setzt auf eine Web-Ansatz, der ohne Browser auskommt, da die 3D-Engine schon im Betriebsystem enthalten ist. Mehr dazu in meinem Video [Was ist AR Quick Look von Apple? Augmented Reality via Web, aber ohne Browser!](https://www.youtube.com/watch?v=9gVTg-ZizSs)
- **Browser-basierte Web-Apps**: Viele AR-Lösungen auf Android (seltener auf iOS) setzen auf diesen Ansatz. Leider ist die Verbreitung von Android mit AR-Fähigkeiten sehr selten gegeben. Siehe dazu meine zwei Videos: [iOS vs. Android, der Augmented Reality-Vergleich](https://www.youtube.com/watch?v=v6R9Zwh8YhQ&list=PLIggDLmpuIxr142TNZhEB53TJM-V-kLdy) und [USDZ vs glTF - Unterschiede der Augmented Reality-Dateiformate](https://www.youtube.com/watch?v=cN8boqmD8Tc&list=PLIggDLmpuIxr142TNZhEB53TJM-V-kLdy&index=6). glTF versucht nun mit dem zukünftigem Standard glTF 2.0 mit USDZ gleichzuziehen. Das wird aber leider noch ein paar Jahre dauern.

Für Anwender sind also USDZ-Lösungen schneller gestartet als eine App-Lösung. Und im Online Marketing ist eine App-Installation, wenn man den Anwender zu MEHR als nur der Installation der App bekommen möchte schon ein NOGO.

Für Unternehmen ergeben sich auch Vorteile: Zum Beispiel geringere Entwicklungskosten als bei einer klassichen App-Entwicklung. Und... die Inhalte sind "Metaverse-Ready", denn USDZ ist inzwischen ein breit aufgestellter Standard, der von vielen Softwarelösungen unterstützt wird.

### Metaverse-Ready???

Da das Dateiformat / der USD-Standard Bestandteil des Metaverse Standards Forums ist, sind die USDZ-Dateien in einigen Metaverse-Plattformen nutzbar. Zum Beispiel im [Omniverse](https://www.nvidia.com/de-de/omniverse/) von Nvidia, zu dem ich in Zukunft noch einen Beitrag verfassen werden. Gerade das [Omniverse](https://www.nvidia.com/de-de/omniverse/) im Zusammenspiel mit der obigen Apple-Lösung bietet für den deutschen Mittelstand viele Optionen. Ganz ohne sich auf einen speziellen Anbieter / Agentur festzulegen. Könnte ja ein Thema sein um eine Anbieterabhängigkeit zu vermeiden.

Bei Fragen hierzu mir einfach eine PN senden: Gerhard Schröder.

### Vor den USDZ-Beispielen: Wie interagiert man mit solchen Inhalten?

Gute Frage, ich habe als Antwort hier direkt ein 90-Sekunden-Video produziert.

[Embed: https://www.youtube.com/watch?v=x3EDBidQbjs](https://www.youtube.com/watch?v=x3EDBidQbjs)

### USDZ-Beispiel 1: Verkaufsmitarbeiter entlasten

Unser Kunde Propan Rheingas GmbH & Co. KG hat in der aktuellen Lage viel mehr Anfragen nach Flüssiggas-Tanks als vor einem Jahr. Klar. Natürlich hat man nicht spontan mehr gut ausgebildete Vertriebsmitarbeiter, also kamen wir mit unser Vertriebs- und AR-Erfahrung ins Spiel.

[Embed: https://www.youtube.com/watch?v=1SAL_kzaeTg](https://www.youtube.com/watch?v=1SAL_kzaeTg)

### USDZ-Beispiel 2: Ein Märchenwald voller Möglichkeiten

Für ein Märchenmuseum haben wir eine Version des Froschkönigs umgesetzt. Falls meine geschätzten Leser nun an einem Desktop- oder Laptop-Rechner sitzen, dann nun das iPhone oder iPad gezückt und hier direkt den QR-Code abscannen und direkt ausprobieren.

![Es wurde kein Alt-Text für dieses Bild angegeben.](/assets/images/2025/11/QRcode.jpeg)

![Es wurde kein Alt-Text für dieses Bild angegeben.](/assets/images/2025/11/BrunnenSzene.jpeg)

![Es wurde kein Alt-Text für dieses Bild angegeben.](/assets/images/2025/11/HandyBeispiel.jpeg)

Alternativ kann man sich hier mein Video zum Froschkönig in Augmented Reality anschauen, und / oder die [Outtakes](https://www.youtube.com/shorts/QN3Gig_L8nc) genießen. Viel Spaß!

[Embed: https://www.youtube.com/watch?v=ufolpQcS3gw](https://www.youtube.com/watch?v=ufolpQcS3gw)

### USDZ-Beispiel 3: Podcast in 3D genießen

Vor ein paar Wochen, in Rahmen eines LinkedIn-Lives, sprach ich mit meinem Co-Host Kai Heddergott und unserem Gast alex wunschel 🎙 über Podcasts im 3D-Raum. Aus dem Gespräch erstellten wir dann eine echte 3D-Audio-Datei als 360-Grad-Video. [Zum reinhören und den echten](https://www.youtube.com/watch?v=lZFDBOcMAec) **Spatialaudio**-[genuß bitte Kopfhörer tragen](https://www.youtube.com/watch?v=lZFDBOcMAec).

Aus dem Gespräch nahmen wir auch einen ca. 2-Minuten-Ausschnitt und erstellten eine USDZ-Datei, bei der man als Zuhörer selbst entscheiden kann WO sich die Sprecher (-stimmen) im Raum befinden sollen. [Das Thema Multi-Objekt-AR habe ich in diesem Video schon vorgestellt und wurde von uns so als Ergänzung zur Apple-Standard-Lösung entwickelt.](https://www.youtube.com/watch?v=UXBtPXEQ8RQ)

[Embed: https://www.youtube.com/watch?v=MYaHfwcmcmk](https://www.youtube.com/watch?v=MYaHfwcmcmk)

Ich kann wirklich nur empfehlen für diese Demo Kopfhörer aufzusetzen und es SELBST auszuprobieren. Falls Du am iPhone oder iPad sitzt, [dies ist der direkte Link zur Datei](https://www.kreativekk.de/wp-content/uploads/ar/Podcast_AR.usdz). Viel Spaß beim Ausprobieren. Das ist m.W. ein **World-First** für ein Multi-Objekt-Spatial-Audio mit USDZ. Spatial Audio hatten wir ja früher schon mit dem Froschkönig umgesetzt.

### USDZ-Beispiel 4: Remote-Vertrieb

[Embed: https://www.youtube.com/watch?v=pUGc_V2mstQ](https://www.youtube.com/watch?v=pUGc_V2mstQ)

Wie man via Website, Newsletter und Social Media eine USDZ-Datei für den Verkauf einsetzt zeigt unser DigitalSales-[Beispiel für die Firma PlugVan GmbH.](https://www.linkedin.com/search/results/all/?keywords=%23digitalsales&origin=HASH_TAG_FROM_FEED)

### USDZ-Beispiel 5: Bürostuhl-Konfiguration in AR

[Embed: https://www.youtube.com/watch?v=5nTA1IrkAas](https://www.youtube.com/watch?v=5nTA1IrkAas)

Dies ist ein Alleinstellungsmerkmal unser AR-Fähigkeiten: Produktionfiguration komplett in AR auf einem Smartphone via USDZ. Das User-Interface war hier noch eine Design-Studie, aber das Potential der von uns entwickelten Lösung ist von Apple-Entwicklern öffentlich mit einem "**Wow!**" ausgezeichnet worden. Wer die Demo ausprobieren möchte, hier ein Link zu einem Blog-Beitrag bei der K3: [Verkaufen mit dem Augmented Reality-Stuhl-Konfigurator: AR mit *.usdz & *.reality](https://visales.de/verkaufen-mit-dem-augmented-reality-stuhl-konfigurator-ar-mit-usdz-reality/). Oder einfach das Video anschauen!

Wir lesen uns in zwei Wochen wieder. Passt auf Euch auf und bleibt GESUND!

Viele Grüße aus Velbert

Gerhard Schröder

&nbsp;

&nbsp;

&nbsp;

&nbsp;

### **Einstieg in AR & USDZ — mit Unterstützung.**

Wir begleiten Unternehmen vom ersten USDZ-Modell bis zum eingebetteten AR-Erlebnis im Vertrieb. Das erste Gespräch dauert 30 Minuten. Ohne Pitch, ohne Vorbereitungspflicht. **Rheingas, Somfy und Carl Hamm haben mit einem Produkt begonnen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

&nbsp;

→ Praxiseinsatz von AR: [AR im B2B-Vertrieb – der große Überblick](https://visales.de/augmented-reality/)

→ OpenUSD im Einsatz: [USDZ & OpenUSD für den Vertrieb](https://visales.de/openusd-dienstleister/)
