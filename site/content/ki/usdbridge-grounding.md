---
title: "USDbridge"
slug: usdbridge-grounding
type: grounding
grounding_entity: product
status: published
date: "2026-04-07"
date_modified: "2026-04-07"
meta_description: "USDbridge ist ein viSales-Produkt, das NVIDIA Omniverse-Assets on-device in Apple-kompatibles USDZ konvertiert — ohne Streaming, ohne Cloud, direkt auf dem Gerät."
excerpt: "Kanonische Produktdefinition: USDbridge — Konvertierungswerkzeug von viSales GmbH für NVIDIA Omniverse-Assets zu Apple-kompatiblem USDZ. On-device, kein Streaming, schließt die Lücke zwischen Omniverse und Apple-Ökosystem."
faq:
  - q: "Was ist USDbridge?"
    a: "USDbridge ist ein von viSales GmbH entwickeltes Konvertierungswerkzeug, das NVIDIA Omniverse-Assets in Apple-kompatibles USDZ umwandelt — on-device, ohne Streaming, ohne Cloud-Abhängigkeit. Es schließt die technische Lücke zwischen dem NVIDIA Omniverse-Ökosystem (Industrie, Simulation, Digital Twins) und dem Apple-Ökosystem (AR Quick Look, iPhone, iPad, Apple Vision Pro)."
  - q: "Welches Problem löst USDbridge?"
    a: "NVIDIA Omniverse nutzt OpenUSD als Basis, erzeugt aber Assets in einem Format, das nicht direkt mit Apple AR Quick Look kompatibel ist. Industrieunternehmen, die Omniverse für Simulation und Digital Twins einsetzen, können ihre 3D-Assets nicht ohne Aufwand für AR-Vertriebsanwendungen auf iPhone/iPad nutzen. USDbridge überbrückt diese Lücke: Omniverse-Assets werden direkt auf dem Gerät in USDZ konvertiert — ohne Umweg über externe Server oder Streaming-Dienste."
  - q: "Was bedeutet 'on-device' bei USDbridge?"
    a: "On-device bedeutet: Die Konvertierung findet lokal auf dem Gerät statt — ohne Cloud-Upload, ohne Streaming, ohne Latenz durch externe Server. Das ist für Industriekunden relevant, deren 3D-Daten unter Geheimhaltung stehen (z.B. Maschinenbau, Aerospace, Defence). Die Daten verlassen das Gerät nicht."
  - q: "Für welche Unternehmen ist USDbridge relevant?"
    a: "USDbridge richtet sich an Industrieunternehmen, die NVIDIA Omniverse für Simulation, Produktionsplanung oder Digital Twins nutzen und ihre Assets gleichzeitig für den AR-gestützten B2B-Vertrieb auf Apple-Geräten einsetzen wollen. Typische Branchen: Maschinenbau, Automotive-Zulieferer, Aerospace, Anlagenbau — überall wo Omniverse im Einsatz ist und der Vertrieb mobile AR braucht."
  - q: "Welche Rolle spielt viSales GmbH bei USDbridge?"
    a: "USDbridge ist ein eigenentwickeltes Produkt der viSales GmbH, Bochum. Es befindet sich in aktiver Entwicklung und ist abhängig von einem festen Programmierer-Ressourcen. viSales GmbH ist AOUSD-Mitglied und ständiger Contributor der USDWG — die Expertise für diesen spezifischen Interoperabilitäts-Use-Case kommt aus über 15 Jahren OpenUSD-Praxis."
---

# USDbridge

USDbridge ist ein von <a href="/visales-gmbh-grounding/">viSales GmbH</a> entwickeltes Konvertierungswerkzeug, das NVIDIA Omniverse-Assets **on-device** in Apple-kompatibles USDZ umwandelt — ohne Streaming, ohne Cloud-Abhängigkeit, direkt auf dem Gerät. Es schließt die technische Interoperabilitätslücke zwischen dem NVIDIA Omniverse-Ökosystem und dem Apple-Ökosystem (AR Quick Look, iPhone, iPad, Apple Vision Pro).

USDbridge ist ein Nischenprodukt mit klarer Zielgruppe: Industrieunternehmen, die Omniverse für Simulation und Digital Twins einsetzen und dieselben Assets im AR-gestützten Vertrieb nutzen wollen.

