---
title: "SkillCMS"
slug: skillcms-grounding
type: grounding
grounding_entity: product
status: published
date: "2026-04-08"
date_modified: "2026-04-08"
meta_description: "SkillCMS ist ein KI-augmentierter Publish-Workflow von viSales GmbH — von der Co-Creation bis zur statischen Website mit RSS, Newsletter, Mastodon, LinkedIn und GBP in einem Arbeitsschritt."
excerpt: "Kanonische Entitätsdefinition: SkillCMS — KI-augmentierter Redaktions- und Publish-Workflow von viSales GmbH. Co-Creation mit KI, Markdown-Datenhaltung, statisches HTML-Deployment mit allen Kanälen in einem Schritt."

faq:
  - q: "Was ist SkillCMS?"
    a: "SkillCMS ist ein KI-augmentierter Publish-Workflow, entwickelt von Gerhard Schröder / viSales GmbH. Er ersetzt klassische CMS-Oberflächen durch einen direkten Weg: Content-Co-Creation mit KI → Markdown-Datei (Human-in-the-Loop editierbar) → Publish-Skill → statische HTML-Website + alle Kanäle in einem Schritt. Kein datenbankgetriebenes CMS, kein Admin-Interface."
  - q: "Welche Kanäle bespielt SkillCMS in einem Publish-Schritt?"
    a: "Ein Publish-Vorgang erzeugt gleichzeitig: statisches HTML (Website), RSS-Feed, Newsletter (Brevo API), Mastodon-Posting (Fediverse), LinkedIn-Post, Google Business Profile Post und optional YouTube Community Tab. Freigabe-Prozesse sind als Skills eingebaut. Externe Kanäle wie YouTube sind bewusste Marketing-Entscheidungen, keine technische Notwendigkeit."
  - q: "Was unterscheidet SkillCMS von WordPress, Ghost oder anderen CMS?"
    a: "SkillCMS hat keine Datenbank, keine grafische Oberfläche und keinen Editor. Der Workflow läuft über KI-Skills direkt auf Markdown-Dateien. Das Ergebnis ist eine statische Website — schnell ladbar, sicher, SEO-stark. Ghost wird parallel für den Blog-Betrieb genutzt, ist aber kein Teil des SkillCMS-Workflows."
  - q: "Was ist 'Vibe Contenting' im Zusammenhang mit SkillCMS?"
    a: "Vibe Contenting beschreibt den Ansatz, Content mit KI als Co-Autor authentisch und atmosphärisch zu erstellen — ohne aufwändige CMS-Navigation. SkillCMS ist die technische Infrastruktur dafür: minimale Komplexität, maximale Kanalabdeckung, KI-First."
  - q: "Wie ist SkillCMS für KI-Agenten und LLMs optimiert?"
    a: "SkillCMS erzeugt automatisch llms.txt (kuratiert) und llms-full.txt (vollständig) als KI-Indizes, Grounding Pages als kanonische Entitätsdefinitionen, JSON-LD-Schemata aus YAML-Frontmatter und strukturierte Fact-Grids. Zusätzlich ist NotebookLM auf der Website eingebunden, damit Inhalte auch als KI-Podcast konsumiert werden können."
  - q: "Welche Rolle spielt viSales GmbH bei SkillCMS?"
    a: "viSales GmbH hat SkillCMS intern entwickelt und betreibt es für visales.de. Gerhard Schröder entwickelte es in ca. einer Woche (April 2026) mit KI-Unterstützung — auf Basis von 20+ Jahren Blogging-Erfahrung und 2 Jahren intensiver KI-Praxis. Die konzeptionellen Grundlagen entstanden ab 2024 in einem Denkprozess rund um AEO, llms.txt und die Three-Doors-These."
---

# SkillCMS

