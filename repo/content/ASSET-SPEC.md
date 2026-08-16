# MeYouAndUs - asset and content spec

The data and image contract between content and the front end. `MeYouAndUs.dc.html` fetches
these files at load. What the files contain and what shape the images are is specified here.
How any of it is presented, meaning colour, type, motion and layout treatment, is a design
decision and lives in `DESIGN-STATE.md`.

**The ownership boundary is in `CONTENT-CONTRACT.md` and that file governs.** An audit on
13 Aug found twenty-nine strings living in the template, so "no content lives in the code" is
an aim rather than a description. `check-strings.py` reports the current state.

Add an entry and a project appears. Reorder the array and the order changes. Change `span`
and the tiling changes. Leave `cover` empty and there's no image to show.

## Folders

```
content/
  projects.json           the 20 projects, text, spans and image paths
  about.json              statement, catalogue, awards, press, residencies, contact
  site.json               tagline, the two site images, section headings and blurbs
img/
  site/
    myu-hero.jpg          2560 x 1440 (16:9). The landing photograph.
    myu-bleed.jpg         2560 x 1440 (16:9). The second full-bleed photograph.
  projects/
    <slug>/
      <slug>-cover.jpg    2400 x 1600 (3:2). The mosaic wall.
      <slug>-wide.jpg     2400 x 860 (2.8:1). Optional, used instead of the cover for
                          projects in a wide cell (span 7 or 8).
      <slug>-poster.jpg   2400 x 1350 (16:9). Optional. The still shown in place of the
                          film until someone presses play.
      <slug>-01.jpg ...   2400 x 1350 (16:9). The project gallery, numbered in display
                          order, no fixed limit. Same size as the poster, so any still
                          can be promoted to a poster without recropping.
```

Filenames repeat the slug so a file still identifies itself once it leaves the folder. The
folder groups, the filename identifies. Lowercase, hyphens, no underscores.

`<slug>` is lowercase, hyphenated, and must match `slug` in the JSON.

### Current slugs, by section

- **Section 1, `interface`:** `bigheads`, `tilo-v2`, `fantasia-express`,
  `bigmouth`, `cakenocake`, `emofie`, `when-i-grow-up`, `tilo-v1`, `humble-market`,
  `meyouandus-series`
- **Section 2, `place`:** `not-the-beatles`, `homewalk`, `kindred-spirits`,
  `sonic-market`, `invisible-arts-network`, `handprint-2012`, `townsend-lane`,
  `wishing-well`, `lowry-to-life`, `handprint-2008`

## Image rules

- JPEG, quality ~80, sRGB.
- **Full colour, never pre-converted.** Any greyscale treatment is applied in code, so the
  file underneath must be the colour original.
- Keep the subject centred. Cells crop from the centre with `object-fit: cover`.
- Long edge 2400px; the two site images 2560px. Aim under 400KB per file.
- Stills and posters are both 2400 x 1350. Covers stay 3:2 and wides stay 2.8:1.

## Cell widths (why the wide crop exists)

The wall is a 12-column grid, row height `clamp(190px, 21vw, 380px)`, zero gaps. At a 1440px
window each cell lands at roughly:

| `span` | Cell size | Ratio |
| --- | --- | --- |
| 8 | 960 x 300 | 3.2:1 |
| 7 | 840 x 300 | 2.8:1 |
| 5 | 600 x 300 | 2:1 |
| 4 | 480 x 300 | 1.6:1 |
| 3 | 360 x 300 | 1.2:1 |

**Each row of the wall must total 12**, and rows do not span across a section break, so each
section's spans must total a multiple of 12 on their own. Both currently total 48.

### Current layout

- **Section 1**, 5+7, 8+4, 4+4+4, 5+4+3 (10 projects, 4 rows)
- **Section 2**, 7+5, 8+4, 8+4, 3+3+3+3 (10 projects, 4 rows)

## Two sections

The projects are split into two thematic sets. Headings and blurbs live in
`content/site.json`; presentation is the front end's business.

| `section` | `theme` | What qualifies |
| --- | --- | --- |
| 1 | `interface` | The work is bound to a device, a screen or a body, and could travel |
| 2 | `place` | The work is bound to a site and couldn't move |

