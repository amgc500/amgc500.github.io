# amgc500.github.io

Source for my homepage, a small Jekyll site served by GitHub Pages.

## How it's put together

- `index.html` — the front page. Plain HTML you can edit directly; the only
  templated part is a loop over the publication list.
- `_data/papers.yml` — **the publication list**. This is where you add or edit
  papers; the front page regenerates from it. Order in the file = order on the
  page (newest first, not auto-sorted). Schema is documented at the top of the file.
- `_includes/paper.html` — renders one paper. Edit here only to change how
  entries look, or to add a new link type.
- `_layouts/` — page shells (`default.html`, `course.html`).
- `assets/css/style.css` — all styling; no frameworks or web fonts.
- `courses/` — one file per course page, using the `course` layout.
- `_config.yml` — site + contact details.

## Adding a paper

Add a block to the top of `_data/papers.yml`:

```yaml
  - title: "My new paper"
    authors: "With A. Coauthor"
    journal: "Some Journal"
    journal_url: "https://doi.org/..."
    year: 2026
    volume: 12
    issue: 3
    pages: "1-20"
    note: "&copy; 2026 Publisher."      # optional free text / HTML
    links:
      pdf: "MyPaper.pdf"
      arxiv: "https://arxiv.org/abs/..."
      code: "https://github.com/..."
```

Every field except `title` is optional. Commit, push, and GitHub rebuilds.

## Switching the look (simple vs Pico)

Two stylesheets ship with the site:

- `assets/css/style.css` — the hand-written stylesheet (default).
- `assets/css/pico.classless.min.css` + `assets/css/pico-overrides.css` —
  vendored [Pico CSS](https://picocss.com) (v2.1.1, MIT, no CDN dependency)
  plus a thin layer for the portrait, sticky nav, and paper list.

Choose one in `_config.yml`:

```yaml
style: "simple"   # or "pico"
```

Because `_config.yml` is only read at startup, restart `jekyll serve` after
changing it (a plain page edit reloads automatically; a config change does not).

## Section navigation

The front page has a sticky nav bar (`<nav class="toc">` in `index.html`) that
links to the `id`-tagged sections (`research`, `group`, `papers`, `teaching`,
`links`). Add a section by giving it an `id` and adding one `<a href="#id">` to
the nav.

## Editing locally (optional)

GitHub Pages builds the site on push, so you don't need to. To preview locally:

```
bundle install
bundle exec jekyll serve
```

then open <http://localhost:4000>.
## Still to do after the move

Recovered files from the old Bath server go in these folders (see
`RECOVERY-CHECKLIST.md` for the exact per-file destinations):

```
assets/img/        your photo (Alexander_Cox_2022.jpg)
papers/            self-hosted paper PDFs + the insider-info notebook
theses/            your thesis + the three self-hosted student theses
teaching/MA50251/  Applied SDEs materials (notes, sheets, notebooks, timetable)
teaching/MA6000D/  Stochastic Control lecture notes
teaching/MA6000K/  Optimal Stopping lecture notes
```

Each folder is created with a `.gitkeep` placeholder so it exists in the repo;
drop the recovered files in and delete `.gitkeep` if you like. Links in the site
already point at these locations, so once the files are in place they resolve.

Still parked for a later pass: the seminar-series pages and `SEPMOT.html`
(and their abstract PDFs and logos), which we deliberately deferred.
