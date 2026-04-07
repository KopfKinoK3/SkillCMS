#!/usr/bin/env python3
"""
SkillCMS Build Script
=====================
Liest Markdown-Dateien aus content/, rendert sie zu HTML
und injiziert sie in das page-Template.

Konfiguration: site.yaml (im selben Verzeichnis)

Usage:
    python3 build.py                    # Baut alle published Seiten
    python3 build.py kontakt            # Baut nur kontakt.html
    python3 build.py --include-drafts   # Baut alle inkl. Entwürfe
    python3 build.py --drafts-only      # Nur Entwürfe bauen (Preview)

Generierte Dateien (bei build_all):
    sitemap.xml   — alle published Seiten
    robots.txt    — Suchmaschinen-Direktiven
    llms.txt      — KI-Crawler-Standard (llmstxt.org)

Frontmatter-Schema (Seiten & Posts):
    title:            Seitentitel (H1 + <title>)
    slug:             URL-Pfad, z.B. "augmented-reality"
    type:             page | post | listing | grounding
    status:           published | draft
    date:             ISO-Datum, z.B. "2026-04-05"  (Posts)
    date_modified:    ISO-Datum — dateModified im Article-Schema
    meta_description: SEO-Beschreibung (max. 160 Zeichen)
    og_image:         Pfad oder URL zum Feature Image
    author:           Name des Autors (Posts, Default: aus site.yaml)
    keywords:         Komma-getrennte Keywords für Article-Schema
    tags:             Liste von Tag-Slugs, z.B. [openusd, webar]
    primary_tag:      Primärer Tag-Slug (für Tag-Listing-Discovery)
    excerpt:          Kurzbeschreibung für Karten & llms.txt

Struktur:
    content/kontakt.md     →  kontakt.html
    content/posts/*.md     →  posts/*.html  (zukünftig)
"""

import os
import sys
import re
import json
import time
import threading
import subprocess
import http.server
import socketserver
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Pfade
# ---------------------------------------------------------------------------
SITE_DIR     = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR  = os.path.join(SITE_DIR, "content")
CONFIG_PATH  = os.path.join(SITE_DIR, "site.yaml")
OUTPUT_DIR   = SITE_DIR   # HTML-Dateien landen im site/-Root


# ---------------------------------------------------------------------------
# Abhängigkeiten sicherstellen
# ---------------------------------------------------------------------------
def ensure_deps():
    """Installiert markdown + PyYAML falls nötig."""
    missing = []
    try:
        import markdown  # noqa
    except ImportError:
        missing.append("markdown")
    try:
        import yaml  # noqa
    except ImportError:
        missing.append("PyYAML")

    if missing:
        # --break-system-packages nur ab pip 22+ (Linux) — auf älteren Systemen weglassen
        import pip
        pip_version = tuple(int(x) for x in pip.__version__.split(".")[:2])
        flags = ["--break-system-packages"] if pip_version >= (22, 0) else []
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install"] + flags + ["-q"] + missing
        )

ensure_deps()

import markdown as md_lib   # noqa: E402
import yaml                  # noqa: E402


# ---------------------------------------------------------------------------
# Site-Config laden
# ---------------------------------------------------------------------------
def load_config():
    """Liest site.yaml und gibt das Config-Dict zurück."""
    if not os.path.exists(CONFIG_PATH):
        print(f"  ⚠  site.yaml nicht gefunden ({CONFIG_PATH})")
        return {}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

CONFIG = load_config()

# ---------------------------------------------------------------------------
# Brevo-Formular-Embed laden und in drei Sektionen splitten
# ---------------------------------------------------------------------------
def load_brevo_embed():
    """Liest _brevo-form.html und gibt (head_html, body_html, foot_html) zurück."""
    # Dateiname aus site.yaml newsletter-Sektion ermitteln
    embed_file = ""
    for col in (CONFIG.get("footer", {}).get("columns", []) or []):
        if col.get("type") == "newsletter" and col.get("brevo_embed_file"):
            embed_file = col["brevo_embed_file"]
            break
    if not embed_file:
        return "", "", ""
    embed_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), embed_file)
    if not os.path.exists(embed_path):
        return "", "", ""
    with open(embed_path, "r", encoding="utf-8") as f:
        raw = f.read()
    def extract(start_marker, end_marker):
        s = raw.find(start_marker)
        e = raw.find(end_marker)
        if s == -1 or e == -1:
            return ""
        return raw[s + len(start_marker):e].strip()
    head_html = extract("<!-- ##BREVO_HEAD_START## -->", "<!-- ##BREVO_HEAD_END## -->")
    body_html = extract("<!-- ##BREVO_BODY_START## -->", "<!-- ##BREVO_BODY_END## -->")
    foot_html = extract("<!-- ##BREVO_FOOT_START## -->", "<!-- ##BREVO_FOOT_END## -->")
    return head_html, body_html, foot_html

BREVO_HEAD, BREVO_BODY, BREVO_FOOT = load_brevo_embed()


def cfg(*keys, default=""):
    """Greift sicher auf verschachtelte Config-Werte zu."""
    val = CONFIG
    for k in keys:
        if not isinstance(val, dict):
            return default
        val = val.get(k, default)
    return val if val is not None else default


# ---------------------------------------------------------------------------
# Frontmatter-Parsing
# ---------------------------------------------------------------------------
def parse_frontmatter(text):
    """Extrahiert YAML-Frontmatter aus Markdown via yaml.safe_load.
    Unterstützt alle YAML-Typen: Strings, Listen, verschachtelte Dicts (z.B. faq:).
    """
    meta = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                parsed = yaml.safe_load(parts[1]) or {}
                if isinstance(parsed, dict):
                    meta = parsed
            except yaml.YAMLError:
                # Fallback: naive Zeilen-Parser für einfache key: value
                for line in parts[1].strip().split("\n"):
                    if ":" in line and not line.startswith(" "):
                        key, val = line.split(":", 1)
                        meta[key.strip()] = val.strip().strip('"').strip("'")
            text = parts[2]
    return meta, text.strip()


# ---------------------------------------------------------------------------
# Toggle-Card Konvertierung
# ---------------------------------------------------------------------------
TOGGLE_ICON_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2.5" stroke-linecap="round" '
    'stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>'
)


def convert_toggles(html):
    """Wandelt <details><summary>...</summary>...</details> in Ghost kg-toggle-card um."""
    def replace_toggle(match):
        summary_text = match.group(1).strip()
        summary_text = re.sub(r'</?(?:strong|em)>', '', summary_text)
        content_raw = match.group(2).strip()
        # Markdown inside <details> is not processed by the main md pass → do it here
        content_inner = md_lib.markdown(
            content_raw,
            extensions=["extra", "meta", "smarty"],
            output_format="html5",
        )
        return (
            f'<div class="kg-card kg-toggle-card" data-kg-toggle-state="close">\n'
            f'  <div class="kg-toggle-heading">\n'
            f'    <button class="kg-toggle-card-icon" aria-label="Inhalt einblenden">{TOGGLE_ICON_SVG}</button>\n'
            f'    <h4 class="kg-toggle-heading-text">{summary_text}</h4>\n'
            f'  </div>\n'
            f'  <div class="kg-toggle-content">\n'
            f'    {content_inner}\n'
            f'  </div>\n'
            f'</div>'
        )

    return re.sub(
        r'<details>\s*<summary>(.*?)</summary>(.*?)</details>',
        replace_toggle,
        html,
        flags=re.DOTALL,
    )


# ---------------------------------------------------------------------------
# Markdown → HTML
# ---------------------------------------------------------------------------
def md_to_html(md_text):
    """Konvertiert Markdown zu HTML (Spacer, Blockquote-Flatten, Toggles)."""
    # Spacer-Divs einfügen (Doppel-/Dreifach-Leerzeilen)
    lines = md_text.split('\n')
    protected = []
    in_blockquote = False
    for line in lines:
        if line.startswith('>'):
            in_blockquote = True
        elif in_blockquote and line.strip() == '':
            in_blockquote = False
        protected.append(line)
    md_text = '\n'.join(protected)

    md_text = re.sub(r'\n{4,}', '\n\n<div class="vs-spacer-lg"></div>\n\n', md_text)
    md_text = re.sub(r'\n{3}',  '\n\n<div class="vs-spacer"></div>\n\n',    md_text)

    html = md_lib.markdown(
        md_text,
        extensions=["extra", "meta", "smarty"],
        output_format="html5",
    )

    # Blockquotes wie Ghost: <p>-Tags → inline mit <br><br>
    def flatten_blockquote(match):
        inner = match.group(1)
        inner = re.sub(r'<p>(.*?)</p>', r'\1<br><br>', inner, flags=re.DOTALL)
        inner = re.sub(r'(<br>\s*)+$', '', inner.strip())
        inner = re.sub(r'\n', '<br>\n', inner)
        inner = re.sub(r'(<br>\s*){3,}', '<br><br>\n', inner)
        return f'<blockquote>\n{inner}\n</blockquote>'

    html = re.sub(
        r'<blockquote>\s*(.*?)\s*</blockquote>',
        flatten_blockquote,
        html,
        flags=re.DOTALL,
    )

    html = convert_toggles(html)
    return html


# ---------------------------------------------------------------------------
# Navigation aus Config generieren
# ---------------------------------------------------------------------------
def build_nav_html(active_slug=""):
    """Generiert <li>-Einträge aus site.yaml navigation."""
    nav_items = cfg("navigation", default=[])
    if not nav_items:
        return ""

    items_html = []
    for item in nav_items:
        label = item.get("label", "")
        slug  = item.get("slug", "")
        url   = item.get("url", f"/{slug}/")

        css_class = f"nav-{slug}"
        if slug == active_slug:
            css_class += " nav-current"

        items_html.append(f'<li class="{css_class}"><a href="{url}">{label}</a></li>')

    return "\n                    ".join(items_html)


