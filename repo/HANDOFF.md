# Content handoff

Reply to `DESIGN-STATE.md`. Design decisions are yours; this file and everything in
`content/` are content only. Anywhere my earlier documents strayed into colour, type, motion
or treatment, that's been removed rather than argued with — `ASSET-SPEC.md` is now a data and
image contract and nothing more.

## Your four asks — done

**1. `projects.json` at 20 entries.** Ready. `section`, `span`, `wide`, `video`, `credits` all
populated. Rows total 12 within each section: section 1 is 5+7, 8+4, 4+4+4, 5+4+3; section 2
is 7+5, 8+4, 8+4, 3+3+3+3. Four projects carry `wide` (`tilo-v2`, `fantasia-express`,
`kindred-spirits`, `invisible-arts-network`). Two have an empty `cover` (`madheads`,
`not-the-beatles`). 13 of 20 carry a `video`.

**2. `imageCredit`.** Added to every project entry, empty string where not required. Currently
set on `handprint-2012` only — Simon Kirwan. Also on `site.images.hero`, same photographer.

**3. A `site` block.** New file, `content/site.json`, rather than a block inside another file,
so it can be fetched independently:

```
tagline                    the hero subline, written to hold one line
images.hero / images.bleed  src, imageCredit, alt — both 2560x1440, real files, not stand-ins
sections[]                  id, theme, heading, blurb for the two sets
```

I've included the section headings and blurbs there too. They're copy, and nothing else in
the build is hard-coded, so they may as well match. Ignore that part if you'd rather keep them
in the component.

`img/site/hero.jpg` and `img/site/bleed.jpg` both exist and are in the repo — swap off
`lowry-to-life.jpg` and `brazil.jpg` when convenient.

**4. `about.json`.** Unchanged.

## Contact

Keep both nav items, and read the same `contact` block in `about.json` for whichever view
shows it. There's one email address and a base — not enough to justify a second file, and if
it ever changes it should change once.

Whether Contact is its own takeover or a block at the foot of About is a design call. The
content works either way. Worth knowing that About is long — 28 catalogue entries, 12 awards,
8 press, 13 residencies — so an email at the bottom of it is a long scroll from the nav.

## Your two confirmations

Both are open questions for Alastair, not things I can settle:

- **`lowry-to-life`** — the image is `Al_colour_27.jpg`, which is what the old site's Lowry to
  Life page used. It reads as a children's drawing rather than anything Lowry-ish, so either
  the old site was wrong or I'm misreading the work. Unconfirmed.
- **`tilo-v2`** — cover and gallery are frame grabs from
  `ART/tilo___digital_&_interactive_art_platform.mp4`. The film is branded "digital &
  interactive art platform", which reads later than the 2013–15 v1 material, but I can't
  confirm it's the 2023 Phoenix Nottingham work. Unconfirmed.

Both are flagged in `ASSET-MANIFEST.md` under stand-ins, along with five others — `sonic-market`
(no photography of it exists anywhere), `bigmouth` (640×360 upscaled), `when-i-grow-up`,
`homewalk`, `fantasia-express`.

## Two consequences of your changes, for the record

- **Footer has no email.** So `contact.email` now surfaces only in the Contact view. Noted in
  the spec; no content change needed.
- **The hero subline is new copy.** "Breaking interfaces and amplifying place" came from the
  design, not from me. It's now `site.tagline` and I've left the wording exactly as built.

## Not built yet, so still worth flagging

`video` and `credits` are populated on the entries but not rendered. Section 2 is a duplicate
of section 1. None of that blocks anything on the content side — the data is there when you
get to it.
