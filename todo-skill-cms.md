# Projekt Skill_CMS – ToDo

**Ziel:** Statische Website-Version von visales.de nachbauen (aktuelles Design-Template) und schrittweise als HTML-Seiten aufbauen – dann via FTP deployen. Ghost CMS als bisheriger Ansatz wird durch statische Generierung ergänzt/ersetzt.

---

## Status — Build-System (fertig)
- [x] Markdown → HTML Build-Pipeline (build.py)
- [x] Ghost Source Theme — CSS-Overrides, Nav 828px, CTA-Button orange
- [x] Nav responsive: Desktop einzeilig (Logo|Links|CTA), Mobile zweizeilig (kein Burger)
- [x] Tag-Listings auto-discovery (`/tag/{slug}.html`)
- [x] RSS 2.0 Feed (`rss.xml`)
- [x] sitemap.xml + robots.txt
- [x] **llms.txt** — KI-Crawler-Standard (llmstxt.org), Seiten + Posts + Quellen
- [x] DX Tooling: `--serve`, `--watch`, `--serve --watch`
- [x] GitHub Pages Deployment via GitHub Actions

## Render-Skill (Cowork-Automatisierung)

Ziel: `python3 site/build.py` als Skill — damit ohne Terminal nutzbar.

| Phase | Inhalt | Status |
|---|---|---|
| **Phase 1** — Local Render | `build.py` ausführen, Output prüfen, fertig | 🔜 als nächstes |
| **Phase 2** — Render + GitHub | + git add/commit/push, Actions-Status | nach Phase 1 |
| **Phase 3** — Render + Deploy | + FTP/SSH Hetzner, RSS-Ping, Mastodon-Post | wenn live |

→ Skill-Name: `skillcms-render`
→ Ablageort: `.claude/skills/skillcms-render/SKILL.md`

---

## Offen — Nächste Schritte

- [ ] **Render-Skill Phase 1** bauen (`skillcms-render`)
- [ ] Content-Migration: Ghost-Seiten als Dummy-MDs anlegen (Leistungen, Fallbeispiele, Über Uns…)
- [ ] Skeleton-Snapshot: alle Dummy-Inhalte, ZIP als `SkillCMS-v1.0-skeleton`
- [ ] FTP-Deployment zu Hetzner (nach Skeleton-Phase) → Render-Skill Phase 3
- [ ] Fediverse Push (Mastodon) — siehe `TODO-fediverse-push.md` → Render-Skill Phase 3

---

## Kontext
- Bisheriger Ansatz: Content via DOM-API in Ghost CMS auf visales.de einpflegen
- Neue Richtung: Statische HTML-Seiten auf Basis des bestehenden Designs
- Skills im Ordner: ghost-cms-skill, ghost-faq-seo (bleiben als Referenz erhalten)

---

## Offene Fragen
- Welches Template liegt genau vor? (Theme-Name, ggf. Handlebars/Ghost-Theme?)
- FTP-Zugangsdaten vorhanden / wo liegt der Webspace?
- Sollen alle ~150 Seiten 1:1 dem aktuellen URL-Schema entsprechen?

---

_Angelegt: 2026-03-20_