# ---------------------------------------------------------------------------
# Cookie-Banner (GDPR)
# ---------------------------------------------------------------------------
def build_cookie_banner():
    """Generiert einen GDPR-konformen Cookie-Banner mit 5 Kategorien."""
    return """
<div id="vs-cookie-banner" class="vs-cookie-banner" aria-live="polite" role="dialog" aria-label="Cookie-Einstellungen">
  <div class="vs-cookie-inner">
    <div class="vs-cookie-text">
      <strong>Cookies &amp; Datenschutz</strong>
      <p>Wir nutzen Cookies für Newsletter, Analysen, Werbung und eingebettete Medien (YouTube, Podcast).
        <a href="/datenschutz/">Datenschutz&shy;erklärung</a>
      </p>
    </div>
    <div class="vs-cookie-actions">
      <button class="gh-button vs-cookie-btn-all" id="vs-cookie-accept-all">Alle akzeptieren</button>
      <button class="vs-cookie-btn-settings" id="vs-cookie-toggle-settings">Einstellungen</button>
      <button class="vs-cookie-btn-deny" id="vs-cookie-deny">Nur notwendige</button>
    </div>
  </div>
  <div id="vs-cookie-settings-panel" class="vs-cookie-settings-panel" hidden>
    <div class="vs-cookie-cats">
      <label class="vs-cookie-cat">
        <span class="vs-cookie-cat-info">
          <strong>Notwendig</strong>
          <small>Technisch erforderlich, immer aktiv</small>
        </span>
        <span class="vs-cookie-toggle vs-cookie-toggle--disabled is-on"><span></span></span>
      </label>
      <label class="vs-cookie-cat">
        <span class="vs-cookie-cat-info">
          <strong>Funktional</strong>
          <small>Newsletter-Anmeldung via Brevo</small>
        </span>
        <span class="vs-cookie-toggle" data-cat="funktional"><span></span></span>
      </label>
      <label class="vs-cookie-cat">
        <span class="vs-cookie-cat-info">
          <strong>Analyse</strong>
          <small>Google Analytics &amp; Search Console</small>
        </span>
        <span class="vs-cookie-toggle" data-cat="analyse"><span></span></span>
      </label>
      <label class="vs-cookie-cat">
        <span class="vs-cookie-cat-info">
          <strong>Marketing</strong>
          <small>Google Ads</small>
        </span>
        <span class="vs-cookie-toggle" data-cat="marketing"><span></span></span>
      </label>
      <label class="vs-cookie-cat">
        <span class="vs-cookie-cat-info">
          <strong>Medien</strong>
          <small>YouTube-Videos, Podcast-Player</small>
        </span>
        <span class="vs-cookie-toggle" data-cat="medien"><span></span></span>
      </label>
    </div>
    <div class="vs-cookie-settings-actions">
      <button class="gh-button vs-cookie-btn-save" id="vs-cookie-save">Auswahl speichern</button>
    </div>
  </div>
</div>
<script>
(function(){
  var STORE_KEY = 'vsConsent';
  var banner    = document.getElementById('vs-cookie-banner');
  var panel     = document.getElementById('vs-cookie-settings-panel');
  var toggles   = banner ? banner.querySelectorAll('.vs-cookie-toggle[data-cat]') : [];

  function getConsent(){ try{ return JSON.parse(localStorage.getItem(STORE_KEY)||'null'); }catch(e){ return null; } }
  function setConsent(obj){
    localStorage.setItem(STORE_KEY, JSON.stringify(obj));
    document.dispatchEvent(new CustomEvent('vsCookieConsent', {detail: obj}));
    if(typeof gtag === 'function'){
      gtag('consent', 'update', {
        'analytics_storage': obj.analyse ? 'granted' : 'denied',
        'ad_storage':        obj.marketing ? 'granted' : 'denied'
      });
    }
  }
  function hideBanner(){ if(banner) banner.style.display='none'; }

  function applyToggles(obj){
    toggles.forEach(function(t){
      if(obj && obj[t.dataset.cat]) t.classList.add('is-on');
      else t.classList.remove('is-on');
    });
  }

  var existing = getConsent();
  if(existing){
    hideBanner();
    if(typeof gtag === 'function'){
      gtag('consent', 'update', {
        'analytics_storage': existing.analyse ? 'granted' : 'denied',
        'ad_storage':        existing.marketing ? 'granted' : 'denied'
      });
    }
    return;
  }

  if(!banner) return;
  banner.style.display = 'block';

  document.getElementById('vs-cookie-accept-all').addEventListener('click', function(){
    var obj = {funktional:true, analyse:true, marketing:true, medien:true};
    setConsent(obj); hideBanner();
  });

  document.getElementById('vs-cookie-deny').addEventListener('click', function(){
    setConsent({funktional:false, analyse:false, marketing:false, medien:false}); hideBanner();
  });

  document.getElementById('vs-cookie-toggle-settings').addEventListener('click', function(){
    var hidden = panel.hidden;
    panel.hidden = !hidden;
    this.textContent = hidden ? 'Einstellungen schließen' : 'Einstellungen';
  });

  toggles.forEach(function(t){
    t.addEventListener('click', function(){ this.classList.toggle('is-on'); });
  });

  document.getElementById('vs-cookie-save').addEventListener('click', function(){
    var obj = {};
    toggles.forEach(function(t){ obj[t.dataset.cat] = t.classList.contains('is-on'); });
    setConsent(obj); hideBanner();
  });
})();
</script>"""


# ---------------------------------------------------------------------------
# Footer aus Config generieren
# ---------------------------------------------------------------------------
def build_footer_html():
    """Generiert den kompletten Footer aus site.yaml."""

    # Trust Bar
    trust_clients = cfg("trust_clients", default="")
    memberships   = cfg("memberships", default=[])
    membership_links = " &amp; ".join(
        f'<a href="{m["url"]}" target="_blank" rel="noopener">{m["label"]}</a>'
        for m in memberships
    )
    trust_html = ""
    if trust_clients or membership_links:
        trust_html = f"""
            <div class="vs-footer-trust">
                <div class="vs-footer-trust-clients">{trust_clients}</div>
                <div class="vs-footer-trust-member">Mitglied der {membership_links}</div>
            </div>"""

    # Spalten
    columns     = cfg("footer", "columns", default=[])
    contact_cfg = cfg("contact", default={})
    social_cfg  = cfg("social", default={})
    cols_html   = []

    for col in columns:
        col_type = col.get("type", "links")
        title    = col.get("title", "")
        h4       = f'<h4>{title}</h4>' if title else ''

        if col_type == "contact":
            company_name = cfg("site", "company", default="")
            addr_street  = contact_cfg.get("address_street", "")
            addr_city    = contact_cfg.get("address_city", "")

            addr_parts = []
            if company_name: addr_parts.append(company_name)
            if addr_street:  addr_parts.append(addr_street)
            if addr_city:    addr_parts.append(addr_city)
            addr_html = (
                f'<p class="vs-footer-address">{"<br>".join(addr_parts)}</p>'
                if addr_parts else ""
            )

            cta_html = '<a href="/kontakt/" class="gh-button vs-footer-cta">Termin buchen</a>'

            contact_links = [
                f'<li><a href="mailto:{contact_cfg.get("email", "")}">{contact_cfg.get("email", "")}</a></li>',
                f'<li><a href="tel:{contact_cfg.get("phone", "").replace(" ", "")}">{contact_cfg.get("phone_display", contact_cfg.get("phone", ""))}</a></li>',
            ]

            # KI & Daten sub-section (same h4 style as column title)
            ki_items_contact = col.get("ki_items", [])
            ki_contact_html = ""
            if ki_items_contact:
                ki_t = col.get("ki_title", "KI & Daten")
                ki_h4_contact = f'<h4 class="vs-footer-col-subtitle">{ki_t}</h4>'
                ki_contact_parts = []
                for k in ki_items_contact:
                    ext_attr = ' target="_blank" rel="noopener"' if k.get("external") else ""
                    ki_contact_parts.append(f'<li><a href="{k["url"]}"{ext_attr}>{k["label"]}</a></li>')
                ki_contact_html = f'{ki_h4_contact}<ul>{"".join(ki_contact_parts)}</ul>'

            cols_html.append(
                f'<div class="vs-footer-col">'
                f'{h4}{addr_html}{cta_html}'
                f'<ul>{"".join(contact_links)}</ul>'
                f'{ki_contact_html}'
                f'</div>'
            )

        elif col_type == "newsletter":
            teaser      = col.get("teaser", "")
            signup_url  = col.get("signup_url", "/newsletter/")
            signup_label= col.get("signup_label", "Anmeldung →")
            archive_url = col.get("archive_url", "/newsletter/")
            archive_lbl = col.get("archive_label", "Alle Ausgaben & Podcasts")

            if BREVO_BODY:
                # Offizielles Brevo-Embed-Formular (aus _brevo-form.html)
                signup_block = BREVO_BODY
            else:
                # Fallback: einfacher CTA-Button
                # ⚠ WARNUNG: _brevo-form.html fehlt oder hat keine ##BREVO_BODY_START## Marker
                print("  ⚠  Newsletter-Formular: _brevo-form.html nicht gefunden oder Marker fehlen → Fallback-Button aktiv")
                signup_block = f'<a href="{signup_url}" class="gh-button vs-footer-signup-btn">{signup_label}</a>'

            teaser_html = f'<p>{teaser}</p>\n                    ' if teaser else ''
            cols_html.append(
                f'<div class="vs-footer-col vs-footer-newsletter">\n'
                f'                    {h4}\n'
                f'                    {teaser_html}{signup_block}\n'
                f'                </div>'
            )

        elif col_type == "stacked":
            # Zwei Spalten übereinander in einer Grid-Zelle
            def render_section(sec):
                sec_title = sec.get("title", "")
                sec_h4 = f'<h4 class="vs-footer-col-title">{sec_title}</h4>' if sec_title else ""
                sec_links = sec.get("links", [])
                li = "".join(
                    f'<li><a href="{lnk["url"]}" target="_blank" rel="noopener">{lnk["label"]}</a></li>'
                    if lnk.get("external") else
                    f'<li><a href="{lnk["url"]}">{lnk["label"]}</a></li>'
                    for lnk in sec_links
                )
                # products sub-section
                prods = sec.get("products", [])
                prod_html = ""
                if prods:
                    p_url   = sec.get("products_url", "")
                    p_title = sec.get("products_title", "Produkte")
                    p_head  = f'<a href="{p_url}" class="vs-footer-sublabel-link">{p_title}</a>' if p_url else f'<span class="vs-footer-sublabel">{p_title}</span>'
                    p_items = "".join(f'<li><a href="{p["url"]}">→ {p["label"]}</a></li>' for p in prods)
                    p_more  = f'<li class="vs-footer-prod-more"><a href="{p_url}">→ Weitere Produkte</a></li>' if p_url else ""
                    prod_html = f'<p class="vs-footer-sublabel">{p_head}</p><ul>{p_items}{p_more}</ul>'
                # ki_items sub-section — als eigene h4
                ki_cfg = sec.get("ki_items", [])
                ki_html2 = ""
                if ki_cfg:
                    kt = sec.get("ki_title", "KI & Daten")
                    ki_h4_2 = f'<h4 class="vs-footer-col-title vs-footer-col-subtitle">{kt}</h4>'
                    ki_parts = []
                    for k in ki_cfg:
                        ext = ' target="_blank" rel="noopener"' if k.get("external") else ""
                        ki_parts.append(f'<li><a href="{k["url"]}"{ext}>{k["label"]}</a></li>')
                    ki_html2 = f'{ki_h4_2}<ul>{"".join(ki_parts)}</ul>'
                return f'{sec_h4}<ul>{li}</ul>{prod_html}{ki_html2}'

            sections    = col.get("sections", [])
            inner_parts = []
            for idx, sec in enumerate(sections):
                sep = '<div class="vs-footer-stack-sep"></div>' if idx > 0 else ""
                inner_parts.append(sep + render_section(sec))
            cols_html.append(f'<div class="vs-footer-col">{"".join(inner_parts)}</div>')

        else:
            links    = col.get("links", [])
            li_items = "".join(
                f'<li><a href="{lnk["url"]}" target="_blank" rel="noopener">{lnk["label"]}</a></li>'
                if lnk.get("external")
                else f'<li><a href="{lnk["url"]}">{lnk["label"]}</a></li>'
                for lnk in links
            )

            # Strategie sub-section (same h4 heading style as column title)
            strategie_items = col.get("strategie_items", [])
            strategie_html = ""
            if strategie_items:
                strat_title = col.get("strategie_title", "Strategie")
                strat_h4 = f'<h4 class="vs-footer-col-subtitle">{strat_title}</h4>'
                strat_parts = []
                for s in strategie_items:
                    ext_attr = ' target="_blank" rel="noopener"' if s.get("external") else ""
                    strat_parts.append(f'<li><a href="{s["url"]}"{ext_attr}>{s["label"]}</a></li>')
                strategie_html = f'{strat_h4}<ul>{"".join(strat_parts)}</ul>'

            products = col.get("products", [])
            products_html = ""
            if products:
                prod_url   = col.get("products_url", "")
                prod_title = col.get("products_title", "Produkte")
                prod_h4    = (
                    f'<h4 class="vs-footer-col-subtitle"><a href="{prod_url}" class="vs-footer-sub-h4-link">{prod_title}</a></h4>'
                    if prod_url else
                    f'<h4 class="vs-footer-col-subtitle">{prod_title}</h4>'
                )
                prod_items = "".join(
                    f'<li class="vs-footer-prod-item"><a href="{p["url"]}">→ {p["label"]}</a></li>'
                    for p in products
                )
                prod_more = (
                    f'<li class="vs-footer-prod-more vs-footer-prod-item"><a href="{prod_url}">→ Weitere Produkte</a></li>'
                    if prod_url else ""
                )
                products_html = f'{prod_h4}<ul>{prod_items}{prod_more}</ul>'

            feeds_items_cfg = col.get("feeds_items", [])
            feeds_html = ""
            if feeds_items_cfg:
                feeds_title = col.get("feeds_title", "Feeds & Social")
                feeds_h4 = f'<h4 class="vs-footer-col-subtitle">{feeds_title}</h4>'
                feeds_parts = []
                for f in feeds_items_cfg:
                    ext_attr = ' target="_blank" rel="noopener"' if f.get("external") else ""
                    feeds_parts.append(f'<li><a href="{f["url"]}"{ext_attr}>{f["label"]}</a></li>')
                feeds_html = f'{feeds_h4}<ul>{"".join(feeds_parts)}</ul>'

            main_list = f'<ul>{li_items}</ul>' if li_items else ''
            cols_html.append(
                f'<div class="vs-footer-col">{h4}{main_list}{strategie_html}{products_html}{feeds_html}</div>'
            )

    cols_joined = "\n                ".join(cols_html)

    # Bottom Bar
    year    = cfg("site", "copyright_year", default="2026")
    company = cfg("site", "company", default="")
    loc     = cfg("site", "location", default="")
    claim   = cfg("site", "claim", default="")
    legal   = cfg("legal", default=[])
    legal_links = "".join(
        f'<a href="{l["url"]}">{l["label"]}</a>'
        for l in legal
    )

    return f"""
        <footer class="gh-footer gh-outer">
            <div class="gh-footer-inner gh-inner">
                {trust_html}
                <div class="vs-footer-grid">
                    {cols_joined}
                </div>
                <div class="vs-footer-bottom">
                    <div class="vs-footer-copy">
                        &copy; {year} {company} &middot; {loc} &middot; {claim}
                    </div>
                    <div class="vs-footer-legal">
                        {legal_links}
                    </div>
                </div>
            </div>
        </footer>"""


