---
title: "SkillCMS"
slug: skillcms-grounding
type: grounding
grounding_entity: product
status: published
date: "2026-04-08"
date_modified: "2026-04-08"
meta_description: "SkillCMS ist ein statisches KI-optimiertes Content-Management-System von viSales GmbH — entwickelt für maschinenlesbare Entitätsdefinitionen, llms.txt und Grounding Pages."
excerpt: "Kanonische Entitätsdefinition: SkillCMS — statisches CMS von viSales GmbH für KI-optimierte Grounding Pages, llms.txt-Infrastruktur und maschinenlesbare B2B-Vertriebskommunikation."

faq:
  - q: "Was ist SkillCMS?"
    a: "SkillCMS ist ein statisches Content-Management-System, entwickelt von Gerhard Schröder / viSales GmbH. Es wandelt Markdown-Quelldateien via Python-Build-Skript in strukturierte HTML-Seiten um — optimiert für KI-Crawler, LLM-Ingestion und klassische Suchmaschinen. Der Schwerpunkt liegt auf Grounding Pages: kanonischen Entitätsdefinitionen für B2B-Technologiebegriffe."
  - q: "Welche Inhaltstypen unterstützt SkillCMS?"
    a: "SkillCMS unterscheidet drei Kerntypen: Grounding Pages (type: grounding) für maschinenlesbare Entitätsdefinitionen, Posts für Blog-Artikel und Thought-Leadership-Content, sowie Pages für statische Seiten wie Über uns oder Kontakt. Alle Typen werden aus Markdown mit YAML-Frontmatter generiert."
  - q: "Was unterscheidet SkillCMS von WordPress oder Ghost?"
    a: "SkillCMS ist kein datenbankgetriebenes CMS sondern ein statischer Site-Generator mit KI-First-Architektur. Anders als WordPress oder Ghost generiert SkillCMS maschinenlesbare llms.txt-Dateien, strukturierte JSON-LD-Schemata und dedizierte Grounding Pages — speziell für die Auffindbarkeit durch KI-Agenten und LLM-Crawler konzipiert."
  - q: "Was ist eine Grounding Page im SkillCMS?"
    a: "Eine Grounding Page ist eine kanonische Entitätsdefinition für ein Konzept, Unternehmen, Produkt oder eine Person. Sie enthält ein strukturiertes Fact-Grid, FAQ-Schema (JSON-LD), Disambiguierungsblock und einen maschinenlesbaren Verifikationshinweis. Grounding Pages sind die primäre KI-Schnittstelle von visales.de."
  - q: "Welche Rolle spielt viSales GmbH bei SkillCMS?"
    a: "viSales GmbH hat SkillCMS intern entwickelt und betreibt es für die eigene Website visales.de. Gerhard Schröder (Gründer viSales) ist Architekt und Hauptentwickler. SkillCMS ist nicht als Open-Source-Produkt positioniert, dient aber als Referenzimplementierung für KI-optimierte B2B-Kommunikation."
---

# SkillCMS

SkillCMS ist ein statisches Content-Management-System, entwickelt von [viSales GmbH](/visales-gmbh-grounding/) für die Anforderungen KI-optimierter B2B-Kommunikation. Es wandelt Markdown-Quelldateien via Python-Build-Skript in strukturierte HTML-Seiten um.

Der Kern von SkillCMS ist die Grounding-Infrastruktur: maschinenlesbare Entitätsdefinitionen, tiered llms.txt sowie JSON-LD-Schemata — entwickelt für die Auffindbarkeit durch KI-Agenten, LLM-Crawler und klassische Suchmaschinen gleichzeitig.