Four projects genuinely sit in both and carry an `alsoTheme`: `fantasia-express` and
`humble-market` (section 1, also place), `not-the-beatles` and `homewalk` (section 2, also
interface). `section` decides where a card is tiled. `alsoTheme` means it should also appear
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
    "blurb": "A paragraph, 100 words maximum. It sets large, so it should read as a statement. Facts first, then the detail with feeling in it. No marketing adjectives.",
    "theme": "place",
    "alsoTheme": "interface",
    "section": 2,
    "span": 7,
    "cover": "img/projects/not-the-beatles/not-the-beatles-cover.jpg",
    "wide": "img/projects/not-the-beatles/not-the-beatles-wide.jpg",
    "video": "https://vimeo.com/000000000",
    "poster": "img/projects/not-the-beatles/not-the-beatles-poster.jpg",
    "credits": "With So-and-so",
    "images": [
      "img/projects/not-the-beatles/not-the-beatles-01.jpg",
      "img/projects/not-the-beatles/not-the-beatles-02.jpg"
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
| `blurb` | 100 words maximum. Facts carry the opening, and there is room for feeling after them. All site copy follows `language.md` in the project root, including the humanity principle, so a blurb should not be flattened into controlled English. |
| `theme` | `"interface"` or `"place"`. Must agree with `section`. |
| `alsoTheme` | Optional, the opposite value. Only for work that genuinely does both. |
| `section` | `1` or `2`. See the two sections above. |
| `span` | 3–8. Rows must total 12, and each section must total a multiple of 12. |
| `cover` | The project's wall image. Empty string means no image exists yet. |
| `wide` | Panoramic 2.8:1 crop, supplied for span-7/8 projects. Takes precedence over `cover` on the wall. |
| `video` | Vimeo share URL. Empty string when there isn't one. See below. |
| `poster` | Self-hosted still for the film, 2400 x 1350. **Empty string means fall back to `cover`.** Never leave the player to supply its own. See below. Carries `posterAlt`. |
| `credits` | Collaborators line. Empty string when there isn't one. |
| `imageCredit` | Photographer credit for the project's images. Empty string when not required. Currently only `handprint-2012` (Simon Kirwan). |
| `images` | Gallery files, 2400 x 1350, **no fixed maximum**. They load into the single 16:9 viewer in the modal, with a thumbnail strip below when there is more than one item. The old 21:9 and 3:2 tiling is gone, so odd and even totals both work. Empty array means none exist. |
| `posterAlt` | Alt text for the poster frame, describing the photograph rather than naming the project. Set on the seven projects that have a poster. Written 13 Aug. |

Paths are relative to the project root (the same folder as `MeYouAndUs.dc.html`).

### Video

All films are hosted on Vimeo. Privacy is set per film so that the public Vimeo channel stays
curated rather than mirroring everything the site embeds. Three settings are in use:

| Setting | On the channel | Vimeo page | Embeds | URL form |
| --- | --- | --- | --- | --- |
| Public | Yes | Yes | Yes | `vimeo.com/<id>` |
| Hide from Vimeo ("embed only") | No | **No** | Yes | `vimeo.com/<id>`, no hash |
| Unlisted | No | Yes, shareable | Yes | `vimeo.com/<id>/<hash>` |

`video` stores the share URL exactly as Vimeo gives it. Embed as
`https://player.vimeo.com/video/<id>`, adding `?h=<hash>` only when the URL has a second
segment. The front end must parse both forms and must not assume the last path segment is the
ID.

**Hide from Vimeo is the preferred setting for films whose only job is to play on this site.**
It achieves the curation goal with no privacy hash to carry, so the URL stays a clean
`vimeo.com/<id>`. Its one cost is that there's no vimeo.com page to send anyone; the film
exists only as an embed. Use Unlisted instead where a sendable link is wanted.

None of these is a security control. An embedded film is visible to anyone who loads the page.
Anything genuinely not for public view should be Private on Vimeo and absent from
`projects.json`.

### Posters

A film should never open on an empty rectangle. Vimeo's own thumbnail lives inside the player
iframe, which is a third-party request, so on a cold load it arrives a second or two late. The
poster is our image, on our domain, outside the iframe. Show it immediately with a play
control over it, and only inject the iframe when someone presses play. The film then loads on
demand, and Vimeo's player script and cookies stay off the page until the visitor asks for
them.

`poster` is a sibling field rather than part of a video object, so it reads the same way as
`credits` and `imageCredit`. When it's empty, fall back to `cover`. Seven projects have a
poster cut from the film itself. Ten films fall back to their cover until better material
exists, and since stills are now cut at poster size, any good gallery frame can fill one.

Each poster carries `posterAlt`. The template must read it rather than reusing the project
title, which is what it does today.

## content/about.json

The About content. There is no photography in it and none is expected. It's a CV, and the
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
| `press[].url` | Empty string means the link is known but the URL is lost, so there is nothing to link to. |
| `press[].note` | Internal only. Never rendered. |
| `contact` | Email and base. The only place contact details live, in About or a Contact view or both, one source either way. **The template currently hard-codes the `mailto:` address while reading the label from here.** |

Current contents: 28 catalogue entries (49 lines with sub-items), 12 awards, 8 press, 13
residencies. Five catalogue entries have no project page and `slug: null`. Catch Me If You
Can, Rise of the Data Collectors, Memory Sphere, Diablo Quintapenhas, Hub Gallery. Every one
of the 20 projects appears in the catalogue.

**The PDF is generated from this file, never written by hand.** Same source, two outputs, so
a CV attached to a funding application can't then drift from the site.

## content/site.json

Site-level copy and the two structural photographs, so neither is hard-coded.

| Field | Notes |
| --- | --- |
| `tagline` | The hero subline. A **display-optional string** per `CONTENT-CONTRACT.md`: the template sets it as three coloured blocks across two lines and must carry the plain string into the accessible layer. |
| `images.hero` / `images.bleed` | `src`, `imageCredit`, `alt`. Both 2560×1440. |
| `sections[]` | `id`, `theme`, `heading`, `blurb` for each of the two sets. The two headings are display-optional; the two blurbs are ordinary text. |

**`site.json` is currently fetched and ignored.** The template hard-codes all five strings.
The fix is in `CONTENT-CONTRACT.md` and costs design nothing. Until it lands, editing this
file changes nothing on the page.

## Migration state

The legacy paths are gone. Every `cover`, `wide`, `poster` and `images` entry in
`projects.json` now points at `img/projects/<slug>/`, and all 20 projects have a cover.

### Outstanding as of 13 Aug

- **Stills are being recut to 2400 x 1350.** Nine of the 27 currently miss the 2400px long
  edge, and `kindred-spirits-01.jpg` is 636 x 358, well under a quarter of the asked-for
  width. Three are not landscape and need a different frame rather than a crop:
  `meyouandus-series-02` and `wishing-well-01` are portrait, `fantasia-express-01` is square.
- **`bigmouth` and `lowry-to-life` list their own cover inside `images`.** Since a film with
  no poster falls back to the cover, both modals show the same photograph twice in the
  thumbnail strip, once with a play triangle and once without. Remove the duplicate.
- **`tilo-v2` needs a film**, `wishing-well` needs one too. `sonic-market` has neither and
  never will.
- **Cover alt text is not written.** All 20 covers still announce themselves as the project
  title. Largest outstanding content job.
- **The loose `img/*.jpg` set from the old WordPress uploads is still on disk** despite the
  rename pass reporting it deleted. Nothing in the JSON references it.

## Files that are no longer used

Safe to delete once new assets land: `img/photoemoticon.jpg`, `img/logo-colour.png`,
`img/logo.png`, `img/logo-black.png`, `img/logo-reverse.png`, `img/logo-ink.svg`,
`img/logo-white.svg`.

`img/brazil.jpg` is now in use. It's the Miguel Perera intervention, and sits in
`meyouandus-series`. The bleed band has its own image at `img/site/myu-bleed.jpg`.

Two legacy files are currently unused and could go either way: `img/humble-market-event.jpg`
and `img/carnival-taxi.jpg` (the latter is in the Humble Market gallery).

The live logo is `img/logo-white.png`, white, transparent background, 1080p wide.

## Brand

Palette from the logo: magenta `#E5007E`, cyan `#009EE2`, yellow `#FFEC00`, ink `#1D1D1B`,
ground `#F3F2F2`, white `#FFFFFF`. `Brand.dc.html` is the design-system sheet and
`DESIGN-STATE.md` records how the front end uses them. Colour roles, typography and motion
are design decisions and are not specified here.

The one place brand and content touch. Images are supplied **full colour, never
pre-converted**, because any greyscale treatment is applied in code and needs the colour
original underneath it.
