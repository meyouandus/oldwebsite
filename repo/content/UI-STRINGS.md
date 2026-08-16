# UI strings - inventory and audit, 13 Aug 2026

Built by reading `MeYouAndUs.dc.html` directly rather than by trusting either handover.

Every piece of text that reaches a visitor, whether they read it or hear it. Three sources now
carry copy. `projects.json` and `about.json`, which content owns. And the template, which
design owns and which nobody has been tracking.

Most of the text on the page lives in the template rather than in `content/`.

`check-strings.py` is the authority on that number and is easier to keep honest than this file.
Its count on 13 Aug was twenty-nine literal strings, three display-optional strings allowed by
the contract, and one control with no accessible name. Run it before trusting anything below.

## Read this first

**The template has five em dashes. The JSON files have none.**

The handover says the hard-coded strings are "still identical to `site.json`". They are not.
When the section blurbs were moved into the template they were retyped with em dashes, and
`language.md` bans them outright. The JSON versions use a spaced hyphen and are correct.

| Line | Template says | JSON says |
| --- | --- | --- |
| 55 | `without thinking — screens, sensors, phones, ticket gates — and bend it` | `without thinking - screens, sensors, phones, ticket gates - and bend it` |
| 92 | `waiting room or station — built with the people` | `waiting room or station - built with the people` |
| 124 | `© 2026 MeYouAndUs — Liverpool / Manchester` | not in JSON |
| 190 | `— {{ p.publication }}` (separator in every press line) | not in JSON |
| 262 | `Images to come — this project predates the archive` | not in JSON |

Lines 55 and 92 are copy I wrote, altered in transit. Lines 124, 190 and 262 are copy written
in the template that has never been through `language.md` at all.

**The play control has no name.** "Play film" was replaced by a triangle, and nothing replaced
the words. The button at line 234 has no `aria-label` and no text. The only thing inside it a
screen reader can read is the poster image, whose `alt` is the project title. So the control
announces itself as "Bigmouth, button". A blind visitor has no way to know a film is there.

The close control is fine. Both X buttons carry `aria-label="Close"`, so the word survived the
switch to an icon. The play control did not.

## Where every string lives

### Header and hero

| What shows | Source | Current text |
| --- | --- | --- |
| Logo, header | template L38 | alt `MeYouAndUs` |
| Nav item 1 | template L40 | `About` |
| Nav item 2 | template L41 | `Contact` |
| Hero image alt | template L47 | `Hundreds of scanned handprints projected onto a railway bridge at night, reflected in the water below` |
| Logo, hero | template L50 | alt `MeYouAndUs` |
| Tagline block 1 | template L51 | `Breaking interfaces` |
| Tagline block 2 | template L51 | `and` |
| Tagline block 3 | template L51 | `amplifying place` |
| Section 1 heading | template L54 | `Breaking` + line break + `interfaces` |
| Section 1 blurb | template L55 | em dash version, see above |
| Bleed image alt | template L87 | `Aerial view at night of a lit outdoor event site, projections and a glowing dome` |
| Section 2 heading | template L91 | `Amplifying` + line break + `place` |
| Section 2 blurb | template L92 | em dash version, see above |

Nothing in this block reads from `site.json`. The line break in both headings is baked in, so
the wrap point belongs to design rather than following from the words.

### Work grids

| What shows | Source | Current text |
| --- | --- | --- |
| Cell title | `projects.json` | `title` |
| Cell meta | `projects.json` | `year` and `place`, joined with a middle dot |
| Cover alt | template L68, L103 | the project `title` |
| Title on cells with no image | template L72, L107 | the project `title` |

Cover `alt` being the bare title is thin. "Handprint 2012" tells a screen reader nothing about
what the photograph shows. Worth deciding whether covers need real alt text in `projects.json`.

### Project modal

| What shows | Source | Current text |
| --- | --- | --- |
| Close button | template L221 | `aria-label="Close"` |
| Title | `projects.json` | `title` |
| Viewer image alt | template L231 | the project `title` |
| Play button | template L234 | **nothing** |
| Poster alt | template L236 | the project `title` |
| Film iframe title | template L244 | `Film` |
| Film thumbnail label | template L459 | `Film` |
| Image thumbnail label | template L462 | `<title> image 1`, `<title> image 2` and so on |
| Empty state | template L262 | `Images to come — this project predates the archive` |
| Detail label 1 | template L266 | `Year` |
| Detail label 2 | template L267 | `Place` |
| Detail label 3 | template L268 | `Commissioner` |
| Year, place, commissioner values | `projects.json` | `year`, `place`, `commissioner` |
| Blurb | `projects.json` | `blurb` |
| Credits | `projects.json` | `credits` |
| Photo credit | template L572 + `projects.json` | `Photography ` + `imageCredit` |

