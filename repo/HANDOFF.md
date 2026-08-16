# Content handoff - export of 13 Aug 2026

Reply to `HANDOVER.md` of 13 Aug. Supersedes the handoff of 11 Aug.

This handoff has a **Text changes** section, and every one from here will. `HANDOVER.md`
reported the close control becoming an X and the film control becoming a triangle as visual
notes, and neither read as what it was, which is a word leaving the page. One of the two words
did not survive the move.

The rules both sides now work to are in `content/CONTENT-CONTRACT.md`. Short version. Content
owns every word, including the ones nobody sees. Design owns every pixel. The template holds no
strings.

## Text changes

**Added.**

- `posterAlt` on the seven projects that carry a poster frame. Real alt text, written from
  looking at each still. Needs one template change to appear, below.
- `content/ui.json`. The 23 chrome strings that were living in the template, lifted out and put
  back through `language.md`. Includes two strings that do not exist on the site at all, a page
  title and a meta description, both marked DRAFT and needing client sign-off.

**Changed.** Both section blurbs in `site.json`, rewritten by Alastair on 15 Aug.

Breaking interfaces, 27 words to 41.

> Old: We take the technology people use without thinking - screens, sensors, phones, ticket
> gates - and bend it into something that makes strangers talk to each other.
>
> New: We have been working with participatory technology for 18 years. What was niche then is
> in everyone's pocket now. Our new direction applies the same artistic sensibility to the
> devices themselves, breaking their interface so they serve real experiences and connections.

Amplifying place, 20 words to 43.

> Old: Work made for one specific street, market, waiting room or station - built with the
> people who already use it.
>
> New: Some artworks respond to their local context. Others create one. Both are built around
> the people passing through, and often the work does not exist without them. We rarely expect
> people to come to us. We disrupt the routine they are already in.

Both blocks were 27 and 20 words. They are now 41 and 43, so they sit level, but each is
roughly double what the modal was styled around. Worth a look at the display size.

**The template will not show either of these.** The section blurbs are two of the five strings
hard-coded in `MeYouAndUs.dc.html`, lines 55 and 92, so the new wording has to be typed in by
hand until the `site.json` fix lands.

**All 20 project blurbs**, rewritten by Alastair on 15 Aug and edited lightly. 1,415 words to
1,575, none over the new 100-word ceiling. Several correct facts the old copy had wrong.
Homewalk is about the first post-COVID exhibition at Phoenix rather than about migration.
Bigheads scans your head into a series of mini games. BIGMOUTH is a megaphone with its
microphone replaced by a camera. The full set is in `content/BLURBS-DRAFT.md` with the previous
text under each one.

**One title changed.** `townsend-lane` is now titled `26:14:17 (WAITING)` rather than
`26:14:17`, in `projects.json` and in the About catalogue entry in `about.json` so the two
match. The title drives the grid label, the modal heading and the current image alt text, so
all three follow. The Wishing Well blurb still refers to it as `26:14:17` in prose, which reads
better mid-sentence.

**Two corrections to project data.** `tilo-v2` and `homewalk` both carried
`"place": "Nottingham"`. Phoenix is in Leicester and both projects were made with Phoenix, so
both now read Leicester. Nothing else in `about.json` referenced Nottingham.

`projects.json` also gained `posterAlt` and nothing else in it moved.

**Removed.** Nothing.

**Requested of design.** Five strings in the template need correcting and one needs writing.
Listed under "What the template needs" below.

## New files in content/

| File | What it is |
| --- | --- |
| `CONTENT-CONTRACT.md` | The ownership boundary, the typography exception, the handover rule |
| `ui.json` | Interface chrome. Labels, control names, section headings, empty states, page metadata |
| `UI-STRINGS.md` | The register. Every string on the page, where it lives, what it says |
| `check-strings.py` | Scans the template and reports any string that did not come from JSON |
| `check-prose.py` | Hunts the `language.md` tells in any markdown or text file |
| `SITE-JSON-WIRING.md` | The homepage change, line by line |

Run the checker before sending anything over.

```
python3 content/check-strings.py MeYouAndUs.dc.html
```

Current result is twenty-nine literal strings, three display-optional strings allowed by the
contract, and one control with no accessible name. A clean run means the boundary held.

## What the template needs

Six changes. The first is the only one that stops the site working for somebody.

**1. The play button has no accessible name.** Line 234. No `aria-label`, no text, and the only
readable thing inside it is the poster image whose `alt` is the project title. A screen reader
announces the control as "Bigmouth, button". The film is undiscoverable without sight.

