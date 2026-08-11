# Migration audit — meyouandus.co.uk → WEBSITE V2

Audited 10 Aug 2026. Sources: the live site (`/`, `/work`, `/about`, `/contact` and all 27
`/work/*` pages), `content/projects.json`, `content/ASSET-SPEC.md`, and the files in `img/`.

**Headline:** the old site has 27 work pages; the new JSON has 12 entries. Most of that
reduction is deliberate and good — 11 of the old pages are fragments of a bigger project.
But 8 real projects fall off the site entirely, 4 images are filed under the wrong project,
and the new schema has nowhere to put video, credits, or press — which is what the old site
actually led with.

---

## 1. Old work pages → new entries

### Correctly consolidated (11 pages → 3 entries)

| Old pages | Folds into |
| --- | --- |
| `the-humble-market`, `humble-market-site`, `intimatron`, `carnival-taxi`, `philosophy-hill` | `humble-market` |
| `handprint-olympics`, `handprint-media-city`, `handprint-trafford-centre` | `handprint-2012` |
| `townsend-lane`, `townsend-lane-dudes`, `2417` | `townsend-lane` |

The old site had these as separate cards with a filter tag, which is why 27 looked like 27
projects. It wasn't. Consolidation is the right call.

### Carried across cleanly (6)

`fantasia-express`, `invisible-arts-network`, `sonic-market`, `emofie`, `kindred-spirits`,
and `time-and-weather` (now inside TILO).

### Deliberately dropped (1)

`lancaster-university-seminar` — a talk, not a work, no text on the page. Belongs in a CV
list if anywhere.

---

## 2. Projects that disappear (8)

These have live pages on the old site and no home in the new one.

| Project | Date | Context | Why it matters |
| --- | --- | --- | --- |
| **Lowry to Life** | Nov 2011 | Salford Uni / MediaCityUK commission. Telematic public artwork on Lowry's Piccadilly Gardens (1954) | Guardian **and** BBC coverage. Arguably the best-documented work you have — and the spec already earmarks `lowry-to-life.jpg` for the hero |
| **Handprint (2008)** | Dec 2008 | Projection on Manchester's 2nd-tallest building | The origin of Handprint 2012. BBC interview. Currently reads as if Handprint began in 2012 |
| **BBC Big Screens** | 2010–11 | Mass-participation artwork, Manchester / Leicester / Edinburgh | A national broadcast platform, entirely absent |
| **BIGMOUTH** | Jan 2016 | Metal, Liverpool Provocations | Corridor8 review. Strong concept (confessional / room 101, spherical projection) |
| **Cakenocake** | Aug 2016 | Self-initiated, Liverpool high street | The only unplugged, no-technology piece — useful counterweight to a wall of screens |
| **When I Grow Up** | May 2014 | Sparks festival, Phoenix Leicester | Its image is currently misfiled under Emofie (see §4) |
| **MeYouAndUs series** | 2010–12 | Miguel Perera Brazil, Exquisite Corpse, FACT, Robots + Avatars, Hub Gallery | The series the practice is *named after* |
| **TILO v1** | 2013–15 | Digital R&D Fund for the Arts. FACT, Phoenix, AHRC showcase, Unilever | Award-winning, two published articles. `tilo-v2` implies a v1 the site never shows |

Plus five more from the About catalogue that never had a work page and still don't:
**Catch Me If You Can** (2018, Phoenix), **Rise of the Data Collectors** (Dec 2017,
Guangzhou — you have a report PDF and photos in `CHINA/`), **Memory Sphere** (Dec 2015,
Kazimier), **Diablo Quintapenhas** (May 2015, Phoenix), **Wishing Well** (2012, Mere Lane
health centre, permanent).

**Decision needed:** a 12-cell wall can't hold 20+ projects. Either accept the cut and add a
plain-text index page for everything else, or widen the wall. Recommendation: keep the wall
at 12 and add a "Full catalogue" page — the About page's exhibition list is already 90% of
that copy and currently has nowhere to go (§5).

---

## 3. New entries with no old-site source (4)

`not-the-beatles` (2024), `bigheads` (2023), `tilo-v2` (2023), `homewalk` (2022). The old
site stops at Fantasia Express, 2019 — so nothing can be migrated for these. Everything has
to be produced fresh: **no cover, no gallery, and no long-form text exists anywhere.**

Candidate footage already in your folders:

- `homewalk` → `ART/homewalk.mp4`
- `tilo-v2` → `ART/tilo___digital_&_interactive_art_platform (1080p).mp4`, `ART/phoenix-update.mp4`, `maybe/tilo.mov`
- `bigheads` → nothing found
- `not-the-beatles` → nothing found

---

## 4. Errors in the current projects.json

Four images are attributed to the wrong project. These are factual errors, not just
placeholders:

| Entry | Problem |
| --- | --- |
| `handprint-2012` | Gallery leads with `lowry-to-life.jpg` — a different 2011 commission — and includes `bbc-big-screens.jpg`, a separate 2010–11 series |
| `townsend-lane` (26:14:17) | Gallery includes `wishing-well.jpg`. Wishing Well is the **Mere Lane** health centre; 26:14:17 is **Townsend Lane**. Two different commissions |
| `emofie` | Gallery includes `when-i-grow-up.jpg` — the 2014 Sparks commission, a different artwork |
| `tilo-v2` | Cover is `tilo-weather.jpg`, a 2014 TILO v1 screen, used for a 2023 v2 entry |

