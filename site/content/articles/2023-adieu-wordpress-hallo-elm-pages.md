---
title: "2023: Adieu Wordpress. Hallo Elm-pages!"
slug: 2023-adieu-wordpress-hallo-elm-pages
status: published
primary_tag: aus-der-agentur
tags: [aus-der-agentur]
feature_image: /assets/images/2025/11/Gerhars_schroeder_zensiert.png
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2023-01-03T07:00:00.000Z"
type: page
template: page
---

**Unser Weg von DEM Standardwerkzeug für Websites zu einem mächtigen Außenseiter ist mein erster LinkedIn-Artikel für 2023. Nehmt Euch eine Tasse Tee oder Kaffee, ein paar Minuten Zeit und dann zeige ich Dir das WIESO und WARUM auf. Bin gespannt auf Eurer Feedback zum neusten Schritt der Agentur.**

## Vorgeschichte: Warum wir von Wordpress weg gehen

Es fing eigentlich vor über einem Jahr an, mit meiner persönlichen Entscheidung Facebook, Twitter, Instagram und WhatsApp zu löschen. Ganz. Kein Rückweg. Alle Accounts weg. Auch für die Firma kein Facebook etc. mehr. Ich duldete damals nur zwei Plattformen, weil Twitter und Instagram noch eine chronologische Timeline besaßen. Ergo: Wir haben daher zunächst Firmen-Instagram- und -Twitter-Account behalten. Im Herbst 22 löschte ich dann auch diese Accounts. 