# ---------------------------------------------------------------------------
# CSS (inline im <head>)
# ---------------------------------------------------------------------------
INLINE_CSS = """
        :root {
            --background-color: #ffffff;
            --ghost-accent-color: #f2902a;
        }

        /* Spacers */
        .vs-spacer    { height: 1rem; }
        .vs-spacer-lg { height: 2rem; }
        .gh-content .vs-spacer + *,
        .gh-content .vs-spacer-lg + * { margin-top: 0 !important; }

        /* ===== Grounding Page — Fact Grid <dl> ===== */
        .grounding-fact-grid {
            display: grid;
            grid-template-columns: minmax(140px, 220px) 1fr;
            gap: 0;
            margin: 2rem 0 2.4rem;
            border: 1px solid rgba(124,139,154,.2);
            border-radius: 6px;
            overflow: hidden;
            font-size: 1.5rem;
        }
        .grounding-fact-grid dt,
        .grounding-fact-grid dd {
            padding: 0.7em 1.1em;
            margin: 0;
            border-bottom: 1px solid rgba(124,139,154,.15);
        }
        .grounding-fact-grid dt {
            font-weight: 700;
            color: #3a4550;
            background: rgba(124,139,154,.07);
        }
        .grounding-fact-grid dd { color: #1a1a1a; }
        .grounding-fact-grid dt:last-of-type,
        .grounding-fact-grid dd:last-of-type { border-bottom: none; }

        /* Disambiguierungs-Block */
        .grounding-disambig {
            background: rgba(242,144,42,.07);
            border-left: 3px solid #f2902a;
            border-radius: 0 6px 6px 0;
            padding: 1.2em 1.4em;
            margin: 2rem 0;
        }
        .grounding-disambig p { margin: 0 0 0.4em; font-weight: 700; }
        .grounding-disambig ul { margin: 0.4em 0 0 1.2em; }
        .grounding-disambig li { margin-bottom: 0.3em; }

        /* Human Notice */
        .grounding-notice {
            font-size: 1.3rem;
            color: #738a94;
            border-top: 1px solid rgba(124,139,154,.2);
            padding-top: 1.2rem;
            margin-top: 3rem;
        }

        /* ===== Navigation — Desktop: Logo | Links(Mitte) | CTA ===== */
        .gh-navigation-inner {
            display: flex !important;
            flex-wrap: nowrap !important;
            align-items: center !important;
            max-width: 920px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            padding-top: 1.2rem !important;
            padding-bottom: 1.2rem !important;
            gap: 0 !important;
        }
        .gh-navigation-brand { flex: 0 0 auto !important; }
        .gh-navigation-menu {
            flex: 1 1 auto !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }
        .gh-navigation-actions { flex: 0 0 auto !important; }
        .gh-burger { display: none !important; }

        /* ===== Navigation — Mobile: Logo+CTA Zeile 1 | Links Zeile 2 ===== */
        @media (max-width: 767px) {
            .gh-navigation-inner {
                flex-wrap: wrap !important;
                padding-top: 0.9rem !important;
                padding-bottom: 0.4rem !important;
            }
            .gh-navigation-brand {
                flex: 1 1 auto !important;
            }
            .gh-navigation-actions {
                flex: 0 0 auto !important;
            }
            .gh-navigation-menu {
                flex: 0 0 100% !important;
                justify-content: flex-start !important;
                overflow-x: auto !important;
                padding-bottom: 0.6rem !important;
                -webkit-overflow-scrolling: touch;
            }
        }
        .vs-nav-cta {
            display: inline-flex;
            align-items: center;
            padding: 0.55em 1.3em;
            background: var(--ghost-accent-color);
            color: #fff !important;
            font-size: 1.4rem;
            font-weight: 700;
            border-radius: 6px;
            text-decoration: none;
            white-space: nowrap;
            transition: background 0.2s ease, opacity 0.2s ease;
        }
        .vs-nav-cta:hover { background: #e07f20; opacity: 1; }

        /* Feature Image — max 828px (720px Textlaufbreite + 15%) */
        .gh-article-image {
            max-width: 828px;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 2.4rem;
        }
        .gh-article-image img {
            border-radius: 6px;
        }
        /* Mindestabstand Feature Image → erster Content-Block */
        .gh-article-image + .gh-content > *:first-child {
            margin-top: 1.6rem;
        }

        /* CTA Button Fix */
        .gh-content a.gh-button {
            color: #fff !important;
            text-decoration: none !important;
        }
        p:has(> .cta-center) { text-align: center; }

        /* ===== 6-Spalten Footer ===== */
        .gh-footer {
            background-color: #fff;
            color: var(--color-secondary-text);
            padding-top: 4rem;
            padding-bottom: 2rem;
            border-top: 1px solid var(--color-border);
        }
        .gh-footer a { color: var(--color-primary-text); }
        .gh-footer a:hover { color: var(--ghost-accent-color); opacity: 1; }

        .vs-footer-trust {
            text-align: center;
            font-size: 1.4rem;
            padding-bottom: 2.5rem;
            margin-bottom: 2.5rem;
            border-bottom: 1px solid var(--color-border);
            color: var(--color-secondary-text);
            line-height: 1.8;
        }
        .vs-footer-trust-clients { margin-bottom: 0.4em; }
        .vs-footer-trust-member { font-size: 1.25rem; opacity: 0.75; }
        .vs-footer-trust a { color: var(--ghost-accent-color); }
        .vs-footer-sublabel-link {
            color: var(--color-primary-text) !important;
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 700;
            text-decoration: none;
        }
        .vs-footer-sublabel-link:hover { color: var(--ghost-accent-color) !important; }

        .vs-footer-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 3rem;
            padding-bottom: 3rem;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--color-border);
        }
        /* ── Inline Newsletter-Block im Artikel ───────────────────────────── */
        .vs-inline-newsletter {
            margin: 2.4em 0;
            padding: 1.6em 2em;
            background: #f8f5f0;
            border-left: 4px solid #f2902a;
            border-radius: 6px;
        }
        .vs-inline-newsletter strong { font-size: 1.5rem; }
        .vs-inline-newsletter p { margin: 0.4em 0 0; }
        .vs-inline-brevo { margin-top: 1em; }
        /* ────────────────────────────────────────────────────────────────── */
        .vs-footer-prod-more { margin-top: 0.4em; }
        .vs-footer-prod-more a { color: var(--ghost-accent-color) !important; font-size: 1.3rem; }
        .vs-footer-prod-item a { color: var(--color-secondary-text) !important; }
        .vs-footer-prod-item a:hover { color: var(--ghost-accent-color) !important; }
        .vs-footer-stack-sep {
            margin-top: 2.4rem;
        }
        .vs-footer-col-subtitle {
            margin-top: 2.2rem !important;
            margin-bottom: 0.9em !important;
        }
        .vs-footer-col > h4.vs-footer-col-subtitle:first-child {
            margin-top: 0 !important;
        }
        .vs-footer-sub-h4-link {
            color: var(--color-primary-text) !important;
            text-decoration: none;
        }
        .vs-footer-sub-h4-link:hover { color: var(--ghost-accent-color) !important; }
        .vs-footer-col h4 {
            color: var(--color-primary-text);
            font-size: 1.5rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1.2em;
        }
        .vs-footer-col ul { list-style: none; padding: 0; margin: 0; }
        .vs-footer-col li { margin-bottom: 0.6em; }
        .vs-footer-col li a { font-size: 1.4rem; color: var(--color-secondary-text); }
        .vs-footer-col li a:hover { color: var(--ghost-accent-color); }
        .vs-footer-col ul li a strong { color: var(--ghost-accent-color); }

        .vs-footer-address {
            font-size: 1.3rem;
            line-height: 1.7;
            color: var(--color-secondary-text);
            margin: 0 0 1.2rem;
        }
        .vs-footer-cta {
            display: inline-block;
            margin-top: 1.6rem;
            margin-bottom: 1.8rem;
            font-size: 1.3rem !important;
            padding: 0.6em 1.2em !important;
        }
        .vs-footer-sublabel {
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: rgba(0,0,0,.4);
            font-weight: 700;
            margin: 1.4rem 0 0.5rem;
        }
        .vs-footer-signup-btn {
            display: inline-block;
            margin-bottom: 1rem;
            font-size: 1.3rem !important;
            padding: 0.6em 1.2em !important;
        }

        .vs-footer-newsletter p {
            font-size: 1.3rem;
            margin-bottom: 1em;
            color: var(--color-secondary-text);
        }
        .vs-newsletter-form { display: flex; flex-direction: column; gap: 0.6em; }
        .vs-newsletter-form input {
            padding: 0.6em 0.8em;
            border: 1px solid var(--color-border);
            border-radius: 6px;
            background: var(--color-lighter-gray);
            color: var(--color-primary-text);
            font-size: 1.4rem;
        }
        .vs-newsletter-form input::placeholder { color: var(--color-secondary-text); }
        .vs-newsletter-form .gh-button {
            font-size: 1.3rem;
            padding: 0.6em 1em;
            color: #fff !important;
        }
        .vs-form-msg {
            font-size: 1.3rem;
            min-height: 1.8em;
            font-weight: 500;
        }
        .vs-input-name {
            /* Vorname-Feld: dezent optional markiert */
            opacity: 0.85;
        }
        .vs-footer-podcast-link {
            display: inline-block;
            margin-top: 0.8em;
            font-size: 1.3rem;
            color: var(--ghost-accent-color) !important;
        }

        /* ── Brevo-Formular viSales-Overrides ─────────────────────────────── */
        .vs-footer-newsletter .sib-form { text-align:left !important; background:transparent !important; padding:0 !important; }
        .vs-footer-newsletter .sib-form-container { max-width:100% !important; }
        .vs-footer-newsletter #sib-container { max-width:100% !important; border:none !important; background:transparent !important; padding:0 !important; margin-top:-0.4em !important; }
        .vs-footer-newsletter a { color:var(--color-primary-text) !important; text-decoration:underline !important; }
        .vs-footer-newsletter #sib-container a { color:var(--color-primary-text) !important; }
        .vs-footer-newsletter .sib-form-block p { margin:0 0 0.4em; font-size:1.3rem; }
        .vs-footer-newsletter .sib-form-block[style*="font-size:24px"] p,
        .vs-footer-newsletter .sib-form-block[style*="font-size:32px"] p { display:none; } /* "Visual Sales" Titel — schon im h4 vorhanden */
        .vs-footer-newsletter .entry__label { font-size:1.2rem !important; color:var(--color-primary-text) !important; }
        .vs-footer-newsletter .input { font-size:1.3rem !important; border-radius:6px !important; }
        .vs-footer-newsletter .sib-form-block__button { background-color:#f2902a !important; border-radius:6px !important; font-size:1.3rem !important; padding:0.6em 1.2em !important; width:100%; }
        .vs-footer-newsletter .entry__specification { font-size:1.1rem !important; }
        .vs-footer-newsletter .sib-form__declaration { margin-top:0.4em; }
        .vs-footer-newsletter .sib-form__declaration > div:first-child { display:none; } /* Schild-Icon ausblenden */
        .vs-footer-newsletter .sib-form__declaration p { font-size:1.1rem !important; color:var(--color-secondary-text) !important; }
        .vs-footer-newsletter .checkbox_tick_positive { flex-shrink:0; }
        /* ────────────────────────────────────────────────────────────────── */

        .vs-footer-bottom {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.3rem;
            color: var(--color-secondary-text);
        }
        .vs-footer-legal { display: flex; gap: 1.5em; }
        .vs-footer-legal a { color: var(--color-secondary-text); font-size: 1.3rem; }
        .vs-footer-copy { max-width: 60%; }

        @media (max-width: 1024px) {
            .vs-footer-grid { grid-template-columns: repeat(3, 1fr); }
        }
        @media (max-width: 640px) {
            .vs-footer-grid { grid-template-columns: 1fr; gap: 2.5rem; }
            .vs-footer-bottom { flex-direction: column; gap: 1em; text-align: center; }
            .vs-footer-copy { max-width: 100%; }
            .vs-footer-trust { font-size: 1.2rem; }
            .vs-footer-trust-sep { display: block; margin: 0.3em 0; }
        }

        /* ===== kg-toggle-card — Pfeil links ===== */
        .kg-toggle-card {
            background: transparent;
            border: 1px solid rgba(124, 139, 154, 0.4);
            border-radius: 4px;
            padding: 1.2em 1.4em;
        }
        .kg-toggle-heading {
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.8em;
            list-style: none;
            user-select: none;
        }
        .kg-toggle-card-icon {
            background: none;
            border: none;
            cursor: pointer;
            padding: 0;
            flex-shrink: 0;
            color: inherit;
            transition: transform 0.25s ease;
            display: flex;
            align-items: center;
        }
        .kg-toggle-card-icon svg { width: 20px; height: 20px; }
        .kg-toggle-card[data-kg-toggle-state="open"] .kg-toggle-card-icon {
            transform: rotate(90deg);
        }
        .kg-toggle-heading-text {
            font-size: 2rem;
            font-weight: 700;
            margin: 0;
            line-height: 1.3;
            font-family: var(--font-sans);
            color: var(--color-primary-text);
        }
        .kg-toggle-content {
            overflow: hidden;
            height: 0;
            transition: height 0.25s ease;
        }
        .kg-toggle-content > *              { margin-top: 1em; }
        .kg-toggle-content > *:first-child  { margin-top: 0.8em; }
        .kg-toggle-content > *:last-child   { margin-bottom: 0.2em; }

        /* ===== Praxis Card Grid ===== */
        .gh-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 4rem 2rem;
        }
        .gh-container.is-grid .gh-feed {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 3rem;
        }
        .gh-card-link {
            text-decoration: none;
            color: inherit;
            display: block;
        }
        .gh-card-link:hover .gh-card-title {
            color: var(--ghost-accent-color);
        }
        .gh-card-image {
            aspect-ratio: 16 / 9;
            overflow: hidden;
            border-radius: 6px;
            margin-bottom: 1.2rem;
            background: var(--color-lighter-gray);
        }
        .gh-card-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.3s ease;
        }
        .gh-card-link:hover .gh-card-image img {
            transform: scale(1.03);
        }
        .gh-card-tag {
            display: block !important;
            color: var(--ghost-accent-color);
            text-transform: uppercase;
            font-size: 1.2rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            margin-bottom: 0.5rem;
        }
        .gh-card-title {
            font-size: 2rem;
            font-weight: 700;
            margin: 0 0 0.8rem;
            line-height: 1.3;
            transition: color 0.2s ease;
        }
        .gh-card-meta {
            display: flex;
            align-items: center;
            gap: 0.5em;
            font-size: 1.3rem;
            color: var(--color-secondary-text);
            margin-top: 0.6rem;
        }
        .gh-card-author::after {
            content: "·";
            margin-left: 0.5em;
        }
        @media (max-width: 640px) {
            .gh-container.is-grid .gh-feed {
                grid-template-columns: 1fr;
                gap: 2rem;
            }
        }

        /* ===== Cookie-Banner ===== */
        .vs-cookie-banner {
            display: none;
            position: fixed;
            bottom: 0; left: 0; right: 0;
            z-index: 9999;
            background: #fff;
            border-top: 2px solid var(--ghost-accent-color);
            box-shadow: 0 -4px 24px rgba(0,0,0,.12);
            font-size: 1.4rem;
        }
        .vs-cookie-inner {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1.6rem 2rem;
            display: flex;
            align-items: center;
            gap: 2rem;
            flex-wrap: wrap;
        }
        .vs-cookie-text { flex: 1; min-width: 220px; }
        .vs-cookie-text strong { display: block; font-size: 1.5rem; margin-bottom: 0.3em; color: var(--color-primary-text); }
        .vs-cookie-text p { margin: 0; color: var(--color-secondary-text); font-size: 1.3rem; line-height: 1.5; }
        .vs-cookie-text a { color: var(--ghost-accent-color); text-decoration: underline; }
        .vs-cookie-actions { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }
        .vs-cookie-btn-all { font-size: 1.3rem !important; padding: 0.55em 1.3em !important; }
        .vs-cookie-btn-settings {
            background: none; border: 1px solid var(--color-border);
            border-radius: 6px; padding: 0.55em 1.1em;
            font-size: 1.3rem; cursor: pointer; color: var(--color-primary-text);
        }
        .vs-cookie-btn-settings:hover { border-color: var(--ghost-accent-color); color: var(--ghost-accent-color); }
        .vs-cookie-btn-deny {
            background: none; border: none; padding: 0.55em 0.5em;
            font-size: 1.2rem; cursor: pointer; color: var(--color-secondary-text);
            text-decoration: underline; text-underline-offset: 2px;
        }
        .vs-cookie-btn-deny:hover { color: var(--color-primary-text); }

        .vs-cookie-settings-panel {
            border-top: 1px solid var(--color-border);
            padding: 1.4rem 2rem 1.8rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        .vs-cookie-cats {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 0.8rem 2rem;
            margin-bottom: 1.4rem;
        }
        .vs-cookie-cat {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: 0.8rem 1rem;
            border: 1px solid var(--color-border);
            border-radius: 8px;
            cursor: pointer;
        }
        .vs-cookie-cat-info strong { display: block; font-size: 1.3rem; color: var(--color-primary-text); }
        .vs-cookie-cat-info small { font-size: 1.1rem; color: var(--color-secondary-text); }
        .vs-cookie-toggle {
            flex-shrink: 0;
            width: 40px; height: 22px;
            background: #d1d5db;
            border-radius: 99px;
            position: relative;
            cursor: pointer;
            transition: background .2s;
        }
        .vs-cookie-toggle span {
            position: absolute;
            top: 3px; left: 3px;
            width: 16px; height: 16px;
            background: #fff;
            border-radius: 50%;
            transition: transform .2s;
            box-shadow: 0 1px 3px rgba(0,0,0,.2);
        }
        .vs-cookie-toggle.is-on { background: var(--ghost-accent-color); }
        .vs-cookie-toggle.is-on span { transform: translateX(18px); }
        .vs-cookie-toggle--disabled { opacity: 0.45; cursor: not-allowed; }
        .vs-cookie-toggle--disabled.is-on { background: var(--ghost-accent-color); }
        .vs-cookie-settings-actions { display: flex; justify-content: flex-end; }
        .vs-cookie-btn-save { font-size: 1.3rem !important; padding: 0.55em 1.3em !important; }

        @media (max-width: 640px) {
            .vs-cookie-inner { flex-direction: column; align-items: flex-start; gap: 1.2rem; }
            .vs-cookie-cats { grid-template-columns: 1fr 1fr; }
        }

        /* ===== D0.2 — Kategorie-Badge (über Titel) — 1:1 Ghost-Stil ===== */
        .vs-post-category-badge {
            display: inline-block;
            color: var(--ghost-accent-color) !important;
            font-size: 1.2rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            text-decoration: none;
            margin-bottom: 1rem;
        }
        .vs-post-category-badge:hover { opacity: 0.8; }

        /* ===== D0.3 — Feature Image ===== */
        .vs-feature-image-wrap {
            display: block;
            max-width: 920px;
            margin: 0 auto 3rem;
            border-radius: 8px;
            overflow: hidden;
        }
        .vs-feature-image-wrap img {
            width: 100%;
            height: auto;
            display: block;
        }

        /* ===== D0.3 — Artikel-Meta (Ghost-Stil) ===== */
        .vs-article-meta {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-top: 2rem;
            margin-bottom: 3.2rem;
        }
        .vs-meta-avatar {
            width: 48px; height: 48px;
            border-radius: 50%;
            object-fit: cover;
            flex-shrink: 0;
        }
        .vs-meta-text {
            display: flex;
            flex-direction: column;
            gap: 0.15em;
        }
        .vs-meta-author {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--color-primary-text);
        }
        .vs-meta-author a { color: inherit; text-decoration: none; }
        .vs-meta-author a:hover { color: var(--ghost-accent-color); }
        .vs-meta-sub {
            font-size: 1.35rem;
            color: var(--color-secondary-text);
            display: flex;
            align-items: center;
            gap: 0.4em;
        }
        .vs-meta-sep { opacity: 0.5; }

        /* ===== D0.4 — Autor-Block unter Content ===== */
        .gh-main { padding-bottom: 0 !important; }
        .gh-footer { margin-top: 0 !important; }

        /* ===== FAQ-Block unter Autor-Box ===== */
        .vs-faq-block {
            max-width: 720px;
            margin-left: auto;
            margin-right: auto;
            padding-top: 6rem;
            padding-bottom: 4rem;
        }
        .vs-faq-heading {
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--color-secondary-text);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 1.6rem;
        }
        .vs-author-block {
            display: flex;
            align-items: flex-start;
            gap: 1.6rem;
            max-width: 720px;
            margin-left: auto;
            margin-right: auto;
            padding: 3rem 0 4rem;
            margin-top: 3rem;
            border-top: 1px solid var(--color-border);
        }
        .vs-author-block-avatar {
            width: 64px; height: 64px;
            border-radius: 50%;
            object-fit: cover;
            flex-shrink: 0;
        }
        .vs-author-block-text { display: flex; flex-direction: column; gap: 0.3rem; }
        .vs-author-block-label {
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            color: var(--color-secondary-text);
            font-weight: 700;
        }
        .vs-author-block-name {
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--color-primary-text);
            text-decoration: none;
        }
        .vs-author-block-name:hover { color: var(--ghost-accent-color); }
        .vs-author-bio {
            font-size: 1.35rem;
            color: var(--color-secondary-text);
            margin: 0.3rem 0 0;
            line-height: 1.6;
        }

        /* ===== D0.1 — Galerie-Grid (kg-gallery-card) ===== */
        .kg-gallery-card {
            width: 100%;
            margin: 2rem 0;
        }
        .kg-gallery-container {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .kg-gallery-row {
            display: flex;
            gap: 6px;
        }
        .kg-gallery-image {
            flex: 1;
            overflow: hidden;
            border-radius: 4px;
            cursor: pointer;
        }
        .kg-gallery-image img {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.3s ease;
        }
        .kg-gallery-image img:hover { transform: scale(1.02); }

        /* PhotoSwipe lightbox trigger */
        .kg-gallery-image a {
            display: block;
            width: 100%;
            height: 100%;
        }

        @media (max-width: 640px) {
            .vs-feature-image-wrap { border-radius: 0; }
            .kg-gallery-row { flex-direction: column; }
        }
"""


