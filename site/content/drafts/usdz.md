---
title: "USDZ im Einsatz: Wie das Format im Arbeitsalltag wirklich funktioniert"
slug: usdz
status: draft
primary_tag: aus-der-agentur
tags: [aus-der-agentur, openusd, usdz]
meta_title: "USDZ im Einsatz: Wie das AR-Format im Alltag funktioniert | viSales"
meta_description: "USDZ im Arbeitsalltag: QR-Code, Keynote, FaceTime, AR Quick Look – wie das Format in der Praxis eingesetzt wird und was du brauche, um loszulegen."
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
type: post
template: post
faq_heading: "Häufige Fragen zu USDZ"
faq:
  - q: "Was ist USDZ und wofür wird es verwendet?"
    a: "USDZ ist ein 3D-Containerformat von Apple, basierend auf dem offenen OpenUSD-Standard. Es bündelt 3D-Geometrie, Materialien und Texturen in einer einzigen Datei. Hauptanwendung: Augmented Reality auf iPhone und iPad per AR Quick Look – direkt im Browser, ohne App-Download. Auch für Keynote-Präsentationen, FaceTime-Demos und Web-Konfiguratoren im Einsatz."
  - q: "Auf welchen Geräten funktioniert USDZ?"
    a: "USDZ läuft nativ auf allen Apple-Geräten ab iOS 12 und macOS Mojave: iPhone, iPad, Mac. Safari öffnet USDZ-Dateien automatisch in AR Quick Look. Android unterstützt USDZ nicht nativ – dort wird in der Regel GLB (glTF) verwendet."
  - q: "Wie unterscheidet sich USDZ von klassischen 3D-Formaten wie OBJ oder FBX?"
    a: "OBJ und FBX sind Austauschformate für 3D-Software – sie benötigen zusätzliche Textur-Dateien und eine Rendering-Engine. USDZ ist ein Self-contained-Format: Alles steckt in einer Datei. Kein entpacken, kein installieren – ein Klick oder QR-Code genügt. Zudem basiert USDZ auf OpenUSD, was Variant Sets und Echtzeit-Komposition ermöglicht."
  - q: "Wie öffne ich eine USDZ-Datei auf dem iPhone?"
    a: "Einfach den Link antippen oder den QR-Code scannen. Safari öffnet USDZ automatisch in AR Quick Look – das 3D-Modell erscheint direkt in der realen Umgebung. Kein App-Download, kein Account nötig. Funktioniert ab iPhone 6S mit iOS 12."
  - q: "Kann ich USDZ in Präsentationen und Videocalls nutzen?"
    a: "Ja. In Apple Keynote lassen sich USDZ-Modelle direkt einbetten und auf Folien drehen. In FaceTime und SharePlay können 3D-Objekte gemeinsam im Raum betrachtet werden. Im Vertrieb bedeutet das: 3D-Demo ohne Reise, direkt im Kundengespräch über den Bildschirm."
---

## Auf einen Blick

> USDZ begegnet den meisten Menschen als QR-Code auf einem Messestand oder als Link auf einer Website, der direkt ein 3D-Objekt öffnet — **ohne App, ohne Installation**. Diese Seite zeigt, wie das Dateiformat im Arbeitsalltag eingesetzt wird: in Keynote, FaceTime und Vertriebsgesprächen. Und warum Apple und NVIDIA dasselbe Format für grundlegend unterschiedliche Zwecke nutzen.

&nbsp;

&nbsp;

## Was ist USDZ – einfach erklärt

USDZ taucht oft unerwartet auf: Ein QR-Code auf einem Messestand, ein Link in einer E-Mail oder ein Beispiel auf einer Website. **Statt einer App öffnet sich direkt ein 3D-Inhalt, den man drehen, heranzoomen oder im Raum betrachten kann.** USDZ ist genau für solche Momente gedacht – wenn 3D-Inhalte schnell verständlich sein sollen, ohne technische Hürden.

> Am einfachsten versteht man USDZ,   
> wenn man es kurz selbst ausprobiert.

![](/assets/images/2026/01/igus-ar-demo-1.jpeg)

**Probier es selbst aus**: Scanne den QR-Code mit deinem Smartphone. Der 3D-Inhalt öffnet sich direkt im Browser – ohne App, ohne Installation. (*Falls nichts passiert, liegt das meist am Gerät oder Browser. In der *Box* "Was passiert beim Öffnen..." erklären wir, woran das liegen kann.)*

<details>
<summary><strong>Was passiert beim Öffnen – und warum sieht das je nach Gerät unterschiedlich aus? (Trouble-Shooting)</strong></summary>

Nach dem Scannen des QR-Codes unterscheidet sich der Ablauf je nach Gerät leicht. Das ist normal und kein Fehler.

