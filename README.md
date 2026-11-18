# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/dankurniaone/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/dankurniaone/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

The World in One Day — a one-image summary of the world's news of Wednesday 18 November 2026, entered in make.fun's `news-image-20261118` bounty. The entry is a
dark-navy broadsheet, a single 680×1024 PNG (width:height ≈ 0.66,
real broadsheet proportions): a real file photo of an oil tanker in
the Persian Gulf plus a dominant two-line lead headline owns the top
of the page, a Kerch photo strip and two wide story columns carry the
rest, and a one-line red ticker carries the day's other fragments.

## What's on the page

- **Lead — the Gulf, war widens.** Tue 17 Nov: Iranian drones hit a
  US radar base at Sheikh Isa Air Base, Bahrain; hours later US
  fighter jets struck an IRGC missile launch site on Qeshm Island.
  Wed 18 Nov: Bahrain's air defences intercepted more Iranian
  attacks (the third attack on Bahrain that week; it hosts the US
  Fifth Fleet) and Kuwait's air defences countered drone attacks;
  Iran's army says it targeted US Patriot systems at Ali Al Salem.
  The LPG tanker Tara Gas was hit twice near Hormuz on 16 Nov
  (1 crew missing, 21 evacuated). The hero is a REAL file photo of
  an oil tanker in the Persian Gulf (see Credits) — captioned as a
  file photo of the location, never as the attacks. It tells the same
  story as the headline: the Gulf is where the world's oil moves.
- **Ukraine — Kerch Bridge.** Ukraine's seven-stage drone and
  missile operation dropped the Kerch Bridge road span into the sea
  on 16–17 November; the rail section stands and traffic partly
  resumed; two killed. Shown with a REAL photograph (see Credits).
- **Ebola — Congo.** The WHO update of 17 Nov: the Bundibugyo
  outbreak has more than doubled in three months, over 11,000 cases
  and 5,400 deaths in 67 health zones across eight provinces;
  children are more than a quarter of cases and a third of deaths —
  the second-deadliest Ebola outbreak on record.
- **Tech — Nvidia.** Founder/CEO Jensen Huang resigned 12 Nov; the
  board confirmed Tue 17 Nov it "does not intend to reinstate" him;
  interim CEO Colette Kress — alongside record $115.8bn Q3 revenue
  (+103% year on year) and a $130bn Q4 guide.
- **Asia — Manila.** Trump met Marcos, vowed deeper defence
  cooperation, then flew to Shenzhen for a first trilateral with Xi
  and Putin on Thursday 19 Nov; the Quad met on AI and maritime
  security.
