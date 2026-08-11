# Snagging list

Everything outstanding on the content side, as of 10 Aug 2026. Nothing here is being actioned
yet. Items are grouped by the sitting they'd best be done in, and ID'd so we can refer to them.

Three things block others and are marked **↑blocker**.

---

## A. File naming - DONE 11 Aug

Kept the folders, made the filenames self-describing. 49 files renamed to
`<slug>-cover.jpg`, `<slug>-wide.jpg`, `<slug>-01.jpg`, and the two site images to
`myu-hero.jpg` and `myu-bleed.jpg`. Paths rewritten in `projects.json` and `site.json`, the
spec updated, all 51 references verified. No generic filenames remain.

---

## B. Video

**Policy, settled 11 Aug 2026.** Everything hosts on Vimeo. **Privacy is set per film**, chosen
so the public Vimeo channel stays curated rather than mirroring everything the site embeds.
Anything not currently on Vimeo gets uploaded. That closes B3, B4 and B5.

**Three settings, not two.** Vimeo's "embed only" — listed in the help centre as *Hide from
Vimeo* — turns out to fit the goal better than Unlisted:

| Setting | On the channel | Vimeo page | Embeds | URL |
| --- | --- | --- | --- | --- |
| Public | Yes | Yes | Yes | `vimeo.com/<id>` |
| Hide from Vimeo | No | **No page at all** | Yes | `vimeo.com/<id>` — **no hash** |
| Unlisted | No | Yes, shareable | Yes | `vimeo.com/<id>/<hash>` |

Verified against `vimeo.com/1217351938`: the page returns nothing, but the film embeds fine
and its embed URL carries no privacy hash. Compare Invisible Arts Network, which is unlisted —
it has a page *and* needs its hash.

**So Hide from Vimeo is the better default here.** Same curation result, and the URL stays a
clean `vimeo.com/<id>` with no hash to carry or lose. The one cost: there's no vimeo.com page
to send anyone, so the film exists only as an embed on the site. Use Unlisted for any film
you'd want to send as a bare link — to a funder, say.

Either way `video` stores whatever Vimeo gives as the share URL, and the front end adds
`?h=` only when there's a second segment.

None of this is a security control — an embedded film is visible to anyone who loads the page.
Anything genuinely not for public view should be Private on Vimeo and absent from
`projects.json`.

**Consequences of a mixed public/unlisted set** — all minor, none blocking:

- **Two URL shapes to parse.** Only Unlisted adds a hash, so using Hide from Vimeo instead
  keeps every URL in one shape. The parser handles both regardless.
- **URLs change when privacy changes.** Switching a film to Unlisted issues a hash it didn't
  have before. So settle privacy first, then harvest URLs (B9), or you'll collect them twice.
- **Only public films are findable on Vimeo**, and only they accrue plays on the channel.
  That's the point of the exercise.
- **Hide from Vimeo has no shareable page.** Nothing to send, nothing to unfurl in Slack or a
  link preview — the site is the only place it exists.
- **Embed permissions are a separate setting from privacy** (B6) and are the thing most likely
  to break the site.

**Decisions still open**

| ID | Question |
| --- | --- |
| ~~B1~~ | **Settled 11 Aug.** `video` stays a bare URL. `poster` is a sibling field, matching `credits` and `imageCredit`. Title and duration come from Vimeo's API at build time if ever needed |
| ~~B2~~ | **Settled 11 Aug.** Self-hosted posters, 2400 x 1350, shown outside the iframe with the player injected on click. Seven cut from local masters; the rest fall back to `cover` |

### Poster frames (B2)

Two separate things, and the difference matters for "an image the moment they land".

**1. Vimeo's own thumbnail — fully under your control.** In the video's settings there's a
Thumbnail section where you can pick a pre-selected frame, scrub the film and hit *Select this
frame*, or upload a custom image. So the still is a choice, not a lottery.

**2. But Vimeo's thumbnail can't be instant.** It lives inside the player iframe, which is a
third-party request — DNS, connection, player JavaScript, then the image. That's typically a
second or two of empty rectangle on a cold load, and longer on mobile. No Vimeo setting fixes
this, because the delay is the iframe itself, not the image.

