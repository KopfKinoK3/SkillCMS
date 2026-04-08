---
title: "Mein erster Claude Skill ist live  und löst ein Problem, das nur wenige CRM-Tools ernst nehmen"
slug: erster-claude-skill-ics-crm-reminder
status: published
primary_tag: ki
tags: [ki]
meta_title: "ICS CRM Reminder: Mein erster Claude Cowork Skill ist live"
meta_description: "Warum ich einen Kalender-Reminder mit CRM-Daten gebaut habe statt mein CRM zu wechseln. Jetzt auf GitHub, ClawHub und LobstrHunt."
feature_image: /assets/images/2026/03/ICS-Kalender.Skill-Claude-KI.jpg
author: "Gerhard Schröder"
author_slug: gerhard
author_image: /assets/images/2025/10/1706254155883-1.jpeg
author_bio: "Gerhard Schröder ist Gründer & GF der viSales GmbH, Bochum. Seit über 15 Jahren spezialisiert auf visuelle Vertriebskommunikation für Maschinenbau & AeroSpace — mit 3D-Visualisierung & OpenUSD. Mitglied der AOUSD, Speaker zu AR & Spatial Sales."
published_at: "2026-03-27T22:25:47.000Z"
type: post
template: post
---

- **Claude Cowork Skills lassen sich als Open Source auf GitHub, ClawHub und LobstrHunt teilen — der erste Skill-Marktplatz für KI-Agenten ist live.**
- **ICS-Kalender-Dateien mit strukturierten CRM-Daten ersetzen das ungepflegte CRM im Kleinstvertrieb — ein Doppelklick reicht.**
- **Nico Lummas Newsletter „The Agentic Founder“ hat LobstrHunt vorgestellt — eine tägliche Skill-Launch-Plattform nach ProductHunt-Vorbild.**

&nbsp;

&nbsp;

Im B2B-Vertrieb gibt es ein Muster, das wir alle kennen: Du hast ein gutes Gespräch, die Demo lief, der Entscheider sagt „Melden Sie sich Mitte April nochmal.“ Du sagst: „Mach ich.“ Und dann trägst du irgendwo „Herr Meyer anrufen“ in den Kalender ein — ohne Kontext, ohne Deal-Status, ohne Erinnerung, worum es eigentlich ging.

Zwei Wochen später klingelst du an, und dein erster Satz ist: „Ähm, wir hatten doch mal über…“ Das ist kein Vertrieb. Das ist Improvisation.

### Ich brauchte kein besseres CRM.   
Ich brauchte einen intelligenteren Kalender.

CRM-Systeme lösen das Problem theoretisch. Praktisch aber nicht — zumindest nicht für kleine Teams und Agenturinhaber, die keine Salesforce-Instanz pflegen wollen, nur um sich an einen Rückruf zu erinnern. Was ich brauche (wenn man ein Still-CRM hat): einen Reminder, der mir beim Klingeln sofort sagt, mit wem ich rede, was der letzte Stand war, wie hoch das Budget ist, und was der nächste logische Schritt wäre .

Genau dafür habe ich den **ICS CRM Reminder** gebaut — einen Claude Cowork Skill, der aus einem kurzen Satz wie „Ruf nächsten Dienstag bei Firma XYZ an, Thema [WebAR-Konfigurator](https://visales.de/usdconfig/), Angebot nachfassen, Budget 25k“ eine saubere ICS-Kalenderdatei erzeugt. Doppelklick, fertig — drin in Apple Calendar, Google Calendar oder Outlook.

Der Kalender-Event enthält nicht nur Datum und Firma, sondern eine komplett strukturierte CRM-Notiz: Kunde, Ansprechpartner, Telefon, Thema, Priorität, Deal-Phase, Budget, letzte Interaktion, nächster Schritt. Alles direkt in der Kalender-Beschreibung — lesbar auf jedem Gerät.

### Claude Skills teilen: Von der lokalen Automatisierung zum Open-Source-Skill

Ich nutze Claude Cowork seit einigen Monaten für meinen Arbeitsalltag bei [viSales](https://visales.de/) — 3D-Visualisierung und WebAR für B2B. Dabei sind Workflows entstanden, die ich immer wieder brauche. Der ICS CRM Reminder war der erste, den ich sauber genug fand, um ihn zu teilen.

> [Mark Zimmermann](https://www.linkedin.com/in/mark-zimmermann-5a005123/) hat mit seinem [LinkedInOptimizer](https://github.com/GodModeAI2025/LinkedInOptimizer) vorgemacht, wie man Claude-Skills als Open Source auf GitHub stellt und damit anderen einen echten Nutzen bietet. Das hat mich motiviert, den gleichen Schritt zu gehen.

Den Anstoß zum Veröffentlichen gab dann jedoch [Nico Lummas LinkedIn-Newsletter „The Agentic Founder“ (Issue #4)](https://www.linkedin.com/pulse/agentic-founder-issue-4-nico-lumma-yhmbf/), in dem er [LobstrHunt](https://lobstrhunt.com) vorgestellt hat — eine tägliche Skill-Launch-Plattform nach ProductHunt-Vorbild, gebaut von NMA aus Hamburg. Dort können Entwickler ihre OpenClaw-Skills launchen, die Community voted, und KI-Agenten geben Performance-Reviews. Das war der Moment, in dem ich dachte: 

> **Wenn nicht jetzt, wan-tan?** (Insider)

Der Skill ist jetzt an drei Stellen verfügbar:

- [GitHub](https://github.com/KopfKinoK3/ics-crm-reminder) — Open Source unter MIT-Lizenz
- [ClawHub](https://clawhub.ai/skills/ics-crm-reminder) — die Skill-Registry für OpenClaw-Agents
- [LobstrHunt](https://lobstrhunt.com) — die tägliche Skill-Launch-Plattform. Hier ist er am 25.03. als überhaupt dritter Skill an den Start gegangen. *(Erinnert sich noch jemand an diese Typen die als Kommentar "ERSTER" schreiben???)* 

Wenn du im B2B-Vertrieb arbeitest und dein CRM eigentlich dein Kalender ist — probier’s aus. Feedback gern direkt auf GitHub oder an [sales@visales.de](mailto:sales@visales.de).

&nbsp;

&nbsp;

### **Du willst wissen ob ein Claude Skill auch für deinen Vertriebsalltag passt?**

In 30 Minuten sortieren wir gemeinsam, ob und wo Automatisierung mit Claude in eurem Workflow konkret etwas bringt — ohne Pitch, ohne Angebot. Kein Verkaufsdruck, eine ehrliche Einordnung. **Rheingas und Somfy haben so angefangen.**

[Einordnungsgespräch buchen](https://visales.de/kontakt/){.gh-button .cta-center}

&nbsp;

&nbsp;

<details>
<summary><strong>Realitätscheck</strong></summary>

Ja, ein ICS-Reminder ist kein CRM. Es gibt keine Pipeline-Ansicht, keine Auswertung, kein Dashboard. Wer 50 Leads pro Woche bearbeitet, braucht ein richtiges System. Aber die meisten B2B-Teams mit unter 10 Leuten haben kein Lead-Volumen-Problem — sie haben ein Vergessen-Problem.

Und dafür ist ein Kalender-Event mit Kontext besser als ein ungepflegtes CRM, in das seit Wochen niemand reingeschaut hat.

Ich lebe "aus dem Kalender" heraus...

**Aber: Ich nutze den Skill** ***nicht*** **für Kundendaten, sondern für das ganze Leben drumherum. Hobby-Zeiten wollen auch VERWALTET werden. Und wenn ich die Local-KI am Laufen habe...**

</details>
