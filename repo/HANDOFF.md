# Content handoff — export of 11 Aug 2026

Reply to `DESIGN-STATE.md`. Design decisions are yours; everything in `content/` and `img/` is
content only. `ASSET-SPEC.md` is a data and image contract and nothing more — where my earlier
documents strayed into colour, type or treatment, that's been removed rather than argued with.

Read `content/ASSET-SPEC.md` for the full contract. This file is what changed.

## Since the last export

**Video is now populated and verified.** 18 of 20 projects carry a film, each URL checked
against Vimeo's oEmbed endpoint rather than taken on trust. YouTube is gone entirely.

**Every URL in this export currently has no privacy hash** — they're all the clean
`https://vimeo.com/<id>` form. The parser must still handle `vimeo.com/<id>/<hash>`, because
any film switched to Unlisted later will gain one. See the Video section of the spec.

**`images` no longer has a cap.** It was 0–3; it's now open-ended, because several projects
have more good photography than three slots allowed. Per your layout the first image sets at
21:9 full width and the rest at 3:2 half width, so an odd total tiles evenly and an even one
leaves a half-width orphan. I'll supply odd totals where the material allows, but the front
end should cope either way.

**One project renamed.** `madheads` → `bigheads`, title **Bigheads** — a trademark-driven
change to the work's actual name. Slug, title and all cross-references updated. It had no
image folder yet, so nothing on disk moved.

**Two entries changed shape.** `when-i-grow-up` is now `"2014 · 2023"` — made for Sparks in
2014, restaged in 2023 on a better screen, and the film attached is from the restaging. Its
About entry carries both stagings as a sub-list.

**New files:** `content/site.json` (tagline, the two site images with credits and alt text,
section headings and blurbs), plus `imageCredit` on every project.

## State of the content

| | |
| --- | --- |
| Projects | 20, ten per section, rows total 12 in both |
| Covers | 18 of 20. `bigheads` and `not-the-beatles` are empty strings |
| Wide crops | 4, on the span-7/8 cells. `not-the-beatles` still needs one |
| Video | 18 of 20 |
| Site images | `hero.jpg` and `bleed.jpg`, both real, both 2560×1440 |
| About | 28 catalogue entries, 12 awards, 8 press, 13 residencies |

Three projects without film: `tilo-v2` and `wishing-well` are pending, `sonic-market` has
none and never will — see below.

## What's still coming

- **Images for `tilo-v2` and `wishing-well`**, and a film for `tilo-v2`
- **`bigheads` and `not-the-beatles`** have films now, so covers can be pulled from them
- **A file rename pass.** Filenames will become self-describing —
  `<slug>-cover.jpg` rather than `<slug>/cover.jpg`. Paths in the JSON will change with them.
  It hasn't happened yet; when it does it's a single co-ordinated change

## Worth knowing

**`sonic-market` has no photograph and no film, and none exists.** A permanent public
installation for Brighton Digital Festival, and the only surviving asset is a graphic panel.
It's the one entry in the twenty with no documentation of the work itself.

**Seven images are stand-ins** — listed in `ASSET-MANIFEST.md`. Worth reading before judging
how any given cell looks.

**Simon Kirwan** shot `handprint-2012/cover.jpg` and `site/hero.jpg`. Carried as `imageCredit`
on the project and on `images.hero` in `site.json`, and still needs somewhere to display.

## Still open on your side

`video` and `credits` are populated but not rendered. `imageCredit` has nowhere to go.
Section 2 is a duplicate of section 1. About and Contact takeovers are empty and ready for
`about.json`. `#/about` is still React state rather than a route, so About is invisible to
search.