**If an image must be there immediately, it has to be our image, served from our own domain,
outside the iframe** — a still with a play control over it, and the iframe only injected when
someone clicks. The film then loads on demand.

That approach also:

- gives an exact crop rather than whatever ratio the film happens to be
- keeps Vimeo's player JavaScript and cookies off the page entirely until someone chooses to
  play, which is both faster and cleaner for consent
- means the poster doesn't change if a film is ever re-uploaded

Content-side that means one more asset per film — `<slug>-poster.jpg` at 2400px — and a
`poster` field. It could default to the project's `cover`, but a still from the film usually
reads better as "this is a film" than a photograph of the installation does.

**How it's built is Design's call**, and worth raising with them, since it changes the modal
from "embed an iframe" to "show an image, then embed on click".

**Tasks**

| ID | Item |
| --- | --- |
| B6 | **Check the embed setting, not just the privacy setting.** On Vimeo, "who can watch" and "where can this be embedded" are separate. An unlisted film with embedding restricted will fail on the site even with a correct hash. Either allow embedding anywhere, or whitelist the live domain on every film |
| B7 | Upload the missing films. Seven projects have none; four have footage sitting locally: `homewalk` (`ART/homewalk.mp4`), `tilo-v2` (`ART/tilo___…1080p.mp4`, `maybe/tilo.mov`), plus `maybe/hprint-bridge.mp4` and `maybe/Sparks snippert.mp4` for Handprint and When I Grow Up, which have films already but these may be better |
| B8 | Re-upload Humble Market from YouTube to Vimeo, then swap the URL |
| B9 | Re-check the 11 existing films after any privacy change — switching a public film to unlisted **issues a hash**, so every one of those URLs in `projects.json` will need updating |
| B10 | 2.3GB of masters across `ART/`, `maybe/`, `HYBRID/`, `CHINA/`, `COMMERCIAL/` with names like `phoenix-update.mp4 (720p).mp4` and `RecordIt-28484B78-….MP4`. If A is worth doing for images, the masters deserve it more — they're the irreplaceable originals |
| B11 | Decide where masters live long-term. They must not go in the site repo |
| B12 | **Ten films still need a poster** - `bigheads`, `fantasia-express`, `bigmouth`, `emofie`, `humble-market`, `meyouandus-series`, `not-the-beatles`, `kindred-spirits`, `lowry-to-life`, `handprint-2008`. All exist on Vimeo only, so I can't cut frames. They fall back to `cover` until a still arrives |

---

## C. Images — gaps and stand-ins

| ID | Item | Note |
| --- | --- | --- |
| C1 | `sonic-market` has **no photograph and no film** | Confirmed 11 Aug. The red graphic panel is the only asset that exists. A permanent public installation, commissioned by Brighton Digital Festival, with no documentation of any kind — the biggest hole in the archive. Everything else in the 20 now has at least one moving image |
| C2 | `bigheads` — no imagery at all | Renders as an empty cell |
| C3 | `not-the-beatles` — no imagery at all | Needs a `wide` too, it's in a span-7 cell |
| C4 | `bigmouth` — 640×360 upscaled 3.75× | Soft. Vimeo holds a larger still of the same frame |
| ~~C5~~ | ~~`when-i-grow-up`~~ | **Done 11 Aug.** Replaced with a frame off the 4K master of the 2023 restaging, showing a child and adult at the screen. Gallery image added from the same source |
| C6 | `tilo-v2` — video frame grab, dark | Also unconfirmed, see D1 |
| C7 | `homewalk` — video frame grab | Acceptable, but a still would be better |
| C8 | `fantasia-express` — square original | The span-8 wide crop is a narrow band of it |
| C9 | `lowry-to-life` — portrait illustration | Also unconfirmed, see D2 |

---

## D. Decisions only Alastair can make

