---
# ============================================================
# POST TEMPLATE — viSales SkillCMS
# Kopieren, umbenennen, alle PLATZHALTER ersetzen.
# Dateiname: {slug}.md → Ablage: site/content/articles/
# Empfohlener Dateiname bei datierten Posts: JJJJ-MM-TT-{slug}.md
# ============================================================

title: "TITEL DES ARTIKELS"
# H1 + <title>-Tag. Max. ~60 Zeichen für SEO.
# Formel: [Thema]: [Outcome/Versprechen] — z.B. "WebAR im Vertrieb: Wie Maschinenbauer Messen ersetzen"

slug: artikel-slug
# URL-Pfad: kebab-case, keine Umlaute, keine Sonderzeichen
# z.B. "webar-im-vertrieb-maschinenbau"

type: post
# NICHT ÄNDERN

status: published
# published | draft

date: "2026-04-07"
# Veröffentlichungsdatum ISO — in Anführungszeichen!

date_modified: "2026-04-07"
# Letztes Änderungsdatum — bei Updates aktualisieren

meta_title: "TITEL | viSales"
# Optional — wenn leer: title + " | viSales" wird automatisch verwendet
# Max. 60 Zeichen inkl. " | viSales"

meta_description: "BESCHREIBUNG DES ARTIKELS IN 1–2 SÄTZEN."
# Max. 160 Zeichen. Outcome-orientiert, kein Marketing-Speak.
# Formel: [Was der Leser lernt/bekommt] + [Kontext viSales/B2B]

excerpt: "KURZBESCHREIBUNG FÜR LISTINGS UND llms.txt."
# 1 Satz, max. 200 Zeichen. Wird in Tag-Listings und llms.txt verwendet.

feature_image: https://kopfkinok3.github.io/SkillCMS/assets/images/JJJJ/MM/bildname.jpg
# Titelbild — immer vollständige GitHub-Pages-URL verwenden!
# Format: https://kopfkinok3.github.io/SkillCMS/assets/images/JJJJ/MM/dateiname.ext
# Bild muss im Repo unter site/assets/images/JJJJ/MM/ liegen.

tags:
  - TAG-SLUG-1
  - TAG-SLUG-2
# Bekannte Tags: impuls, vertriebskommunikation, openusd, webar, ki-sicherheit,
#                skill-abo, prompt-injection, claude-skills
# Neue Tags: kebab-case, lowercase, Tag-MD in site/content/tags/ anlegen

primary_tag: TAG-SLUG-1
# Primärer Tag — erscheint als Badge über dem Artikel-Titel

author: "Gerhard Schröder"
# Standard-Autor — nur ändern bei Gastbeiträgen

author_slug: gerhard
# Entspricht dem slug in site.yaml unter author:

keywords: "keyword1, keyword2, keyword3"
# Für Article-Schema (JSON-LD) — 3–6 Keywords, komma-getrennt
---

<!-- ============================================================ -->
<!-- SNIPPET-BULLETS (optional, empfohlen für Artikel-Einstieg)   -->
<!-- 3–5 fettgedruckte Kernaussagen als Bullet-Liste              -->
<!-- ============================================================ -->

- **[Kernaussage 1 — die wichtigste Erkenntnis des Artikels]**
- **[Kernaussage 2 — zweite wichtige These]**
- **[Kernaussage 3 — dritte These oder Handlungsempfehlung]**


<!-- ============================================================ -->
<!-- EINLEITUNG                                                    -->
<!-- 1–2 Absätze: Problem/Kontext + Warum dieser Artikel jetzt    -->
<!-- ============================================================ -->

[Einstiegssatz — direkt ins Thema, kein "In diesem Artikel..."]

[Kontext-Absatz: Warum ist das relevant? Für wen? Welches Problem wird gelöst?]

> [Optional: Blockquote als Leitmotiv oder zentrale These des Artikels]


## [H2: Erster Hauptabschnitt]

[Fließtext. B2B-Sprache, outcome-orientiert. Keine Superlative ohne Beleg.]

[Weitere Absätze...]


## [H2: Zweiter Hauptabschnitt]

[Text]

### [H3: Unterabschnitt optional]

[Text]


## [H2: Dritter Hauptabschnitt — oder: Was das für [Zielgruppe] bedeutet]

[Text]

<!-- Bildergalerie (optional) — immer vollständige GitHub-Pages-URLs: -->
<!--
<div class="kg-card kg-gallery-card kg-width-wide">
<div class="kg-gallery-container">
<div class="kg-gallery-row">
<div class="kg-gallery-image"><a href="https://kopfkinok3.github.io/SkillCMS/assets/images/JJJJ/MM/bild1.jpg"><img src="https://kopfkinok3.github.io/SkillCMS/assets/images/JJJJ/MM/bild1.jpg" alt="Bildbeschreibung"></a></div>
<div class="kg-gallery-image"><a href="https://kopfkinok3.github.io/SkillCMS/assets/images/JJJJ/MM/bild2.jpg"><img src="https://kopfkinok3.github.io/SkillCMS/assets/images/JJJJ/MM/bild2.jpg" alt="Bildbeschreibung"></a></div>
</div>
</div>
</div>
-->


## Fazit

[1–2 Absätze: Zusammenfassung der Kernaussagen + konkreter nächster Schritt für den Leser]

[Optional: Link zu weiterführendem Artikel oder Kontakt]

---
*[Meine Liebe zu Tolkien, Teil 1](https://visales.de/...) — [Kurzbeschreibung verwandter Artikel]*
<!-- Verwandte Artikel verlinken — optional, aber gut für Interlinking -->
