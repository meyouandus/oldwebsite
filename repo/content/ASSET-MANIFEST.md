# Asset manifest — what's real, what's a stand-in

Built 10 Aug 2026 from `OLDSITEIMAGES/wp-content/uploads/`, the `maybe/happening drone/`
folder, and frame grabs from `ART/`. 48 files, 13MB total. All full colour, sRGB, centre
cropped, 2400px covers and 2560px site images per `ASSET-SPEC.md`.

## Good — use as is

These came off 2400–5000px originals and are genuinely the right image for the project.

| Project | Source | Note |
| --- | --- | --- |
| `handprint-2012` | `SKY5156` (4928×3280) | Professional shot, **credit Simon Kirwan / the-lightbox.com** |
| `kindred-spirits` | `meyouandus-tate-70` (4912×2760) | Native 1.78:1, crops to the span-8 wide cell without loss |
| `invisible-arts-network` | `DJI_0004` (4000×2250) | Drone shot of the projected bridge at The Happening |
| `tilo-v1` | `tilo-fact-weather` (4103×2308) | The "1233 27APR" screens already in your mockup |
| `townsend-lane` | `townsend-4` (4912×3264) | |
| `humble-market` | `humble-market_02` (4000×3000) | Carnival wigs and the police car |
| `meyouandus-series` | `miguel-perera-brazil` (4976×2800) | Night crowd, Brazil |
| `cakenocake` | `29570662046` (2507×1411) | The NOGOD/GOD signboard |
| `emofie` | `12237295866` (2160×960) | Face grid |
| `wishing-well` | `09_aeilbeck-wishing-well` (2828×2121) | |
| `handprint-2008` | `handprint_sm` (2000×1333) | Night street, Manchester |
| `hero.jpg` | `SKY5160` (4928×3280) | Hands on the bridge. Dark, wide, holds the white logo lockup. **Credit Simon Kirwan** |
| `bleed.jpg` | `DJI_0009` (4000×2250) | Aerial of The Happening site, for the Amplifying place band |

## Stand-ins — replace before launch

| Project | What I used | Problem |
| --- | --- | --- |
| `sonic-market` | `sonicmarket-web` red graphic panel | **There is no photography of Sonic Market anywhere in the folders.** The old site only ever had the graphic. A permanent public installation with no documentation is the biggest gap here |
| `bigmouth` | `552980867_640` (640×360) | Only surviving still, upscaled 3.75×. Soft. The Vimeo film is the real record |
| `when-i-grow-up` | `spark-6` (1200×600) | Under half spec width |
| `tilo-v2` | Frame grab, `tilo___digital_&_interactive_art_platform.mp4` | Dark, and I can't confirm the footage is v2 rather than v1 — check before it ships |
| `homewalk` | Frame grab, `homewalk.mp4` | Hand holding a phone with a map. Fine, but it's a video still |
| `fantasia-express` | `opening-frame-web` (2160×2160) | Square original, so the span-8 wide crop is a narrow band of it |
| `lowry-to-life` | `Al_colour_27` (2448×3492) | Portrait illustration cropped to landscape, and I'm **not certain this is Lowry to Life** — it's what the old site's page used, but it reads as a children's drawing. Worth confirming |

## Empty — nothing exists

`bigheads` and `not-the-beatles` have no imagery in any folder. Their `cover` is an empty
string, so they render as drop-slots until something is shot.

`not-the-beatles` sits in a span-7 cell and will want a `wide.jpg` too.

## Discarded

- `FANTASIA_EXPRESS_UI_V5.png` (8192×3664) — it's a brochure/UI spec sheet, not artwork
- The four `ian-web*.jpg` files — all logo lockups, no photography
- `Tilo_logo_WHI_BG.jpg`, `myu-logo*.png` — logos
- `lancaster-photoemoticon` kept, but as an Emofie gallery image, not the Lancaster seminar

## Video

Live intake in progress — see `VIDEO-INTAKE.csv` for the running state. Every URL is verified
against Vimeo's oEmbed endpoint as it arrives.

All URLs collected so far carry **no privacy hash**, so they're all the clean
`https://vimeo.com/<id>` form. The front end must still handle `vimeo.com/<id>/<hash>` in case
any film ends up Unlisted — see `ASSET-SPEC.md`.

`humble-market` is still on YouTube (`youtu.be/ZL3KvwN7eJk`); a Vimeo trailer exists at
`1217351938` and is awaiting confirmation.

## Attribution

`handprint-2012/cover.jpg` and `site/hero.jpg` are both Simon Kirwan photographs
(the-lightbox.com), per the original filenames. Carried as `imageCredit` on the project entry
and on `images.hero` in `site.json`.
