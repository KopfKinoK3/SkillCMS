---
# ============================================================
# PAGE TEMPLATE — viSales SkillCMS
# Kopieren, umbenennen, alle PLATZHALTER ersetzen.
# Dateiname: {slug}.md → Ablage: site/content/pages/
# ============================================================

title: "SEITENTITEL"
# H1 + <title>-Tag. Max. ~60 Zeichen.

slug: seiten-slug
# URL-Pfad: kebab-case — z.B. "leistungen", "ueber-uns", "fallbeispiele"

type: page
# NICHT ÄNDERN
# Erlaubte Werte: page | listing | home
#   page     — Standard-Textseite (Kontakt, Über Uns, Leistungen, Impressum)
#   listing  — Übersichtsseite mit Card-Grid (Tag-Listings, Artikel-Übersicht)
#   home     — Startseite (eigenes Layout, D0.6 — noch in Entwicklung)

status: published
# published | draft

date: "2026-04-07"
# Erstell-Datum ISO — in Anführungszeichen!

date_modified: "2026-04-07"
# Letztes Änderungsdatum

meta_description: "BESCHREIBUNG DER SEITE IN 1–2 SÄTZEN."
# Max. 160 Zeichen. Outcome-orientiert.
# Was bekommt/erfährt der Besucher auf dieser Seite?

excerpt: "KURZBESCHREIBUNG FÜR llms.txt."
# 1 Satz. Wird in llms.txt verwendet.
# Optional bei reinen Service-Seiten (Impressum, Datenschutz).

# feature_image: https://kopfkinok3.github.io/SkillCMS/assets/images/JJJJ/MM/bild.jpg
# Optional — nur wenn die Seite ein Hero-Bild hat
# Bei Standard-Pages (Kontakt, Impressum) weglassen

# keywords: "keyword1, keyword2"
# Optional — nur für SEO-relevante Seiten sinnvoll
---

<!-- ============================================================ -->
<!-- INTRO / LEAD                                                  -->
<!-- 1–2 Sätze: Was bekommt der Besucher hier?                    -->
<!-- Bei Kontakt/CTA-Seiten: direkt zum Punkt                     -->
<!-- ============================================================ -->

> [Optional: Blockquote als zentrales Versprechen oder Leitmotiv]

[Einleitungstext — was erwartet den Besucher? Direkt und klar.]


## [H2: Erster Abschnitt]

[Text. Für Seiten wie "Leistungen": Hier kommt die Leistungsbeschreibung.]
[Für "Über Uns": Firmengeschichte, Team, Positionierung.]
[Für "Kontakt": Warum Termin buchen, was passiert beim Erstgespräch.]


## [H2: Zweiter Abschnitt — optional]

[Text]

<!-- CTA-Block (optional) — für Seiten mit Conversion-Ziel: -->
<!--
<div class="gh-content">
<a href="/kontakt/" class="gh-button">Termin buchen</a>
</div>
-->


## [H2: Weiterer Abschnitt — optional]

[Text]

<!-- ============================================================ -->
<!-- HINWEISE FÜR SPEZIELLE PAGE-TYPEN:                          -->
<!--                                                              -->
<!-- LEISTUNGEN: H2 pro Leistung, je 2–3 Absätze                 -->
<!-- ÜBER UNS: Geschichte → Team → Positionierung → Kunden        -->
<!-- FALLBEISPIELE: type: listing verwenden (Card-Grid)           -->
<!-- KONTAKT: Kurz halten, CTA prominent, kein langer Text        -->
<!-- IMPRESSUM/DATENSCHUTZ: Nur Pflichttext, kein excerpt nötig   -->
<!-- ============================================================ -->