Text discrepancies against the old site:

- **`invisible-arts-network`** — `commissioner` reads "Six-month residency and public event",
  which is a description, not a commissioner. It was a residency **for Rural Media**.
- **`fantasia-express`** — the project page credits Innovate UK with LNER; the About page
  credits the Department for Transport. Pick one. Collaborators (Corporation Pop, Immersive
  Storylab, LNER) have nowhere to go.
- **`humble-market`** — the Anglo/Brazilian company **ZU UK** is the named collaborator on
  the old site and isn't mentioned.
- **`emofie`** — dated 2016 here; the old site dates the app to Oct 2015 and the Phoenix
  installation to May 2016. `"2015–16"` is more accurate.
- **`kindred-spirits`** — blurb says "pairing visitors with strangers they never meet", which
  isn't quite what the work did (coloured tickets → costume → photobooth → 36-screen wall of
  everyone who chose your colour). Worth rewriting from the source text.

Blurb lengths, checked against the 30–45 word rule: **11 of 12 are under it.** Only
`humble-market` (31) reaches the range. The rest run 15–25 words — `kindred-spirits` is 15,
`fantasia-express` 17, `sonic-market` and `emofie` 19. They read as captions rather than the
statements the spec describes, and at display size in the modal they'll look thin. Either
lengthen them or relax the rule in ASSET-SPEC.md to 15–45.

On the good side: the wall geometry is sound (spans total 12 on every one of the five rows),
and every path in the JSON resolves to a file that actually exists — nothing is broken, just
legacy.

---

## 5. Content with nowhere to live

The new spec covers a project wall and modals. The old site has three bodies of content the
schema can't hold:

1. **Video.** 18 of the old pages lead with a Vimeo or YouTube embed — it is the primary
   documentation for most of these works, and for the performance pieces it's the *only*
   documentation. `projects.json` has no video field. This is the single biggest loss in the
   migration.
2. **Credits and collaborators.** Corporation Pop, ZU UK, Amaze, Pixel Inspiration, Mash
   Cinema, Kepla, Tomo, Pufferfish, tenantspin. No field.
3. **The About page in full** — founding statement, a 30-item exhibition catalogue, 13
   awards/memberships, 8 press links, 13 residencies, and the 9-minute showreel
   (vimeo.com/124827585). The new spec doesn't mention an About page at all.

Also unaccounted for: the contact form.

**Suggested schema additions:** `video` (string, Vimeo/YouTube URL), `credits` (string),
`links` (array of `{label, url}`). All three are optional and don't disturb the existing
contract.

---

## 6. Image gap

Every image in `img/` is legacy: **1500px on the long edge, spec wants 2400px.** Nothing
currently in the folder meets the spec. Re-export from the originals is needed across the
board, not just for the empty slots.

| Need | Status |
| --- | --- |
| `img/site/hero.jpg` 2560×1440 | **Missing.** Nearest is `lowry-to-life.jpg` at 1500×998 |
| `img/site/bleed.jpg` 2560×1440 | **Missing.** `brazil.jpg` is 1500×844 |
| `img/projects/<slug>/` structure | **Doesn't exist.** All 30 files are flat in `img/` |
| `cover.jpg` × 12 | 9 present as legacy files, 3 empty (`not-the-beatles`, `bigheads`, `homewalk`); `tilo-v2` has one but it's a wrong-generation image |
| `wide.jpg` for span 7–8 | **None exist.** Needed for `invisible-arts-network` (8), `kindred-spirits` (8), `not-the-beatles` (7) |

Aspect-ratio problems in the current set:

- `fantasia-express.jpg` and `-2.jpg` are **1:1 square** going into a 1.6:1 cell — heavy
  side-cropping
- `sonic-market.jpg` is 1.22:1 into a 1.6:1 cell
- `wishing-well.jpg` is **portrait** 3:4 — will crop badly anywhere on the wall
- `kindred-spirits.jpg` (1.78:1) is the cover for a span-8, 3.2:1 cell — will lose roughly
  half its width

Files confirmed safe to delete once replaced: `photoemoticon.jpg` (Lancaster seminar, page
dropped), `logo.png`, `logo-black.png`, `logo-reverse.png`, `logo-colour.png`,
`logo-ink.svg`, `logo-white.svg`. Keep `logo-white.png` (1800×578).

---

## 7. Recommended order of work

1. **Fix the four misattributed images** in `projects.json` — 10 minutes, and it's currently
   wrong in public-facing copy.
2. **Decide the catalogue question** (§2): 12-project wall + full-text catalogue page, or a
   wider wall.
3. **Add `video` to the schema** and populate from the old site — the URLs are all captured
   and it costs nothing but a field.
4. **Settle the About page**, which is the largest single block of homeless content.
5. **Re-export images to 2400px** into `img/projects/<slug>/`, then repoint the JSON.
6. **Shoot or grab** covers for the four 2022–24 projects; frame-grabs will do for Homewalk
   and TILO v2.
7. **Hero and bleed** at 2560px — the Lowry to Life originals are the obvious hero candidate
   if a high-res version survives.
