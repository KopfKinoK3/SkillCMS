---
title: "Apple hat die Kauf-direkt-in-AR-Taste: AR Quick Look mit Banner"
slug: ar-quick-look-banner-safari-vertrieb
status: published
primary_tag: apple
tags: [apple, impuls, openusd, augmented-reality, vertriebskommunikation]
meta_title: "AR Quick Look Banner: AR-Commerce direkt in Safari | viSales"
meta_description: "Apple AR Quick Look mit Banner-Funktion: Drei Beispiele zeigen, wie USDZ-Modelle im Safari-Browser zum Vertriebstool werden — ohne App, ohne SDK."
feature_image: /assets/images/2026/03/AR-Quick-Look-Banner-Vertrieb.jpg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-03-26T12:44:29.000Z"
type: post
template: post
faq_heading: "Häufige Fragen zu AR Quick Look Banner"
faq:
  - q: "Was ist AR Quick Look Banner in Safari?"
    a: "AR Quick Look Banner ist eine Apple-Funktion in Safari, die einen anpassbaren Aktions-Button direkt über dem 3D-Viewer einblendet. Statt nur ein Produkt zu betrachten, kann der Nutzer aus der AR-Ansicht heraus direkt handeln – Anfrage stellen, konfigurieren oder kaufen. Kein App-Download, läuft ab iOS 13.3."
  - q: "Welche drei Banner-Typen bietet Apple AR Quick Look?"
    a: "Apple unterscheidet drei Typen: Custom Action Banner – ein einfacher Button mit frei definierbarer Aktion (z.&nbsp;B. Anfrage, Termin). Custom HTML Banner – vollständig anpassbares Banner mit eigenem HTML-Inhalt. Apple Pay Banner – direkter Kauf-Button aus der AR-Ansicht, mit Apple Pay als Zahlungsmethode."
  - q: "Warum sind AR Quick Look Banner für den B2B-Vertrieb relevant?"
    a: "Sie verwandeln einen passiven 3D-Viewer in einen aktiven Vertriebskanal: Interessenten können direkt aus der AR-Ansicht eine Anfrage schicken oder einen Termin buchen. Der Schritt vom Erleben zum Handeln wird minimal. Besonders wirksam auf Messen und in Produkt-E-Mails mit QR-Code-Link."
  - q: "Auf welchen Geräten funktioniert AR Quick Look Banner?"
    a: "AR Quick Look Banner funktioniert auf allen Apple-Geräten mit Safari ab iOS 13.3: iPhone und iPad. macOS Safari zeigt USDZ als 3D-Viewer, aber ohne AR-Funktion. Android-Geräte nutzen Google Scene Viewer – dort ist keine Banner-Funktion verfügbar."
  - q: "Wie aufwendig ist die technische Umsetzung von AR Quick Look Banner?"
    a: "Minimal. Ein einziges HTML-Attribut am Link-Tag genügt für Custom Action. Für Custom HTML Banner wird eine kleine HTML-Datei als Parameter übergeben. Wer bereits USDZ-Dateien und einen Webserver hat, kann das Feature in unter einer Stunde umsetzen – ohne App-Entwicklung, ohne Backend."
ki_text: true
ki_bild: true
---

Letzte Woche habe ich einem Kunden gezeigt, wie sein Produkt in Augmented Reality aussieht. Auf dem iPhone, direkt im Safari. Kein App-Download, kein QR-Code-Scan mit Drittanbieter-App. Einfach ein Link, tippen, fertig. Das kennt er schon. Dann habe ich ihm gezeigt, was passiert, wenn man unten im AR-Viewer auf den Button tippt. 

Er sagte: „Moment — da kann ich direkt kaufen?“

## AR Quick Look mit Banner: 3 Varianten