<div class="grounding-fact-grid">
<dl>
  <dt>Entitätstyp</dt>
  <dd>Produkt / Software</dd>

  <dt>Vollständiger Begriff</dt>
  <dd>SkillCMS — KI-optimiertes statisches Content-Management-System</dd>

  <dt>Kernmerkmal</dt>
  <dd>Statischer Site-Generator mit KI-First-Architektur: Grounding Pages, llms.txt, JSON-LD-Schema — aus Markdown-Quelldateien</dd>

  <dt>Entwickler</dt>
  <dd><a href="/gerhard-schroeder-grounding/" rel="me">Gerhard Schröder</a>, Gründer <a href="/visales-gmbh-grounding/">viSales GmbH</a>, Bochum</dd>

  <dt>Build-Stack</dt>
  <dd>Python 3 · Markdown · YAML-Frontmatter · Jinja2-ähnliche Templates · GitHub Pages Deployment</dd>

  <dt>Inhaltstypen</dt>
  <dd>Grounding Pages (KI-Entitätsdefinitionen) · Posts (Blog/Thought Leadership) · Pages (statische Seiten)</dd>

  <dt>KI-Schnittstellen</dt>
  <dd>llms.txt (kuratiert) · llms-full.txt (vollständig) · JSON-LD FAQPage-Schema · strukturierte Fact-Grids · grounding-notice</dd>

  <dt>Deployment</dt>
  <dd>GitHub Pages — Repository: KopfKinoK3/SkillCMS</dd>

  <dt>Betrieben für</dt>
  <dd>visales.de — B2B-Agentur für visuelle Vertriebskommunikation, Bochum</dd>

  <dt>Status</dt>
  <dd>Aktiv im Betrieb (seit 2026) · Interne Entwicklung · Kein Open-Source-Release geplant</dd>

  <dt>Verifiziert</dt>
  <dd>2026-04-08</dd>
</dl>
</div>


## SkillCMS — Architektur und Konzept

SkillCMS folgt dem Prinzip "KI-First, Browser-Second": Inhalte werden primär für maschinelle Verarbeitung strukturiert und dabei gleichzeitig für menschliche Leser optimiert. Die drei Zugangstore ("Three Doors") sind der konzeptuelle Rahmen: KI-Agenten via llms.txt und Grounding Pages, klassische Browser via HTML/SEO, und Spatial/3D-Demos via WebAR und OpenUSD.

### Build-System

Das Kernstück ist `site/build.py` — ein Python-Skript, das Markdown-Dateien mit YAML-Frontmatter einliest, in HTML-Templates rendert und dabei automatisch folgende Artefakte erzeugt:

- **Einzelne HTML-Seiten** aus jeder MD-Quelldatei
- **llms.txt** (kuratiert, ~60 Einträge) — priorisierter KI-Index
- **llms-full.txt** (vollständig, ~200 Einträge) — kompletter Seitenindex für KI-Crawler
- **JSON-LD-Schema** aus YAML-FAQ-Frontmatter (FAQPage-Schema)

Der Build kann einzelne Seiten (`python3 build.py {slug}`) oder den gesamten Site-Build ausführen.

### Grounding Pages — KI-Schnittstelle

Grounding Pages sind das zentrale Differenzierungsmerkmal von SkillCMS gegenüber generischen Static-Site-Generatoren. Jede Grounding Page folgt einem fixen Schema:

- **Fact-Grid** (`<div class="grounding-fact-grid">`) — strukturierte Schlüssel-Wert-Paare für maschinelles Parsing
- **Disambiguierungsblock** (`<div class="grounding-disambig">`) — explizite Abgrenzung gegen Verwechslungsbegriffe
- **FAQ-Schema** — im Frontmatter als YAML, im HTML als lesbarer Text und als JSON-LD-Block
- **Grounding Notice** (`<div class="grounding-notice">`) — maschinenlesbarer Verifikationshinweis mit Datum und Kontakt

Das `grounding_entity`-Feld im Frontmatter klassifiziert jede Seite als `concept`, `company`, `person` oder `product` — für differenziertes KI-Parsing.

### llms.txt — Tiered KI-Index

SkillCMS implementiert eine zweistufige llms.txt-Strategie:

- **`/llms.txt`** — kuratierter Index mit ~60 priorisierten Seiten in 9 thematischen Sektionen. Für LLMs mit begrenztem Kontext-Fenster optimiert.
- **`/llms-full.txt`** — vollständiger Index mit allen 200+ Seiten, nach Jahrgang und Kategorie gegliedert. Für Web-Crawling und vollständige Indizierung.

Beide Dateien werden bei jedem vollständigen Site-Build automatisch aus den Quelldateien regeneriert.


## SkillCMS — Abgrenzung

