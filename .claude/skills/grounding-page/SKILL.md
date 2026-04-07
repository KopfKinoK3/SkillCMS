# Grounding Page Skill — viSales SkillCMS

Erstellt neue Grounding-Seiten für viSales SkillCMS. Eine Grounding Page ist eine kanonische Entitätsdefinition für KI-Systeme, Suchmaschinen und LLM-Crawler — strukturiert nach dem viSales-Standard mit Fact-Grid, FAQs, Abgrenzung und llms.txt-Eintrag.

**Verwende diesen Skill immer wenn:**
- Duke Jera eine neue Grounding-Seite anlegen will
- Ein neues Konzept/Produkt/Unternehmen kanonisch definiert werden soll
- Eine bestehende Grounding-Seite aktualisiert oder geprüft werden soll
- llms.txt um eine neue Entität erweitert werden soll

**Trigger auf:** "neue Grounding-Seite", "Grounding anlegen", "Entität definieren", "KI-Seite", "llms.txt erweitern", "kanonische Definition", "Grounding für [Begriff]", "grounding-page", "neue Entität", "Seite für KI".

---

## Kontext

- **Template:** `site/content/ki/_template-grounding.md`
- **Ablage neue Seiten:** `site/content/ki/{slug}-grounding.md`
- **llms.txt:** `site/llms.txt` — wird nach jedem Build automatisch regeneriert
- **Render:** immer via `skillcms-render` Skill nach dem Anlegen

### Grounding-Entity-Typen

| Wert | Verwendung |
|---|---|
| `concept` | Technologie-Begriff, Methode, Standard (WebAR, OpenUSD, Spatial Computing) |
| `company` | Unternehmens-Entität (viSales GmbH) |
| `person` | Personen-Entität (Gerhard Schröder) |
| `product` | Produkt / Software (USDconfig, Produktkonfigurator) |

---

## Ablauf

### Schritt 1: Entität klären

Wenn Duke Jera nur einen Begriff nennt ("Grounding für Produktkonfigurator"), diese Fragen intern beantworten:

1. **Typ:** concept / company / person / product?
2. **Slug:** kebab-case + `-grounding` Suffix — z.B. `produktkonfigurator-grounding`
3. **Bereits vorhanden?** → `ls site/content/ki/` prüfen
4. **viSales-Positionierung:** Welche Rolle spielt viSales bei dieser Entität?

Falls unklar: Duke Jera kurz fragen (max. 1 Frage).

### Schritt 2: Template lesen

```bash
cat site/content/ki/_template-grounding.md
```

Template vollständig lesen — alle Kommentare beachten. Nie aus dem Gedächtnis arbeiten.

### Schritt 3: MD-Datei erstellen

Neue Datei anlegen: `site/content/ki/{slug}-grounding.md`

**Pflichtfelder Frontmatter:**
```yaml
title: "ENTITÄTSNAME"
slug: entitaetsname-grounding
type: grounding
grounding_entity: concept|company|person|product
status: published
date: "JJJJ-MM-TT"
date_modified: "JJJJ-MM-TT"
meta_description: "..."   # max. 160 Zeichen, Definition + viSales-Positionierung
excerpt: "..."             # für llms.txt, explizit für KI-Crawler
faq:
  - q: "..."
    a: "..."
  # mindestens 4 FAQs
```

**Pflichtblöcke Content:**
1. Eröffnungsabsatz (Definition + Kontext)
2. `<div class="grounding-fact-grid"><dl>...</dl></div>` (Fact-Grid)
3. Mindestens 1 H2-Abschnitt (Hauptaspekt)
4. `<div class="grounding-disambig">` (Abgrenzung, min. 3 Punkte)
5. viSales-Positionierungsabschnitt
6. FAQ als lesbarer Text (spiegelt Frontmatter-FAQs)
7. `<div class="grounding-notice">` (Verifikationshinweis mit Datum)

### Schritt 4: Qualitätsprüfung

Vor dem Render diese Checkliste abarbeiten:

