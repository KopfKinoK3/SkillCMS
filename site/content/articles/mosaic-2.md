---
title: "Mosaic 2: Spatial Web Browser für visionOS 26. Alpha auf GitHub"
slug: mosaic-2
status: published
primary_tag: apple
tags: [apple, aus-der-agentur, ki, openusd, spatial-computing]
meta_description: "Mosaic 2 ist ein Open-Source visionOS-Browser, der spatial-backdrop-Tags automatisch erkennt und USDZ-Environments ohne App-Download lädt. Alpha auf GitHub."
feature_image: /assets/images/2026/03/Cafe-am-Ende-des-Metaverse.jpg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-03-21T02:48:32.000Z"
type: post
template: post
faq_heading: "Häufige Fragen"
faq:
  - q: "Was ist spatial-backdrop genau?"
    a: "Ein HTML-Link-Tag der in visionOS 26 eingeführt wurde: &lt;link rel=\"spatial-backdrop\" href=\"environment.usdz\"&gt;. Er weist kompatible Browser an, die verlinkte USDZ-Datei als immersive Hintergrundumgebung zu laden."
  - q: "Welche visionOS-Version wird benötigt?"
    a: "Mosaic 2 baut auf visionOS 26 (Developer Preview). Der spatial-backdrop-Standard ist Teil dieser Preview. Für ältere visionOS-Versionen gibt es keinen nativen Support."
  - q: "Kann ich eigene spatial-backdrop-Seiten testen?"
    a: "Ja. Den spatial-backdrop-Tag in den HTML-Head deiner Seite einfügen, USDZ-Datei auf einem HTTPS-Server hosten – und Mosaic 2 erkennt sie automatisch."
  - q: "Ist das relevant für B2B-Produktpräsentationen?"
    a: "Sehr: Stell dir eine Produktseite vor, deren 3D-Modell sich direkt auf dem Vision Pro als räumliche Umgebung öffnet – kein App Store, kein QR-Code, kein Setup. Das ist die Richtung, in die wir arbeiten."
---

- **spatial-backdrop (=Website-Environments) ist ein neuer HTML-Standard in visionOS 26: Websites liefern damit eine USDZ-Datei mit, die als immersive Umgebung direkt im Browser erscheint, ohne App-Download, ohne App Store. **
- **Mosaic 2 erkennt spatial-backdrop-Tags automatisch, lädt die USDZ-Datei im Hintergrund und rendert sie als RealityKit ImmersiveSpace: Drei Statuskreise zeigen den Fortschritt in Echtzeit.**
- **Das Projekt ist Alpha: funktionsfähig, experimentell, Open Source – Pull Requests, Issues und Demo-Seiten auf GitHub sind ausdrücklich willkommen. **

&nbsp;

&nbsp;

<details>
<summary><strong>Welches "Problem" löst Mosaic 2?</strong></summary>

Die aktuelle Beta von visionOS 26 erlaubt es Spatial Backdrops im Safari zu starten. Wechselt man jedoch die URL / Website, so wird man aus der VR-Web-Landschaft (Spatial Backdrop) herausgeworfen und ist im AR-Modus.

Erneut muss der Nutzer manuell für die neue Website das Environment / Backdrop aktivieren durchs Drehen der Krone. Ein eher uneleganter Vorgang, der die **Immersion des Surfens durch den VR-Space** unterbricht.

Mosaic 2 lässt den Surfer die ganze Zeit im VR-Space weiterreisen so lange er auf Backdrop-Websites reist. Ruft er jedoch eine URL "ohne Backdrop" auf, so wird der AR-Modus automatisch aktiviert.

</details>

<details>
<summary><strong>Warum ich mit Mosaic 2 angefangen habe: Schlechter Kaffee...</strong></summary>

