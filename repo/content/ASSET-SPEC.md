# MeYouAndUs — asset + content spec

The data and image contract between content and the front end. `MeYouAndUs.dc.html` fetches
these files at load; **no content lives in the code**. This document specifies what the files
contain and what shape the images are. How any of it is presented — colour, type, motion,
layout treatment — is a design decision and lives in `DESIGN-STATE.md`.

Add an entry and a project appears. Reorder the array and the order changes. Change `span`
and the tiling changes. Leave `cover` empty and there's no image to show.

## Folders

```
content/
  projects.json           the 20 projects — text, spans, image paths
  about.json              statement, catalogue, awards, press, residencies, contact
  site.json               tagline, the two site images, section headings and blurbs
img/
  site/
    hero.jpg              2560 x 1440 (16:9). The landing photograph.
    bleed.jpg             2560 x 1440 (16:9). The second full-bleed photograph.
  projects/
    <slug>/
      cover.jpg           2400 x 1600 (3:2)  — the mosaic wall
      wide.jpg            2400 x  860 (2.8:1) — OPTIONAL. Used instead of cover.jpg when
                                                present, for projects in a wide cell
                                                (span 7 or 8)
      01.jpg 02.jpg 03.jpg  2400px on the long edge, any ratio — the project gallery
```

`<slug>` is lowercase, hyphenated, and must match `slug` in the JSON. Current slugs, by
section:

- **Section 1, `interface`:** `madheads`, `tilo-v2`, `fantasia-express`,
  `bigmouth`, `cakenocake`, `emofie`, `when-i-grow-up`, `tilo-v1`, `humble-market`,
  `meyouandus-series`
- **Section 2, `place`:** `not-the-beatles`, `homewalk`, `kindred-spirits`,
  `sonic-market`, `invisible-arts-network`, `handprint-2012`, `townsend-lane`,
  `wishing-well`, `lowry-to-life`, `handprint-2008`

## Image rules

- JPEG, quality ~80, sRGB.
- **Full colour, never pre-converted.** Any greyscale treatment is applied in code, so the
  file underneath must be the colour original.
- Keep the subject centred — cells crop from the centre with `object-fit: cover`.
- Long edge 2400px; the two site images 2560px. Aim under 400KB per file.

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

The projects are split into two thematic sets. Headings and blurbs live in
`content/site.json`; presentation is the front end's business.

| `section` | `theme` | What qualifies |
| --- | --- | --- |
| 1 | `interface` | The work is bound to a device, a screen or a body, and could travel |
| 2 | `place` | The work is bound to a site and couldn't move |

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
    "blurb": "One or two sentences, plain and factual, 30–45 words. It sets large, so it should read as a statement, not a press release.",
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
| `slug` | Must match the image folder name. The project's stable identifier. |
| `title` | The project's name. Used wherever the project is identified. |
| `year` | A string, so ranges work: `"2012–14"`. |
| `place` | City or venue. Pairs with `year` as the project's meta line. |
| `commissioner` | Funder or commissioning body; `"Self-initiated"` when there isn't one. |
| `blurb` | 30–45 words, plain and factual, no marketing adjectives. |
| `theme` | `"interface"` or `"place"`. Must agree with `section`. |
| `alsoTheme` | Optional, the opposite value. Only for work that genuinely does both. |
| `section` | `1` or `2`. See the two sections above. |
| `span` | 3–8. Rows must total 12, and each section must total a multiple of 12. |
| `cover` | The project's wall image. Empty string means no image exists yet. |
| `wide` | Panoramic 2.8:1 crop, supplied for span-7/8 projects. Takes precedence over `cover` on the wall. |
| `video` | Vimeo or YouTube URL. Empty string when there isn't one. Present on 13 of 20. |
| `credits` | Collaborators line. Empty string when there isn't one. |
| `imageCredit` | Photographer credit for the project's images. Empty string when not required. Currently only `handprint-2012` (Simon Kirwan). |
| `images` | 0–3 gallery files. Per `DESIGN-STATE.md` the first sets at 21:9 and the rest at 3:2, so supply accordingly. Empty array means none exist. |

Paths are relative to the project root (the same folder as `MeYouAndUs.dc.html`).

## content/about.json

The About content. There is no photography in it and none is expected — it's a CV, and the
only images the site needs are the two in `site.json` plus the project assets.

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
| `date` | Free text, so `"Dec 2008"`, `"2013–15"` and `""` all work. |
| `works[].slug` | Matches a `slug` in `projects.json`, or `null`. When set, the entry can link through to that project. |
| `works[].sub` | Optional venue list for works that toured or recurred. |
| `press[].url` | Empty string means the link is known but the URL is lost — there is nothing to link to. |
| `press[].note` | Internal only. Never rendered. |
| `contact` | Email and base. This is the only place contact details live, in About or a Contact view or both — one source either way. |

Current contents: 28 catalogue entries (49 lines with sub-items), 12 awards, 8 press, 13
residencies. Five catalogue entries have no project page and `slug: null` — Catch Me If You
Can, Rise of the Data Collectors, Memory Sphere, Diablo Quintapenhas, Hub Gallery. Every one
of the 20 projects appears in the catalogue.

**The PDF is generated from this file, never written by hand.** Same source, two outputs — a
CV attached to a funding application can't then drift from the site.

## content/site.json

Site-level copy and the two structural photographs, so neither is hard-coded.

| Field | Notes |
| --- | --- |
| `tagline` | The hero subline. Written to sit on one line. |
| `images.hero` / `images.bleed` | `src`, `imageCredit`, `alt`. Both 2560×1440. |
| `sections[]` | `id`, `theme`, `heading`, `blurb` for each of the two sets. |

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

Palette from the logo: magenta `#E5007E`, cyan `#009EE2`, yellow `#FFEC00`, ink `#1D1D1B`,
ground `#F3F2F2`, white `#FFFFFF`. `Brand.dc.html` is the design-system sheet and
`DESIGN-STATE.md` records how the front end uses them. Colour roles, typography and motion
are design decisions and are not specified here.

The one place brand and content touch: images are supplied **full colour, never
pre-converted**, because any greyscale treatment is applied in code and needs the colour
original underneath it.