# ---------------------------------------------------------------------------
# JavaScript (inline am Ende des <body>)
# ---------------------------------------------------------------------------
INLINE_JS = """
    // kg-toggle-card interaktiv
    document.querySelectorAll('.kg-toggle-card').forEach(function(card) {
        var heading = card.querySelector('.kg-toggle-heading');
        var content = card.querySelector('.kg-toggle-content');
        if (!heading || !content) return;

        function openToggle() {
            card.setAttribute('data-kg-toggle-state', 'open');
            content.style.height = content.scrollHeight + 'px';
        }
        function closeToggle() {
            card.setAttribute('data-kg-toggle-state', 'close');
            content.style.height = '0';
        }

        heading.addEventListener('click', function() {
            card.getAttribute('data-kg-toggle-state') === 'open'
                ? closeToggle()
                : openToggle();
        });

        heading.setAttribute('tabindex', '0');
        heading.setAttribute('role', 'button');
        heading.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                heading.click();
            }
        });
    });

    // D0.1 — Galerie Lightbox via PhotoSwipe 5
    (function() {
        var galleries = document.querySelectorAll('.kg-gallery-card');
        if (!galleries.length) return;

        // Lade PhotoSwipe dynamisch
        var cssLink = document.createElement('link');
        cssLink.rel = 'stylesheet';
        cssLink.href = 'https://cdnjs.cloudflare.com/ajax/libs/photoswipe/5.4.4/photoswipe.min.css';
        document.head.appendChild(cssLink);

        var script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/photoswipe/5.4.4/umd/photoswipe.umd.min.js';
        script.onload = function() {
            galleries.forEach(function(gallery) {
                var images = gallery.querySelectorAll('.kg-gallery-image img');
                var items = [];
                images.forEach(function(img) {
                    var w = img.naturalWidth  || img.getAttribute('width')  || 1200;
                    var h = img.naturalHeight || img.getAttribute('height') || 800;
                    items.push({ src: img.src, width: parseInt(w), height: parseInt(h) });
                });

                images.forEach(function(img, idx) {
                    // Wrap in <a> falls noch nicht vorhanden
                    if (img.parentElement.tagName !== 'A') {
                        var a = document.createElement('a');
                        a.href = img.src;
                        img.parentNode.insertBefore(a, img);
                        a.appendChild(img);
                    }
                    img.parentElement.addEventListener('click', function(e) {
                        e.preventDefault();
                        var pswp = new PhotoSwipe({
                            dataSource: items,
                            index: idx,
                            bgOpacity: 0.92,
                            showHideAnimationType: 'fade',
                        });
                        pswp.init();
                    });
                });
            });
        };
        document.body.appendChild(script);
    })();
"""