The word "Photography" is a template string prepended to your data. It follows `language.md` as
it stands, but it is design's to change and content's to check.

The "Project" label is gone. Confirmed, no such string anywhere in the file.

### About panel

| What shows | Source | Current text |
| --- | --- | --- |
| Panel title | template L40 via `data-page` | `About` |
| Statement | `about.json` | `statement[]` |
| Heading | template L148 | `Selected works` |
| Catalogue rows | `about.json` | `works[].date`, `.title`, `.detail`, `.sub[]` |
| Heading | template L169 | `Awards and funding` |
| Awards rows | `about.json` | `awards[].date`, `.detail` |
| Heading | template L179 | `Press` |
| Press rows | `about.json` | `press[].date`, `.title`, `.publication` |
| Press separator | template L190 | ` — ` between title and publication |
| Heading | template L197 | `Residencies and talks` |
| Residencies rows | `about.json` | `residencies[].date`, `.detail` |

The four section headings are template strings. They read as though they came from `about.json`
and they never did.

`showreel` is confirmed dormant. Lines 547 and 548 pull `about.showreel.url` and
`.caption` into the render values, and nothing on the page uses either. The handover's warning
is correct and worth repeating. The code reads `about.showreel.url` with no guard, so deleting
the `showreel` key throws and the whole About panel dies. Leave it in place.

### Contact panel and footer

| What shows | Source | Current text |
| --- | --- | --- |
| Panel title | template L41 via `data-page` | `Contact` |
| Email, visible | `about.json` | `contact.email` |
| Email, the actual link | template L210 | hard-coded `mailto:info@meyouandus.co.uk` |
| Base | `about.json` | `contact.base` |
| Footer line | template L124 | `© 2026 MeYouAndUs — Liverpool / Manchester` |
| Footer logo | template L125 | alt `MeYouAndUs` |

Both problems here are in the last column.

The email address appears twice. The visible label comes from `about.json`, the `mailto:` is
typed into the template. Change the address in the JSON and the page shows the new one while
still mailing the old one. Silent, and the kind of thing nobody finds for a year.

`Liverpool / Manchester` also appears twice, once from `about.json` and once typed into the
footer copyright. Change the base and the footer disagrees with the Contact panel.

### Not on the page at all

The document has no `<title>` and no meta description. Nothing for a search result, a browser
tab, a bookmark or a link preview. That is copy, it does not exist, and it is not on anyone's
list.

## Defects, worst first

1. **Play control has no accessible name.** The film is unreachable and undetectable without
   sight. `aria-label="Play film"` on the button at L234 fixes it.
2. **Five em dashes in template copy**, two of them in strings that are correct in the JSON.
   Straight breach of `language.md`.
3. **No page title and no meta description.**
4. **Email link hard-coded** while its label comes from JSON. They can drift apart without
   anyone noticing.
5. **`Liverpool / Manchester` duplicated** between `about.json` and the footer.
6. **`about.showreel` is unguarded.** Deleting the key throws and takes the About panel with
   it.
7. **`site.json` is fetched into state and never read.** Confirmed at L338 and L507 onward.
   `site` appears nowhere in the render values.
8. **Alt text is the project title** on covers, viewer images and posters. Thin, and it means
   the play button inherits a name that describes a photograph rather than a control.
9. **`id="about"` sits on the Amplifying place section** (L85), so the About link's fallback
   anchor points at the wrong part of the page if the click handler does not fire.
10. **Thumbnail labels are generated in JS** at L459 and L462. `Film` and `<title> image 2` are
    strings nobody wrote deliberately.

## What I need from design

- Add `aria-label="Play film"` to the play button, or tell me what it should say.
- Confirm the five em dashes get replaced with spaced hyphens, and that lines 55 and 92 go back
  to matching `site.json` word for word.
- Confirm whether `site.json` stays as the record of that copy or gets deleted. Until that is
  settled the tagline and both section blurbs exist in two places that already disagree.
- Point the `mailto:` at `about.contact.email` rather than a typed address, and pull the footer
  location from `about.contact.base`.
- Say who writes the page title and meta description, and where they will live.
- Say whether covers should carry real alt text. If yes I will add an `alt` field per project
  in `projects.json` and write them.
