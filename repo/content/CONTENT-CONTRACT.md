# Content and design - the working contract

Version 1, 13 Aug 2026. Supersedes the ownership language in `ASSET-SPEC.md` and
`DESIGN-STATE.md` wherever the two disagree.

Written after an audit of `MeYouAndUs.dc.html` found twenty-nine strings living in the template,
two of them silently rewritten out of house style on the way in, and one control that lost its
name entirely when it became an icon. None of that was anyone's fault. There was no rule
covering it.

Here is the rule.

## The one principle

**Content owns every word. Design owns every pixel. A word is still a word when it is not
displayed.**

Alt text, button labels, the page title, a caption a screen reader reads aloud and nobody sees.
All of it is writing. It goes through `language.md` and it lives in `content/`.

## The boundary

Content decides what the words are, in every form they take. Design decides where they appear,
what they look like, whether they are displayed or only announced, how many pieces they are
broken into and where the line breaks fall.

Neither side edits the other's without a note. Design does not retype a string into the
template. Content does not specify a colour, a weight or a wrap point.

## Where strings live

| File | Holds | Owner |
| --- | --- | --- |
| `content/projects.json` | Project data and the words that describe each work | Content |
| `content/about.json` | Statement, catalogue, awards, press, residencies, contact | Content |
| `content/site.json` | Tagline, section headings and blurbs, site image alt text | Content |
| `content/ui.json` | Interface chrome. Labels, control names, headings, empty states, page metadata | Content |
| The template | No strings at all | Design |

`ui.json` is new and holds what design had been typing directly. Every string it contains was
lifted out of the template on 13 Aug and put back through `language.md` on the way.

The last row is the whole contract. A literal string in the template is a defect, the same way
a hard-coded colour in a JSON file would be.

## The typography exception

Some copy is not a sentence any more. The hero tagline is three coloured blocks stepping across
two lines, and flattening that back to a plain string would throw away the design.

The exception does not put the words in the template. It changes what the template does with
them.

A **display-optional string** lives in JSON like any other. The template may render it as
typography, split it, colour it, animate it, or replace it with an image. What the template must
do is carry the plain string into the accessible layer, so the words still exist for a screen
reader, a search engine and, later, a CMS field.

For the tagline that means the container carries the whole string, and only the pieces that
carry no function are hidden from assistive technology.

**Corrected 16 Aug.** The first version of this snippet hid all three blocks. Two of them are
links that jump to each section, so hiding them removed those controls from keyboard and screen
reader users. Design caught it. Hide the decoration, never the controls.

```html
<p aria-label="{{ tagline }}">
  <a href="#work"  aria-label="Jump to Breaking interfaces">Breaking interfaces</a>
  <span aria-hidden="true">and</span>
  <a href="#place" aria-label="Jump to Amplifying place">amplifying place</a>
</p>
```

`tagline` comes from `site.json`. The three blocks stay exactly as designed. Edit the string in
the JSON and the accessible name follows, while the visible blocks stay design's to set.

One caveat on `aria-label` here. Screen readers apply it unreliably to a plain `<p>`, because
the element has no role to hang it on. While the blocks are real text the sentence is read
anyway, so nothing is lost today. When any of the three becomes an image or an SVG, put
`role="img"` on the container alongside the `aria-label`, or carry the sentence in
visually-hidden text. Either survives the treatment.

The same pattern covers anything that later becomes an image or an SVG. The words survive the
treatment.

**This resolves the open question in the handover.** `site.json` does not get deleted and the
template does not lose the coloured blocks. The file becomes readable again as the source of the
accessible name, and the visual treatment stays where it belongs.

Three strings currently qualify for the exception. The tagline and the two section headings,
which are split across a line break and carry a scroll wipe. Everything else on the page is
ordinary displayed text and should read from JSON directly.

## How drift gets caught

Not by reading each other's handover documents. That is how five em dashes and a nameless button
got through.

`content/check-strings.py` scans the template and reports every literal string it finds outside
a handlebars expression. Run it before either side sends anything over. A clean run means the
template holds no copy. A dirty run lists exactly which lines to fix.

```
python3 content/check-strings.py "path/to/MeYouAndUs.dc.html"
```

It also flags house-style breaches in whatever it finds, so an em dash typed into the template
fails the check rather than waiting for someone to notice.

`content/check-prose.py` does the same job for the writing itself. Point it at any markdown or
text file and it reports the tells listed in `language.md`.

```
python3 content/check-prose.py content/*.md
```

`language.md` says to apply the rules backwards as well as forwards, so run it over old drafts
rather than only new ones. Every document in `content/` passed on 13 Aug.

The register of what exists lives in `content/UI-STRINGS.md`. Regenerate it whenever the checker
output changes.

## Accessibility, and who calls it

Content calls it. Accessible text is text.

Three standing rules.

**Every control has a name.** An icon-only button carries an `aria-label`. When a word becomes
an icon, the word moves into the label, it does not disappear. The close control did this
correctly. The play control did not, and the film is currently unreachable without sight.

**Every image has alt text written for it.** Reusing the project title is a placeholder.
"Handprint 2012" names the work and says nothing about the photograph. Covers need real alt
text, which means an `alt` field per project in `projects.json`. That work has not been done and is the
largest outstanding content job on the site.

**Decorative images are marked decorative.** `alt=""`, deliberately, rather than left to
default.

## What an image path is

An `alt` string is writing and belongs to content. The file path next to it is an asset
reference and belongs to design, which is why `images.hero.src` and `images.bleed.src` in
`site.json` are not read by the template and should not be. Replacing the photograph means
overwriting the file at the same path. Changing the path is a template edit.

Both `src` values stay in `site.json` as a record of where the files live. Editing them changes
nothing, and `ASSET-SPEC.md` says so.

## Handover discipline

Both sides send a handover. Both handovers carry a section headed **Text changes**, listing
every string added, removed, reworded or moved, including strings that became icons and strings
that stopped being displayed.

A text change buried in a visual changelog does not count as having been reported. The close and
play controls were both mentioned in the last handover, as notes about an X and a triangle, and
neither read as the removal of a word.

If the section is empty, say so. "Text changes: none" is a useful sentence.

## Why this shape, given a CMS is coming

The test for any string is whether someone who cannot read code could change it.

Every string in `content/` passes. Every string in the template fails, and would have to be
found, extracted and rewired at the point the site moves to a CMS, by someone reading a
thirty-nine thousand character file looking for words. The four JSON files map onto CMS fields
more or less directly. The template maps onto nothing.

Doing the extraction now costs a day. Doing it during a CMS migration costs a week and misses
things, because by then nobody remembers which strings were deliberate.

## Open, needs a decision

- The page title and meta description do not exist. Drafts are in `ui.json`, marked as drafts.
  Client sign-off needed on both.
- Cover alt text for twenty projects. A content job. Not started, and it needs the images to
  hand.
- `Liverpool / Manchester` appears in `about.json` and again typed into the footer. The footer
  should read from the JSON.
- The `mailto:` link is a typed address while its visible label comes from JSON. Same fix.
- `about.showreel` is parsed, unguarded and never displayed. Leave the key in place until the
  template guards it, or the About panel throws.