# ---------------------------------------------------------------------------
# Draft-Banner
# ---------------------------------------------------------------------------
DRAFT_BANNER = """
    <div style="position:fixed;top:0;left:0;right:0;z-index:9999;
                background:#f2902a;color:#fff;text-align:center;
                padding:0.5em 1em;font-weight:700;font-size:1.4rem;
                letter-spacing:0.05em;">
        &#9888; ENTWURF &mdash; nicht ver&ouml;ffentlicht
    </div>
    <div style="height:2.5rem;"></div>"""


# ---------------------------------------------------------------------------
# JSON-LD Schema
# ---------------------------------------------------------------------------
def build_jsonld(meta, is_draft=False):
    """
    Generiert JSON-LD structured data aus site.yaml schema-Block + Seiten-Frontmatter.

    Siteweite Schemas (jede Seite):
      - Organization   (@id, foundingDate, address, knowsAbout, memberOf, sameAs)
      - Person         (@id, jobTitle, worksFor, knowsAbout, memberOf, sameAs)
      - ProfessionalService (Local SEO: geo, priceRange, telephone)
      - WebSite

    Seitenspezifisch:
      - Article        (posts: headline, datePublished, dateModified, keywords, image)
      - WebPage        (pages: name, description, isPartOf)

    Frontmatter-Felder die ausgewertet werden:
      title, meta_description, slug, type, date, date_modified,
      og_image, author, keywords, tags
    """
    if is_draft:
        return ""

    site_url   = cfg("site", "url",   default="https://visales.de").rstrip("/")
    site_title = cfg("site", "title", default="viSales")
    site_desc  = cfg("site", "description", default="")
    site_logo  = cfg("site", "logo",  default="assets/images/logo-visales.png")
    company    = cfg("site", "company", default="viSales GmbH")

    # Schema-Block aus site.yaml
    sc         = cfg("schema", default={})
    sc_org     = sc.get("organization", {})   if isinstance(sc, dict) else {}
    sc_person  = sc.get("person", {})         if isinstance(sc, dict) else {}
    sc_profserv= sc.get("professional_service", {}) if isinstance(sc, dict) else {}
    sc_website = sc.get("website", {})        if isinstance(sc, dict) else {}

    slug       = meta.get("slug", "page")
    title      = meta.get("title", site_title)
    page_desc  = meta.get("meta_description", site_desc)
    page_type  = meta.get("type", "page")
    date       = str(meta.get("date", ""))
    date_mod   = str(meta.get("date_modified", date))
    og_image   = meta.get("og_image", "")
    keywords   = meta.get("keywords", "")
    tags_raw   = meta.get("tags", [])
    canonical  = f"{site_url}/{slug}/"

    # keywords: aus 'keywords' oder 'tags' Frontmatter
    if not keywords and tags_raw:
        if isinstance(tags_raw, list):
            keywords = ", ".join(str(t) for t in tags_raw)
        elif isinstance(tags_raw, str):
            keywords = tags_raw

    # --------------- Hilfsfunktionen ----------------------------------------
    def member_of_list(members):
        return [{"@type": "Organization", "name": m.get("name",""), "url": m.get("url","")}
                for m in (members or [])]

    def logo_obj(url):
        return {"@type": "ImageObject", "url": url}

    def address_obj(a):
        return {
            "@type":           "PostalAddress",
            "streetAddress":   a.get("street", ""),
            "postalCode":      a.get("postal_code", ""),
            "addressLocality": a.get("city", ""),
            "addressRegion":   a.get("region", ""),
            "addressCountry":  a.get("country", "DE"),
        }

    # --------------- 1. Organization ----------------------------------------
    org_logo_url = sc_org.get("logo") or f"{site_url}/{site_logo}"
    org_addr     = sc_org.get("address", {})

    org_schema = {
        "@context":    "https://schema.org",
        "@type":       "Organization",
        "@id":         sc_org.get("id", f"{site_url}/#organization"),
        "name":        sc_org.get("name", company),
        "url":         site_url,
        "logo":        logo_obj(org_logo_url),
        "foundingDate": sc_org.get("founding_date", "2010"),
        "description": sc_org.get("description", site_desc),
        "address":     address_obj(org_addr),
        "areaServed":  sc_org.get("area_served", "DE"),
        "knowsAbout":  sc_org.get("knows_about", []),
        "memberOf":    member_of_list(sc_org.get("member_of", [])),
        "sameAs":      sc_org.get("same_as", []),
    }
    email = cfg("contact", "email", default="")
    phone = cfg("contact", "phone", default="")
    if email: org_schema["email"]     = email
    if phone: org_schema["telephone"] = phone

    # --------------- 2. Person -----------------------------------------------
    person_schema = {
        "@context":   "https://schema.org",
        "@type":      "Person",
        "@id":        sc_person.get("id", f"{site_url}/#gerhard-schroeder"),
        "name":          sc_person.get("name", cfg("author", "name", default="Gerhard Schröder")),
        "alternateName": sc_person.get("alternate_name", ""),
        "givenName":     sc_person.get("given_name", "Gerhard"),
        "familyName":    sc_person.get("family_name", "Schröder"),
        "birthDate":     sc_person.get("birth_year", ""),
        "birthPlace":    {"@type": "Place", "name": sc_person.get("birth_place", "")} if sc_person.get("birth_place") else None,
        "jobTitle":      sc_person.get("job_title", "Geschäftsführer"),
        "worksFor":   {"@id": sc_person.get("works_for_id",
                                            sc_org.get("id", f"{site_url}/#organization"))},
        "url":        sc_person.get("url", f"{site_url}/ueber-uns/"),
        "image":      sc_person.get("image", cfg("author", "avatar", default="")),
        "description": sc_person.get("description", ""),
        "knowsAbout": sc_person.get("knows_about", []),
        "memberOf":   member_of_list(sc_person.get("member_of", [])),
        "sameAs":     sc_person.get("same_as", []),
    }

    # --------------- 3. ProfessionalService (Local SEO) ----------------------
    profserv_addr = sc_org.get("address", {})
    geo_cfg       = sc_profserv.get("geo", {})
    profserv_schema = {
        "@context":    "https://schema.org",
        "@type":       "ProfessionalService",
        "name":        sc_profserv.get("name", company),
        "description": sc_profserv.get("description", site_desc),
        "url":         sc_profserv.get("url", site_url),
        "telephone":   sc_profserv.get("telephone", phone),
        "image":       sc_profserv.get("image", org_logo_url),
        "address":     address_obj(profserv_addr),
        "priceRange":  sc_profserv.get("price_range", "€€€"),
    }
    if geo_cfg.get("latitude"):
        profserv_schema["geo"] = {
            "@type":    "GeoCoordinates",
            "latitude":  geo_cfg["latitude"],
            "longitude": geo_cfg["longitude"],
        }

    # --------------- 4. WebSite ----------------------------------------------
    website_schema = {
        "@context": "https://schema.org",
        "@type":    "WebSite",
        "name":     sc_website.get("name", site_title),
        "url":      sc_website.get("url", site_url),
    }

    # --------------- 5. Article / WebPage / AboutPage (Grounding) ------------
    if page_type == "post" and date:
        author_name = meta.get("author", sc_person.get("name", "Gerhard Schröder"))
        page_schema = {
            "@context":         "https://schema.org",
            "@type":            "Article",
            "headline":         title,
            "description":      page_desc,
            "url":              canonical,
            "datePublished":    date,
            "dateModified":     date_mod or date,
            "author":           {"@id": sc_person.get("id", f"{site_url}/#gerhard-schroeder"),
                                 "@type": "Person", "name": author_name},
            "publisher":        {"@id": sc_org.get("id", f"{site_url}/#organization"),
                                 "@type": "Organization", "name": company,
                                 "logo": logo_obj(org_logo_url)},
            "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        }
        if og_image:
            page_schema["image"] = {"@type": "ImageObject",
                                    "url": og_image if og_image.startswith("http")
                                           else f"{site_url}/{og_image}"}
        if keywords:
            page_schema["keywords"] = keywords
    elif page_type == "grounding":
        # Grounding Page: AboutPage mit mainEntity → kanonische Entitätsdefinition
        grounding_entity = meta.get("grounding_entity", "organization")
        if grounding_entity == "person":
            main_entity_id = sc_person.get("id", f"{site_url}/#gerhard-schroeder")
        else:
            main_entity_id = sc_org.get("id", f"{site_url}/#organization")
        page_schema = {
            "@context":   "https://schema.org",
            "@type":      "AboutPage",
            "name":       title,
            "description": page_desc,
            "url":        canonical,
            "isPartOf":   {"@type": "WebSite", "name": site_title, "url": site_url},
            "mainEntity": {"@id": main_entity_id},
            "dateModified": date_mod or date,
        }
    else:
        page_schema = {
            "@context":  "https://schema.org",
            "@type":     "WebPage",
            "name":      title,
            "description": page_desc,
            "url":       canonical,
            "isPartOf":  {"@type": "WebSite", "name": site_title, "url": site_url},
        }

    # --------------- 6. FAQPage (optional — aus Frontmatter faq: Liste) ------
    faq_list   = meta.get("faq", [])
    faq_schema = None
    if faq_list and isinstance(faq_list, list):
        faq_schema = {
            "@context":   "https://schema.org",
            "@type":      "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name":  item.get("q", ""),
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text":  item.get("a", ""),
                    }
                }
                for item in faq_list if item.get("q") and item.get("a")
            ]
        }

    # --------------- Ausgabe -------------------------------------------------
    def ld(schema):
        return (f'    <script type="application/ld+json">\n'
                f'{json.dumps(schema, ensure_ascii=False, indent=2)}\n'
                f'    </script>')

    blocks = [ld(org_schema), ld(person_schema),
              ld(profserv_schema), ld(website_schema), ld(page_schema)]
    if faq_schema:
        blocks.append(ld(faq_schema))
    return "\n".join(blocks)


# ---------------------------------------------------------------------------
# Seite zusammenbauen
# ---------------------------------------------------------------------------
def calc_reading_time(html_text, wpm=200):
    """Schätzt Lesezeit aus HTML-Text (~200 Wörter/Min)."""
    import re as _re
    plain = _re.sub(r'<[^>]+>', ' ', html_text)
    words = len(plain.split())
    minutes = max(1, round(words / wpm))
    return minutes