| ID | Question |
| --- | --- |
| D1 | Is the TILO platform film v2 (2023, Phoenix Nottingham) or v1 material? |
| D2 | Is `Al_colour_27.jpg` really Lowry to Life? It's what the old site used but it reads as a children's drawing. **Now testable** — a Lowry to Life film has turned up (`vimeo.com/166343780`, 86s), so a frame from it settles both the cover and this question |
| D3 | The Guardian press link is mangled at source (`guardian.co.uk/U.K./…/Nov./…`). Find the live URL, or drop the entry? |
| D4 | Five catalogue entries have no project page — Catch Me If You Can, Rise of the Data Collectors, Memory Sphere, Diablo Quintapenhas, Hub Gallery. Stay as text-only, or promote any? |
| D5 | Does `AUDIT.md` belong in a public repo? It's blunt about what the old site got wrong |
| D6 | Where do `OLDSITEIMAGES/` (165MB) and the video masters (2.3GB) live? Not the site repo |
| D7 | Is there an Instagram? Currently no social links anywhere |

---

## E. Content still to produce

| ID | Item |
| --- | --- |
| E1 | The All Projects page — structure and copy. Five text-only catalogue entries land here (D4) |
| E2 | Alt text for all project images. Only the two site images have it |
| E3 | Blurbs for `bigheads` and `tilo-v2` are thin — both were written without a film or photograph to work from |
| E6 | **Rewrite the `fantasia-express` blurb from the Vimeo description.** The original does the turn better than my compression of it — states the R&D framing plainly, then undercuts it: *"Actually, that is a lie, the Fantasia Express is an alien spaceship sent to earth to capture relics of our imagination. A cross between Predator and The Hitch-hiker's Guide to the Galaxy."* Approved 11 Aug |
| E7 | As each film comes in, check its Vimeo description against the blurb — Fantasia's was better than mine, others may be too. Cheapest content win available |
| E8 | **Add *Forest* to the About catalogue** — a second Phoenix Sparks festival commission, May 2017, film at `vimeo.com/219313639`. It appears nowhere in `about.json`, which means the old site's catalogue was already incomplete. Parked in `VIDEO-UNASSIGNED.csv`; a candidate for the All Projects page (E1) rather than the wall of 20 |
| E9 | If *Forest* was missing from the catalogue, others may be too. Worth a pass over the Vimeo library against `about.json` once the intake is done — the account is turning out to be a better record than the old website was |
| E4 | The About PDF, generated from `about.json` |
| E5 | `not-the-beatles` and `bigheads` have no `credits` — check whether anyone should be named |

---

## F. With Design — tracking only

From `DESIGN-STATE.md`, not ours to do, but they gate what content is visible:

| ID | Item |
| --- | --- |
| F1 | Two-section loop — section 2 is currently a duplicate of section 1 |
| F2 | `video` and `credits` populated but not rendered |
| F3 | `imageCredit` has nowhere to display — Simon Kirwan needs a line |
| F4 | About and Contact takeovers are blank, ready for `about.json` |
| F5 | `#/about` as a real URL — still React state, so About is invisible to search |
| F6 | Swap the stage photographs onto the real `hero.jpg` / `bleed.jpg` |
| F7 | Empty cells still neutral rather than section-coloured |

---

## G. Pre-launch checks

| ID | Item |
| --- | --- |
| G1 | Every image path resolves and every Vimeo URL still plays |
| G2 | Image credits appear wherever the credited images do |
| G3 | Total page weight — 14MB of images today, before any section 2 assets |
| G4 | Redirects from the old `/work/<slug>` URLs. 27 pages currently indexed; nearly all change slug or disappear |
| G5 | Alt text present on every image |

---

## Suggested order

1. ~~**A**~~ done.
2. **D**, because five of the seven are one-line answers that unblock other items.
3. **B6–B9** as one Vimeo session: set privacy, check embed settings, upload the missing
   films, then collect every URL in its final hashed form and update the JSON once. Doing the
   privacy change and the URL harvest separately means doing the harvest twice.
4. **B1 / B2** whenever the modal gets built — they only matter once a film is on screen.
5. **C** and **E** as material comes in.
6. **G** last, against the built site.
