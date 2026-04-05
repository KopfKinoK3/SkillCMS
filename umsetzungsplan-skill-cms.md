# Umsetzungsplan: Skill_CMS – Statische Website visales.de

**Stand:** 2026-03-20
**Ziel:** Das aktuelle Design-Template von visales.de als statische HTML-Seiten nachbauen und schrittweise die komplette Website (~150 Seiten) für FTP-Deployment aufbauen.

---

## Phase 0 – Analyse & Grundlage

**Aufgaben:**
1. Aktuelles Theme von visales.de vollständig analysieren (HTML-Struktur, CSS-Klassen, JS-Dependencies)
2. Header und Footer als wiederverwendbare HTML-Komponenten isolieren
3. Alle externen Abhängigkeiten dokumentieren (Fonts, Icons, externe Scripts, CDN-Links)
4. Asset-Struktur ermitteln (Bilder, CSS-Dateien, JS-Dateien)

**Output:** `template-analyse.md` + Asset-Liste

---

## Phase 1 – Statische Referenzseite (Meilenstein 1)

**Aufgaben:**
1. `index.html` erstellen – nur Header + Footer, Body leer (oder Platzhalter)
2. CSS und JS aus Ghost-Theme extrahieren oder neu schreiben
3. Responsive-Check (Mobile, Tablet, Desktop)
4. Visueller Abgleich mit der Live-Seite

**Output:** `index.html` (läuft lokal im Browser, sieht aus wie visales.de)

> ✅ **Wenn dieser Schritt klappt, ist der Proof-of-Concept erbracht.**

---

## Phase 2 – Template-Architektur für Skalierung

**Aufgaben:**
1. Entscheiden: Reines HTML oder Static Site Generator (z.B. Eleventy, Hugo, Jekyll)?
   - Option A: Manuell (volle Kontrolle, mehr Arbeit)
   - Option B: SSG mit Templates (empfohlen für 150 Seiten)
2. Gemeinsame Komponenten definieren: Header, Footer, Navigation, Meta-Tags
3. Seiten-Typen identifizieren (Startseite, Leistungsseite, Case Study, Blog-Post, Kontakt, ...)
4. URL-Struktur festlegen (entspricht dem aktuellen Schema?)

---

## Phase 3 – Seiten-Generierung (~150 Seiten)

**Aufgaben:**
1. Bestehende Inhalte aus Ghost/visales.de exportieren (oder manuell übertragen)
2. Für jeden Seitentyp eine Template-Datei erstellen
3. Content-Migration: Seite für Seite befüllen (ggf. halbautomatisch via Script)
4. Interne Verlinkung prüfen und bereinigen
5. SEO-Meta-Tags aus bestehendem SEO-Ordner einspielen

---

## Phase 4 – FTP-Deployment

**Aufgaben:**
1. FTP-Zugangsdaten sicher hinterlegen
2. Deployment-Script schreiben (z.B. `deploy.sh` mit `lftp` oder `ncftp`)
3. Testdeploy auf Staging-Pfad
4. Produktiv-Deploy + DNS-Check
5. Redirect-Regeln prüfen (301 für alte URLs, wenn nötig)

---

## Empfohlene Tool-Stack

| Bereich | Tool |
|---|---|
| Static Site Generator | Eleventy (11ty) – sehr flexibel, kein Framework-Overhead |
| CSS | 1:1 aus Ghost-Theme extrahiert / oder Tailwind für Neuaufbau |
| Deploy | `lftp` Script oder GitHub Actions → FTP |
| Content-Source | Ghost JSON-Export oder Markdown-Dateien |

---

## Nächste Schritte (sofort)

1. **Du:** Welches Ghost-Theme läuft aktuell auf visales.de? (Theme-Name oder GitHub-Link)
2. **Evelyn:** Screenshot/Analyse von Header + Footer von visales.de
3. **Evelyn:** Erste statische HTML-Seite mit Header + Footer bauen

---

_Erstellt von Maid Evelyn, 2026-03-20_
