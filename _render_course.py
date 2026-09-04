import re, sys, markdown
src = sys.argv[1]; outhtml = sys.argv[2]
raw = open(src, encoding="utf-8").read()
fm, body = raw.split('---',2)[1], raw.split('---',2)[2]
def fmval(k):
    m = re.search(rf'^{k}:\s*"?(.*?)"?\s*$', fm, flags=re.M); return m.group(1) if m else ""
title, code, term = fmval('title'), fmval('code'), fmval('term')
body = re.sub(r"{{\s*'([^']+)'\s*\|\s*relative_url\s*}}", r"\1", body)
html_body = markdown.markdown(body, extensions=['def_list','sane_lists','attr_list'])
meta = " &middot; ".join(x for x in [code, term] if x)
page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="assets/css/pico.classless.min.css">
<link rel="stylesheet" href="assets/css/pico-overrides.css"></head>
<body><main class="page"><article class="course">
<p class="breadcrumb"><a href="#">&larr; Alexander Cox</a></p>
<h1>{title}</h1><p class="course-meta">{meta}</p>
{html_body}</article></main></body></html>"""
open(outhtml,"w",encoding="utf-8").write(page)
print("wrote", outhtml)
