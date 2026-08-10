# Handoff — content and assets are ready, the code needs to catch up

Everything in `content/` and `img/` is final enough to build against. `MeYouAndUs.dc.html`
currently reads a 12-entry flat `projects.json` and will need four changes to use it.

Read `content/ASSET-SPEC.md` first — it's the full contract. This file is just what changed.

## 1. The wall is now two sections, not one list

`projects.json` has **20 entries**, each with a `section` of `1` or `2`. Loop over sections,
not over projects. Rows must total 12 **within** a section — they don't run across the break.

| `section` | `theme` | Heading | Copy already written in the mockup |
| --- | --- | --- | --- |
| 1 | `interface` | Breaking interfaces | "We take the technology people use without thinking…" |
| 2 | `place` | Amplifying place | "Work made for one specific street, market, waiting room or station…" |

- Section 1 rows: 5+7, 8+4, 4+4+4, 5+4+3
- Section 2 rows: 7+5, 8+4, 8+4, 3+3+3+3

The "02" marker on the Amplifying place band implies a chapter structure. If a third band
gets added for All Projects / About, it's `03`.

## 2. New fields on every project

| Field | What to do with it |
| --- | --- |
| `wide` | Present on the four span-7/8 projects. **Use it instead of `cover` on the wall** — it's a 2.8:1 crop that suits a panoramic cell. `cover` stays the 3:2 for everywhere else |
| `video` | Vimeo or YouTube URL, present on 13 of 20. Should lead the modal above the gallery. Empty string means no film |
| `credits` | Collaborator line, set small under the blurb. Empty string means none |
| `theme` / `alsoTheme` | `alsoTheme` is on the four projects that are genuinely both. It's for filtering on the All Projects page — **do not tile anything twice on the home wall** |

## 3. Empty cells take their section's colour

Two projects have no cover: `madheads` (section 1) and `not-the-beatles` (section 2). The
drop-slot behaviour already in the build is right — just make the placeholder inherit the
section colour rather than grey. Magenta in section 1, cyan in section 2.

`not-the-beatles` is in a span-7 cell and has no `wide` yet, so it stays a drop-slot until
there's a photograph.

## 4. About is a takeover, not a page

New file: `content/about.json`. Same modal mechanism as a project, but full bleed and routed
at `#/about` so it has a real URL and can be indexed.

Treatment is the inverse of the wall — the wall is all image and no words, About is all words
and no image. Ink `#1D1D1B` on ground `#F3F2F2`, one typographic column, dates in a left
rail, **no photography in it at all**.

Structure: `statement`, `showreel`, `contact`, `works` (28 entries, some with a `sub` array of
venues), `awards`, `press`, `residencies`. Entries in `works` carry a `slug` when they match a
project — link those titles into the project modal so About isn't a dead end. `press` items
with an empty `url` should render as plain text, not a broken link.

Nav currently reads WORK / CONTACT with no route to About or to the full catalogue. Both
need adding.

## 5. Colour roles

| Colour | Job |
| --- | --- |
| Magenta `#E5007E` | Section 1 band and its drop-slots |
| Cyan `#009EE2` | Section 2 band, its drop-slots, and the footer |
| Yellow `#FFEC00` | Project modals |
| Ink `#1D1D1B` | The About takeover |

On yellow: as the full field behind colour photographs it fights badly. Better as the modal's
furniture — rules, meta line, close control, captions — against ink or ground. Worth building
both and looking.

## Notes

- Footer social links have been removed — `contact.links` is an empty array. The old Vimeo
  and Instagram links in the HTML footer should come out too.
- `img/projects/handprint-2012/cover.jpg` and `img/site/hero.jpg` are Simon Kirwan
  photographs and need a credit line. There's no field for image credit yet.
- `content/ASSET-MANIFEST.md` lists which images are final and which are stand-ins. Seven are
  placeholder-grade — worth knowing before judging how a cell looks.
- The old flat `img/*.jpg` files are not in this repo. Nothing references them any more.