**Auf dem iPhone (USDZ):**  
Zunächst erscheint **(1)** eine Abfrage, ob die 3D-Datei geladen werden soll. Nach dem Download öffnet sich eine Vorschau im Browser. Erst durch einen weiteren **(2)** Tipp auf das Vorschaubild startet die AR-Ansicht. **Dieser zusätzliche Schritt ist Teil des Sicherheits- und Download-Konzepts von Apple.**  
  
**Wichtig:** Auf dem iPhone funktioniert die AR-Ansicht aktuell nur über Safari. Ist Chrome oder ein anderer Browser als Standard eingestellt, kann es passieren, dass sich beim Scannen des QR-Codes nichts sichtbar öffnet. In diesem Fall hilft es, den Link direkt in Safari zu öffnen.

****Auf Android-Geräten (\*.glb):**  
Hier öffnet sich die AR-Ansicht in der Regel direkt, ohne eine vorgelagerte Download-Abfrage. Der technische Ablauf ist ein anderer, das Nutzungserlebnis für Anwender jedoch vergleichbar.

Wenn sich der Ablauf auf deinem Gerät unterscheidet, liegt das meist am Browser oder an den Geräteeinstellungen – nicht am Inhalt selbst.

**Wir erklären diese Unterschiede bewusst offen, weil sie im Alltag immer wieder für Verwirrung sorgen:**** USDZ funktioniert nativ auf iPhone, iPad, Mac und Apple Vision Pro. Auf Android wird bei unseren Projekten in der Regel eine GLB-Alternative ausgeliefert.