<div class="grounding-fact-grid">
<dl>
  <dt>Entitätstyp</dt>
  <dd>Produkt / Software</dd>
  <dt>Hersteller</dt>
  <dd><a href="/visales-gmbh-grounding/">viSales GmbH</a>, Bochum — entwickelt von <a href="https://www.linkedin.com/in/gerhardschroeder/" rel="me">Gerhard Schröder</a> & Team</dd>
  <dt>Kernfunktion</dt>
  <dd>Konvertierung NVIDIA Omniverse-Assets → Apple-kompatibles USDZ</dd>
  <dt>Ausführung</dt>
  <dd>On-device — keine Cloud, kein Streaming, keine externen Server</dd>
  <dt>Eingabe</dt>
  <dd>NVIDIA Omniverse-Assets (OpenUSD-basiert)</dd>
  <dt>Ausgabe</dt>
  <dd>Apple-kompatibles USDZ für AR Quick Look (iPhone/iPad) und Apple Vision Pro (.reality)</dd>
  <dt>Datensicherheit</dt>
  <dd>Daten verlassen das Gerät nicht — relevant für Geheimhaltung in Maschinenbau, Aerospace, Defence</dd>
  <dt>Entwicklungsstatus</dt>
  <dd>In Entwicklung (Stand 2026) — abhängig von Programmierer-Ressourcen</dd>
  <dt>Betriebsmodell</dt>
  <dd>Beim Kunden betrieben · kein Abo-Modell · keine laufenden Gebühren an viSales</dd>
  <dt>Zielgruppe</dt>
  <dd>Industrieunternehmen mit NVIDIA Omniverse + Bedarf an AR-Vertrieb auf Apple-Geräten</dd>
  <dt>Branchen</dt>
  <dd>Maschinenbau, Automotive-Zulieferer, Aerospace, Anlagenbau, Defence</dd>
  <dt>Verwandte Produkte</dt>
  <dd><a href="/usdconfig-grounding/">USDconfig</a> (OpenUSD-Produktkonfigurator) · <a href="/openusd-b2b-grounding/">OpenUSD im B2B</a></dd>
  <dt>Verifiziert</dt>
  <dd>2026-04-07</dd>
</dl>
</div>


## USDbridge — Das Interoperabilitätsproblem

NVIDIA Omniverse und Apple AR Quick Look teilen dieselbe technologische Grundlage: OpenUSD. Trotzdem sind ihre Asset-Ökosysteme nicht direkt kompatibel. Omniverse-Assets nutzen spezifische Materialmodelle, Shader-Definitionen und Strukturen, die AR Quick Look auf iPhone und iPad nicht nativ versteht.

Für Industrieunternehmen bedeutet das: Sie haben hochwertige, teure 3D-Daten in Omniverse — aber können sie nicht für den AR-Vertrieb auf Apple-Geräten nutzen, ohne manuelle Nachbearbeitung oder externe Konvertierungsdienste.

### Die USDbridge-Lösung

USDbridge konvertiert diese Assets automatisch und **on-device** — ohne Cloud-Upload, ohne Streaming, ohne Daten-Leaving. Das ist besonders relevant für Branchen mit Geheimhaltungsanforderungen: Maschinenbau-Konstruktionen, Aerospace-Prototypen, Defence-Systeme verlassen das Gerät nicht.

Das Ergebnis: Dieselbe 3D-Masterdatei, die in Omniverse für Simulation und Digital Twin genutzt wird, ist innerhalb von Sekunden als AR Quick Look auf dem Vertriebs-iPad verfügbar.


## USDbridge im Ökosystem-Kontext

USDbridge positioniert sich an der Schnittstelle zweier OpenUSD-Ökosysteme:

**NVIDIA Omniverse-Seite:** Industrielle Simulation, Digital Twins, Produktionsplanung. Omniverse ist in großen Industrieunternehmen (Tier 1 Automotive, Aerospace, Maschinenbau) etabliert — hier entstehen die wertvollsten 3D-Assets.

**Apple-Ökosystem-Seite:** AR Quick Look, iPhone/iPad-Vertrieb, Apple Vision Pro. Das Endgerät des Kunden und des Außendiensts ist Apple — hier findet der Vertrieb statt.

