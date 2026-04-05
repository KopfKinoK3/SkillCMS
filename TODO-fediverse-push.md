# TODO: Fediverse Push — Static Site Publish Skill

**Status:** In Planung / On Hold
**Ziel:** Beim Publish eines neuen Artikels auf der Static-HTML-Site automatisch einen Mastodon-Post anstoßen (mit Review-Schritt).

---

## Entscheidungen (bereits getroffen)

| Parameter | Wert |
|---|---|
| Instanz | `https://mastodon.social` |
| Handle | `@visales@mastodon.social` |
| Post-Flow | Claude generiert Vorschlag → Duke reviewt/passt an → Bestätigung → POST |
| Hashtags | Dynamisch aus Artikel-Kontext generiert |
| Token-Scope | `write:statuses` (minimal) |

---

## API Credentials

> ⚠️ Token gehört in eine lokale `config.env` — nie hardcoded im Skill

```
MASTODON_INSTANCE=https://mastodon.social
MASTODON_ACCESS_TOKEN=O7onE6sNbZDwKIwWoiQ-CDFUk2P2nCwPrQTjdsV24N0
MASTODON_ACCOUNT=@visales@mastodon.social
```

---

## TODO-Liste

### Phase 1: Account & Setup
- [ ] Mastodon-Account `@visales` auf mastodon.social erstellen (falls noch nicht done)
- [ ] Profil einrichten: Bio, visales.de Link, Avatar (Warm-Tech-Stil), Banner
- [ ] Token testen: Testpost via `curl` oder Script prüfen ob Auth funktioniert

### Phase 2: Fediverse-Push-Baustein entwickeln
- [ ] Python-Funktion / Bash-Script für Mastodon-POST schreiben
  - Input: Titel, Teaser, URL, Tags (aus Artikel-Frontmatter)
  - Output: Generierter Post-Vorschlag (160–300 Zeichen + Hashtags)
- [ ] Review-Schritt einbauen: Claude zeigt Vorschlag → User bestätigt oder passt an
- [ ] POST-Call: `POST /api/v1/statuses` mit Bearer Token
- [ ] Fehlerbehandlung: API-Fehler, Rate Limits, Duplicate-Check

### Phase 3: Integration in Publish-Skill
- [ ] Abstimmen mit Static-Site-Publish-Workflow (anderer CoWork-Chat)
- [ ] Reihenfolge im Publish-Flow festlegen:
  1. HTML generieren / aktualisieren
  2. RSS-Feed `feed.xml` updaten (neuer `<item>` oben)
  3. **Mastodon Post-Vorschlag generieren + Review** ← dieser Baustein
  4. FTP Push (HTML + RSS)
  5. Mastodon POST abfeuern (nach FTP-Bestätigung)
- [ ] Skill-Datei `publish-static-article/SKILL.md` schreiben

### Phase 4: Optional (separates Projekt)
- [ ] Monthly Email-Newsletter — eigener Skill, eigenes Projekt

---

## Post-Format (Vorlage)

```
🔶 [Artikel-Titel]

[2–3 Sätze Teaser — outcome-orientiert, kein Clickbait]

→ [URL]

#[DynamicTag1] #[DynamicTag2] #[DynamicTag3] #WebAR #OpenUSD #viSales
```

**Zeichenlimit Mastodon:** 500 Zeichen (mastodon.social Standard)

---

## API-Referenz

```bash
# Test-Call
curl -X POST https://mastodon.social/api/v1/statuses \
  -H "Authorization: Bearer O7onE6sNbZDwKIwWoiQ-CDFUk2P2nCwPrQTjdsV24N0" \
  -d "status=Test von viSales Publish Bot 🔶"
```

```python
# Python-Snippet (Basis)
import requests

def post_to_mastodon(text, token, instance="https://mastodon.social"):
    r = requests.post(
        f"{instance}/api/v1/statuses",
        headers={"Authorization": f"Bearer {token}"},
        data={"status": text}
    )
    return r.json()
```

---

## Verknüpfte Projekte

- **Static Site Publish Skill** → anderer CoWork-Chat (Koordination nötig)
- **RSS-Feed-Generator** → Teil des Publish-Skills
- **Email Newsletter** → separates Projekt, later

---

*Erstellt: 2026-04-05 | Duke Jera / viSales*
