---
title: "Vom Impuls zur Reichweite: Wie ein Artikel bei viSales entsteht"
slug: skillcms-workflow-vom-impuls-zur-reichweite
type: post
status: draft
date: "2026-04-09"
primary_tag: "aus-der-agentur"
tags: ["aus-der-agentur", "ki", "skill-abo"]
meta_title: "Vom Impuls zur Reichweite — der viSales Content-Workflow mit SkillCMS"
meta_description: "Wie entsteht ein viSales-Artikel — von der Idee über den KI-assistierten Build bis zur Distribution auf Mastodon, YouTube und LinkedIn? Ein Blick hinter die Kulissen."
feature_image: "/assets/images/skillcms-content-workflow.svg"
author: "Gerhard Schröder"
---

Ich werde oft gefragt, wie ich es schaffe, regelmäßig Inhalte zu publizieren — trotz Projektarbeit, Kundengesprächen und dem ganzen Rest, der zum Alltag einer kleinen B2B-Agentur gehört.

Die ehrliche Antwort: Ich habe den Prozess neu gebaut.

Nicht optimiert. Neu gebaut.

&nbsp;

## Warum ein eigenes System?

Ich habe lange mit Ghost gearbeitet — und Ghost ist gut. Aber irgendwann war mir klar, dass ich keine CMS-Abhängigkeit mehr will. Keine Datenbank, die gepatcht werden muss. Keine Plugin-Inkompatibilitäten nach einem Update. Kein Backend, das mich nachts wachhält.

Was ich will: Markdown-Dateien, ein Python-Script, und eine Website, die sich anfühlt wie ein Produkt — nicht wie ein Framework.

Das Ergebnis heißt SkillCMS. Und der Workflow dahinter hat inzwischen elf Schritte, vier Phasen und einen Kreislauf, der sich selbst speist.

&nbsp;

## Phase A — Content-Entstehung: Kopf & KI

Jeder Artikel beginnt an einem von drei Orten.

Entweder kommt die Idee direkt aus dem Alltag — aus einem Kundengespräch, einem Konferenzbeitrag, einer Beobachtung, die sich nicht loslässt. Oder sie kommt aus der Google Search Console: welche Fragen stellen Menschen, die nach Themen wie WebAR, OpenUSD oder B2B-Visualisierung suchen? Oder sie ist in der Content-Strategie bereits angelegt — ein Thema, das wir bewusst besetzen wollen.

Was ich dann entscheide: welches Format. Ein Kurzimpuls, der schnell einen Gedanken auf den Punkt bringt. Ein Visual Sales Newsletter, der tiefer geht. Oder ein Vertriebskommunikationsbeitrag, der ein Thema grundlegend aufarbeitet.

Für jedes Format gibt es einen eigenen Claude-Skill — einen strukturierten Gesprächsleitfaden, der mir hilft, den Kern eines Themas herauszuarbeiten. Nicht ich tippe, was der Algorithmus gerne hätte. Ich rede, erkläre, widerspreche, korrigiere. Die KI strukturiert, verdichtet, fragt nach. Das Ergebnis ist mein Gedanke — nur besser artikuliert.

Ich nenne das: **Kopf & KI**.

&nbsp;

## Phase A — Fertigstellung: Freigabe & Automatisierung

Bevor ein Artikel in den Build geht, durchläuft er zwei automatisierte Schritte.

Der FAQ-Skill analysiert den Text und schlägt strukturierte Fragen und Antworten vor — mit JSON-LD Schema-Markup, das Suchmaschinen direkt verstehen. Der CTA-Skill prüft, wo im Funnel der Artikel steht, und setzt passende Handlungsaufrufe: TOFU für Awareness, MOFU für Abwägung, BOFU für Entscheidung.

Dann schaue ich drüber. Korrigiere, wo nötig. Und gebe frei.

&nbsp;

## Phase B — Build: Ein Befehl, alles gerendert

```
python3 build-visales.py
```

Das ist der gesamte Build-Prozess.

Aus einer Markdown-Datei mit YAML-Frontmatter entsteht eine vollständige HTML-Seite: mit Navigation, Footer, Newsletter-Einbindung, Autorenbox, Tag-Badges, FAQ-Toggles, JSON-LD Schema und OpenGraph-Tags. Dazu werden automatisch Tag-Listing-Seiten, eine Sitemap, ein RSS-Feed, robots.txt und llms.txt aktualisiert.

Statisch. Kein Backend. Maximale Performance.

Vor dem Deployment schaue ich die Seite lokal im Browser an — Layout, Bilder, Links, alles. Dann geht sie per FTP auf visales.de.

&nbsp;

## Phase C — Distribution: Reichweite ohne Algorithmus-Abhängigkeit

Live ist nicht fertig. Live ist der Startschuss.

Der Artikel erscheint als Teaser auf Mastodon — im offenen Fediverse, mit chronologischem Feed und einer Technik-Community, die echte Inhalte schätzt. Als Community-Post auf YouTube, wo bestehende Abonnenten erreicht werden. Als GBP-Post auf Google Business, für lokale Sichtbarkeit in Bochum und darüber hinaus.

Und auf LinkedIn: einen Entwurf erstelle ich mit dem LinkedIn-Skill, auf Basis meines Stils und meiner Positionierung. Den finalen Text schreibe ich selbst. Das Posting mache ich selbst. LinkedIn ist Beziehungsarbeit — das sollte nicht delegiert werden.

&nbsp;

## Phase D — Kreislauf: Der Claude-Loop

Was nach ein paar Wochen passiert, ist der interessanteste Teil.

Die Search Console zeigt, welche Artikel ranken, welche knapp darunter liegen, welche Klickraten unter den Erwartungen bleiben. Ein zyklischer Claude-Loop analysiert diese Daten, vergleicht sie mit dem bestehenden Content und schlägt konkrete Optimierungen vor: neue Abschnitte, aktualisierte FAQs, stärkere Titel, bessere interne Verlinkung.

Ich entscheide, was umgesetzt wird. Manchmal führt das zu einem überarbeiteten Artikel. Manchmal zu einem neuen Thema — und der Kreislauf beginnt von vorne.

**Schritt 1.**

&nbsp;

## Was das bedeutet

Das hier ist kein Tool-Stack-Bericht. Das ist eine Entscheidung darüber, was ich von meiner Arbeitszeit erwarte.

Ich will Inhalte publizieren, die meinen Gedanken entsprechen — nicht dem, was ein CMS-Template nahelegt. Ich will Distribution ohne manuelle Routinearbeit. Und ich will einen Prozess, der besser wird, je mehr ich ihn benutze.

SkillCMS ist dafür das Werkzeug. Der Workflow ist die Entscheidung.

Wer das System selbst einsetzen will — oder wissen möchte, wie eine ähnliche Infrastruktur für die eigene Content-Arbeit aussehen könnte: [Gespräch anfragen](https://visales.de/kontakt/).

---

*Dieser Artikel wurde mit SkillCMS gebaut — dem statischen Site-Generator von viSales, der Markdown-Dateien in performante, KI-lesbare HTML-Seiten verwandelt.*