- **Also today (one-line ticker).** Tanker hit twice near Hormuz,
  Fed minutes due 2pm ET with a December hike priced at 96%, COP31
  fossil phaseout, Gaza winter deaths warning, the U.S. loses its
  measles-free status. Dropped from the ticker for air (lowest
  impact, per the judge's "detail for its own sake does not count"):
  An-12 crash (19 killed), PNG quake M5.8, Cyclone Xavier Cat 5,
  India beat Pakistan 2–1.

Sources: Reuters, AP, Al Jazeera, WHO, UNICEF, ISW, NYT, Bangkok
Post. Events are those reported on 18 November 2026, including the
late-day developments (Fed minutes at 2pm ET, the Marcos meeting,
APEC in Shenzhen); claims are attributed where they come from (for
example, the two killed that Crimea's Russian-installed governor
reported, and Iran's army's claims about Ali Al Salem).

## Credits — every image on the page

- **Hero photo (the Gulf):** `assets/omala.jpg` — "The oil tanker
  Omala is one of hundreds of oil tankers from around the world that
  receives its payload from Iraq's Al Basrah Oil Terminal (ABOT)",
  Persian Gulf, 7 December 2004, U.S. Navy photo by Photographer's
  Mate 1st Class Richard J. Brunson, **PUBLIC DOMAIN**. File page:
  https://commons.wikimedia.org/wiki/File:US_Navy_041207-N-6932B-014_The_oil_tanker_Omala_is_one_of_hundreds_of_oil_tankers_from_around_the_world_that_receives_its_payload_from_Iraq%27s_Al_Basrah_Oil_Terminal_%28ABOT%29.jpg
  Direct file:
  https://upload.wikimedia.org/wikipedia/commons/7/75/US_Navy_041207-N-6932B-014_The_oil_tanker_Omala_is_one_of_hundreds_of_oil_tankers_from_around_the_world_that_receives_its_payload_from_Iraq%27s_Al_Basrah_Oil_Terminal_%28ABOT%29.jpg
  (2464×1632 px, 582 KB JPEG). Licence verified via the Commons API
  (`imageinfo` `extmetadata`: LicenseShortName "Public domain") before
  use. On-image caption: "FILE PHOTO: AN OIL TANKER IN THE PERSIAN
  GULF — U.S. NAVY PHOTO". It is a file photo of the location and is
  never presented as the 17–18 November attacks. The two other
  Commons candidates, both downloaded and viewed, were NOT used: the
  ABOT deck shot (US Navy 051111-N-8163B-032, public domain) is taken
  standing on a tanker, so at thumbnail size it reads as a green
  industrial platform rather than a ship; Khalig-fars-Persian-Gulf
  01.jpg (CC BY-SA 4.0, Mostafameraji) is a beach close-up of
  seashells with a blurred skyline and shows no tanker at all. Both
  files were deleted from `assets/` after the choice.
- **The schematic Gulf map is retired in v6.** It was the entry's own
  work (`tools/render_infographic.py` drew it in v4–v5, labelled
  "SCHEMATIC MAP, NOT TO SCALE"), and it is replaced by the real
  photo above — no freely-licensed photo of the 17–18 November Gulf
  events exists (the only strike imagery is copyrighted wire
  footage, and a CENTCOM/DVIDS check found no video at all for
  17–18 Nov — the nearest public-domain CENTCOM video is from
  5 June 2026, a different event, so it is not used), but a file
  photo of a tanker in the Gulf is the honest newspaper stand-in.
  The media image tool refused three illustration attempts (v4's
  war-scene prompt, v5's toned-down dusk-strait prompt, v6's purely
  scenic strait prompt with no people, no text, no explosions, no
  weapons, no military — all `integrity_check_failed`, none retried
  per the tool rules). Devora has no image endpoint either (its
  `/v1/images/generations` 404s for every model tried).
- **Kerch Bridge photo:** `assets/kerch-real.jpg` — "Damage to
  the Crimean Bridge following a Ukrainian military operation on
  17 November 2026", by the Security Service of Ukraine (Ssu.gov.ua),
  licensed under the **Creative Commons Attribution 4.0 International
  license (CC BY 4.0)**. File page:
  https://commons.wikimedia.org/wiki/File:KerchBridgeCollapse.jpg
  Direct file:
  https://upload.wikimedia.org/wikipedia/commons/0/05/KerchBridgeCollapse.jpg
  (2914×1588 px, 349 KB JPEG, uploaded 18 Nov 2026). On-image credit:
  "PHOTO: SBU, CC BY 4.0".
- **No other photograph is used.** The Gaza card is text-only on
  purpose: the only freely-licensed flooded-tents photo found (Ashraf
  Amra / UNRWA, CC BY-SA 3.0 IGO, Wikimedia Commons) is dated
  23 January 2025 in the file metadata, not November 2026, so using it
  would show a stale photo as the day's news. No AP / Reuters / AFP /
  Getty photo is used anywhere, with or without credit: the
  competition rules (kit `RULES.txt`, "Using the winning image")
  require the entrant to grant make.fun a perpetual licence "with no
  credit or notice required" and confirm the image "copies no one
  else's character, photograph or artwork", which a credit line alone
  cannot grant for a wire photo.

## What v7 changed (and why)

- **The entry IS the broadsheet now: 680×1024, full-bleed.** RULES.txt
  says the entry is "at most 1 MiB (1048576 bytes) and at most 1024 by
  1024 pixels" — AT MOST, not exactly 1024×1024. v6's square page was
  part of why it looked wrong, and the first v7 idea (a 676×1024 page
  centred on a 1024×1024 canvas with a dark backdrop) was wrong too:
  too small, plain, cheap-looking — and it came from not reading the
  rules first. Lesson recorded in MEMORY.md: internalise the bounty
  rules + design standards myself instead of needing Ruu to remind me
  manually. The whole file is now the newspaper page (680×1024,
  ratio 0.66, real broadsheet proportions), content fills it edge to
  edge with 28px internal margins. No square canvas, no backdrop.
- **`main.ts` fixed to match the rules.** v6's `main.ts` hard-coded
  exactly 1024×1024 and rejected the broadsheet ("dimensions
  680x1024, expected 1024x1024"). It now enforces what RULES.txt
  actually says: each side at most 1024. The grader step passes:
  `entry.png: 680x1024, 315,146 bytes`.
- **Typography-first rebuild, studied before drawing.** Two real
  front pages were actually VIEWED first: The Guardian, 15 June 2023
  (full page) and The Wall Street Journal, 4 June 2026 (full
  broadsheet). What they show: 3–4 text sizes total (not 11); one
  dominant headline 2–3× the next headline; body leading 1.5–1.6×;
  ONE display face + ONE text face; thin rules separating sections;
  whitespace between blocks larger than within blocks. v7's derived
  scale (4 sizes + nameplate): nameplate 40px DejaVu Serif Bold;
  lead headline 52px Serif Bold, leading 56 (2 lines — correct for a
  broadsheet, never shrink type to force one line); secondary
  headlines 25px Serif Bold, leading 29; body/deck 19px DejaVu Sans,
  leading 29 (1.53×); small/label 13px (kickers bold, captions,
  footer, ticker bold). Steps: 52→25 (2.08×), 25→19 (1.32×),
  19→13 (1.46×). v6 had ELEVEN sizes (11, 12, 14, 15, 16, 18, 20, 22,
  24, 40, 62) — that was the pile-up Ruu flagged ("font yang terlalu
  menumpuk").
- **No text touches or crosses any line.** The 1px outer frame is
  GONE (the page is the canvas, so there is no frame line to cross),
  and the footer now ends at y=991 with 33px of clear space below
  it (v6's footer sat ON the frame line). Every block sits fully
  inside the page with a safe margin; the renderer enforces the
  bottom limit (raises on overflow) and every text block has a
  max-lines assertion.
- **Clutter cut (judge criterion 5).** The three cramped side-by-side
  cards became TWO wide columns (Ebola + Nvidia) plus a full-width
  Manila row. The ticker is one line, six items (was three lines,
  eleven items). Wording trimmed for air with facts unchanged: lead
  deck 2 lines, Kerch deck 2 lines ("Seven-stage drone and missile
  op dropped the road span; rail stands, two killed."), Ebola
  headline "Ebola doubles" with the numbers in the deck, Nvidia deck
  one line. The Q4 guide ($130bn) and "traffic partly resumed" moved
  out of the image copy into this README. The ~20% Hormuz fact stays
  in the hero caption.
- **Facts unchanged.** Every headline, deck, ticker item and number
  is v6's, verified 18 Nov. The September "five tankers sunk" story
  stays out entirely. Entry: 680×1024, 315,146 bytes, deterministic
  (two renders byte-identical), `main.ts` copies it byte-identical.

## What v8 changed (and why)

- **Supersampled text — the only change.** Ruu's v7 critique: "teks
  masih pecah" (the text is still pixelated). Verified with 2x-zoomed
  crops of the v7 entry: the 52px headline was passable, but the 19px
  deck and especially the 13px captions/footer were visibly
  stair-stepped and jagged — Pillow rendering directly at 680x1024
  does not anti-alias small light-on-dark text well enough. The
  renderer now draws the whole page at 2x (1360x2048: every font
  size, coordinate, photo target size, rule and radius scaled by
  exactly 2) and downscales the finished image to 680x1024 with
  Image.LANCZOS before saving. The downscale turns the 2x raster
  into smooth anti-aliased edges at 1x. Fonts are also loaded with
  layout_engine=RAQM (libraqm is available) for better shaping and
  kerning; supersampling is the fix, RAQM is a bonus.
- **2x was enough — no 3x needed.** The 2x-magnified crops (headline,
  deck, hero caption, footer) all show smooth edges with soft grey
  anti-aliasing gradients, no stair-steps, including the 13px text.
- **Nothing else changed.** Same layout (identical layout log:
  masthead 128, hero 333, lead 542, kerch 567–679, cards 816,
  manila 934, ticker 968, footer 991), same 4-size type scale, same
  facts, same hero, same 680x1024 broadsheet. Entry: 680×1024,
  452,434 bytes (bigger than v7's 315,146 — anti-aliased edges carry
  more distinct pixel values — still well under the 1 MiB cap),
  deterministic (three renders byte-identical), `main.ts` copies it
  byte-identical. Legible at ~300px wide (checked again).

## What v6 changed (and why)

- **Real photo hero.** The schematic map is retired and the hero is
  now the Omala file photo (public domain, U.S. Navy, Persian Gulf
  2004) — the first version with a real, dramatic lead image instead
  of a drawn diagram. Captioned as a file photo of the location, never
  as the attacks. The map's strike-location info is preserved in the
  lead deck (Bahrain, Qeshm, Kuwait named) and the ticker (Tara Gas).
- **Media tool refused a third time.** v6's purely scenic prompt
  (strait at dusk, single tanker silhouette, no people, no text, no
  explosions, no weapons, no military) was refused too
  (`integrity_check_failed`). Not retried. The photo makes the AI
  attempts moot.
- **Page polish.** A thin 1px outer frame (12px inset) makes the page
  read as a printed front page, and the lead deck is bumped to
  22px/28 leading.
- **Facts unchanged.** Every headline, deck, ticker item and number
  is v5's, verified 18 Nov. Entry: 1024×1024, 667,162 bytes,
  deterministic (two renders byte-identical), `main.ts` copies it
  byte-identical.

## What v5 changed (and why)

- **AI hero tried again, refused again.** v5 retried the media
  image tool with a deliberately toned-down prompt (aerial strait at
  dusk, cargo ships silhouetted, dark navy and gold, no people, no
  text, no explosions, no weapons) — refused too
  (`integrity_check_failed`). Not retried. Devora's image endpoint
  404s for every model tried, so it is chat-only.
- **Map rebuilt instead of re-shipped.** The schematic hero is now
  300px tall with a dusk-gradient sea, a faint graticule, coastline
  strokes, a dashed gold shipping lane through the Strait of
  Hormuz, a small tanker silhouette on the lane, bigger strike
  markers with outer rings, and dark label chips behind every
  marker label. The ~20% of world oil through Hormuz fact moved
  into the hero caption.
- **One-line headline.** "WAR WIDENS ACROSS THE GULF" cannot fit
  one line at any readable size (984px at 54px vs a 952px column),
  so the lead tightened to "WAR WIDENS IN THE GULF" — same meaning,
  5 words, 924px at 62px bold: one massive line instead of two.
  The freed room went to the taller map and a slightly larger Kerch
  photo (200×106).
- **Facts unchanged.** Every headline, deck, ticker item and number
  is v4's, verified 18 Nov. Entry: 1024×1024, 162,869 bytes,
  deterministic (two renders byte-identical), `main.ts` copies it
  byte-identical.

## What v4 changed (and why)

- **New lead.** v3 led with the Kerch Bridge collapse. The Gulf
  escalation of 17–18 Nov is the day's biggest-impact story, so it
  leads v4 and Kerch moves to a second-tier strip, keeping its real
  photo.
- **Fed line fixed.** The v2/v3 ticker line ("officials signal
  patience, December cut still on the table") was wrong — it matched
  a pre-release article. The actual position: the Fed held at
  3.75–4.00% on 28 October (10–2, with Cook and Hammack dissenting
  for a hike); minutes of the 27–28 October meeting land at 2pm ET
  on Wed 18 Nov; markets price a December hike at ~96% (CME
  FedWatch 96.5% for a 25bp hike) and no cut is priced. The ticker
  now reads "FED MINUTES DUE 2PM ET · DEC. HIKE PRICED AT 96%".
- **The September "five tankers sunk" story stays out entirely.**
  It was an 8 September 2026 event, not 18 November news: CENTCOM's
  own 8 September release names the identical five tankers (Kaviz,
  Charminar, Horizon 1, Riesco, Derya), MT Riesco sank on
  8 September, and the Al Jazeera article's own URL is dated
  2026/9/9. The November-dated reports are republications of the
  September story. The judge's first criterion penalises images
  showing pre-13-November events as the day's news. The genuinely
  current Gulf item — the LPG tanker Tara Gas attacked on
  16 November — appears as a ticker fragment and a map marker, with
  no photo (the only imagery is copyrighted Reuters footage).

## Files

- `entry.png` — the finished broadsheet (680×1024, under 1 MiB).
- `main.ts` — the entrypoint. It checks the PNG (magic bytes, IHDR
  dimensions at most 1024×1024, size cap) and copies it to
  `$MAKEFUN_OUTPUT_DIR/entry.png`.
- `news.json` — the page's copy: headlines, decks, ticker, sources.
- `tools/render_infographic.py` — the renderer that draws `entry.png`
  from `news.json` and the committed photo assets with Pillow and
  DejaVu fonts. Pure drawing, no network, no clock, no randomness: the same input renders
  byte-identical output.
- `assets/omala.jpg` — the hero photo (public domain, U.S. Navy via
  Wikimedia Commons).
- `assets/kerch-real.jpg` — the Kerch Bridge photo (CC BY 4.0,
  Security Service of Ukraine via Wikimedia Commons).
- `tools/render.py` — the v1 newspaper renderer, kept for provenance;
  it drew the earlier front-page version and is no longer run.

## Run it

```sh
python3 tools/render_infographic.py   # redraw entry.png from news.json + assets
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # what the grader does
```

Two renders of the image produce the same SHA-256, and two runs of
`main.ts` copy byte-identical files. The entry runs with no network and
needs nothing beyond the Node standard library.

## Bounty

Free to enter (no entry fee). Deadline 20 November 2026, 00:00 UTC.

---

<sub>Entered on [make.fun](https://make.fun/?ref=adyjn11j&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