def format_date_de(date_str):
    """Formatiert ISO-Datum → '05 Apr. 2026'."""
    months = ["Jan.","Feb.","Mär.","Apr.","Mai","Jun.",
              "Jul.","Aug.","Sep.","Okt.","Nov.","Dez."]
    try:
        parts = str(date_str).split("-")
        d, m, y = int(parts[0][-2:]) if len(parts[0]) > 4 else int(parts[2]), int(parts[1]), int(parts[0][:4])
        # Handle YYYY-MM-DD
        if len(parts) == 3 and len(parts[0]) == 4:
            y, m, d = int(parts[0]), int(parts[1]), int(parts[2][:2])
        return f"{d:02d} {months[m-1]} {y}"
    except Exception:
        return str(date_str)


def build_post_article_html(meta, content_html, is_draft=False):
    """Baut den <article>-Block für type:post mit Header, Meta, Feature Image, Autor-Block."""
    title         = meta.get("title", "")
    primary_tag   = meta.get("primary_tag", "")
    feature_image = meta.get("feature_image", "")
    date_raw      = meta.get("date", "") or meta.get("published_at", "")
    date_str      = str(date_raw).split("T")[0] if date_raw else ""

    # Author from frontmatter or site.yaml
    author_name   = meta.get("author",       cfg("author", "name",   default="Gerhard Schröder"))
    author_url    = cfg("author", "url",    default="/author/gerhard/")
    author_avatar = cfg("author", "avatar", default="")
    author_bio    = cfg("author", "bio",    default="")

    date_display  = format_date_de(date_str) if date_str else ""
    reading_time  = calc_reading_time(content_html)
    tag_slug      = primary_tag.lower().replace(" ", "-") if primary_tag else ""
    article_class = f"gh-article post{' tag-' + tag_slug if tag_slug else ''}"

    # D0.2 — Kategorie-Badge ÜBER dem Titel
    badge_html = ""
    if primary_tag:
        badge_html = f'<a class="vs-post-category-badge" href="/tag/{tag_slug}/">{primary_tag}</a>\n'

    # Kompakte Meta-Zeile: Avatar · Name · Datum · Lesezeit
    avatar_html = ""
    if author_avatar:
        avatar_html = f'<img class="vs-meta-avatar" src="{author_avatar}" alt="{author_name}">'

    meta_html = f"""
            <div class="gh-article-meta vs-article-meta">
                {avatar_html}
                <div class="vs-meta-text">
                    <span class="vs-meta-author"><a href="{author_url}">{author_name}</a></span>
                    <div class="vs-meta-sub">
                        <time datetime="{date_str}">{date_display}</time>
                        <span class="vs-meta-sep">&mdash;</span>
                        <span>{reading_time} min read</span>
                    </div>
                </div>
            </div>"""

    # D0.3 — Feature Image (kein Badge darauf)
    feature_html = ""
    if feature_image:
        feature_html = f"""
    <figure class="gh-article-image vs-feature-image-wrap">
        <img src="{feature_image}" alt="{title}" loading="eager">
    </figure>"""

    # Autor-Block unter Content
    author_block_html = ""
    if author_name and author_avatar:
        bio_html = f'<p class="vs-author-bio">{author_bio}</p>' if author_bio else ""
        author_block_html = f"""
            <aside class="vs-author-block gh-canvas">
                <img class="vs-author-block-avatar" src="{author_avatar}" alt="{author_name}">
                <div class="vs-author-block-text">
                    <span class="vs-author-block-label">Über den Autor</span>
                    <a href="{author_url}" class="vs-author-block-name">{author_name}</a>
                    {bio_html}
                </div>
            </aside>"""

    # FAQ-Block aus Frontmatter — nach Autor-Box, vor Footer
    # Rendert via convert_toggles() → gleiches kg-toggle-card Design wie Content-Toggles
    faq_block_html = ""
    faq_list = meta.get("faq", [])
    if faq_list and isinstance(faq_list, list):
        faq_items_raw = ""
        for item in faq_list:
            q = item.get("q", "")
            a = item.get("a", "")
            if q and a:
                faq_items_raw += f"<details><summary>{q}</summary>{a}</details>\n"
        if faq_items_raw:
            faq_items_html = convert_toggles(faq_items_raw)
            faq_block_html = f"""
            <section class="vs-faq-block gh-canvas">
                <h2 class="vs-faq-heading">Häufige Fragen</h2>
                {faq_items_html}
            </section>"""

    draft_label = ' <span style="color:#f2902a">[DRAFT]</span>' if is_draft else ""

    return f"""        <article class="{article_class}">
            <header class="gh-article-header gh-canvas">
                {badge_html}<h1 class="gh-article-title is-title">{title}{draft_label}</h1>
                {meta_html}
            </header>
            {feature_html}
            <section class="gh-content gh-canvas is-body">
                {content_html}
            </section>
            {author_block_html}
            {faq_block_html}
        </article>"""


def build_page(meta, content_html, is_draft=False):
    """Baut eine komplette HTML-Seite aus Meta + Content + Config."""

    title         = meta.get("title",        cfg("site", "title",       default="viSales"))
    description   = meta.get("meta_description", cfg("site", "description", default=""))
    slug          = meta.get("slug",         "page")
    og_image      = meta.get("og_image",     "")
    feature_image = meta.get("feature_image","")
    page_type     = meta.get("type",         "page")

    site_title  = cfg("site", "title",  default="viSales")
    site_url    = cfg("site", "url",    default="https://visales.de").rstrip("/")
    logo        = cfg("site", "logo",   default="assets/images/logo-visales.png")

    # Relativer Basis-Pfad für Assets — je nach Slug-Tiefe (z.B. "tag/skill-abo" → "../")
    slug_depth = len([p for p in slug.split("/") if p]) - 1
    base       = "../" * max(0, slug_depth)

    canonical    = f"{site_url}/{slug}/"
    # og:image priority: feature_image > og_image > default logo
    og_img_src   = feature_image or og_image
    og_image_url = og_img_src if og_img_src.startswith("http") else (
                   f"{site_url}/{og_img_src}" if og_img_src else f"{site_url}/assets/images/logo-visales.png")
    og_type      = "article" if page_type == "post" else "website"
    robots       = "noindex, nofollow" if is_draft else "index, follow"
    full_title      = f"{title} \u2014 {site_title}" if title != site_title else title

    nav_html     = build_nav_html(active_slug=slug)
    footer_html  = build_footer_html()

    # CTA-Button aus site.yaml nav_cta
    nav_cta_cfg = cfg("nav_cta", default={})
    if nav_cta_cfg and isinstance(nav_cta_cfg, dict):
        cta_label = nav_cta_cfg.get("label", "Kontakt")
        cta_url   = nav_cta_cfg.get("url", "/kontakt/")
        nav_cta_html = f'<a class="vs-nav-cta" href="{cta_url}">{cta_label}</a>'
    else:
        nav_cta_html = ""
    draft_banner = DRAFT_BANNER if is_draft else ""
    jsonld       = build_jsonld(meta, is_draft=is_draft)

    # Article HTML block — post / listing / page template
    if page_type == "post":
        article_html = build_post_article_html(meta, content_html, is_draft)
    elif page_type == "listing":
        # Kein gh-canvas — Card-Grid steuert Breite selbst via gh-container
        article_html = (
            f'        <article class="gh-article">\n'
            f'            <section class="gh-content is-body">\n'
            f'                {content_html}\n'
            f'            </section>\n'
            f'        </article>'
        )
    else:
        draft_label = ' <span style="color:#f2902a">[DRAFT]</span>' if is_draft else ""
        article_html = (
            f'        <article class="gh-article">\n'
            f'            <header class="gh-article-header gh-canvas">\n'
            f'                <h1 class="gh-article-title is-title">{title}{draft_label}</h1>\n'
            f'            </header>\n'
            f'            <section class="gh-content gh-canvas is-body">\n'
            f'                {content_html}\n'
            f'            </section>\n'
            f'        </article>'
        )

    # Brevo-Inject nur wenn Embed vorhanden
    brevo_head_inject = f"<!-- Brevo Form Styles -->\n{BREVO_HEAD}" if BREVO_HEAD else ""
    brevo_foot_inject = f"<!-- Brevo Form Scripts -->\n{BREVO_FOOT}" if BREVO_FOOT else ""

    # Cookie-Banner
    cookie_banner = build_cookie_banner()

    return f"""<!DOCTYPE html>
<html lang="de" class="has-dark-text">
<head>
    <title>{full_title}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <meta name="robots" content="{robots}">
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" type="application/rss+xml" title="viSales – Artikel &amp; Insights" href="{base}rss.xml">
    <link rel="alternate" type="application/rss+xml" title="Visual Com Podcast" href="https://visualcom.podcaster.de/visual-com.rss">

    <!-- Google tag (gtag.js) — consent-gesteuert -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-8JEPNB0BL5"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        // Default: alles verweigern bis Consent
        gtag('consent', 'default', {{
            'ad_storage': 'denied',
            'analytics_storage': 'denied',
            'wait_for_update': 500
        }});
        gtag('js', new Date());
        gtag('config', 'G-8JEPNB0BL5');
        gtag('config', 'AW-1024175020');
    </script>

    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:image" content="{og_image_url}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{og_image_url}">

    <!-- Preload -->
    <link rel="preload" as="style" href="{base}assets/css/screen.css">
    <link rel="preload" as="font" type="font/woff2" href="{base}assets/fonts/atkinson-regular.woff2" crossorigin="anonymous">
    <link rel="preload" as="font" type="font/woff2" href="{base}assets/fonts/atkinson-bold.woff2" crossorigin="anonymous">

    <!-- Fonts -->
    <style>
        @font-face {{
            font-family: "Atkinson Hyperlegible";
            font-style: normal; font-weight: 400; font-display: swap;
            src: url({base}assets/fonts/atkinson-regular.woff2) format("woff2");
        }}
        @font-face {{
            font-family: "Atkinson Hyperlegible";
            font-style: italic; font-weight: 400; font-display: swap;
            src: url({base}assets/fonts/atkinson-italic.woff2) format("woff2");
        }}
        @font-face {{
            font-family: "Atkinson Hyperlegible";
            font-style: normal; font-weight: 700; font-display: swap;
            src: url({base}assets/fonts/atkinson-bold.woff2) format("woff2");
        }}
        @font-face {{
            font-family: "Atkinson Hyperlegible";
            font-style: italic; font-weight: 700; font-display: swap;
            src: url({base}assets/fonts/atkinson-bold-italic.woff2) format("woff2");
        }}
    </style>

    <!-- Theme CSS -->
    <link rel="stylesheet" type="text/css" href="{base}assets/css/screen.css">

    <!-- SkillCMS Custom Styles -->
    <style>{INLINE_CSS}
    </style>

    <!-- Structured Data -->
{jsonld}
{brevo_head_inject}
</head>
<body class="{'post-template' if page_type == 'post' else 'page-template'} page-{slug} has-sans-title has-sans-body">
{draft_banner}
<div class="gh-viewport">

    <!-- NAVIGATION -->
    <header id="gh-navigation" class="gh-navigation is-left-logo gh-outer">
        <div class="gh-navigation-inner gh-inner">
            <div class="gh-navigation-brand">
                <a class="gh-navigation-logo is-title" href="/">
                    <img src="{base}{logo}" alt="{site_title}">
                </a>
                <button class="gh-burger gh-icon-button" aria-label="Menu">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <nav class="gh-navigation-menu">
                <ul class="nav">
                    {nav_html}
                </ul>
            </nav>
            <div class="gh-navigation-actions">{nav_cta_html}</div>
        </div>
    </header>

    <!-- MAIN CONTENT -->
    <main class="gh-main">
{article_html}
    </main>

    {footer_html}

</div>

<script src="{base}assets/js/source.js"></script>
<script>{INLINE_JS}
</script>
{brevo_foot_inject}
{cookie_banner}
</body>
</html>"""