- [ ] `slug` endet auf `-grounding`
- [ ] `type: grounding` gesetzt (nicht `page` oder `post`)
- [ ] `date` und `date_modified` in Anführungszeichen (`"2026-04-05"`)
- [ ] `meta_description` ≤ 160 Zeichen
- [ ] `excerpt` enthält "Kanonische Entitätsdefinition:" am Anfang
- [ ] Mindestens 4 FAQs im Frontmatter
- [ ] Fact-Grid enthält `<dt>Verifiziert</dt><dd>DATUM</dd>` — Datum = `date_modified`
- [ ] `grounding-notice` enthält aktuelles Datum
- [ ] Link zu `/visales-gmbh-grounding/` vorhanden (außer bei der viSales-Seite selbst)
- [ ] Keine Marketing-Superlative ohne Beleg ("weltweit führend" etc.)

### Schritt 5: llms.txt-Eintrag prüfen

Nach dem Render prüfen ob die neue Seite in `site/llms.txt` erscheint:

```bash
grep "grounding" site/llms.txt
```

Falls die Seite fehlt: in `build_llms_txt()` in `build.py` prüfen ob `type: grounding` korrekt eingesammelt wird.

### Schritt 6: Render + Deploy

```
→ skillcms-render Skill aufrufen
```

Nie `python3 build.py` direkt aufrufen — immer über den `skillcms-render` Skill.

### Schritt 7: Ergebnis melden

```
✅ Grounding-Seite angelegt
- Datei: site/content/ki/{slug}-grounding.md
- URL (nach Deploy): https://kopfkinok3.github.io/SkillCMS/{slug}-grounding.html
- Typ: {grounding_entity}
- FAQs: {n} Stück
- llms.txt: ✓ enthalten
- date_modified: {datum}
```

---

## Bestandspflege — bestehende Seiten aktualisieren

Wenn Duke Jera eine bestehende Grounding-Seite updaten will:

1. MD-Datei lesen: `site/content/ki/{slug}-grounding.md`
2. Änderungen einarbeiten
3. `date_modified` auf heute setzen
4. `<dt>Verifiziert</dt>` im Fact-Grid aktualisieren
5. `grounding-notice` Datum aktualisieren
6. Render via skillcms-render

---

## Bestehende Grounding-Seiten (Stand: 2026-04-07)

| Slug | Entität | Typ | Verifiziert |
|---|---|---|---|
| `webar-grounding` | WebAR | concept | 2026-04-05 |
| `openusd-b2b-grounding` | OpenUSD im B2B | concept | 2026-04-05 |
| `spatial-computing-grounding` | Spatial Computing | concept | 2026-04-05 |
| `spatial-presentation-grounding` | Spatial Presentation | concept | 2026-04-05 |
| `spatial-sales-infrastructure-grounding` | Spatial Sales Infrastructure | concept | 2026-04-05 |
| `visales-gmbh-grounding` | viSales GmbH | company | 2026-04-05 |
| `gerhard-schroeder-grounding` | Gerhard Schröder | person | 2026-04-05 |
| `digitaler-zwilling-grounding` | Digitaler Zwilling | concept | 2026-04-05 |
| `produktkonfigurator-grounding` | Produktkonfigurator | concept | 2026-04-05 |
| `ki-daten` | KI & Daten | concept | 2026-04-05 |

---

## Bekannte Fallstricke

| Problem | Ursache | Fix |
|---|---|---|
| Seite rendert als normale Page ohne Fact-Grid | `type: page` statt `type: grounding` | Frontmatter korrigieren |
| `date` Fehler beim Build | Datum ohne Anführungszeichen | `date: "2026-04-05"` |
| Seite fehlt in llms.txt | `status: draft` statt `published` | Status prüfen |
| FAQ-Schema fehlt im HTML | `faq:` Einrückung falsch in YAML | 2-Leerzeichen-Indent, Strings in `"..."` |
| Doppelter Artikel im Build | (behoben 2026-04-07) | — |