Apple hat in Safari eine Funktion eingebaut, die fast niemand nutzt: [AR Quick Look](https://visales.de/wozu-braucht-man-ar-quick-look-von-apple/) mit Banner**.** Die Idee: Ein USDZ-3D-Modell öffnet sich nativ im AR-Viewer (AR Quick Look), und am unteren Rand erscheint ein Banner — mit Produktname, Preis und einem Call-to-Action-Button. Kein SDK, kein Framework, keine App. Nur ein HTML-Link mit URL-Parametern.

Das klingt zu einfach, um relevant zu sein. Ist es aber!

### Custom Action Banner

Apple unterscheidet drei Banner-Typen. Der erste ist ein Custom Action Banner — du hängst an die USDZ-URL einfach Fragment-Parameter wie *callToAction*, *checkoutTitle* und *price*. Im AR-Viewer erscheint dann ein Banner mit Button. Der Außendienst zeigt dem Kunden eine Industriepumpe in AR auf dem iPad, der Kunde tippt auf „Angebot anfordern“ — und das Event wird per JavaScript abgefangen. [Apple zeigt das mit einer Kinderrutsche für 145 Dollar](https://developer.apple.com/augmented-reality/quick-look/models/kids-slide/slide.usdz#callToAction=Browse%20API&checkoutTitle=Kids%20Slide&checkoutSubtitle=Playground%20in%20your%20backyard&price=$145&allowsContentScaling=0) — aber übertragen auf B2B-Produkte wird es spannend: Messe-Demo, Showroom, Vertriebstermin.

→ [Kinderrutsche in AR ausprobieren](https://developer.apple.com/augmented-reality/quick-look/models/kids-slide/slide.usdz#callToAction=Browse%20API&checkoutTitle=Kids%20Slide&checkoutSubtitle=Playground%20in%20your%20backyard&price=$145&allowsContentScaling=0) (iPhone & iPad)

### Custom HTML Banner

Der zweite Typ ist ein Custom HTML Banner — statt vordefinierter Felder lädst du eine eigene HTML-Datei als Banner. Eigenes Branding, eigene Layouts, in drei Größen. [Apples Beispiel zeigt das mit Solarpanels und einem individuellen Info-Banner](https://developer.apple.com/augmented-reality/quick-look/models/solar-panels/solar_panels.usdz#custom=https://developer.apple.com/augmented-reality/quick-look/models/solar-panels/solar_panels_custom.html?1&customHeight=large&allowsContentScaling=0). Auf Messen könnte das heißen: Das Kundenlogo im AR-Viewer, technische Specs direkt unter dem 3D-Modell, oder eine Aktionsbotschaft mit Messepreis. Die Einschränkung: kein JavaScript im Banner, nur Display.

→ [Solarpanel in AR ausprobieren](https://developer.apple.com/augmented-reality/quick-look/models/solar-panels/solar_panels.usdz#custom=https://developer.apple.com/augmented-reality/quick-look/models/solar-panels/solar_panels_custom.html?1&customHeight=large&allowsContentScaling=0) (iPhone & iPad)

### Apple Pay Banner

Der dritte Typ ist der Apple Pay Banner — und das ist das Feature, über das kaum jemand spricht. Ein USDZ-Modell mit integriertem Apple-Pay-Button. Der Kunde sieht das Produkt in AR, tippt auf „Kaufen“, und die Transaktion läuft über Apple Pay. [Apple hat dafür eine eigene Demo-Seite](https://applepaydemo.apple.com/ar-quick-look/). Für B2C-Shops, Ersatzteilbestellungen oder Zubehör-Konfiguratoren ist das ein Kanal, den fast niemand bespielt.

→ [Apple-Pay-Demo](https://applepaydemo.apple.com/ar-quick-look/) (iPhone & iPad)

### Warum AR Quick Look Banner für B2B-Vertrieb relevant sind

Was diese drei Banner-Typen gemeinsam haben: Sie machen aus einem passiven 3D-Viewer einen aktiven Vertriebskanal. Der Sprung von „schönes Modell anschauen“ zu „konkrete Aktion auslösen“ passiert ohne Medienbruch, ohne App-Wechsel, ohne Ladezeit. Alles nativ in Safari.

<details>
<summary><strong>Realitätscheck</strong></summary>

Die Einschränkung liegt auf der Hand: AR Quick Look ist ein reines Apple-Feature. Android hat nichts Vergleichbares mit nativer Banner-Integration. Wer also eine Lösung braucht, die auf allen Geräten funktioniert, kommt um eine WebAR-Lösung auf Basis von WebXR oder model-viewer nicht herum.

Außerdem: Die Custom HTML Banners sind rein statisch — kein JavaScript, keine Interaktivität im Banner selbst. Wer einen echten Konfigurator im AR-Viewer will, kann aber auf die Varianten-AR Quick Look-Funktion setzen.

AR Quick Look mit Banner ist kein Ersatz für eine vollwertige WebAR-Anwendung. Es ist ein extrem niedriger Einstiegspunkt mit überraschend hoher Wirkung — solange man die Grenzen kennt.

Und: Apple Pay im AR-Viewer klingt spektakulär, ist aber kaum dokumentiert und in der Praxis fast nicht im Einsatz. Das Feature existiert seit iOS 13.3, also seit über sechs Jahren. Dass es trotzdem kaum genutzt wird, sagt etwas über über die Trägheit der E-Commerce-Branche.

</details>

> Technisch ist die Umsetzung trivial. Ein einziges HTML-Tag reicht aus, um ein 3D-Modell mit Produktname, Preis und Call-to-Action in AR zu öffnen. Die ganze Magie liegt im USDZ-Asset und in der Beratung, wie man den CTA sinnvoll in den Vertriebsprozess einbaut. 

Genau das ist der Punkt, an dem Agenturen wie viSales ins Spiel kommen. Nicht das HTML-Tag ist die Leistung. Sondern zu wissen, welcher CTA bei welchem Kunden in welcher Phase funktioniert.

[Erstgespräch mit viSales](https://visales.de/kontakt){.gh-button .cta-center}

AR Quick Look mit Banner existiert seit iOS 13.3 — also seit über sechs Jahren. Dass es trotzdem kaum genutzt wird, liegt nicht an der Technik. Es liegt daran, dass die meisten Unternehmen AR noch als Showroom-Gimmick betrachten statt als Vertriebswerkzeug. Die Banner-Funktion zeigt: Apple hat den Commerce-Layer längst eingebaut. 

Man muss ihn nur nutzen.

&nbsp;

&nbsp;

→ Übersicht: [Augmented Reality im E-Commerce](https://visales.de/augmented-reality-im-ecommerce-ein-uberblick/)  
→ [Vom 3D-Modell zum Web-Konfigurator: Was OpenUSD & USDZ im B2B-Vertrieb wirklich leisten: USDconfig 1.1](https://visales.de/usdconfig-demo/)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

### **Einstieg in AR Quick Look — mit Unterstützung.**

Wir begleiten Unternehmen vom ersten USDZ-Modell bis zum eingebetteten AR-Erlebnis mit Kauf-Button im Vertrieb. Das erste Gespräch dauert 30 Minuten. Ohne Pitch, ohne Vorbereitungspflicht. **Rheingas, Somfy und Carl Hamm haben mit einem Produkt begonnen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;