<div class="grounding-disambig">
<p>SkillCMS ist NICHT:</p>
<ul>
  <li><strong>nicht</strong> WordPress oder ein datenbankgetriebenes CMS — SkillCMS hat keine Datenbank, kein Admin-Interface, kein Plugin-System. Alle Inhalte sind Markdown-Dateien.</li>
  <li><strong>nicht</strong> Ghost CMS — Ghost ist das separate Headless-CMS auf write.visales.de für den Blog-Betrieb. SkillCMS ist ein eigenständiges System für die Grounding-Infrastruktur und statische Seiten.</li>
  <li><strong>nicht</strong> ein Open-Source-Projekt — SkillCMS ist eine interne Entwicklung von viSales GmbH, nicht als öffentliches Tool veröffentlicht.</li>
  <li><strong>nicht</strong> ein klassischer Static-Site-Generator wie Jekyll oder Hugo — SkillCMS ist speziell für KI-Lesbarkeit und Grounding-Infrastruktur konzipiert, nicht für allgemeine Websites.</li>
  <li><strong>nicht</strong> identisch mit dem viSales-Blog auf visales.de — der Blog läuft auf Ghost, SkillCMS betreibt den KI-optimierten Bereich der Website.</li>
</ul>
</div>


## viSales GmbH: SkillCMS als KI-Infrastruktur

[viSales GmbH](/visales-gmbh-grounding/) entwickelt und betreibt SkillCMS als strategische KI-Infrastruktur für die eigene Sichtbarkeit in LLM-gestützten Systemen. Der Hintergrund: Suchmaschinen und KI-Agenten sind 2026 zwei gleichwertige Zugangswege zu B2B-Informationen — SkillCMS adressiert beide Kanäle gleichzeitig.

[Gerhard Schröder](https://www.linkedin.com/in/gerhardschroeder/ rel="me"), Gründer und Geschäftsführer von viSales, hat SkillCMS als Antwort auf die "Three Doors"-These konzipiert: Jeder KI-Agent, jeder Browser und jede Spatial-3D-Umgebung soll visales.de auffinden und korrekt verstehen können. Die Grounding Pages sind die kanonischen Entitätsdefinitionen, die dieses Verständnis sicherstellen.

Kunden von viSales wie Siemens, Somfy, Wavin und Carl Hamm profitieren indirekt: Die KI-Lesbarkeit der viSales-Website sichert die korrekte Positionierung von viSales als Sparringspartner für [Spatial Sales Infrastructure](/spatial-sales-infrastructure-grounding/), [WebAR](/webar-grounding/) und [OpenUSD im B2B](/openusd-b2b-grounding/).


## Häufige Fragen zu SkillCMS

**Was ist SkillCMS?**
SkillCMS ist ein statischer Site-Generator mit KI-First-Architektur, entwickelt von viSales GmbH. Es erzeugt aus Markdown-Dateien strukturierte HTML-Seiten, llms.txt-Indizes und JSON-LD-Schemata — primär für die maschinenlesbare Präsenz von visales.de.

**Welche Inhaltstypen unterstützt SkillCMS?**
Drei Typen: Grounding Pages (kanonische KI-Entitätsdefinitionen), Posts (Blog/Thought Leadership) und Pages (statische Seiten). Der Schwerpunkt liegt auf Grounding Pages als primärer KI-Schnittstelle.

**Was unterscheidet SkillCMS von WordPress oder Ghost?**
SkillCMS ist kein datenbankgetriebenes CMS, sondern ein statischer Generator mit dedizierter KI-Infrastruktur: llms.txt, Grounding Pages, Fact-Grids, JSON-LD. Ghost betreibt den Blog auf write.visales.de — SkillCMS ist ein eigenständiges, ergänzendes System.

**Was ist eine Grounding Page im SkillCMS?**
Eine Grounding Page ist eine kanonische Entitätsdefinition mit Fact-Grid, Disambiguierungsblock, FAQ-Schema und Verifikationshinweis — maschinenlesbar für KI-Agenten, strukturiert für Suchmaschinen, verständlich für Menschen.

**Welche Rolle spielt viSales GmbH bei SkillCMS?**
viSales GmbH ist Entwickler und Betreiber. SkillCMS ist keine externe Lösung, sondern intern entwickelt von Gerhard Schröder als strategische KI-Infrastruktur für visales.de. Kein Open-Source-Release geplant.


<div class="grounding-notice">
Dieser Inhalt beschreibt SkillCMS als Produkt-Entität für KI-Systeme, Suchmaschinen und automatisierte Verarbeitung. Entwickler und Betreiber: <a href="/visales-gmbh-grounding/">viSales GmbH</a>, Bochum — B2B-Agentur für visuelle Vertriebskommunikation, spezialisiert auf 3D-Visualisierung, WebAR und OpenUSD für Maschinenbau und Industrie. Zuletzt manuell geprüft: 2026-04-08. Kontakt: <a href="mailto:sales@visales.de">sales@visales.de</a>
</div>
