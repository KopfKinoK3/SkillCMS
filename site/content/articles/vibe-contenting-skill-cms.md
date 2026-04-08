---
title: "Vibe-Contenting braucht kein smartes CMS. Es braucht ein... dummes?"
slug: vibe-contenting-skill-cms
status: published
primary_tag: aus-der-agentur
tags: [aus-der-agentur, ki]
meta_title: "KI-gestütztes CMS: Warum Markdown Ghost schlägt"
meta_description: "Warum ein minimales, API-first CMS für KI-Workflows besser ist als ein komplexes Backend – und wie Claude direkt in Ghost schreibt."
feature_image: /assets/images/2026/03/Gerhard_Schr--der_viSales_Umzug.jpeg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-03-09T23:27:04.000Z"
type: post
template: post
---

Seit ein paar Wochen arbeite ich mit [Claude](https://claude.ai) Code und Claude Cowork – KI-Assistenten, die einen echten Browser bedienen können. Auch das Ghost-Backend und die SEO-Metadaten-Felder. Theoretisch.

Praktisch: Es funktioniert. Aber es dauert, denn jede Interaktion kostet Token. Wer mit einem normalen Firmenpaket arbeitet, verbrennt für das, was früher fünf Minuten Handarbeit war, ein Vielfaches – in Zeit und Kosten. *(Zum Feierabend kann man ja noch so´nen Auto-Task anwerfen...)*

Das hat mich zurückgeworfen auf eine Frage, die ich eigentlich schon beantwortet glaubte.

## Dreißig Jahre CMS und am Ende Markdown

Ich habe Webseiten von Hand mit [HTML](https://de.wikipedia.org/wiki/Hypertext_Markup_Language) geschrieben. [Netscape Composer](https://en.wikipedia.org/wiki/Netscape_Composer), dann puristisch im Texteditor – [LaTeX](https://de.wikipedia.org/wiki/LaTeX)-Vorerfahrung macht das möglich. Dann [blog.de](https://www.blog.de) *-vor dessen Relaunch-*, täglich zwei DIN-A4-Seiten. Dann WordPress, erst privat als padlive.de, dann geschäftlich unter kreativekommunikationskonzepte.de. Jahrelang, bis 2025.

Der Wechsel via Elmpages zu Nuxt kam, weil Markdown einen klareren Workflow erlaubt. Ghost kam danach, weil es [Fediverse](https://de.wikipedia.org/wiki/Fediverse), Newsletter, [RSS](https://visales.de/apple-rss-button-offenes-web/) und Blog in einem kann. Nur: Ghost ist im Kern auf den eigenen US-Server ausgelegt. Die Entkopplung von US-Diensten ist echte Handarbeit.

## Token lügen nicht

Wenn ein KI-Agent durch ein CMS-Backend navigiert, wird schlagartig klar, was Komplexität wirklich kostet. Nicht in Lernzeit, sondern in Token. Ein gut strukturiertes Markdown-File ist für Claude trivial. Ein Ghost-Backend mit verschachtelten UI-Elementen, Modalen, Dropdown-Menüs – das ist Navigation. Jeder Klick ein Schritt. Jeder Schritt ein Preis.

> **Das ideale CMS für KI-gestütztes Arbeiten ist nicht das funktionsreichste. Es ist das, das am wenigsten im Weg steht.**

[Nuxt](https://nuxt.com/) mit [Markdown](https://de.wikipedia.org/wiki/Markdown)-CMS und Claude Code, der direkt in Dateien schreibt – keine UI, die navigiert werden muss, kein Backend, das erklärt werden will. Und was fehlt, lässt sich ergänzen. Ich habe dreißig Jahre gebraucht, um wieder dort zu landen, wo ich angefangen habe: beim Texteditor, nur dass der jetzt mitdenkt?

<details>
<summary><strong>**Realitätscheck**</strong></summary>

Ghost ist nicht kaputt. Wer es einmal sauber aufgesetzt hat – eigenes Hosting, eigener Mailversand, keine US-Abhängigkeiten – bekommt ein System, das Newsletter, Fediverse, RSS und Blog wirklich integriert.

Kein anderes Open-Source-CMS kann das so direkt. Die Token-Kosten sind ein Effizienzproblem, kein Architekturproblem. Vielleicht ist die Antwort nicht das einfachere CMS, sondern der bessere Prompt?

Ich berichte ob wir Ghost gezähmt bekommen.

</details>

<details>
<summary><strong>Skill-CMS: Was wäre, wenn Claude den Rest übernimmt?**?**</strong></summary>

Ein Gedankenexperiment: Ein minimales CMS, welches nur noch die Kernfunktionen bereitstellt: Newsletter-API, Fediverse-Anbindung, RSS, Datenhaltung. Kein Editor, keine Oberfläche, die navigiert werden muss.

Der Rest? Ein Skill in Claude. Oder eine Sammlung davon. Einen Skill für Impulse, einen für Newsletter, einen für SEO-Metadaten. (Habe ich jetzt schon...) Claude schreibt direkt in die Struktur – kein Backend, keine UI-Navigation, keine Token für Klicks.

Das wäre kein CMS mehr im klassischen Sinne. Es wäre eine API mit Persönlichkeit.

Ob das realistisch ist? Technisch heute schon denkbar. Ob Ghost oder Nuxt so gebaut werden wollen – andere Frage.

</details>

Der Plastikflamingo vom Umzugsfoto hat übrigens die [Flutkatastrophe 2021 in Velbert](https://www.youtube.com/watch?v=BEOGrtxORbQ) nicht überlebt. Irgendwie passend: Manchmal räumt das Leben den alten Stack einfach weg und man fängt neu an. 

Wieder beim Texteditor! 

&nbsp;

&nbsp;

### **Du willst wissen ob sichtbarer Content für dein Unternehmen passt?**

In 30 Minuten sortieren wir gemeinsam, ob und wo 3D-Inhalte in eurem Vertrieb konkret etwas bringen — ohne Pitch, ohne Angebot. Kein Verkaufsdruck, eine ehrliche Einordnung. **Rheingas und Somfy haben so angefangen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

<details>
<summary><strong>**Update > 10. März 2026, 23:00 Uhr > Es funktioniert!**</strong></summary>

Während dieser Artikel heute in der früh an den Start ging, habe ich mit Claude.ai das Gedankenexperiment "Skill-CMS via Ghost" direkt live getestet und der erste POST-Call hat geklappt. D.h. ich habe mit Claude einen Skill erstellt, der aus Claude heraus einen neuen Beitrag im Ghost-CMS **"Hallo World"** anlegte im Entwurfsmodus.

**So ging es Schritt für Schritt:**

1. **Ghost Admin API aktivieren** – In den Ghost-Settings unter **Integrations → Add custom integration** eine neue Integration anlegen. Ghost generiert dabei automatisch einen Admin API Key.
2. **Authentifizierung verstehen** – Die Ghost Admin API nutzt JWT (JSON Web Token). Der API Key besteht aus zwei Teilen: einer ID und einem Secret. Daraus wird ein kurzlebiges Token generiert, das jede Anfrage signiert.
3. **Keinen Klick gemacht** – Statt durch das Backend zu navigieren, hat Claude einen einzigen `POST`-Request an `/ghost/api/admin/posts/` geschickt – mit Titel, Text, Tags und Status in einem einzigen JSON-Objekt.
4. **Ergebnis:** Ein Draft mit dem Titel **"Hello World"** lag innerhalb von Sekunden im Backend. Kein Editor geöffnet, kein Modal bedient, kein Publish-Button gesucht.

**Was das bedeutet:** Die Token-Kosten für "Artikel erstellen" sind damit von ~20 Schritten auf einen einzigen Call geschrumpft. Das ist keine Optimierung – das ist ein anderes Level des Postens.

Der Skill, der das automatisiert, ist der nächste Schritt...  
  
**Schneller, zweiter Test um 23:20 Uhr:**

Claude kann nun bestehende Artikel **lesen, ergänzen, korrigieren, mit Metadaten anreichern**, alles ohne das Backend auch nur zu öffnen. Ein Skill, der z.B. SEO-Metadaten für alle Artikel auf einmal ergänzt, wäre damit technisch trivial.

**Ich könnte nun auch ein ganzes Skill-CMS mit Claude-Code erstellen und eine Sammlung statischer Seiten -**wie es Nuxt-CMS macht**- erstellen kann und via FTP hochladen lassen...**

</details>

&nbsp;

&nbsp;

Dieser Gedanke entstand während der eigenen [Ghost-Migration](https://ghost.org) und ersten Erfahrungen mit [Claude Code](https://code.claude.com/docs/de/overview) als [Brave](https://brave.com/de/)-Browser-Agent. Inspirationen dazu sind auch der KI-Podcast mit Mark und Jens [Think Different. Think AI.](https://think-ai.podigee.io) und der YouTube-Channel von [Christoph Magnussen](https://www.youtube.com/christophmagnussen). Mehr bei mir zu [KI im Arbeitsalltag](https://visales.de/tag/ki/).