```html
<button onClick="{{ playFilm }}" aria-label="Play film" ...>
```

**2. Read `posterAlt`.** Line 236 currently sets `alt="{{ workTitle }}"` on the poster image.
It should read the new field. Seven projects have one, and the fallback where a project has no
poster stays as it is for now.

**3. Five em dashes.** Lines 55, 92, 124, 190 and 262. `language.md` bans them. Lines 55 and 92
are copy that is correct in `site.json` and was retyped into the template with the wrong
punctuation, so those two should go back to matching the JSON word for word. Corrected versions
of the other three are in `ui.json`.

**4. The email link is a typed address.** Line 210 hard-codes `mailto:info@meyouandus.co.uk`
while the visible label at the same line comes from `about.json`. Change the address in the JSON
today and the page shows the new one and mails the old one. Point the `href` at
`about.contact.email`.

**5. The footer.** Line 124 reads
`© 2026 MeYouAndUs — Liverpool / Manchester`. An em dash, a year that is wrong in January, and a
location duplicated from `about.contact.base`. Pattern in `ui.json` under `footer`.

**6. `about.showreel` is unguarded.** Lines 547 and 548 read `about.showreel.url` and
`.caption` with no fallback, and nothing on the page renders either. Deleting the key throws and
takes the whole About panel with it. The key stays in `about.json` until the template guards it.

## Corrections after design's first pass, 16 Aug

**The tagline snippet in `CONTENT-CONTRACT.md` was wrong and design was right.** It hid all
three blocks with `aria-hidden`, and two of them are links that jump to each section. Hiding a
focusable link removes it from keyboard and screen reader users. The contract now hides only the
"and" block and gives each link its own label. Design's fix, which puts the sentence on the `<p>`
and hides only the middle block, does the same job.

Worth knowing for later. `aria-label` on a plain `<p>` is applied unreliably, because the element
has no role to hang it on. While the blocks are real text the sentence gets read anyway. When any
of the three becomes an image, add `role="img"` alongside the label, or use visually-hidden text.

**Image `src` staying literal is correct.** An `alt` string is writing. The path next to it is an
asset reference and belongs to design. `images.hero.src` and `images.bleed.src` in `site.json`
are a record of where the files live and are not read. `CONTENT-CONTRACT.md` and `ASSET-SPEC.md`
now say so, so nobody edits them expecting an effect.

**`SITE-JSON-WIRING.md` was written after the push** and did not reach the repo. It is there now.
Everything in it was worked out independently from the contract and `ui.json`, so it is a
cross-check rather than new instruction.

## site.json, resolved

`HANDOVER.md` asked for a decision and offered two options, delete the file or lose the coloured
blocks. There is a third and it costs design nothing.

The tagline and the two section headings become **display-optional strings**. The words stay in
`site.json`. The template renders them exactly as designed and carries the plain string into the
accessible layer.

```html
<p aria-label="{{ tagline }}">
  <span aria-hidden="true">Breaking interfaces</span>
  <span aria-hidden="true">and</span>
  <span aria-hidden="true">amplifying place</span>
</p>
```

The typography is untouched. `site.json` becomes a file that is read again rather than one
everybody agreed to ignore, and the copy survives into a CMS.

The three strings are readable today because they are still real text. The pattern matters the
moment any of them becomes an image, which is the kind of change that arrives as a visual note.

**`content/SITE-JSON-WIRING.md` has the whole change written out.** Line numbers, the guarded
reads to add to `renderVals()`, the markup swaps, and how to keep the coloured blocks and the
designed line breaks while the words come from JSON.

## State of the content

| | |
| --- | --- |
| Projects | 20, ten per section |
| Covers | 20 of 20 |
| Video | 17 of 20 |
| Posters | 7, each now with written alt text |
| Cover alt text | 0 of 20. Still the bare project title |
| About | 28 catalogue entries, 12 awards, 8 press, 13 residencies |
| Page title and meta description | Drafted in `ui.json`, not signed off, not on the page |

## Still open

- **Cover alt text for twenty projects.** The largest outstanding content job. Every image on
  the site currently announces itself as the project title. Not started, because the stills are
  still being worked on.
- **Page title and meta description.** Drafts in `ui.json`, client sign-off needed.
- **Images and a film for `tilo-v2`, images for `wishing-well`.** Carried over.
- **Four year values use an en dash**, `2013–15` and three like it. A legitimate typographic use
  rather than a prose tell, so they have been left. The checker flags them. Content call, still
  open.
- **`sonic-market` has no photograph and no film** and none exists. Unchanged.