Am 18. März, im Rahmen des [XR Symposiums in Heidelberg](https://xrsymposium.vrlogic.de) stand ich kurz vor meinem Vortrag zu [OpenUSD für Entscheider](https://visales.de/openusd/) mit [Thomas Riedel](https://www.droid-boy.de) zusammen. Er hatte vor zwei oder drei Jahren mal gesagt er wünsche sich ein "Metaverse wie ein Wordpress-System".

Daran dachte ich auf der langen Rückfahrt als ich Müde wurde und an einer Raststätte einen schlecht schmeckenden Kaffee kaufte. (Tee war aus...) Dazu kam dann die Gedanken an meine Beiträge [Warum Apple dem Metaverse näher ist als Meta](https://visales.de/apple-metaverse-openusd/) und zur [Website der Zukunft](https://visales.de/website-zukunft-ki-agent-2d-openusd/).

Ich verzog beim bitteren Automatenkaffee die Stirn...

Warum sollte ich nun auf Apple WARTEN? Wenigstens eine Vibecode-Demo via Xcode, Claude Code und einfach das Thema ins Gespräch bringen... so mein Ziel...

</details>

Als Apple auf der WWDC visionOS 26 vorstellte, war da ein kleiner HTML-Tag, der mich sofort elektrisiert hat – der [*spatial-backdrop*-Tag](https://visales.de/spatial-website/). Die Idee dahinter ist so einfach wie radikal: Eine Website kann eine räumliche USDZ-Datei mitliefern. Der Browser rendert sie als Hintergrundumgebung – vollständig immersiv, direkt aus dem HTML, ohne App, ohne Setup.

> **Mehr zu den Spatial Backdrops von Apple** im WebKit Blog – der offizielle Entwickler-Blog von Apple: [Try out your website in the spatial web](https://webkit.org/blog/15421/try-out-your-website-in-the-spatial-web/). Hier wird Web Backdrop / `spatial-backdrop` erstmals öffentlich beschrieben, mit dem genauen HTML-Markup. Dazu schaut gern auch die WWDC25 Session [What's new for the spatial web.](https://www.youtube.com/watch?v=KhmQDkefpVM)

[Embed: https://www.youtube.com/watch?v=0R67WhTgq-A&feature=youtu.be](https://www.youtube.com/watch?v=0R67WhTgq-A&feature=youtu.be)

Das ist der Moment, [auf den wir bei viSales seit Jahren hinarbeiten](https://youtu.be/6eHVZESUXsQ). 3D-Content, der im offenen Web funktioniert, ohne Installationshürde, ohne proprietäre Plattform.

Also hab ich gebaut. 

<details>
<summary><strong>Ehrlicherweise: Claude Code</strong></summary>

Meine letzte "echte" Programmierung ist in meinen Augen über 40 Jahre her. Damals, mit Turbo Pascal 3.0 und Borland Datenbank-Erweiterung. Alles in HTML viel Jahre später zählt für mich nicht in den echten Programmierbereich.

Ich habe also letzte Nacht mein Claude Code mit Xcode und Github verknüpft, ein Briefing verfasst und dann als Human-in-the-loop Token im Wert von 4 Euro verbraucht für die Demo-App.

Da ich hier am Wochenende nur einen MacMini (M1) und ein MacBook Air (M1) zur Hand hatte... dauerten die Schritte zwar jeweils ein paar Minuten, aber das war mir nun EGAL.

Ich wollte "den Beweis" wie die **Experience** sein würde wenn man durch ein "Web-Metaverse" surfen könnte.

</details>

<details>
<summary><strong>Warum Mosaic 2 als Name?</strong></summary>

Logisch, in Anlehnung an meinen ersten Browser, den [NCSA Mosaic](https://de.wikipedia.org/wiki/NCSA_Mosaic). Meine Gedanken beim verfassen des Apple-Metaverse-Beitrags war... Wenn die Backdrops Nahtlos "Bereist" werden könnten, ohne normale Websites dazwischen, dann wäre das für mich ein neuer Mosaic-Moment.

Ist sicher TOTAL übertrieben, aber mir machte die Idee eine kleine Freude.  
  
**(Ja, es gab auch einen damaligen Mosaic 2.0 der Tabellen konnte...)**

</details>

## Was Mosaic 2 macht

Mosaic 2 ist ein visionOS-Browser auf Basis von WKWebView, der beim Laden einer Seite den HTML-Head auf spatial-backdrop-Tags prüft. Findet er eine USDZ-URL, startet er sofort den Download im Hintergrund – **während du noch auf der Seite surfst**.

Drei kleine Statuskreise in der Adressleiste zeigen den Fortschritt:

- **Kreis 1 (weiß):** Seite geladen
- **Kreis 2 (orange → weiß):** USDZ wird heruntergeladen / fertig
- **Kreis 3 (cyan):** Backdrop bereit – Tippen öffnet den ImmersiveSpace

<details>
<summary><strong>Die drei Kreise</strong></summary>

Da ich feststellte das die Backdrops teilweise echt eine längere Ladezeit haben... was gerade in den ersten App-Versionen im VisionOS-Simulator auf dem M1... dauerte... wollte ich irgendwann wissen...

Lädt der Browser, ist ein Crash eingetreten oder bin ich zu **Ungeduldig**?

Die drei Farben haben folgenden Ursprung: Weiß ist die Hintrgrundfarbe unser Website. Orange die Agentur-Signalfarbe und Türkis / Cyan ist in meinen Grafiken für Farbe für "Spatial" = Augmented Reality & Co.

</details>

Ist die Datei gecacht, öffnet sich der RealityKit ImmersiveSpace mit einem Tipp auf den dritten Kreis. Das Environment wird als AnchorEntity am Kopf befestigt – du stehst buchstäblich darin.

<details>
<summary><strong>Demo-Websites zum Ausprobieren</strong></summary>

Fünf Demo-Seiten sind bereits direkt in der App als Quick-Nav-Buttons eingebaut: Zgoll, Campfire, Tron, Cyberpunk und Porta Nubi. Alle fünf haben spatial-backdrop-Tags und funktionieren out of the box.

* [Tron Immersive](https://www.sketchbot.tv/tron) by [Steve Talkowski](https://www.linkedin.com/in/stevetalkowski/overlay/about-this-profile/) (Sehr tolle Demo: Aus dem Film TRON ist ein Kampfpanzer animiert und mit Spatial Audio erlebbar)
* [Zgoll-Room](https://visales.de/zgoll/) by viSales (Statt des ganzen Produktkonfigurators mit lauter Einzelnräumen ist auf dieser Projektreferenzseite eine umfangreiche Backdrop-Animation)
* [Campfire Space](https://campfirespace.com/) by [Mathew Spendlove](https://www.linkedin.com/in/mathew-spendlove/overlay/about-this-profile/)
* [Cyberpunk Lair](https://www.toddheberlein.com/blog/2025/8/10/immersive-web-pages) by [Todd Heberlein](https://www.linkedin.com/in/todd-heberlein-18bb2842/overlay/about-this-profile/) (Bin nicht sicher ob es an mir liegt das die Website nicht läuft)
* [Porta Nubi](https://www.tempuno.com/work/porta-nubi/) by [Michael Temper](https://www.linkedin.com/in/michael-temper/overlay/about-this-profile/) (Bin nicht sicher ob es an mir liegt das die Website nicht läuft)

Bis auf unsere Demo sind die Links von [Joseph Simpson](https://www.linkedin.com/in/vrhermit/) - Danke!

</details>

<details>
<summary><strong>Warum sind in Mosaic 2 oben die Buttons zu den Websites?</strong></summary>

Ich kenne leider in diesem frühen Beta-Stadium von Spatial Backdrops noch kein weiteres Webverzeichnis ala [Yahoo 1994](https://de.wikipedia.org/wiki/Yahoo_(Webportal)). Also habe ich die paar Demos die ich zusammenbringen wollte dort in den Header der App gepackt damit man in dem Mini-Kosmos der Backdrops reisen kann.

Bis zum echten Matrix-Feeling ist es noch eine Weile hin...

</details>

## Die technischen Entscheidungen dahinter

Zwei Dinge haben beim Entwickeln mehr Zeit gekostet als erwartet – und beide sind es wert, sie zu dokumentieren.

**Pre-Download statt Lazy-Load:** Der USDZ-Download startet sofort wenn der spatial-backdrop-Tag gefunden wird – nicht erst wenn der User den ImmersiveSpace öffnet. Das sorgt dafür, dass Kreis 3 bereits cyan leuchtet wenn du auf den Button tippst. Kein Warten, kein Rätselraten.

**Navigation ohne Loop:** WKWebView und SwiftUI kämpfen gerne darum wer die aktuelle URL bestimmt. Die Lösung war ein isLoading-Flag im Coordinator, das Reload-Zyklen beim Linkklick verhindert, und ein onURLChanged-Callback der beide State-Variablen synchron hält.

Das Projekt ist bewusst minimal gehalten. Keine überkomplexe Architektur. Wenige Dateien, klare Verantwortlichkeiten. Der Code soll lesbar sein für alle, die mit visionOS und RealityKit einsteigen wollen.

## Wo das hinführt

spatial-backdrop ist heute noch Developer Preview, aber die Richtung ist klar: Das offene Web wird räumlich. OpenUSD ist das Format der Wahl – nicht zufällig ist mein Unternehmen viSales Mitglied der [Alliance for OpenUSD](https://aousd.org).

Was das für B2B-Vertrieb bedeutet: Produktseiten, Konfiguratoren, technische Dokumentation – alles könnte eine räumliche Ebene bekommen, die auf Apple Vision Pro ohne App-Download abrufbar ist. Keine Installationsbarriere für den Kunden, kein App-Review-Prozess für den Hersteller.

Das ist keine ferne Zukunft. Mosaic 2 läuft heute im Simulator. Die Demo-Seiten funktionieren. Der Stack ist etabliert.

## Alpha auf GitHub

Den Code gibt es auf GitHub unter [https://github.com/visales/mosaic-2](https://github.com/KopfKinoK3/mosaic-2). Xcode 26 beta und visionOS 26 Simulator vorausgesetzt – dann läuft es sofort.

> **Disclaimer:** Ich habe die App nur via Vibecoding erstellt. Für mehr als eine Personal-Demo taugt die App sicher nicht. Nutzung daher ECHT auf eigene Gefahr. Lief bei mir nur im visionOS-Simulator!

Was ich mir wünsche: 

- Wer spatial-backdrop-Seiten betreibt oder kennt: Issues auf GitHub oder eine Email an [sales@visales.de](mailto:sales@visales.de)
- Wer an visionOS entwickelt: Pull Requests.
- Wer Feedback zum UX-Konzept hat: hier in den Kommentaren, via [LinkedIn-Direktnachricht](https://www.linkedin.com/in/gerhardschroeder/) oder direkt per Mail: [sales@visales.de](mailto:sales@visales.de)

Viele Grüße aus Bochum,

Gerhard Schröder

PS: Video: [Spatial Backdrop & Environments meiner Agentur](https://www.youtube.com/watch?v=6eHVZESUXsQ) (ca. 2 Min.) Wenn es zu dem Thema Gesprächsbedarf bei einer Tasse Remote-Tee oder -Kaffee gibt, [einfach melden](https://visales.de/kontakt).

[Embed: https://www.youtube.com/watch?v=6eHVZESUXsQ](https://www.youtube.com/watch?v=6eHVZESUXsQ)

PSS: Vielleicht lässt sich die Kernfunktion ja in ein Browser-PlugIn integrieren oder... Apple baut so in der Art den Safari-Browser aus und AndroidXR zieht mit??? 

&nbsp;

&nbsp;

→ Praxiseinsatz AR im Vertrieb: [AR im B2B-Vertrieb bei viSales](https://visales.de/augmented-reality/)  
→ Alle OpenUSD-Lösungen: [OpenUSD-Tools & Dienste von viSales](https://visales.de/openusd-dienstleister/)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

### **Du willst wissen ob Spatial Web für dein Produkt passt?**

In 30 Minuten sortieren wir gemeinsam, ob und wo räumliche Präsentationen in eurem Vertrieb konkret etwas bringen — ohne Pitch, ohne Angebot. Kein Verkaufsdruck, eine ehrliche Einordnung. **Rheingas und Somfy haben so angefangen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;
