---
title: "Der Weg zur 3D-Datei für alle Zwecke: OpenUSD & .usdz"
slug: der-weg-zur-3d-datei-fur-alle-zwecke-openusd-usdz
status: published
primary_tag: impuls
tags: [impuls, openusd, usdz, 3d-visualisierung]
meta_title: "Von CAD zu USDZ: Der Weg zur 3D-Datei für alle Zwecke | viSales"
meta_description: "Du willst deine Produkte in 3D erlebbar machen? Vielleicht sogar direkt in Augmented Reality zeigen, ohne App-Installation, direkt per QR-Code?"
feature_image: /assets/images/2025/10/CAD_usdz_industrial_metaverse_openUSD.png
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2025-06-15T06:00:00.000Z"
type: post
template: post
faq:
  - q: "Wie konvertiert man CAD-Daten in USDZ?"
    a: "CAD-Daten lassen sich auf mehreren Wegen in USDZ konvertieren: direkt aus Programmen wie CATIA oder SolidWorks über OpenUSD-Plugins, über Zwischenformate (FBX, OBJ, STEP) oder per spezialisiertem Dienstleister. Entscheidend ist die Ausgangsqualität der CAD-Datei."
  - q: "Was ist der Unterschied zwischen OpenUSD und USDZ?"
    a: "OpenUSD (Universal Scene Description) ist ein offenes 3D-Format für komplexe Szenen und Workflows – entwickelt von Pixar, standardisiert durch Apple, NVIDIA und BMW. USDZ ist das komprimierte, mobiloptimierte Paketformat auf OpenUSD-Basis – ideal für AR auf iOS und Android."
  - q: "Welche CAD-Programme exportieren direkt nach OpenUSD oder USDZ?"
    a: "Zunehmend mehr Programme unterstützen OpenUSD nativ – darunter CATIA (via Plugin), Blender, Cinema 4D und Autodesk-Produkte. Für Programme ohne direkten Export gibt es spezialisierte Konverter-Tools oder Dienstleister wie viSales."
  - q: "Kann man USDZ auch ohne CAD-Daten erstellen?"
    a: "Ja, aber der Aufwand steigt erheblich. Ohne CAD-Daten muss das 3D-Modell aus Fotos (Photogrammetrie) oder per Hand modelliert werden. Mit vorhandenen CAD-Daten ist die Konvertierung nach USDZ dagegen ein gut planbarer Schritt."
---

- **Eine USDZ-Datei lässt sich auf vier Wegen erstellen: aus CAD-Daten (Plan A), aus Animations-Software wie Blender (Plan B), durch Neuerstellung oder 3D-Scan (Plan C) oder per KI-Generierung (Plan D).**
- **CAD-Quelldaten sind der effizienteste Ausgangspunkt für USDZ — sofern die Geometrie freigegeben und sauber genug für die Konvertierung zu OpenUSD ist.**
- **OpenUSD ist der gemeinsame Standard hinter USDZ: ein offenes Format für AR, Apple Vision Pro, industrielle Visualisierung und Real-Time-3D aus einer einzigen Quelldatei.**

**Du willst deine Produkte in 3D erlebbar machen? Vielleicht sogar direkt in Augmented Reality (AR) zeigen, ohne App-Installation, direkt per QR-Code? Klingt nach Zukunftsmusik? Ist es nicht. Die gute Nachricht: Es geht. Die schlechte? Der Weg zur passenden 3D-Datei ist oft holpriger als gedacht. Hier kommen vier typische Pfade, die unsere Kunden nehmen – mit ihren Tücken und Lösungen. Klar und praxisnah. Ohne Buzzword-Bingo. **

## Plan A: CAD-Datei zu OpenUSD

Der Klassiker. Marketing fragt bei der Konstruktion nach den 3D-Daten. Und dann kommt das erste große Fragezeichen: "Können wir die rausgeben?" Klar, kein Unternehmen will seine Konstruktionsgeheimnisse ungefiltert weiterreichen. Also wird erstmal über Geheimhaltungsvereinbarungen (NDAs) gesprochen, alles völlig verständlich.

Wenn das geklärt ist, bekommen wir üblicherweise STEP-Dateien oder ähnliche Formate. Und dann beginnt die eigentliche Arbeit: Aus den komplexen CAD-Modellen machen wir schlanke, visuell attraktive und AR-fähige 3D-Dateien. Das heißt:

- Überflüssige Details raus (Bohrlöcher, interne Verschraubungen etc.)
- Dateigröße schrumpfen (Performance!)
- Texturen erstellen (denn CAD hat oft keine)

Das läuft teilweise automatisiert, aber wir haben auch eigene Tools entwickelt, um genau dort nachzubessern, wo Standardsoftware noch versagt. Und wenn's schnell gehen muss, geht auch Plan A inhouse beim Kunden: Wir bieten Workshops, um euch fit zu machen.

## Plan B: 3D-Animationsdatei zu OpenUSD

"Wir haben da schon was in Blender/3ds Max machen lassen!" – hören wir oft. Klingt erstmal gut. Ist aber meist nicht direkt nutzbar. Denn viele 3D-Daten aus der Werbung sind auf "sieht gut aus" optimiert, nicht auf "läuft flüssig auf dem Smartphone".

