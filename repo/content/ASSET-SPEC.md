# MeYouAndUs — asset + content spec

The front end is already wired to this contract. `MeYouAndUs.dc.html` fetches
`content/projects.json` at load and builds the whole project wall and every project modal
from it. **No project content lives in the code.** Your job is images in `img/` and text in
`content/projects.json`.

Add an entry → a card appears. Reorder the array → the wall reorders. Change `span` → the
tiling changes. Leave `cover` empty → that cell shows a drag-and-drop placeholder instead of
an image.

## Folders

```
content/
  projects.json           the single source of truth for project text + image paths
img/
  site/
    hero.jpg              2560 x 1440 (16:9), dark, wide. The landing photograph.
    bleed.jpg             2560 x 1440 (16:9). The "Amplifying place" full-bleed band.
  projects/
    <slug>/
      cover.jpg           2400 x 1600 (3:2)  — the mosaic wall
      wide.jpg            2400 x  860 (2.8:1) — OPTIONAL. Used instead of cover.jpg when
                                                present, for projects in a wide cell
                                                (span 7 or 8)
      01.jpg 02.jpg 03.jpg  2400px on the long edge, any ratio — the project modal gallery
```

`<slug>` is lowercase, hyphenated, and must match `slug` in the JSON. Current slugs, by
section:

- **Section 1, breaking the interface:** `madheads`, `tilo-v2`, `fantasia-express`,
  `bigmouth`, `cakenocake`, `emofie`, `when-i-grow-up`, `tilo-v1`, `humble-market`,
  `meyouandus-series`
- **Section 2, amplifying place:** `not-the-beatles`, `homewalk`, `kindred-spirits`,
  `sonic-market`, `invisible-arts-network`, `handprint-2012`, `townsend-lane`,
  `wishing-well`, `lowry-to-life`, `handprint-2008`

## Image rules

- JPEG, quality ~80, sRGB.
- **Full colour.** The greyscale on the wall is applied in code (`filter: grayscale(1)
  contrast(1.06)`) and lifted on hover; modal galleries show colour. Never pre-convert.
- Keep the subject centred — every cell crops from the centre with `object-fit: cover`.
- Long edge 2400px; the hero wants 2560px. Aim under 400KB per file.

## Cell widths (why `wide.jpg` exists)

The wall is a 12-column grid, row height `clamp(190px, 21vw, 380px)`, zero gaps. At a 1440px
window each cell lands at roughly:

| `span` | Cell size | Ratio |
| --- | --- | --- |
| 8 | 960 x 300 | 3.2:1 |
| 7 | 840 x 300 | 2.8:1 |
| 5 | 600 x 300 | 2:1 |
| 4 | 480 x 300 | 1.6:1 |
| 3 | 360 x 300 | 1.2:1 |

**Each row of the wall must total 12**, and rows do not span across a section break — each
section's spans must total a multiple of 12 on their own.

Current layout:

- **Section 1** — 5+7, 8+4, 4+4+4, 5+4+3 (10 projects, 4 rows)
- **Section 2** — 7+5, 8+4, 8+4, 3+3+3+3 (10 projects, 4 rows)

## Two sections

The home page wall is split by theme, matching the two calls to action:

| `section` | `theme` | Heading | What qualifies |
| --- | --- | --- | --- |
| 1 | `interface` | Breaking the interface | The work is bound to a device, a screen or a body, and could travel |
| 2 | `place` | Amplifying place | The work is bound to a site and couldn't move |

Four projects genuinely sit in both and carry an `alsoTheme`: `fantasia-express` and
`humble-market` (section 1, also place), `not-the-beatles` and `homewalk` (section 2, also
interface). `section` decides where a card is tiled; `alsoTheme` means it should also appear
when the other theme is used as a filter on the All Projects page. Nothing is tiled twice.

## content/projects.json

An array of 20. Array order is wall order, within `section` order.

```json
[
  {
    "slug": "not-the-beatles",
    "title": "Not the Beatles Tour",
    "year": "2024",
    "place": "Liverpool",
    "commissioner": "Self-initiated",
    "blurb": "One or two sentences, plain and factual, 30–45 words. It sets at display size in the modal, so it should read as a statement, not a press release.",
    "theme": "place",
    "alsoTheme": "interface",
    "section": 2,
    "span": 7,
    "cover": "img/projects/not-the-beatles/cover.jpg",
    "wide": "img/projects/not-the-beatles/wide.jpg",
    "video": "https://vimeo.com/000000000",
    "credits": "With So-and-so",
    "images": [
      "img/projects/not-the-beatles/01.jpg",
      "img/projects/not-the-beatles/02.jpg"
    ]
  }
]
```

| Field | Notes |
| --- | --- |
| `slug` | Must match the image folder name. Used as the modal's identity. |
| `title` | Shown on hover over the cell and as the modal headline (uppercase, display size). |
| `year` | A string, so ranges work: `"2012–14"`. |
| `place` | City or venue. Joined with `year` as the hover meta line. |
| `commissioner` | Funder or commissioning body; `"Self-initiated"` when there isn't one. |
| `blurb` | 30–45 words, plain and factual, no marketing adjectives. |
| `theme` | `"interface"` or `"place"`. Must agree with `section`. |
| `alsoTheme` | Optional, the opposite value. Only for work that genuinely does both. |
| `section` | `1` (breaking the interface) or `2` (amplifying place). |
| `span` | 3–8. Rows must total 12, and each section must total a multiple of 12. |
| `cover` | Wall image. Empty string or omitted → a drop-slot placeholder renders. |
| `wide` | Optional panoramic crop; takes precedence over `cover` on the wall. |
| `video` | Optional Vimeo or YouTube URL. Leads the modal when present. Empty string when there isn't one. |
| `credits` | Optional collaborators line, set small under the blurb. Empty string when there isn't one. |
| `images` | 0–3 files for the modal. First one prints at 21:9 full width, the rest at 3:2 half width. An empty array shows an "images to come" note. |