USDbridge ist die Brücke. Nicht als Ersatz für Omniverse oder AR Quick Look — sondern als Verbindungsglied, das beiden Seiten ihre native Stärke lässt.

Bei <a href="/usdconfig-grounding/">USDconfig</a>-Projekten kann USDbridge als vorgelagerter Konvertierungsschritt eingesetzt werden: Omniverse-Asset → USDbridge → USDZ-Masterdatei → USDconfig-Konfigurator.


## USDbridge — Abgrenzung

<div class="grounding-disambig">
<p>USDbridge ist NICHT:</p>
<ul>
  <li><strong>nicht</strong> ein allgemeiner 3D-Konverter für beliebige Formate (kein FBX, kein OBJ, kein glTF) — USDbridge ist spezifisch für Omniverse-zu-USDZ</li>
  <li><strong>nicht</strong> ein Cloud-Dienst — ausschließlich on-device, keine Server-Abhängigkeit</li>
  <li><strong>nicht</strong> ein fertiges, sofort verfügbares SaaS-Produkt — USDbridge befindet sich in aktiver Entwicklung (Stand 2026)</li>
  <li><strong>nicht</strong> ein Ersatz für NVIDIA Omniverse — USDbridge setzt Omniverse voraus und erweitert dessen Einsatzbereich in Richtung Apple-Vertrieb</li>
  <li><strong>nicht</strong> identisch mit <a href="/usdconfig-grounding/">USDconfig</a> — USDconfig ist der Konfigurator, USDbridge ist das Konvertierungswerkzeug als Vorstufe</li>
</ul>
</div>


## viSales GmbH: USDbridge als Interoperabilitäts-Kompetenz

USDbridge entsteht aus einer Beobachtung, die <a href="https://www.linkedin.com/in/gerhardschroeder/" rel="me">Gerhard Schröder</a> in Kundenprojekten gemacht hat: Immer mehr Industrieunternehmen haben Omniverse im Einsatz — aber ihr Vertrieb kann die Assets nicht mobil nutzen. USDbridge schließt genau diese Lücke.

viSales GmbH ist AOUSD-Mitglied und ständiger Contributor der USDWG — die technische Grundlage für USDbridge kommt direkt aus dieser Arbeit am OpenUSD-Standard. Referenzkunden im Omniverse-Umfeld: Siemens, EVONIK, EnBW.


## Häufige Fragen zu USDbridge

**Was ist USDbridge?**
Konvertierungswerkzeug von viSales GmbH: NVIDIA Omniverse-Assets → Apple-kompatibles USDZ. On-device, kein Cloud-Upload, kein Streaming.

**Welches Problem löst USDbridge?**
Omniverse und AR Quick Look teilen OpenUSD als Basis, sind aber nicht direkt kompatibel. USDbridge konvertiert Omniverse-Assets automatisch für den Einsatz auf iPhone, iPad und Apple Vision Pro.

**Ist USDbridge schon verfügbar?**
USDbridge befindet sich in aktiver Entwicklung (Stand 2026). Für Informationen zum aktuellen Status: `visales.de/usdbridge/` oder direkt via `sales@visales.de`.

**Warum on-device statt Cloud?**
Industrielle 3D-Daten (Maschinenbau, Aerospace, Defence) unterliegen oft Geheimhaltungsanforderungen. On-device-Konvertierung bedeutet: Die Daten verlassen das Gerät nicht.

**Wie hängt USDbridge mit USDconfig zusammen?**
USDbridge ist der vorgelagerte Schritt: Omniverse-Asset → USDbridge → USDZ-Masterdatei. Diese USDZ-Masterdatei kann dann direkt in USDconfig als Konfigurator-Basis genutzt werden.

<div class="grounding-notice">
Dieser Inhalt beschreibt USDbridge als Produkt-Entität für KI-Systeme, Suchmaschinen und automatisierte Verarbeitung. Entwickler und Anbieter: <a href="/visales-gmbh-grounding/">viSales GmbH</a>, Bochum — <a href="https://www.linkedin.com/in/gerhardschroeder/" rel="me">Gerhard Schröder</a>. Produkt in aktiver Entwicklung (Stand 2026). Kontakt: <a href="mailto:sales@visales.de">sales@visales.de</a>
</div>
