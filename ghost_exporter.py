"""
Ghost CMS → Markdown Exporter
Konvertiert Ghost Lexical JSON → Markdown mit YAML-Frontmatter
"""
import json, re
from markdownify import markdownify as md

def lexical_to_markdown(lexical_str):
    """Convert Ghost Lexical JSON to Markdown."""
    lexical = json.loads(lexical_str) if isinstance(lexical_str, str) else lexical_str
    root = lexical.get("root", lexical)
    return process_children(root.get("children", []))

def process_children(children):
    parts = []
    for node in children:
        result = process_node(node)
        if result is not None:
            parts.append(result)
    return "\n\n".join(parts)

def process_node(node):
    t = node.get("type", "")
    
    if t == "extended-heading":
        tag = node.get("tag", "h2")
        level = int(tag[1]) if tag and tag[0] == "h" else 2
        text = inline_children(node)
        return f"{'#' * level} {text}"
    
    elif t == "paragraph":
        text = inline_children(node)
        # Empty paragraph = explicit spacing — render as non-breaking space to preserve blank line
        return text if text.strip() else "&nbsp;"
    
    elif t in ("extended-quote", "blockquote"):
        text = inline_children(node)
        # Split by actual line breaks in the inline text
        lines = text.split("\n")
        return "\n".join(f"> {line}" for line in lines)
    
    elif t == "list":
        tag = node.get("tag", "ul")
        items = []
        for i, child in enumerate(node.get("children", [])):
            text = inline_children(child)
            if tag == "ol":
                items.append(f"{i+1}. {text}")
            else:
                items.append(f"- {text}")
        return "\n".join(items)
    
    elif t == "toggle":
        heading_html = node.get("heading", "")
        content_html = node.get("content", "")
        heading_text = html_to_md(heading_html).strip()
        content_md = html_to_md(content_html).strip()
        return f"<details>\n<summary><strong>{heading_text}</strong></summary>\n\n{content_md}\n\n</details>"

    elif t == "button":
        text = node.get("buttonText", "")
        url = node.get("buttonUrl", "")
        alignment = node.get("alignment", "center")
        return f"[{text}]({url}){{.gh-button .cta-{alignment}}}"

    elif t == "html":
        raw_html = node.get("html", "")
        # iframes und post-faq: roh durchreichen — nicht durch markdownify jagen
        if "<iframe" in raw_html or 'class="post-faq"' in raw_html or "class='post-faq'" in raw_html:
            return raw_html.strip()
        return html_to_md(raw_html).strip()
    
    elif t == "image" or t == "extended-image":
        src = node.get("src", "")
        alt = node.get("alt", "")
        caption = node.get("caption", "")
        result = f"![{alt}]({src})"
        if caption:
            result += f"\n*{html_to_md(caption).strip()}*"
        return result
    
    elif t == "horizontalrule":
        return "---"
    
    elif t == "bookmark":
        url = node.get("url", "")
        title = node.get("metadata", {}).get("title", url)
        return f"[{title}]({url})"
    
    elif t == "embed":
        url = node.get("url", "")
        caption = node.get("caption", "")
        return f"[Embed: {caption or url}]({url})"
    
    elif t == "codeblock":
        code = node.get("code", inline_children(node))
        lang = node.get("language", "")
        return f"```{lang}\n{code}\n```"
    
    else:
        # Fallback: try to process children
        if node.get("children"):
            return process_children(node["children"])
        return None

def inline_children(node):
    """Process inline children (text, links, linebreaks) into a single string."""
    parts = []
    for child in node.get("children", []):
        parts.append(inline_node(child))
    return "".join(parts)

