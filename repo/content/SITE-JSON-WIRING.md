# Wiring the homepage to site.json

For whoever maintains `MeYouAndUs.dc.html`. Five strings and four image attributes are typed
into the template. They should come from `content/site.json`, which the page already fetches
and then ignores.

## What is wrong now

`site.json` is fetched at line 338 and stored as `this.state.site`. The word `site` never
appears again in `renderVals()`, so nothing on the page reads it. Editing the file changes
nothing.

Meanwhile these are typed into the markup.

| Line | What | Should come from |
| --- | --- | --- |
| 47 | hero `src` and `alt` | `images.hero.src`, `images.hero.alt` |
| 51 | tagline, as three coloured blocks | `tagline` |
| 54 | Breaking interfaces heading | `sections[0].heading` |
| 55 | Breaking interfaces blurb | `sections[0].blurb` |
| 87 | bleed `src` and `alt` | `images.bleed.src`, `images.bleed.alt` |
| 91 | Amplifying place heading | `sections[1].heading` |
| 92 | Amplifying place blurb | `sections[1].blurb` |

Both blurbs and both headings changed on 15 Aug. The versions in the template are now the old
copy.

## The logic change

In `renderVals()`, alongside the existing `const about = this.state.about;`

```js
const site = this.state.site;
```

Then add to the returned object. The guards matter. `about.showreel.url` is read at line 547
with no guard, and deleting that key throws and takes the whole About panel down. Do not repeat
that here.

```js
tagline:   site ? site.tagline : "",
heroSrc:   site && site.images ? site.images.hero.src  : "img/site/myu-hero.jpg",
heroAlt:   site && site.images ? site.images.hero.alt  : "",
bleedSrc:  site && site.images ? site.images.bleed.src : "img/site/myu-bleed.jpg",
bleedAlt:  site && site.images ? site.images.bleed.alt : "",
s1Heading: site && site.sections ? site.sections[0].heading : "",
s1Blurb:   site && site.sections ? site.sections[0].blurb   : "",
s2Heading: site && site.sections ? site.sections[1].heading : "",
s2Blurb:   site && site.sections ? site.sections[1].blurb   : "",
```

## The markup changes

**Lines 55 and 92 are plain paragraphs.** Straight swap, nothing else to think about.

```html
<p style="...">{{ s1Blurb }}</p>
<p style="...">{{ s2Blurb }}</p>
```

**Lines 47 and 87 are the two photographs.**

```html
<img src="{{ heroSrc }}"  alt="{{ heroAlt }}"  style="position:absolute;inset:0">
<img src="{{ bleedSrc }}" alt="{{ bleedAlt }}" style="position:absolute;inset:0">
```

**Lines 54 and 91 are the headings with a designed line break.** The string in JSON is
"Breaking interfaces" with no break in it, because where it breaks is a design decision and
stays yours. Force the wrap in CSS, or split on whitespace in the template. Either keeps the
words in `site.json` and the typography in your hands.

**Line 51 is the tagline, set as three coloured blocks across two lines.** The whole sentence
lives in `site.json` as one string. How it splits into blocks is yours, so split it in the
template rather than adding block fields to the JSON.

## The one accessibility condition

The tagline and the two headings are **display-optional strings** under
`content/CONTENT-CONTRACT.md`. Render them however you like, as long as the words reach the
accessible layer.

Right now they are real text in the DOM, so a screen reader already gets them and nothing extra
is needed. The condition applies the moment any of the three becomes an image, an SVG, or picks
up `aria-hidden`. At that point the container carries the sentence.

```html
<p aria-label="{{ tagline }}">
  <span aria-hidden="true">Breaking interfaces</span>
  <span aria-hidden="true">and</span>
  <span aria-hidden="true">amplifying place</span>
</p>
```

One caution if you do that. The pink and blue blocks are links that jump to each section. Hiding
them from assistive technology removes those controls, so give each link its own `aria-label`
rather than hiding it.

## Checking it worked

```
python3 content/check-strings.py MeYouAndUs.dc.html
```

The seven lines above should stop being reported. The three display-optional strings are
reported separately and are expected to stay until you restyle them.

`content/site.json` also carries `images.hero.imageCredit`, which is Simon Kirwan. It still has
nowhere to display. Open question for the client rather than a fix.