# ---------------------------------------------------------------------------
# Einzelne Datei bauen (intern — arbeitet mit absolutem Dateipfad)
# ---------------------------------------------------------------------------
def build_file(md_path, include_drafts=False, drafts_only=False):
    """
    Baut eine HTML-Seite aus einem absoluten Markdown-Dateipfad.
    Output-Slug kommt aus dem Frontmatter-Feld 'slug:' (flat URL-Struktur).
    Gibt (True, meta) | (False, {}) | (True, None/skipped) zurück.
    Seiten mit type:listing werden übersprungen — build_praxis_listing() übernimmt.
    """
    if not os.path.exists(md_path):
        print(f"  ✗ {md_path} nicht gefunden")
        return False, {}

    with open(md_path, "r", encoding="utf-8") as f:
        raw = f.read()

    meta, body = parse_frontmatter(raw)

    # Listing-Seiten werden von build_praxis_listing() gebaut, nicht hier
    if meta.get("type", "page").lower() == "listing":
        return True, None

    # Slug aus Frontmatter; Fallback: Dateiname ohne Datum-Präfix und .md
    filename = os.path.splitext(os.path.basename(md_path))[0]
    # Datum-Präfix entfernen (z.B. "2026-04-05-slug" → "slug")
    filename_clean = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename)
    slug = meta.get("slug", filename_clean)

    status   = meta.get("status", "published").lower()
    is_draft = (status == "draft")

    if is_draft and not include_drafts:
        print(f"  ○ {slug}.html übersprungen (Entwurf)")
        return True, None

    if not is_draft and drafts_only:
        return True, None

    content_html = md_to_html(body)
    page_html    = build_page(meta, content_html, is_draft=is_draft)

    out_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html)

    draft_marker = " [ENTWURF]" if is_draft else ""
    rel_path     = os.path.relpath(md_path, SITE_DIR)
    print(f"  ✓ {slug}.html{draft_marker} ← {rel_path} ({len(page_html):,} Bytes)")
    return True, {**meta, "slug": slug}


# ---------------------------------------------------------------------------
# Einzelne Seite bauen (CLI-Interface: nach Slug suchen)
# ---------------------------------------------------------------------------
def build_single(slug, include_drafts=False, drafts_only=False):
    """
    Sucht content/{slug}.md oder content/posts/*{slug}.md und baut die Seite.
    """
    # 1. In content/pages/ und content/ki/
    for subdir in ["pages", "ki", "articles", "drafts"]:
        direct = os.path.join(CONTENT_DIR, subdir, f"{slug}.md")
        if os.path.exists(direct):
            return build_file(direct, include_drafts=include_drafts, drafts_only=drafts_only)

    # 2. In content/posts/ (mit optionalem Datum-Präfix)
    posts_dir = os.path.join(CONTENT_DIR, "articles")
    if os.path.isdir(posts_dir):
        for fname in os.listdir(posts_dir):
            if fname.endswith(".md") and slug in fname:
                return build_file(
                    os.path.join(posts_dir, fname),
                    include_drafts=include_drafts,
                    drafts_only=drafts_only,
                )

    print(f"  ✗ Keine Markdown-Datei für '{slug}' gefunden")
    return False, {}