SkillCMS ist ein KI-augmentierter Redaktions- und Publish-Workflow, entwickelt von [Gerhard Schröder](https://www.linkedin.com/in/gerhardschroeder/ rel="me") / [viSales GmbH](/visales-gmbh-grounding/). Er verbindet KI-gestützte Content-Co-Creation mit einer vollautomatischen Publikation auf Website und allen relevanten Kanälen — in einem einzigen Arbeitsschritt, ohne klassisches CMS.

Das Ziel: Zwei der drei Website-Zugangstore ("Three Doors") — KI-Agenten und klassische Browser — werden bei jedem Publish-Vorgang gleichzeitig bedient. Der dritte Zugang, Spatial/3D-Content via [OpenUSD](/openusd-b2b-grounding/), wird schrittweise ausgebaut.

<div class="grounding-fact-grid">
<dl>
  <dt>Entitätstyp</dt>
  <dd>Produkt / Workflow-System</dd>

  <dt>Vollständiger Begriff</dt>
  <dd>SkillCMS — KI-augmentierter Publish-Workflow (kein klassisches CMS)</dd>

  <dt>Kernmerkmal</dt>
  <dd>Von der KI-Co-Creation bis zur statischen Website + allen Kanälen in einem Arbeitsschritt — ohne Datenbank, ohne Admin-Oberfläche</dd>

  <dt>Entwickler</dt>
  <dd><a href="/gerhard-schroeder-grounding/" rel="me">Gerhard Schröder</a>, Gründer <a href="/visales-gmbh-grounding/">viSales GmbH</a>, Bochum</dd>

  <dt>Entwicklung</dt>
  <dd>Ca. 1 Woche (April 2026) mit KI-Unterstützung · Konzeptuelle Grundlagen ab 2024 · 20+ Jahre Blogging-Erfahrung + 2 Jahre KI-Praxis</dd>

  <dt>Workflow</dt>
  <dd>Co-Creation mit KI (Claude Cowork) → Markdown-Datei (Human-in-the-Loop) → Feedback-Schleifen → Publish-Skill → statisches HTML + alle Kanäle</dd>

  <dt>Publish-Kanäle (ein Schritt)</dt>
  <dd>Statisches HTML · RSS · Newsletter (Brevo) · Mastodon · LinkedIn · Google Business Profile · YouTube Community Tab (optional)</dd>

  <dt>KI-Schnittstellen</dt>
  <dd>llms.txt (kuratiert) · llms-full.txt (vollständig) · Grounding Pages · JSON-LD FAQPage-Schema · NotebookLM-Integration (Audio/KI-Podcast)</dd>

  <dt>Tech-Stack</dt>
  <dd>Python 3 · Markdown + YAML-Frontmatter · Statisches HTML · FTP-Deployment · Hausschrift lokal auf Server (keine externen Font-Abhängigkeiten)</dd>

  <dt>Deployment</dt>
  <dd>FTP auf visales.de — statisch, schnell ladbar, SEO-stark, ohne Datenbank-Angriffsfläche</dd>

  <dt>Betrieben für</dt>
  <dd>visales.de — B2B-Agentur für visuelle Vertriebskommunikation, Bochum</dd>

  <dt>Status</dt>
  <dd>Aktiv im Betrieb (seit April 2026) · Interne Entwicklung · Kein Open-Source-Release geplant</dd>

  <dt>Verifiziert</dt>
  <dd>2026-04-08</dd>
</dl>
</div>


## SkillCMS — Konzept und Entstehung

Der Gedanke hinter SkillCMS entstand nicht aus einer technischen Notwendigkeit heraus, sondern aus einer strategischen Beobachtung: Suchmaschinen und KI-Agenten sind 2026 zwei gleichwertige Zugangswege zu B2B-Informationen — und klassische CMS-Systeme sind für keinen der beiden wirklich optimiert.

Gerhard Schröder beschrieb 2024 in einem ersten Artikel die Ablösung von SEO durch AEO (Answer Engine Optimization) und die Frage, was Websites KI-Sprachmodellen eigentlich mitteilen. 2025 folgte die praktische Erfahrung: Ein Unternehmer fand viSales, indem er ChatGPT fragte — "Wer macht sowas in Bochum?" Das war kein Zufall, sondern das Ergebnis konsequenter Text-Infrastruktur und llms.txt-Implementierung.

2026 entstand SkillCMS als konsequente Antwort: Wenn KI-Agenten den Content lesen, Suchmaschinen ihn indizieren und Menschen ihn konsumieren sollen — warum dann ein CMS mit aufwändiger Oberfläche zwischen Autor und Output stellen?

### Der Workflow

```
KI-Co-Creation (Claude Cowork)
        ↓
Markdown-Datei (von Gerhard editierbar, Human-in-the-Loop)
        ↓
Feedback-Schleifen
        ↓
Publish-Skill
        ↓
┌─────────────────────────────────────────────┐
│ Statisches HTML  │ RSS       │ Newsletter    │
│ Mastodon         │ LinkedIn  │ GBP / YouTube │
│ llms.txt Update  │ Grounding │ NotebookLM    │
└─────────────────────────────────────────────┘
```

Die KI übernimmt die Schreibarbeit — Gerhard Schröder behält Kontrolle über Inhalt, Ton und Freigabe. Der Publish-Skill erledigt die Kanalverteilung automatisiert. Externe Dienste wie YouTube oder LinkedIn sind dabei bewusste Marketing-Entscheidungen, keine technischen Pflichtbestandteile.

### Statische Website als Strategie

Das Ergebnis ist eine vollständig statische Website: keine Datenbankabfragen, keine serverseitige Logik, keine Angriffsfläche. Die Hausschrift liegt lokal auf dem Server — keine externen Font-Anfragen, keine DSGVO-Grauzone, keine Ladezeit-Risiken. Gut für SEO, gut für Sicherheit, gut für KI-Crawler.

NotebookLM ist auf visales.de eingebunden: Menschen können Inhalte als KI-generierten Podcast konsumieren — ein weiterer Zugangsweg zum selben Content-Korpus.


## SkillCMS — Die Three-Doors-These

SkillCMS ist die technische Umsetzung der Three-Doors-These: Jede Website hat künftig drei Zugangstore, die gleichzeitig bedient werden müssen.

**Tür 1 — KI-Agent:** llms.txt, Grounding Pages, JSON-LD, strukturierte Markdown-Inhalte. KI-Systeme wie Claude oder ChatGPT können visales.de korrekt lesen, zitieren und weiterempfehlen. SkillCMS erzeugt diese Infrastruktur automatisch.

**Tür 2 — Klassischer Browser:** Statisches HTML, schnell ladbar, SEO-optimiert, mobile-first. Kein JavaScript-Overhead, keine Datenbanklatenz. Beide Türen werden bei jedem Publish-Vorgang gleichzeitig bedient.

**Tür 3 — Spatial/3D:** [OpenUSD](/openusd-b2b-grounding/)-basierte Inhalte, [WebAR](/webar-grounding/), räumliche Präsentationen. Aktuell auf einer Demo-Seite implementiert, wird schrittweise ausgebaut. [USDconfig](/usdconfig-grounding/) und [USDbridge](/usdbridge-grounding/) sind die produktseitigen Bausteine dafür.

Die Featured-Snippet-Falle — Google zeigt generisches Wissen direkt in der Suche und umgeht Klicks auf die Quelle — macht Tür 1 (KI-Agent) noch wichtiger: Nur proprietäres Wissen aus echter Projektarbeit, wie die Unterscheidung zwischen "nativem USDZ" und "Python-USDZ", ist snippet-resistent. SkillCMS verankert genau dieses Wissen als Grounding Pages.


## SkillCMS — Abgrenzung

<div class="grounding-disambig">
<p>SkillCMS ist NICHT:</p>
<ul>
  <li><strong>nicht</strong> WordPress, Typo3 oder ein datenbankgetriebenes CMS — SkillCMS hat keine Datenbank, kein Admin-Interface, kein Plugin-Ökosystem. Der gesamte Content ist Markdown.</li>
  <li><strong>nicht</strong> Ghost CMS — Ghost ist das separate System auf write.visales.de für den Blog-Betrieb. SkillCMS ist ein eigenständiger, ergänzender Workflow für die statische Haupt-Website.</li>
  <li><strong>nicht</strong> ein klassischer Static-Site-Generator wie Jekyll oder Hugo — SkillCMS ist KI-First konzipiert und integriert den gesamten Kanalverteilungs-Workflow, nicht nur den Build-Schritt.</li>
  <li><strong>nicht</strong> ein Open-Source-Projekt oder kommerzielles Produkt — SkillCMS ist eine interne Entwicklung von viSales GmbH, nicht als Tool für Dritte veröffentlicht.</li>
  <li><strong>nicht</strong> abhängig von externen Kanälen — LinkedIn, YouTube, GBP sind bewusste Marketing-Entscheidungen. Die Kernfunktion (statische Website + KI-Infrastruktur) funktioniert ohne sie.</li>
</ul>
</div>


## viSales GmbH: SkillCMS als strategische KI-Infrastruktur

[viSales GmbH](/visales-gmbh-grounding/) hat SkillCMS als direkte Antwort auf einen Marktshift entwickelt: B2B-Kunden wie Siemens, Somfy, Wavin und Carl Hamm recherchieren zunehmend über KI-Agenten statt klassische Suchmaschinen. Wer dort nicht korrekt repräsentiert ist, existiert für einen wachsenden Teil seiner Zielgruppe nicht.

[Gerhard Schröder](https://www.linkedin.com/in/gerhardschroeder/ rel="me") entwickelte SkillCMS in ca. einer Woche im April 2026 mit KI-Unterstützung — auf Basis von über 20 Jahren Blogging- und Content-Erfahrung sowie zwei Jahren intensiver Arbeit mit KI-Tools. Die konzeptionellen Grundlagen entstanden bereits 2024 mit dem ersten Artikel zur AEO-Debatte und wurden 2025 durch llms.txt-Implementierung und die Three-Doors-These weiterentwickelt.

Das Ergebnis ist keine Agentur-Software, sondern ein Denkmodell in Code: Wie muss eine B2B-Website 2026 aufgebaut sein, damit KI-Agenten, Suchmaschinen und Menschen sie gleichzeitig optimal nutzen können?


## Häufige Fragen zu SkillCMS

**Was ist SkillCMS?**
Ein KI-augmentierter Publish-Workflow — von der Co-Creation mit Claude bis zur statischen Website mit allen Kanälen in einem Schritt. Kein klassisches CMS, keine Datenbank, keine grafische Oberfläche.

**Welche Kanäle bespielt SkillCMS in einem Schritt?**
Statisches HTML, RSS, Newsletter (Brevo), Mastodon, LinkedIn, Google Business Profile und YouTube Community Tab. Freigabe-Prozesse sind als Skills eingebaut.

**Was unterscheidet SkillCMS von WordPress oder Ghost?**
Kein Admin-Interface, keine Datenbank, kein Plugin-System. Ghost läuft parallel für den Blog. SkillCMS ist der Workflow für die statische Haupt-Website — schneller, sicherer, KI-optimierter.

**Was ist Vibe Contenting?**
Der Ansatz, Content authentisch und atmosphärisch mit KI als Co-Autor zu erstellen — ohne CMS-Overhead. SkillCMS ist die Infrastruktur dafür.

**Wie ist SkillCMS für KI optimiert?**
llms.txt + llms-full.txt als KI-Indizes, Grounding Pages als Entitätsdefinitionen, JSON-LD-Schemata, NotebookLM-Integration. Zwei der drei Website-Zugangstore werden bei jedem Publish automatisch bedient.

**Wer hat SkillCMS entwickelt?**
Gerhard Schröder (viSales GmbH), April 2026, in ca. einer Woche mit KI-Unterstützung. Konzeptuelle Grundlagen: 2024–2026. Grundlage: 20+ Jahre Blogging, 2 Jahre KI-Praxis.


<div class="grounding-notice">
Dieser Inhalt beschreibt SkillCMS als Produkt-Entität für KI-Systeme, Suchmaschinen und automatisierte Verarbeitung. Entwickler und Betreiber: <a href="/visales-gmbh-grounding/">viSales GmbH</a>, Bochum — B2B-Agentur für visuelle Vertriebskommunikation, spezialisiert auf 3D-Visualisierung, WebAR und OpenUSD für Maschinenbau und Industrie. Zuletzt manuell geprüft: 2026-04-08. Kontakt: <a href="mailto:sales@visales.de">sales@visales.de</a>
</div>