Manche Agenturen gehen dann den Weg, einfach alle Variantenbilder vorzurendern. Sieht schick aus, ist aber kein echtes 3D. Kein AR. Kein Konfigurator. Nur Bilder. Das ist wie ein Online-Shop, bei dem man nichts anklicken kann.

Sollten so jedoch 3D-Daten aus einer 3D-Animationssoftware wie 3ds Max oder Blender vorliegen, beginnt die eigentliche Arbeit: **Datenumkonvertierung**. Und wer jetzt denkt, das wäre nur ein Knopfdruck – weit gefehlt. Jedes Programm speichert bestimmte Dinge anders ab: Shader (Materialinformationen), Lichtquellen, Gruppierungen. Alles kann, nichts muss – und oft passt es nicht zusammen.

> Man stelle sich eine Welt vor, in der PDF nicht funktioniert und Word-Dokumente von jedem Programm anders dargestellt werden. Genau so ist leider der Stand bei 3D-Dateien.

Wenn man also die 3D-Daten durch dieses Nadelöhr befreit hat, kommt als nächster Schritt die **Datenreduktion**. Denn gerade wenn die Daten für Grafikzwecke erstellt wurden, zählte vor allem eines: Es soll gut aussehen. Dass das Rendering für einen Prospekt mehrere Minuten oder sogar Stunden braucht, ist völlig egal – es wird ja nur einmal exportiert. Für einen AR-Konfigurator dagegen müssen Daten leicht, schnell ladbar und effizient aufgebaut sein. Performance ist kein nice-to-have, sondern Pflicht.

Wenn wir die Originaldateien bekommen – oft OBJ oder Blender (.blend), seltener FBX – beginnt die Umwandlung: Shader bereinigen, Geometrie vereinfachen, für OpenUSD (das ist das Dateiformat hinter *.usdz) aufbereiten. Dann läuft das auch auf dem iPhone oder iPad, und zwar direkt über den Browser.

**Best Case:** Bei einem Möbelhersteller haben wir genau das gemacht. Nach zwei Tagen war das ursprünglich zu "fette" 3D-Modell ein fertiger AR-Konfigurator.

## Plan C: Neu modellieren oder scannen

Keine CAD-Daten? Kein Blender-Modell? Dann bleibt oft nur der Weg über Neuaufbau oder Digitalisierung.

Wir scannen kleinere Objekte per Photogrammetrie (Fotos aus vielen Winkeln), größere Anlagen notfalls mit Partnern im 3D-Laserscan. Oder wir modellieren neu. Klingt aufwendig, ist aber manchmal der einfachste Weg – vor allem, wenn z. B. Sondermaschinen aus vielen Quellen zusammenkommen und keine zentrale Datenbasis vorhanden ist.

Beispiel: Eine komplette Fabrikhalle für eine Analyse-Software. Statt aufwändige CAD-Daten zu suchen, haben wir ein Low-Poly-Modell (vereinfachte Darstellung) aufgebaut – mit nur den Infos, die wirklich gebraucht wurden. Farbe? RAL reicht. Kein Schnickschnack. Dafür lauffähig, schnell, übersichtlich.

## Plan D: KI zu OpenUSD

"Da gibt’s doch jetzt KI!" Klar. Und wir testen diese Tools auch. Aber: Was aktuell rauskommt, ist oft eher Frankenstein als Ferrari.

Die Geometrie wirkt aus der Ferne okay, aber intern ist das ein zusammengeflicktes Datenchaos. Keine sauberen Strukturen, keine kontrollierbare Qualität. Und für AR auf Apple-Geräten muss alles **perfekt** sitzen: leicht, schnell, kompatibel. Das schaffen aktuelle KI-Lösungen (noch) nicht.

Wir probieren viel, auch mit lokalen Modellen (Datenschutz!). Und vielleicht taugt das irgendwann mal für Deko oder Kontextrahmen. Aber nicht für deinen echten Produktkonfigurator.

## Fazit: Der Weg ist machbar – aber nicht trivial

Egal ob CAD, Blender, Scan oder KI: Am Ende braucht es **eine saubere, performante OpenUSD-Datei** (das ist das Format für Apple AR, kurz *.usdz). Und genau dabei helfen wir. Mit Tools, Erfahrung, und manchmal auch mit dem Mut zu sagen: "Lass uns das Ding einfach neu bauen."

Wir beraten dich ehrlich. Und zeigen dir gern echte Beispiele, was geht. Bevor du viel Geld für die falschen Daten ausgibst, sprich mit mir &gt; [Unverbindliche Terminanfrage](https://visales.de/kontakt/). Tee zur Hand, Kamera an, los geht's!

&nbsp;

&nbsp;

&nbsp;

### **Einstieg in AR & USDZ — mit Unterstützung.**

Wir begleiten Unternehmen vom ersten USDZ-Modell bis zum eingebetteten AR-Erlebnis im Vertrieb. Das erste Gespräch dauert 30 Minuten. Ohne Pitch, ohne Vorbereitungspflicht. **Rheingas, Somfy und Carl Hamm haben mit einem Produkt begonnen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

## Typische Entscheiderfragen

→ Praxiseinsatz von AR: [AR im B2B-Vertrieb – der große Überblick](https://visales.de/augmented-reality/)

→ OpenUSD im Einsatz: [USDZ & OpenUSD für den Vertrieb](https://visales.de/openusd-dienstleister/)