→ Ausführlicher Vergleich: [Apple vs. Android Augmented Reality](https://visales.de/apple-vs-android-augmented-reality-unterschiede-erklart)

</details>

<details>
<summary><strong>Wie steuere ich eine USDZ-Datei?</strong></summary>


</details>

### USDZ ist ein Dateiformat, wie PPT oder MP3, basierend auf OpenUSD

USDZ ist kein klassisches 3D-Format, sondern ein Container,  vergleichbar mit einer beliebigen ZIP-Datei: Das Kürzel steht für **USD** (Universal Scene Description, entwickelt von [Pixar](https://www.pixar.com)) + **Z** (Zip). Eine USDZ-Datei verpackt Geometrie, Materialien, Animationen und "Programmierung"  in eine einzige Datei, die direkt auf Endgeräten abgespielt werden kann.

Der entscheidende Unterschied zu klassischen 3D-Dateien wie OBJ oder FBX: USDZ braucht oft keine zusätzliche Software zum Öffnen. Auf iPhone, iPad, Mac und Apple Vision Pro ist der Player bereits im Betriebssystem integriert.

> **USDZ in einem Satz:** Eine in sich geschlossene 3D-Datei, die auf Apple-Geräten **ohne App** direkt angezeigt werden kann.

→ [Herkunft und Geschichte von OpenUSD & USDZ ausführlich erklärt](https://visales.de/openusd-geschichte-strategie/)

&nbsp;

&nbsp;

## Wo begegnet dir USDZ heute?

USDZ taucht meist beiläufig auf: als Link auf einer Website, als QR-Code auf einer Messe oder als Vorschau in einer Präsentation. Statt eines Bildes oder Videos öffnet sich ein 3D-Inhalt, den man drehen, heranzoomen oder im Raum betrachten kann.

<details>
<summary><strong>Typische Situationen, in denen USDZ eingesetzt wird</strong></summary>

USDZ wird meist nicht als neue Technologie wahrgenommen, sondern taucht in ganz normalen Situationen auf.

**Auf Websites:** Produkte oder Objekte lassen sich direkt im Browser räumlich ansehen.

**In Präsentationen und Meetings**: 3D-Inhalte können gezeigt werden, ohne Apps oder spezielle Software.

**Auf Messen und Events**: Ein QR-Code reicht, um einen AR-Inhalt direkt auf dem Smartphone zu öffnen.

**In E-Mails oder internen Abstimmungen**: Ein Link ersetzt mehrere Bilder oder lange Erklärungen.

In all diesen Situationen geht es nicht um Technik, sondern darum, Inhalte schneller verständlich zu machen.

**Special: Gemeinsames Betrachten per FaceTime**: In [Apple FaceTime](https://support.apple.com/de-de/105088)-Calls lassen sich USDZ-Inhalte gemeinsam ansehen und im Raum platzieren. Gesprächspartner sehen dabei denselben AR-Inhalt und können ihn parallel besprechen – ohne zusätzliche Tools.

</details>

&nbsp;

&nbsp;

## Wie wird USDZ im Büroalltag genutzt?

USDZ wird nicht nur gezeigt, sondern im Alltag weiterverarbeitet: in Präsentationen, Abstimmungen oder zur internen Weitergabe. Gerade im Büro entstehen daraus Screenshots, kurze Videos oder direkte Einbindungen in bestehende Tools.

<details>
<summary><strong>USDZ für Vertriebs- & Marketing-Grafiken</strong></summary>


</details>

<details>
<summary><strong>USDZ in Videocalls (Facetime) nutzen inkl. Bildschrimfreigabe</strong></summary>


</details>

<details>
<summary><strong>USDZ in Präsentationen nutzen (z. B. mit Keynote)</strong></summary>

Eine USDZ-Datei lässt sich in Präsentationen nicht nur einmal zeigen, sondern über mehrere Folien hinweg einsetzen. Dabei kann dasselbe 3D-Objekt auf jeder Folie in einer neuen Position, Perspektive oder Skalierung platziert werden.

Lässt man die Präsentation anschließend ablaufen, entsteht der Eindruck einer durchgehenden Animation – ähnlich wie bei einem klassischen Animationsvideo, nur ohne vorherige Renderarbeit. Änderungen am Objekt oder an der Abfolge lassen sich dabei jederzeit direkt in der Präsentation vornehmen.

**Bonus-Tipp:** Die Präsentation kann anschließend als Video exportiert werden. So entsteht aus wenigen Folien schnell ein kundenindividuelles Animationsvideo, das sich zum Beispiel für Angebote oder zur Weitergabe per E-Mail, YouTube oder LinkedIn eignet.

→ [Videobeispiel einer Keynote-Animation mit einer USDZ-Datei](https://www.youtube.com/watch?v=gF0UVu3Bau8) (46 Sek.)  
  
**Hinweis zu PowerPoint:** PowerPoint unterstützt bisher keine USDZ-Dateien direkt. 3D-Inhalte lassen sich dort jedoch über Formate wie GLB einbinden. Der Funktionsumfang unterscheidet sich von Keynote, ermöglicht aber ebenfalls räumliche Darstellungen innerhalb von Präsentationen.

</details>

<details>
<summary><strong>USDZ in Apple Freeform nutzen</strong></summary>


</details>

<details>
<summary><strong>USDZ auf der Website und im Newsletter einbinden</strong></summary>


</details>

USDZ-Dateien entstehen aus CAD-Daten oder 3D-Software,  das übernimmt in der Regel ein Dienstleister, die Konstruktions- oder Marketingabteilung. 

→ [OpenUSD Dienstleister viSales](https://visales.de/openusd-dienstleister-in-deutschland-visales-aus-bochum/)

## 

## 

&nbsp;

&nbsp;

--

&nbsp;

## 

&nbsp;

&nbsp;

- 

&nbsp;

&nbsp;

<details>
<summary><strong>Apple & Omniverse: USDZ-Ansätze & Arbeitsbegriffe zur Einordnung</strong></summary>

**USDZ wird im Web oft nur als Apple-AR-Format beschrieben.**  
In der Praxis existieren jedoch mehrere sehr unterschiedliche Nutzungsansätze, die dort meist vermischt werden.

Da es hierfür bislang **keine allgemein etablierte Terminologie** gibt, verwenden wir bei viSales zwei **Arbeitsbegriffe**, um diese Unterschiede klar und nachvollziehbar zu machen. Es handelt sich dabei **nicht um offizielle Standardbegriffe**, sondern um bewusst gewählte Bezeichnungen für unterschiedliche technische und organisatorische Wege der Nutzung.

**Natives USDZ (viSales-Arbeitsbegriff – Apple-zentrierter Ansatz)**

Mit **„nativem USDZ“** bezeichnen wir bei viSales einen Ansatz, bei dem:

* USDZ als **in sich geschlossener Container** genutzt wird
* Geometrie, Materialien, Animationen **und Interaktionsinformationen**  
  direkt im USDZ-Archiv enthalten sind
* keine externen Skripte oder zusätzlichen Laufzeitdateien erforderlich sind
* die Datei **unmittelbar auf Endgeräten** lauffähig ist  
  (z. B. iPhone, iPad oder Apple Vision Pro über [AR Quick Look](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/))
* der Fokus auf **Distribution, Präsentation und Endnutzer-Interaktion** liegt

Dieser Ansatz ist insbesondere im Apple-Ökosystem verbreitet. Er ermöglicht interaktive [AR-Inhalte ohne App-Entwicklung](https://visales.de/augmented-reality/), etwa für [Messe-iPads](https://visales.de/messen/), Produktpräsentationen oder webbasierte Vorschauen.

**Python-USDZ (viSales-Arbeitsbegriff – NIVIDIA Omniverse, Pipeline- und Skript-orientierter Ansatz)**

Mit **„Python-USDZ“** bezeichnen wir bei viSales einen Ansatz, bei dem:

* USD / USDZ als Bestandteil einer **modularen OpenUSD-Pipeline** verwendet wird
* Logik, Verhalten und Interaktion **außerhalb der Datei** definiert sind
* Python-Skripte zur Steuerung, Simulation und Automatisierung eingesetzt werden
* Szenen aus mehreren Dateien, Referenzen und Layern bestehen
* der Fokus auf **Simulation, Kollaboration, Digital-Twin-Szenarien und Systemintegration** liegt

Dieser Ansatz ist typisch für Umgebungen wie **NVIDIA Omniverse**, in denen USDZ nicht primär als Distributionsformat, sondern als **flexibler Baustein innerhalb komplexer Workflows** dient.

**Zwei gleichwertige Wege – unterschiedliche Ziele**

Beide Ansätze:

* basieren auf dem [OpenSource-3D-Standard OpenUSD](https://visales.de/openusd/)
* sind technisch valide und gleichwertig
* verfolgen jedoch unterschiedliche Optimierungsziele

Der eine Ansatz ist näher am **Endgerät und an der direkten Nutzererfahrung**, der andere näher an **Systemen, Simulation und Automatisierung**.

viSales nutzt bewusst den Weg des **nativen USDZ** für die Vertriebs- und Produktkommunikation – etwa für [AR-Erlebnisse auf iPads](https://visales.de/augmented-reality/), iPhone oder der Apple Vision Pro, bei denen Inhalte schnell, stabil und ohne App-Entwicklung einsetzbar sein müssen.

</details>

### Warum dieser Ansatz für Endnutzer sichtbar ist

Weil alle Informationen im Container stecken, braucht der Empfänger keine App zu installieren — AR Quick Look ist auf iPhone, iPad, Mac und Apple Vision Pro bereits Teil des Betriebssystems. Ein Link oder QR-Code reicht, den Rest übernimmt das Gerät.

Genau deshalb ist der native USDZ-Ansatz im Vertrieb so verbreitet: nicht weil er technisch überlegener ist, sondern weil er keine Einstiegshürden hat.

### Warum dieser Ansatz für Simulation und Digital Twins sinnvoll ist

Weil Logik und Verhalten außerhalb der Datei definiert sind, lassen sich Szenen modular aufbauen und automatisiert steuern. Mehrere Teams können gleichzeitig an denselben Daten arbeiten — ohne sich gegenseitig zu blockieren. Produktvarianten, Simulationszustände oder Echtzeit-Daten werden nicht in die Datei gebrannt, sondern zur Laufzeit eingespeist.

Das macht diesen Ansatz skalierbar: für große Portfolios, komplexe Anlagen und Szenarien, die sich ständig verändern.

→ Technische Dokumentation zum USD-Workflow: [OpenUSD.org](https://openusd.org/release/index.html)

## Was USDZ bewusst nicht ist

**USDZ -via **[**AR Quick Look**](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/)**- ist kein Allheilmittel** und kein Ersatz für Game Engines, komplexe Echtzeit-Applikationen wie [NVIDIA Omniverse](https://visales.de/nvidia-omniverse-mittelstand/) oder sonstige Workflows, die während der Laufzeit externe Daten einbinden müssen. Wer eine laufende Simulation braucht, deren Ergebnisse live ins 3D-Modell zurückgeschrieben werden, kommt mit Non-App-USDZ nicht weit. Dafür gibt es andere Werkzeuge: *Apps mit USDZ-Inhalten*!

**USDZ ist auch kein Effekt**. QR-Code, AR-Ansicht, Staunen — das ist der erste Moment. Der eigentliche Wert entsteht, wenn dieselbe Datei ein halbes Jahr später noch in der Präsentation, auf der Messe und im Angebot funktioniert — ohne Neuproduktion.

**Wann (Non-App-)USDZ eher nicht passt:** wenn Inhalte in Echtzeit mit externen Systemen kommunizieren müssen, wenn komplexe Nutzerlogik oder Programmierung gefragt ist, oder wenn der Empfänger ausschließlich Android nutzt und kein GLB-Fallback vorgesehen ist.

### 

&nbsp;

**USDZ ist kein Dogma**. Es ist ein Werkzeug — mit klaren Stärken, klaren Grenzen und unterschiedlichen Ausprägungen je nach Ziel. Wer es als Allheilmittel verkauft, hat es nicht verstanden. Wer es kennt, setzt es dort ein wo es wirkt. Wer USDZ im Vertriebsalltag richtig einordnen will, kommt an OpenUSD nicht vorbei: 

→  [OpenUSD für Entscheider](https://visales.de/openusd-fuer-entscheider/)
