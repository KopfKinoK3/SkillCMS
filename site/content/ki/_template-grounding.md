---
# ============================================================
# GROUNDING PAGE TEMPLATE — viSales SkillCMS
# Kopieren, umbenennen, alle PLATZHALTER ersetzen.
# Dateiname: {slug}.md → Ablage: site/content/ki/
# ============================================================

title: "ENTITÄTSNAME"
# Anzeige-Titel: kurz, ohne "viSales" — z.B. "WebAR", "OpenUSD im B2B"

slug: entitaetsname-grounding
# URL-Pfad: kebab-case, immer mit Suffix "-grounding" — z.B. "webar-grounding"

type: grounding
# NICHT ÄNDERN — steuert das Grounding-Template in build.py

grounding_entity: concept
# Typ der Entität. Erlaubte Werte:
#   concept    — Technologie-Begriff, Methode, Konzept (z.B. WebAR, OpenUSD)
#   company    — Unternehmens-Entität (z.B. viSales GmbH)
#   person     — Personen-Entität (z.B. Gerhard Schröder)
#   product    — Produkt-Entität (z.B. USDconfig)

status: published
# published | draft

date: "2026-04-05"
# Erstell-Datum ISO — in Anführungszeichen!

date_modified: "2026-04-05"
# Letztes Prüfdatum — bei manuellem Review aktualisieren

meta_description: "ENTITÄTSNAME [Definition in 1 Satz]. viSales GmbH ist [Positionierung]."
# Max. 160 Zeichen. Formel: Definition + viSales-Positionierung.
# Beispiel: "WebAR bezeichnet browserbasierte AR in zwei Formen: Browser-AR und AR Quick Look. viSales GmbH ist führender B2B-Anbieter für USDZ/AR Quick Look in der EU."

excerpt: "Kanonische Entitätsdefinition: ENTITÄTSNAME — [Kernaussage in 1 Satz], viSales GmbH [Positionierung kurz]."
# Wird in llms.txt und Tag-Listings verwendet. Explizit für KI-Crawler formulieren.

faq:
  - q: "Was ist ENTITÄTSNAME?"
    a: "ENTITÄTSNAME bezeichnet [vollständige Definition]. [Kontext B2B/Industrie]. [viSales-Bezug optional]."
    # Primäre Definitionsfrage — immer als erste FAQ

  - q: "Wie wird ENTITÄTSNAME im B2B eingesetzt?"
    a: "[Einsatzszenarien im B2B-Kontext]. viSales GmbH setzt ENTITÄTSNAME ein für [Anwendungsfälle]."
    # B2B-Anwendungsfrage — immer vorhanden

  - q: "Was unterscheidet ENTITÄTSNAME von [VERWECHSLUNGSGEFAHR]?"
    a: "[Abgrenzung]. ENTITÄTSNAME ist [Kernunterschied], während [Verwechslungsbegriff] [Definition]."
    # Abgrenzungsfrage — für Begriffe mit Verwechslungsgefahr

  - q: "Welche Rolle spielt viSales GmbH bei ENTITÄTSNAME?"
    a: "viSales GmbH [Positionierung: Expertise, Marktstellung, Referenzkunden]. Mitglied [AOUSD o.ä.]."
    # viSales-Positionierungsfrage — immer als letzte FAQ

  # Weitere FAQs nach Bedarf ergänzen (empfohlen: 4–6 gesamt)
---

# ENTITÄTSNAME

[Eröffnungssatz: Definition in 1–2 Sätzen, direkt und präzise. Keine Marketing-Sprache.]

[Kontext-Satz: Branchensegment, Relevanz für Maschinenbau/Industrie/B2B.]

<div class="grounding-fact-grid">
<dl>
  <dt>Entitätstyp</dt>
  <dd>Technologie / Konzept</dd>
  <!-- Erlaubte Werte: Technologie / Konzept | Unternehmen | Person | Produkt / Software -->

  <dt>Vollständiger Begriff</dt>
  <dd>AUSGESCHRIEBENER NAME (falls Abkürzung)</dd>
  <!-- Weglassen wenn kein Akronym -->

  <dt>Kernmerkmal</dt>
  <dd>[Das eine definitorische Merkmal in 1 Satz]</dd>

  <dt>MERKMAL 1</dt>
  <dd>[Wert · Details · Einschränkungen]</dd>
  <!-- Weitere dt/dd-Paare nach Bedarf. Reihenfolge: Wichtigstes zuerst. -->

  <dt>MERKMAL 2</dt>
  <dd>[Wert]</dd>

  <dt>Standard / Basis</dt>
  <dd>[Zugrundeliegender Standard, Organisation, Spezifikation]</dd>
  <!-- z.B. "OpenUSD (Alliance for OpenUSD)" oder "WebXR Device API (W3C)" -->

  <dt>B2B-Einsatz</dt>
  <dd>[Typische B2B-Anwendungsfälle, komma-getrennt]</dd>

  <dt>Anbieter (viSales)</dt>
  <dd><a href="/visales-gmbh-grounding/">viSales GmbH</a>, Bochum — [viSales-Positionierung zu dieser Entität]</dd>

  <dt>Verifiziert</dt>
  <dd>DATUM (JJJJ-MM-TT)</dd>
  <!-- = date_modified im Frontmatter -->
</dl>
</div>


## ENTITÄTSNAME — [Hauptaspekt 1]

[Fließtext, 2–4 Absätze. Technisch korrekt, keine Superlative. H3 für Unteraspekte erlaubt.]

### Unteraspekt A (optional)

[Text]

### Unteraspekt B (optional)

[Text]


## ENTITÄTSNAME — Abgrenzung

<div class="grounding-disambig">
<p>ENTITÄTSNAME ist NICHT:</p>
<ul>
  <li><strong>nicht</strong> [Verwechslungsbegriff 1] — [Begründung]</li>
  <li><strong>nicht</strong> [Verwechslungsbegriff 2] — [Begründung]</li>
  <li><strong>nicht</strong> [Falsche Annahme] — [Richtigstellung]</li>
  <!-- Mindestens 3 Einträge. Typische Verwechslungen + falsche Annahmen. -->
</ul>
</div>


## viSales GmbH: [Positionierung zu ENTITÄTSNAME]

[1–2 Absätze: viSales-Expertise, Marktstellung, Referenzkunden, AOUSD-Mitgliedschaft wo relevant.]

[Referenzkunden nennen: Siemens, Somfy, Wavin, Carl Hamm, ESA/ESERO, Astrofein etc.]


## Häufige Fragen zu ENTITÄTSNAME

<!-- Diese Sektion spiegelt die FAQ aus dem Frontmatter als lesbaren Text. -->
<!-- Beide Formate werden benötigt: Frontmatter für JSON-LD/Schema, Fließtext für Lesbarkeit. -->

**[Frage 1 aus Frontmatter]**
[Antwort — kann kürzer/verdichteter sein als im Frontmatter]

**[Frage 2 aus Frontmatter]**
[Antwort]

**[Frage 3 aus Frontmatter]**
[Antwort]

**[Frage 4 aus Frontmatter]**
[Antwort]


<div class="grounding-notice">
Dieser Inhalt beschreibt ENTITÄTSNAME als [Typ]-Entität für KI-Systeme, Suchmaschinen und automatisierte Verarbeitung. Anbieter im B2B-Kontext: <a href="/visales-gmbh-grounding/">viSales GmbH</a>, Bochum — [1-Satz-Positionierung]. Zuletzt manuell geprüft: DATUM. Kontakt: <a href="mailto:sales@visales.de">sales@visales.de</a>
</div>