Paths are relative to the project root (the same folder as `MeYouAndUs.dc.html`).

## content/about.json

The About view is a **takeover, not a page** — same mechanism as a project modal, full bleed,
routed at `#/about` so it has a real URL and can be indexed and linked. The home page stays a
single HTML file.

Treatment is the inverse of the wall: the wall is all image and no words, About is all words
and no image. Ink `#1D1D1B` on ground `#F3F2F2`, one typographic column, dates in a left
rail, no photography anywhere in it. That restraint is the design idea — don't decorate it.

```
{
  "statement":   [ "paragraph", "paragraph" ],
  "showreel":    { "url", "caption" },
  "contact":     { "email", "base", "links": [ { "label", "url" } ] },
  "works":       [ { "date", "title", "detail", "slug", "sub": [ "line" ] } ],
  "awards":      [ { "date", "detail" } ],
  "press":       [ { "date", "title", "publication", "url", "note" } ],
  "residencies": [ { "date", "detail" } ]
}
```

| Field | Notes |
| --- | --- |
| `date` | Free text, so `"Dec 2008"`, `"2013–15"` and `""` all work. Sets in the left rail. |
| `works[].slug` | Matches a `slug` in `projects.json`, or `null`. When set, the title links into that project's modal — this is what stops About being a dead end. |
| `works[].sub` | Optional venue list for works that toured or recurred. Indents under the entry. |
| `press[].url` | Empty string means the link is known but the URL is lost. Render as plain text, not a broken link. |
| `press[].note` | Internal only. Never rendered. |

Current contents: 28 catalogue entries (49 lines with sub-items), 12 awards, 8 press, 13
residencies. Five catalogue entries have no project page and `slug: null` — Catch Me If You
Can, Rise of the Data Collectors, Memory Sphere, Diablo Quintapenhas, Hub Gallery. Every one
of the 20 projects appears in the catalogue.

**The PDF is generated from this file, never written by hand.** Same source, two outputs — a
CV attached to a funding application can't then drift from the site.

## Migration state

`content/projects.json` currently points at the **legacy** filenames I pulled from the old
WordPress uploads (`img/tilo-weather.jpg`, `img/misc-2017.jpg`, and so on) — inconsistent
sizes, whatever the old site happened to have. When new assets are produced under
`img/projects/<slug>/`, update the `cover` / `wide` / `images` paths in the JSON to match and
the old files can be deleted.

Seven projects have no cover and render placeholders: `madheads`, `tilo-v2`, `bigmouth`,
`cakenocake`, `not-the-beatles`, `homewalk`, `handprint-2008`. The first two and the last
three need new photography; `bigmouth` and `cakenocake` have stills on the old site that
haven't been pulled down yet.

Note also that `tilo-v1` and `tilo-v2` are now separate entries. `img/tilo-weather.jpg` and
`img/tilo-information.jpg` are v1 screens and belong to `tilo-v1` — v2 needs its own.

Four images were previously filed under the wrong project and have been moved:
`lowry-to-life.jpg` and `bbc-big-screens.jpg` out of `handprint-2012`, `wishing-well.jpg`
out of `townsend-lane`, `when-i-grow-up.jpg` out of `emofie`. Each now sits with the project
it actually documents.

## Files that are no longer used

Safe to delete once new assets land: `img/photoemoticon.jpg`, `img/logo-colour.png`,
`img/logo.png`, `img/logo-black.png`, `img/logo-reverse.png`, `img/logo-ink.svg`,
`img/logo-white.svg`.

`img/brazil.jpg` is now in use — it's the Miguel Perera intervention, and sits in
`meyouandus-series`. The "Amplifying place" bleed band needs its own `img/site/bleed.jpg`.

Two legacy files are currently unused and could go either way: `img/humble-market-event.jpg`
and `img/carnival-taxi.jpg` (the latter is in the Humble Market gallery).

The live logo is `img/logo-white.png` — white, transparent background, 1080p wide.

## Brand

Colours come from the logo: magenta `#E5007E`, cyan `#009EE2`, yellow `#FFEC00`, ink
`#1D1D1B`, ground `#F3F2F2`. Type is Archivo throughout. `Brand.dc.html` in this project is
the full design-system sheet — logo usage, colour roles, type scale, components, do/don'ts.

Each colour has one job, so nothing competes:

| Colour | Role |
| --- | --- |
| Magenta | Section 1, breaking interfaces — band and its empty drop-slots |
| Cyan | Section 2, amplifying place — band, empty drop-slots, and the footer |
| Yellow | Project modals |
| Ink | The About takeover |

Empty cells inherit their section's colour rather than showing a grey placeholder. This is
deliberate: a missing cover reads as a colour block, so the wall can ship before the
photography exists.

On yellow: as the full field behind colour photographs it fights badly. Use it as the modal's
furniture — rules, meta line, close control, captions — against ink or ground. Worth building
both and looking before committing.