Mein Weg seit dem Frühjahr 2022: FediVerse & Mastodon antesten. War für viele vor einem Jahr ein absoluter Exot. Außerdem habe ich mir diverse „Social Networks“ im 3D- und Photogrammetrie-Bereich angeschaut als Vorgeschmack auf echte XR-Social-Networks. Mehr dazu zu anderer Zeit, vielleicht in Form von [YouTube-Videos auf meinem Kanal](https://www.youtube.com/channel/UCa2cj_wluqNSh72Q5VJ735A).

## Wordpress und Mastodon?

Generell ist Wordpress nicht von Hause aus „Mastodon-Ready“, aber es gibt ein schönes PlugIn, das mit wirklich nur ein paar Klicks die Anbindung ans FediVerse, dem Datenaustauschprotokoll zwischen diversen Kurznachrichts-Mastdon- und Bilderplattformen wie PixelFed-Servern ermöglicht: [ActivityPub](https://de.wordpress.org/plugins/activitypub/). Sehr zu empfehlen.

Aber… wir nutzten für unsere Website das tolle [Divi-Theme](https://www.elegantthemes.com/gallery/divi/). 

Und damit steigen wir in das Rabbit-Hole der Kreuzunverträglichkeiten von Themes, PlugIns und Co. ein. Es es wie mit Medikamenten. 

*Nur weil Du A verträgst und B sagt dies NICHTS darüber aus, ob Du A und B gleichzeitig verträgst. So war es auch bei Divi und ActivityHub.*

Theme-Wechsel und damit ein Relaunch der Website oder den mir wichtigen Schritt zum Support der dezentralen Web-Idee? 

Keine spaßige Sache. Es muss auch dazu Lösungen geben.

## Wordpress und Google Fonts?

Klar. Es gibt auch da Probleme. 

Viele Wordpress-PlugIns aus den USA sehen nicht die Notwendigkeit „ohne Google Fonts“ auszukommen. Ebenso unser Divi-Theme. Wieder ein Grund für einen Relaunch? 

Wir haben erst einiges an Arbeitszeit investiert um im ganzen Theme alle Aufrufe von Google Fonts zu löschen, denn wir haben schon seit ein paar Jahren eine spezielle Opensource Hausschrift eingeführt von der Braille Foundation (NAME), die auch für Menschen mit Sehbeinträchtigungen besser zu lesen ist. 

> Wer von Inklusion im Unternehmen spricht muss auch seine „Fancy Hausschrift“ auf den Prüfstand stellen. Maßstab ist da nicht mehr der Grafiker, der den Font X oder Y cool findet, sonst der Gedanken an Brillenträger und Co., oder?

Ergo Google Fonts raus und [Atkinson Hyperlegible](https://brailleinstitute.org/freefont) in Wordpress installiert. 

*Unser (ehemaliger) Grafiker *[Sebastian Niemann](https://www.linkedin.com/in/sebastian-n-84b6981a2/)* schlug unseren neuen Font vor. Soviel also zu Grafiker ohne keinen Bezug zum Thema Inklusion...*

Trotzdem… wenig Aufwand für das Thema Inklusion und viel Aufwand für das Thema Datenschutz und ein Leben ohne Google Fonts.

## No-Cookie-Website / Statische Websites

Hand auf Herz: Brauchen wir als XR- / Grafik- / Video-Agentur wirklich Google Analytics oder Matomo, welches wir kurz vor der Contenixx 2022, eingeführt haben? 

Und: Geht für uns eine Website auch ganz ohne Cookies?

Ich erinnerte mich an die erste Firmenseite für meinen damaligen Arbeitgeber 1997, THB.de, die ich noch mit dem NetScape-Navigator programmierte. Der Weg von [LaTeX](https://de.wikipedia.org/wiki/LaTeX) via [SGML](https://de.wikipedia.org/wiki/Standard_Generalized_Markup_Language) zum HTML 1.0 war ein Katzensprung. Damals waren Websites alle Statisch, ohne Nachladen, Cookies und Co. 

Wordpress nutzt eine Datenbank um aus den Texten und Bildern für jede Anfrage NEU eine Seite zu erstellen. Durch den Einsatz von speziellen Tools (Plugins) kann man nach jedem Seiten-Update ein solche statische Website erzeugen lassen. 

Warum dann nicht gleich eine statische Seite für uns als kleine Agentur? Wir betreiben keinen Shop und haben auch sonst keine wirklich dynamischen Inhalte wie eine Tageszeitung. Selbst solche Newssites erzeugen aus Gründen der Serverlast / Kostengründen in der Regel solche statischen Seiten.

Am Ende: Hauen wir also doch unsere 13 Jahre alte Wordpress-Instanz /in die Tonne/?

## Auftritt elm 

Unser Hauseigener elm-Botschafter [Thomas Kumlehn](https://www.linkedin.com/in/thomas-kumlehn/) schwärmt von dieser Programmiersprache schon seit langer Zeit. Für Laien: [Elm](https://en.wikipedia.org/wiki/Elm_%28programming_language%29) ist eine Programmiersprache, die am ENDE Javascript ausgibt, also DIE Progammiersprache fürs Web, neben HTML einer der heutigen Grundpfeiler des Internets. 

JavaScript hat aber eine Fehler, dazu gehört seine Fehleranfälligkeit. Man kann absichtlich oder unabsichtlich viele Dinge FALSCH machen. Stichwort Bugs, Exploits und Co.

Auftritt elm - /Meine Rechtschreibkorrektur möchte immer ELF schreiben, was ich auch Ok finde/ - ist eine Art Zwischensprache mit der ich fehlerfreien Javascript-Quellcode erzeugen kann. 

*Tadaaaaa!*

Wir nutzen elm eigentlich in der Agentur für einen ganz anderen Zweck: Einfache interaktive USDZ-Dateien können mit einem WYSIWYG-Editor von Apple erstellt werden. Unsere wesentlich komplexeren XR-Konfiguratoren, die ja auch Fehlerfrei sein sollen (!) erstellen wir via unser Eigenentwicklung ConfigXR mit… elm. 

Stichwort ConfigXR: [Mehr dazu auf YouTube an einem Bürostuhl—Beispiel](https://youtu.be/5nTA1IrkAas). Weitere Videos gibt es schon bald dazu. Spolier: ConfigXR 2.0.

## Von SGML über HTML und MarkDown

Noch mehr Nerdkram: Ich schrieb ja schon das ich via LaTeX zu HTML kam. In unserer Agentur „sprechen“ aber auch nur 2 oder 3 Personen HTML und der Rest verfasst Texte, für Konzepte, Angebote oder Gastbeiträge / die Website.

Doch da gibt es ja mit dem System [MarkDown](https://de.wikipedia.org/wiki/Markdown), eine einfache Lösung reine Textdateien mit simplen Steuerbefehlen, wie z.B…

1. # am Anfang einer Zeile erzeugt eine H1-Überschrift
2. ## erzeugte eine H2-Überschrift
3. - erzeugt einen Aufzählungspunkt für eine Liste

…einen Jedermann-Text, der mit dem Tool elm-pages direkt zu dem Content-Bereich einer Website oder eines Blog-Beitrags umgeformt wird. 

Voila, mit meinem kostenlosen Lieblingseditor [Bear](https://apps.apple.com/us/app/bear-markdown-notes/id1016366447) (auf macOS) kann ich direkt die Texte für [LinkedIn-Newsletter zum Thema visuelle Kommunikation](https://www.linkedin.com/newsletters/schr%C3%B6ders-notizen-6964950674841157632/) und unsere Website erstellen. 

## elm-pages für unsere neue Website

[Elm-pages](https://package.elm-lang.org/packages/dillonkearns/elm-pages/latest/) ist ein Webseiten-Generator, der aus MarkDown-Dateien HTML-Inhalte mit allen Rahmendaten wie Navigation im Kopf der Seite oder Impressums-Link im Fußbereich der Seite erstellt. 

Jede Änderung an einem Text führt zu einem Update aller notwendigen Seiten, die dann via FTP-Upload auf den Server gepackt werden können. Es geht auch etwas Eleganter, aber so ist es für uns als Agentur schon Ok.

Wir bereiten gerade eine solche neue Website vor. 

Dieser Text wird dann unser erster Beitrag im neuen Blog werden. Zunächst stellen wir aber die Startseite, Leistungen und Team-Seite auf die neue Lösung um. Erst danach werden einige alte Blog-Beiträge in das neue System übernommen.

## Ausblick 2023

Wir werden elm-pages ans ActivityHub anbinden: Entweder via Tools oder direkt. Das schauen wir in den nächsten Wochen. Notfalls nutzen wir für den Blog sogar eine [FediVerse-Lösung](https://fediverse.party/en/miscellaneous/). Eher gehen wir aber den einfacheren Weg.

Außerdem möchte wir unser [AR-Wordpress-PlugIn](https://youtube.com/shorts/luJyTXWeJQg) via elm-pages zum Laufen bringen und frei zur Verfügung stellen / Open Source via unser [K3-GitHub](https://github.com/KopfKinoK3).

**Falls nun jemand Fragen zu elm, elm-pages oder unserem elm-Juwel ConfigXR hat, einfach melden.** 

Viele Grüße aus Velbert,

Gerhard Schröder

**Update 2025: **Statt ELM-pages sind wir via NUXT nun bei Ghost6 (mit Fediverse-Anbindung) gelandet.

&nbsp;