def inline_node(node):
    t = node.get("type", "")

    if t in ("extended-text", "text"):
        text = node.get("text", "")
        fmt = node.get("format", 0)
        # Ghost format bitmask: 1=bold, 2=italic, 4=strikethrough, 8=underline, 16=code
        if isinstance(fmt, int):
            if fmt & 16:
                # Code-span: kein HTML-Escaping nötig, Backticks schützen
                text = f"`{text}`"
            else:
                # Escape spitze Klammern damit <model>-Tag nicht als HTML-Element gerendert wird
                text = text.replace("<", "&lt;").replace(">", "&gt;")
            if fmt & 1:
                text = f"**{text}**"
            if fmt & 2:
                text = f"*{text}*"
            if fmt & 4:
                text = f"~~{text}~~"
        else:
            # format=0 oder kein int: trotzdem escapen
            text = text.replace("<", "&lt;").replace(">", "&gt;")
        return text

    elif t == "link":
        url = node.get("url", "")
        text = inline_children(node)
        return f"[{text}]({url})"

    elif t == "linebreak":
        # Soft line break: two trailing spaces + newline (Markdown hard line break)
        return "  \n"
    
    elif t == "tab":
        return "\t"
    
    else:
        # Fallback
        if node.get("children"):
            return inline_children(node)
        return node.get("text", "")

def html_to_md(html_str):
    """Convert HTML snippet to Markdown."""
    if not html_str:
        return ""
    # Clean up Ghost-specific spans (style, class) + unwrap bare <span> wrappers
    cleaned = re.sub(r'style="[^"]*"', '', html_str)
    cleaned = re.sub(r"style='[^']*'", '', cleaned)
    cleaned = re.sub(r'class="[^"]*"', '', cleaned)
    cleaned = re.sub(r"class='[^']*'", '', cleaned)
    result = md(cleaned, strip=["span"]).strip()
    # Fix double-bold artefacts: ****text**** → **text**
    result = re.sub(r'\*{4}([^*]+)\*{4}', r'**\1**', result)
    return result

def extract_faq_from_content(content):
    """
    Sucht nach <div class="post-faq">...</div> im Content.
    Extrahiert alle darin enthaltenen <details>/<summary> als FAQ-Liste.
    Entfernt auch den H2/H3 direkt VOR dem Block (wird als faq_heading zurückgegeben).
    Gibt (bereinigter_content, faq_liste, faq_heading) zurück.
    faq_liste = [{"q": "...", "a": "..."}, ...]
    faq_heading = str oder ""
    """
    faq_list = []
    faq_heading = ""

    pattern = re.compile(
        r'<div\s+class=["\']post-faq["\'][^>]*>(.*?)</div>',
        re.DOTALL | re.IGNORECASE
    )

    def extract_faqs(match):
        block = match.group(1)
        details = re.findall(
            r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>',
            block, re.DOTALL | re.IGNORECASE
        )
        for q_html, a_html in details:
            q = re.sub(r'<[^>]+>', '', q_html).strip()
            a = re.sub(r'<[^>]+>', '', a_html).strip()
            a = re.sub(r'\s+', ' ', a).strip()
            if q and a:
                faq_list.append({"q": q, "a": a})
        return ""  # Remove the block from content

    cleaned_content = pattern.sub(extract_faqs, content)

    # H2/H3 direkt vor dem (nun entfernten) FAQ-Block herausziehen
    # Suche das letzte ## / ### vor der Lücke (leere Zeilen wo der Block war)
    if faq_list:
        heading_pattern = re.compile(
            r'(#{2,3})\s+(.+?)\n(\n*$)',
            re.MULTILINE
        )
        # Finde letztes Heading am Ende des bereinigten Contents
        matches = list(heading_pattern.finditer(cleaned_content))
        if matches:
            last = matches[-1]
            heading_text = last.group(2).strip().strip('*').strip()
            # Nur entfernen wenn es wirklich die FAQ-Headline ist (am Ende des Textes)
            tail = cleaned_content[last.end():].strip()
            if not tail or tail.replace('&nbsp;', '').replace('\n', '').strip() == '':
                faq_heading = heading_text
                cleaned_content = cleaned_content[:last.start()].rstrip()

    # Clean up any leftover blank lines from removal
    cleaned_content = re.sub(r'\n{4,}', '\n\n\n', cleaned_content)

    return cleaned_content, faq_list, faq_heading

