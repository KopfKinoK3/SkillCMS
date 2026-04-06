# SkillCMS — Claude Instructions

## Build

```bash
cd /path/to/SkillCMS
python3 site/build.py
```

Output landet in `site/dist/`. Danach pushen:

```bash
git add -A && git commit -m "Beschreibung" && git push
```

GitHub Pages deployed automatisch von `main` — URL: https://kopfkinok3.github.io/SkillCMS/

## Projekt-Struktur

```
site/
  build.py          # Build-Script (Python 3, PyYAML + Markdown benötigt)
  site.yaml         # Globale Konfiguration, Schema.org, Navigation, Footer
  content/
    pages/          # Statische Seiten (kontakt, praxis, über-uns …)
    ki/             # Grounding Pages für KI-Crawler (Entity-Seiten)
    posts/          # Blog-Posts (Dateiname: YYYY-MM-DD-slug.md)
  dist/             # Build-Output (nicht committen — wird von build.py erzeugt)
```

## Frontmatter-Felder

| Feld | Bedeutung |
|---|---|
| `type: grounding` | Erzeugt AboutPage JSON-LD statt WebPage |
| `grounding_entity: organization\|person` | Welche Entität in mainEntity |
| `faq:` | Liste `[{q: "...", a: "..."}]` → FAQPage JSON-LD |
| `status: published` | Pflicht damit Seite gebaut wird |

## Grounding Pages

- `/visales-gmbh-grounding/` — Entitätsseite viSales GmbH
- `/gerhard-schroeder-grounding/` — Entitätsseite Gerhard Schröder

## Wichtige Hinweise

- API-Keys (Brevo etc.) gehören NICHT in `site.yaml` — GitHub Push Protection blockt den Push
- Build-Pfad ist session-abhängig (`/sessions/[id]/mnt/Claude/...`) — immer über den gemounteten Ordner arbeiten
- Stabiler lokaler Pfad: `~/Documents/Claude/Software_Dev/SkillCMS`