# ---------------------------------------------------------------------------
# rss.xml generieren
# ---------------------------------------------------------------------------
def build_rss():
    """
    Erzeugt rss.xml (RSS 2.0) aus allen published Posts in content/posts/.
    Sortiert nach Datum absteigend. Inkl. Atom self-link und media:content für Feature Images.
    """
    site_url    = cfg("site", "url",         default="https://visales.de").rstrip("/")
    site_title  = cfg("site", "title",       default="viSales")
    site_desc   = cfg("site", "description", default="")
    email       = cfg("contact", "email",    default="")
    author_name = cfg("author",  "name",     default="Gerhard Schröder")
    author_tag  = f"{email} ({author_name})" if email else author_name

    posts_dir = os.path.join(CONTENT_DIR, "articles")
    items     = []

    if os.path.isdir(posts_dir):
        for fname in sorted(os.listdir(posts_dir)):
            if not fname.endswith(".md"):
                continue
            meta = read_post_meta_yaml(os.path.join(posts_dir, fname))
            if str(meta.get("status", "published")).lower() != "published":
                continue

            filename       = os.path.splitext(fname)[0]
            filename_clean = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename)
            slug           = str(meta.get("slug", filename_clean))
            date_raw       = meta.get("date", "")
            date_str       = str(date_raw).split("T")[0] if date_raw else ""
            title          = str(meta.get("title", "")).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            description    = str(meta.get("meta_description", "")).replace("&", "&amp;").replace("<", "&lt;")
            feature_image  = str(meta.get("feature_image", ""))
            link           = f"{site_url}/{slug}/"

            # pubDate im RFC-822-Format: "Sat, 05 Apr 2026 00:00:00 +0000"
            pub_date = ""
            if date_str:
                try:
                    parts   = date_str.split("-")
                    y, m, d = int(parts[0]), int(parts[1]), int(parts[2][:2])
                    dt      = datetime(y, m, d, tzinfo=timezone.utc)
                    pub_date = dt.strftime("%a, %d %b %Y %H:%M:%S +0000")
                except Exception:
                    pub_date = ""

            enclosure_tag = ""
            if feature_image:
                enclosure_tag = f'\n      <enclosure url="{feature_image}" type="image/jpeg" length="0"/>'

            items.append((date_str, (
                f'  <item>\n'
                f'    <title>{title}</title>\n'
                f'    <link>{link}</link>\n'
                f'    <guid isPermaLink="true">{link}</guid>\n'
                f'    <description>{description}</description>\n'
                f'    <pubDate>{pub_date}</pubDate>\n'
                f'    <author>{author_tag}</author>'
                f'{enclosure_tag}\n'
                f'  </item>'
            )))

    # Neueste zuerst
    items.sort(key=lambda x: x[0], reverse=True)
    items_xml = "\n".join(item for _, item in items)

    now_rfc822 = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

    rss = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"\n'
        '  xmlns:atom="http://www.w3.org/2005/Atom"\n'
        '  xmlns:content="http://purl.org/rss/1.0/modules/content/">\n'
        '  <channel>\n'
        f'    <title>{site_title}</title>\n'
        f'    <link>{site_url}/</link>\n'
        f'    <description>{site_desc}</description>\n'
        f'    <language>de</language>\n'
        f'    <lastBuildDate>{now_rfc822}</lastBuildDate>\n'
        f'    <atom:link href="{site_url}/rss.xml" rel="self" type="application/rss+xml"/>\n'
        f'{items_xml}\n'
        '  </channel>\n'
        '</rss>\n'
    )

    out_path = os.path.join(OUTPUT_DIR, "rss.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(rss)

    print(f"  ✓ rss.xml ({len(items)} Item(s))")


# ---------------------------------------------------------------------------
# sitemap.xml generieren
# ---------------------------------------------------------------------------
def build_sitemap(published_pages):
    """
    Erzeugt sitemap.xml aus einer Liste von Dicts mit keys:
        slug, type, date (optional)
    published_pages: nur published, keine Drafts.
    """
    site_url = cfg("site", "url", default="https://visales.de").rstrip("/")
    now      = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Priorität nach Seiten-Typ
    priority_map = {
        "page":        "0.8",
        "leistung":    "0.9",
        "fallbeispiel": "0.7",
        "seo":         "0.6",
        "post":        "0.6",
    }
    changefreq_map = {
        "page":        "monthly",
        "leistung":    "monthly",
        "fallbeispiel": "yearly",
        "seo":         "monthly",
        "post":        "yearly",
    }

    url_blocks = []
    for page in published_pages:
        slug       = page["slug"]
        page_type  = page.get("type", "page")
        lastmod    = page.get("date", "") or now   # Fallback: heutiges Build-Datum
        priority   = priority_map.get(page_type, "0.7")
        changefreq = changefreq_map.get(page_type, "monthly")

        url_blocks.append(
            f"  <url>\n"
            f"    <loc>{site_url}/{slug}/</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            f"    <changefreq>{changefreq}</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            f"  </url>"
        )

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(url_blocks)
        + "\n</urlset>\n"
    )

    out_path = os.path.join(OUTPUT_DIR, "sitemap.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"  ✓ sitemap.xml ({len(url_blocks)} URL(s))")


# ---------------------------------------------------------------------------
# robots.txt generieren
# ---------------------------------------------------------------------------
def build_robots():
    """Erzeugt robots.txt mit Sitemap-Verweis."""
    site_url = cfg("site", "url", default="https://visales.de").rstrip("/")

    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {site_url}/sitemap.xml\n"
    )

    out_path = os.path.join(OUTPUT_DIR, "robots.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("  ✓ robots.txt")


# ---------------------------------------------------------------------------
# llms.txt generieren (KI-Crawler-Standard)
# ---------------------------------------------------------------------------
def build_llms_txt(published_pages):
    """
    Erzeugt llms.txt nach dem Standard von llmstxt.org.
    Format: Markdown — H1 Site-Name, Blockquote Tagline,
    dann Abschnitte für Seiten und Posts mit kurzen Beschreibungen.
    """
    site_url     = cfg("site", "url",         default="https://visales.de").rstrip("/")
    site_title   = cfg("site", "title",       default="viSales")
    site_desc    = cfg("site", "description", default="")
    site_tagline = cfg("site", "tagline",     default=site_desc)

    lines = []
    lines.append(f"# {site_title}\n")
    if site_tagline:
        lines.append(f"> {site_tagline}\n")
    lines.append("")

    # Grounding Pages zuerst — kanonische Entitätsdefinitionen
    grounding = [p for p in published_pages if p.get("type") == "grounding"]
    if grounding:
        lines.append("## Identität\n")
        lines.append("> Kanonische Entitätsdefinitionen für KI-Systeme und Suchmaschinen.\n")
        for p in grounding:
            slug    = p.get("slug", "").strip("/")
            title   = p.get("title", slug)
            excerpt = p.get("excerpt", "")
            url     = f"{site_url}/{slug}/"
            entry   = f"- [{title}]({url})"
            if excerpt:
                entry += f": {excerpt}"
            lines.append(entry)
        lines.append("")

    # Seiten (ohne Grounding Pages)
    pages = [p for p in published_pages if p.get("type") not in ("post", "grounding")]
    if pages:
        lines.append("## Seiten\n")
        for p in pages:
            slug    = p.get("slug", "").strip("/")
            title   = p.get("title", slug)
            excerpt = p.get("excerpt", "")
            url     = f"{site_url}/{slug}/" if slug else site_url + "/"
            entry   = f"- [{title}]({url})"
            if excerpt:
                entry += f": {excerpt}"
            lines.append(entry)
        lines.append("")

    # Posts
    posts = [p for p in published_pages if p.get("type") == "post"]
    if posts:
        # Neueste zuerst
        posts_sorted = sorted(posts, key=lambda x: str(x.get("date", "")), reverse=True)
        lines.append("## Artikel\n")
        for p in posts_sorted:
            slug    = p.get("slug", "").strip("/")
            title   = p.get("title", slug)
            excerpt = p.get("excerpt", "")
            url     = f"{site_url}/{slug}/"
            entry   = f"- [{title}]({url})"
            if excerpt:
                entry += f": {excerpt}"
            lines.append(entry)
        lines.append("")

    # Optional: Maschinenlesbare Zusatzquellen
    lines.append("## Weitere Quellen\n")
    lines.append(f"- [RSS Feed]({site_url}/rss.xml): Alle Artikel als RSS 2.0")
    lines.append(f"- [Sitemap]({site_url}/sitemap.xml): Vollständige URL-Liste")
    lines.append("")

    content = "\n".join(lines)
    out_path = os.path.join(OUTPUT_DIR, "llms.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("  ✓ llms.txt")


# ---------------------------------------------------------------------------
# Praxis-Listing /praxis/ bauen
# ---------------------------------------------------------------------------
def read_post_meta_yaml(md_path):
    """Liest Frontmatter einer Markdown-Datei via yaml.safe_load (vollständig)."""
    with open(md_path, "r", encoding="utf-8") as f:
        raw = f.read()
    if not raw.startswith("---"):
        return {}
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except Exception:
        return {}


def build_tag_listing(tag_slug):
    """
    Erzeugt tag/{tag_slug}.html — Card-Grid-Übersicht für einen Tag.
    Filtert published Posts nach primary_tag oder tags-Liste.
    Liest optionale Metadata aus content/tags/{tag_slug}.md.
    """
    posts_dir = os.path.join(CONTENT_DIR, "articles")

    # Optionale Tag-Metadata
    tag_md = os.path.join(CONTENT_DIR, "tags", f"{tag_slug}.md")
    if os.path.exists(tag_md):
        tag_meta_file = read_post_meta_yaml(tag_md)
        tag_label       = str(tag_meta_file.get("title", tag_slug.replace("-", " ").title()))
        tag_description = str(tag_meta_file.get("meta_description", ""))
    else:
        tag_label       = tag_slug.replace("-", " ").title()
        tag_description = ""

    # Posts mit diesem Tag sammeln
    post_data = []
    if os.path.isdir(posts_dir):
        for fname in sorted(os.listdir(posts_dir)):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(posts_dir, fname)
            meta  = read_post_meta_yaml(fpath)

            if str(meta.get("status", "published")).lower() != "published":
                continue

            primary_tag = str(meta.get("primary_tag", "")).strip()
            tags_raw    = meta.get("tags", [])
            if isinstance(tags_raw, str):
                tags_list = [t.strip() for t in tags_raw.split(",")]
            elif isinstance(tags_raw, list):
                tags_list = [str(t).strip() for t in tags_raw]
            else:
                tags_list = []

            if primary_tag != tag_slug and tag_slug not in tags_list:
                continue

            filename       = os.path.splitext(fname)[0]
            filename_clean = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename)
            slug           = str(meta.get("slug", filename_clean))
            date_raw       = meta.get("date", "")
            date_str       = str(date_raw).split("T")[0] if date_raw else ""

            post_data.append({
                "slug":          slug,
                "title":         str(meta.get("title", "")),
                "feature_image": str(meta.get("feature_image", "")),
                "primary_tag":   primary_tag,
                "date":          date_str,
            })

    # Neueste zuerst
    post_data.sort(key=lambda p: p.get("date", ""), reverse=True)

    author_name = cfg("author", "name", default="Gerhard Schröder")

    # Cards bauen
    cards_html = []
    for p in post_data:
        post_slug     = p["slug"]
        title         = p["title"]
        feature_image = p["feature_image"]
        pt            = p["primary_tag"]
        date_str      = p["date"]
        date_display  = format_date_de(date_str) if date_str else ""
        pt_slug       = pt.lower().replace(" ", "-") if pt else ""
        pt_label      = pt.upper() if pt else ""
        card_class    = f"gh-card post{' tag-' + pt_slug if pt_slug else ''}"

        img_html = ""
        if feature_image:
            img_html = (
                f'                <figure class="gh-card-image">'
                f'<img src="{feature_image}" alt="{title}" loading="lazy"></figure>\n'
            )

        tag_card_html = ""
        if pt_label:
            tag_card_html = f'                <p class="gh-card-tag">{pt_label}</p>\n'

        cards_html.append(
            f'            <article class="{card_class}">\n'
            f'                <a class="gh-card-link" href="/{post_slug}/">\n'
            f'{img_html}'
            f'{tag_card_html}'
            f'                    <h3 class="gh-card-title is-title">{title}</h3>\n'
            f'                    <footer class="gh-card-meta">\n'
            f'                        <span class="gh-card-author">{author_name}</span>\n'
            f'                        <time class="gh-card-date" datetime="{date_str}">{date_display}</time>\n'
            f'                    </footer>\n'
            f'                </a>\n'
            f'            </article>'
        )

    cards_joined = "\n".join(cards_html)
    content_html = (
        '<div class="gh-container is-grid">\n'
        '    <div class="gh-feed">\n'
        f'{cards_joined}\n'
        '    </div>\n'
        '</div>'
    )

    listing_meta = {
        "title":            tag_label,
        "slug":             f"tag/{tag_slug}",
        "type":             "listing",
        "meta_description": tag_description,
    }

    page_html = build_page(listing_meta, content_html)

    # Output: site/tag/{tag_slug}.html
    tag_dir  = os.path.join(OUTPUT_DIR, "tag")
    os.makedirs(tag_dir, exist_ok=True)
    out_path = os.path.join(tag_dir, f"{tag_slug}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html)

    print(f"  ✓ tag/{tag_slug}.html ({len(post_data)} Post(s), {len(page_html):,} Bytes)")


# ---------------------------------------------------------------------------
# Alle Seiten bauen
# ---------------------------------------------------------------------------
def collect_md_files():
    """Sammelt alle Markdown-Dateien aus content/ und content/posts/."""
    files = []

    # content/pages/*.md, ki/*.md, articles/*.md, drafts/*.md
    for subdir in ["pages", "ki", "articles", "drafts"]:
        d = os.path.join(CONTENT_DIR, subdir)
        if os.path.isdir(d):
            for fname in sorted(os.listdir(d)):
                if fname.endswith(".md"):
                    files.append(os.path.join(d, fname))

    return files


def build_all(include_drafts=False, drafts_only=False):
    """Baut alle Markdown-Dateien in content/ und content/posts/ + sitemap.xml + robots.txt."""
    all_files = collect_md_files()
    if not all_files:
        print("Keine Markdown-Dateien in content/ gefunden.")
        return

    mode = ""
    if drafts_only:
        mode = " (nur Entwürfe)"
    elif include_drafts:
        mode = " (inkl. Entwürfe)"

    # Seiten vs. Posts für übersichtliche Ausgabe aufteilen
    page_files = [f for f in all_files if "/posts/" not in f]
    post_files = [f for f in all_files if "/posts/" in f]

    total = len(all_files)
    print(f"SkillCMS Build{mode} — {total} Datei(en) ({len(page_files)} Seiten, {len(post_files)} Posts)\n")

    published_pages = []

    if page_files:
        print("── Seiten ──────────────────────────")
        for fpath in page_files:
            ok, meta = build_file(fpath, include_drafts=include_drafts, drafts_only=drafts_only)
            if ok and meta:
                published_pages.append({
                    "slug":    meta.get("slug", ""),
                    "type":    meta.get("type", "page"),
                    "date":    meta.get("date", ""),
                    "title":   meta.get("title", ""),
                    "excerpt": meta.get("excerpt", meta.get("description", "")),
                })

    if post_files:
        print("\n── Posts ───────────────────────────")
        for fpath in post_files:
            ok, meta = build_file(fpath, include_drafts=include_drafts, drafts_only=drafts_only)
            if ok and meta:
                published_pages.append({
                    "slug":    meta.get("slug", ""),
                    "type":    meta.get("type", "post"),
                    "date":    meta.get("date", ""),
                    "title":   meta.get("title", ""),
                    "excerpt": meta.get("excerpt", meta.get("description", "")),
                })

    # Tag-Listings + sitemap.xml + robots.txt nur beim Full-Build
    if not drafts_only:
        # Alle einzigartigen Tags aus published Posts sammeln
        all_tags = set()
        posts_dir_scan = os.path.join(CONTENT_DIR, "articles")
        if os.path.isdir(posts_dir_scan):
            for fname in os.listdir(posts_dir_scan):
                if not fname.endswith(".md"):
                    continue
                meta = read_post_meta_yaml(os.path.join(posts_dir_scan, fname))
                if str(meta.get("status", "published")).lower() != "published":
                    continue
                pt = str(meta.get("primary_tag", "")).strip()
                if pt:
                    all_tags.add(pt)
                tags_raw = meta.get("tags", [])
                if isinstance(tags_raw, list):
                    for t in tags_raw:
                        ts = str(t).strip()
                        if ts:
                            all_tags.add(ts)
                elif isinstance(tags_raw, str):
                    for t in tags_raw.split(","):
                        ts = t.strip()
                        if ts:
                            all_tags.add(ts)

        if all_tags:
            print(f"\n── Tag-Listings ({len(all_tags)} Tags) ──────────")
            for tag in sorted(all_tags):
                build_tag_listing(tag)

        print()
        build_sitemap(published_pages)
        build_robots()
        build_rss()
        build_llms_txt(published_pages)

    print("\n✓ Fertig.")


# ---------------------------------------------------------------------------
# Phase 6 — DX Tooling: Dev-Server + File-Watcher
# ---------------------------------------------------------------------------
DEV_PORT = 8765


class _SilentHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP-Handler der aus OUTPUT_DIR serviert — ohne Console-Spam."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=OUTPUT_DIR, **kwargs)

    def log_message(self, fmt, *args):  # noqa
        pass  # Stille Logs im Watch-Modus


def run_dev_server(port=DEV_PORT):
    """Startet einen simplen HTTP-Dev-Server in einem Daemon-Thread."""
    with socketserver.TCPServer(("", port), _SilentHandler) as httpd:
        httpd.serve_forever()


def _collect_mtimes():
    """Sammelt mtimes aller .md-Dateien in content/ + site.yaml."""
    mtimes = {}
    for root, _, files in os.walk(CONTENT_DIR):
        for fname in files:
            if fname.endswith(".md"):
                fpath = os.path.join(root, fname)
                mtimes[fpath] = os.path.getmtime(fpath)
    if os.path.exists(CONFIG_PATH):
        mtimes[CONFIG_PATH] = os.path.getmtime(CONFIG_PATH)
    return mtimes


def watch_and_rebuild(port=DEV_PORT, interval=0.8):
    """
    Beobachtet content/ + site.yaml auf Änderungen.
    Bei .md-Änderung: gezielter Einzelbuild + betroffene Tag-Listings.
    Bei site.yaml-Änderung: Full Build.
    """
    last_mtimes = _collect_mtimes()
    print(f"  Watching content/ … Ctrl+C zum Stoppen.\n")

    while True:
        time.sleep(interval)
        current_mtimes = _collect_mtimes()

        changed = [
            fpath for fpath, mtime in current_mtimes.items()
            if fpath not in last_mtimes or last_mtimes[fpath] != mtime
        ] + [
            fpath for fpath in last_mtimes
            if fpath not in current_mtimes   # gelöscht
        ]

        if not changed:
            continue

        last_mtimes = current_mtimes
        labels = [os.path.relpath(f, SITE_DIR) for f in changed]
        print(f"  Geändert: {labels}")

        # site.yaml → Full Build
        if any(f == CONFIG_PATH for f in changed):
            print("  ↺  site.yaml — Full Build …")
            global CONFIG
            CONFIG = load_config()
            build_all(include_drafts=True)
        else:
            for fpath in changed:
                if not fpath.endswith(".md"):
                    continue
                if "/posts/" in fpath:
                    # Post: Einzelbuild + betroffene Tags neu generieren
                    ok, meta = build_file(fpath, include_drafts=True)
                    if ok and meta:
                        pt = str(meta.get("primary_tag", "")).strip()
                        if pt:
                            build_tag_listing(pt)
                        tags_raw = meta.get("tags", [])
                        tag_list = (
                            [str(t).strip() for t in tags_raw]
                            if isinstance(tags_raw, list)
                            else [t.strip() for t in str(tags_raw).split(",")]
                        )
                        for t in tag_list:
                            if t and t != pt:
                                build_tag_listing(t)
                    build_rss()
                else:
                    # Normale Seite
                    build_file(fpath, include_drafts=True)

        print(f"  ✓  http://localhost:{port}/\n")


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    args = sys.argv[1:]

    include_drafts = "--include-drafts" in args
    drafts_only    = "--drafts-only"    in args
    serve_mode     = "--serve"          in args
    watch_mode     = "--watch"          in args

    # Port überschreiben: --port=9000
    port = DEV_PORT
    for a in args:
        if a.startswith("--port="):
            try:
                port = int(a.split("=", 1)[1])
            except ValueError:
                pass

    # Slug-Argumente (alles ohne --Flags)
    slugs = [a for a in args if not a.startswith("--")]

    if serve_mode or watch_mode:
        # Initialer Build (inkl. Drafts für Dev)
        build_all(include_drafts=True)

        if serve_mode:
            t = threading.Thread(target=run_dev_server, args=(port,), daemon=True)
            t.start()
            print(f"\n  Dev-Server: http://localhost:{port}/")

        if watch_mode:
            watch_and_rebuild(port=port)
        else:
            # Nur serve, kein watch → blockieren bis Ctrl+C
            print("  Ctrl+C zum Stoppen.")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n  Server gestoppt.")

    elif slugs:
        for slug in slugs:
            slug = slug.replace(".md", "").replace(".html", "")
            build_single(slug, include_drafts=include_drafts, drafts_only=drafts_only)
    else:
        build_all(include_drafts=include_drafts, drafts_only=drafts_only)