def page_to_markdown(page_data):
    """Convert a Ghost page/post JSON to full Markdown with frontmatter."""
    title = page_data.get("title", "")
    slug = page_data.get("slug", "")
    meta_desc = page_data.get("meta_description") or page_data.get("custom_excerpt") or ""
    meta_title = page_data.get("meta_title") or ""
    feature_image = page_data.get("feature_image") or ""
    og_image = page_data.get("og_image") or ""
    tags = [t["slug"] for t in page_data.get("tags", [])]
    primary_tag = page_data.get("primary_tag") or {}
    primary_tag_slug = primary_tag.get("slug", "")
    is_page = page_data.get("type", "post") == "page" or "pages" in str(page_data.get("url", ""))
    content_type = "page" if is_page else "post"
    published = page_data.get("published_at", "")
    status = page_data.get("status", "published")

    # Author
    authors = page_data.get("authors", [])
    author = authors[0] if authors else {}
    author_name = author.get("name", "")
    author_slug = author.get("slug", "")
    author_image = author.get("profile_image", "")
    author_bio = author.get("bio", "")

    # Frontmatter
    fm_lines = [
        "---",
        f'title: "{title}"',
        f"slug: {slug}",
        f"status: {status}",
    ]
    if primary_tag_slug:
        fm_lines.append(f"primary_tag: {primary_tag_slug}")
    if tags:
        fm_lines.append(f"tags: [{', '.join(tags)}]")
    if meta_title:
        fm_lines.append(f'meta_title: "{meta_title}"')
    if meta_desc:
        fm_lines.append(f'meta_description: "{meta_desc}"')
    if feature_image:
        fm_lines.append(f"feature_image: {feature_image}")
    if og_image:
        fm_lines.append(f"og_image: {og_image}")
    if author_name:
        fm_lines.append(f'author: "{author_name}"')
    if author_slug:
        fm_lines.append(f"author_slug: {author_slug}")
    if author_image:
        fm_lines.append(f"author_image: {author_image}")
    if author_bio:
        # Escape quotes in bio
        fm_lines.append(f'author_bio: "{author_bio.strip()}"')
    if published:
        fm_lines.append(f'published_at: "{published}"')  # Anführungszeichen → YAML parsed als String, nicht datetime
    # Beide Felder setzen: type für SkillCMS build.py, template für Theme-Kompatibilität
    fm_lines.append(f"type: {content_type}")
    fm_lines.append(f"template: {content_type}")
    fm_lines.append("---")
    
    frontmatter = "\n".join(fm_lines)
    
    # Content
    lexical = page_data.get("lexical", "")
    if lexical:
        content = lexical_to_markdown(lexical)
    elif page_data.get("html"):
        content = html_to_md(page_data["html"])
    else:
        content = ""

    # FAQ-Extraktion: <div class="post-faq"> → Frontmatter faq: Liste + faq_heading
    content, faq_list, faq_heading = extract_faq_from_content(content)
    if faq_list:
        faq_lines = []
        if faq_heading:
            faq_lines.append(f'faq_heading: "{faq_heading}"')
        faq_lines.append("faq:")
        for item in faq_list:
            q = item["q"].replace('"', '\\"')
            a = item["a"].replace('"', '\\"')
            faq_lines.append(f'  - q: "{q}"')
            faq_lines.append(f'    a: "{a}"')
        # fm_lines endet mit "---", FAQ davor einfügen
        fm_lines[-1:-1] = faq_lines
        frontmatter = "\n".join(fm_lines)

    return f"{frontmatter}\n\n{content}\n"

if __name__ == "__main__":
    with open("kontakt_raw.json") as f:
        page = json.load(f)
    result = page_to_markdown(page)
    print(result)
