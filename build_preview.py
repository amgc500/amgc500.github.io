#!/usr/bin/env python3
"""Render a static preview of the front page from _data/papers.yml + index.html.

This is NOT part of the site -- GitHub's Jekyll builds the real thing. It only
mirrors the Liquid logic in _includes/paper.html so you can see the result
without a local Jekyll install. Output: preview.html.
"""
import html
import re
import yaml
from pathlib import Path

ROOT = Path(__file__).parent
papers = yaml.safe_load((ROOT / "_data/papers.yml").read_text())["papers"]

KEYS = ["pdf", "arxiv", "code", "video", "slides", "doi"]
LABELS = {"pdf": "pdf", "arxiv": "arXiv", "code": "code",
          "video": "video", "slides": "slides", "doi": "DOI"}


def render_paper(p):
    out = [f'<span class="paper-title">&ldquo;{html.escape(p["title"])}&rdquo;</span>']
    if p.get("authors"):
        out.append(f'<br><span class="paper-authors">{html.escape(p["authors"])}.</span>')

    if p.get("journal") or p.get("year") or p.get("volume") or p.get("pages"):
        ref = []
        if p.get("journal"):
            j = html.escape(p["journal"])
            if p.get("journal_url"):
                j = f'<a href="{p["journal_url"]}">{j}</a>'
            if p.get("open_access"):
                j += " (Open Access)"
            ref.append(j)
        cite = ""
        if p.get("year"):
            cite += f'({p["year"]})'
        if p.get("volume"):
            cite += f' {p["volume"]}'
        if p.get("issue"):
            cite += f' ({p["issue"]})'
        if p.get("pages"):
            cite += f' {p["pages"]}'
        cite = cite.strip()
        line = ref[0] if ref else ""
        if cite:
            line += (", " if p.get("journal") else "") + cite
        out.append(f'<span class="paper-ref">{line}.</span>')

    if p.get("links"):
        anchors = [f'<a href="{p["links"][k]}">{LABELS[k]}</a>'
                   for k in KEYS if p["links"].get(k)]
        if anchors:
            out.append(f'<span class="paper-links">{", ".join(anchors)}.</span>')

    if p.get("note"):
        out.append(f'<span class="paper-note">{p["note"]}</span>')

    return '<li class="paper">\n  ' + "\n  ".join(out) + "\n</li>"


papers_html = "\n".join(render_paper(p) for p in papers)

# Pull the prose out of index.html (everything the loop doesn't generate) so the
# preview matches the real front page. We strip Liquid tags and substitute config.
index = (ROOT / "index.html").read_text()
index = index.split("---", 2)[2]  # drop front matter

cfg = yaml.safe_load((ROOT / "_config.yml").read_text())
contact = cfg["contact"]

# crude Liquid -> value substitutions, enough for a faithful preview
index = index.replace("{{ site.contact.role }}", contact["role"])
index = index.replace("{{ site.contact.office }}", contact["office"])
index = index.replace("{{ site.contact.phone }}", contact["phone"])
index = index.replace("{{ site.contact.email }}", contact["email"])
index = re.sub(r"{{ '([^']+)' \| relative_url }}", r"\1", index)
# address loop (offset 2 -> last two lines)
addr = "".join(
    l + (",<br>\n" if i < len(contact["address"][2:]) - 1 else "\n")
    for i, l in enumerate(contact["address"][2:])
)
index = re.sub(r"{%- comment -%}.*?{%- endcomment -%}", "", index, flags=re.S)
index = re.sub(
    r"{% for line in site\.contact\.address offset: 2 %}.*?{% endfor %}",
    addr, index, flags=re.S)
# replace the papers loop
index = re.sub(
    r"{%- for paper in site\.data\.papers\.papers %}.*?{%- endfor %}",
    papers_html, index, flags=re.S)
# drop any remaining liquid
index = re.sub(r"{%-?.*?-?%}", "", index, flags=re.S)

THEMES = {
    "simple": '<link rel="stylesheet" href="assets/css/style.css">',
    "pico": ('<link rel="stylesheet" href="assets/css/pico.classless.min.css">\n'
             '<link rel="stylesheet" href="assets/css/pico-overrides.css">'),
}

for name, head in THEMES.items():
    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Alexander Cox</title>
{head}</head>
<body><main class="page">
{index}
<footer class="site-footer"><p>Preview ({name}) — rendered {len(papers)} papers.</p></footer>
</main></body></html>"""
    (ROOT / f"preview_{name}.html").write_text(doc)

print(f"Wrote preview_simple.html and preview_pico.html with {len(papers)} papers.")
