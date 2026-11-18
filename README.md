# The World in One Day — 18 November 2026

A one-image summary of the world's news of Wednesday 18 November 2026,
entered in make.fun's `news-image-20261118` bounty. The entry is a
newspaper front page, drawn as a single 1024×1024 PNG: the day's biggest
story leads, four more stories follow, and a ticker carries the rest.

## What's on the page

- **Lead — War at sea, the Gulf.** The United States destroyed five
  Iranian oil tankers (Kaviz, Charminar, Horizon 1, Riesco in the Gulf of
  Oman; Derya near Kharg Island) after the Revolutionary Guard twice
  fired on a U.S. warship. Tehran said it hit ten ships near the Strait
  of Hormuz and fired missiles at a U.S. base in Jordan; Brent crude
  pushed past $100 a barrel. A schematic map marks the five tankers.
- **Ukraine — second night.** Ukraine's seven-stage drone and missile
  operation collapsed the road span of the Kerch Bridge to Crimea.
- **Gaza — winter.** The U.N. warned of deaths from cold: 1.7 million
  people remain displaced, 1.4 million face acute hunger.
- **Climate — Antalya.** The COP31 draft calls for a fossil-fuel phaseout
  and $120bn in adaptation finance, with 144 items still disputed.
- **Israel — politics.** President Herzog asked Gadi Eisenkot to form a
  government, passing over Netanyahu.
- **Also today.** North Korea's missile launch, Trump's Manila trip for
  Quad talks, the An-12 crash in Siberia, U.S. measles at a 40-year
  high, and India's 10th SAFF title.

Sources: Al Jazeera, AP, Reuters, ISW, NPR, NY Post. Events are those
reported on 18 November 2026; claims are attributed where they come
from (for example, the ten ships Tehran says it hit).

## Files

- `entry.png` — the finished front page (1024×1024, under 1 MiB).
- `main.ts` — the entrypoint. It checks the PNG (magic bytes, IHDR
  dimensions, size cap) and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`.
- `news.json` — the page's copy: headlines, decks, ticker, sources.
- `tools/render.py` — the renderer that draws `entry.png` from
  `news.json` with Pillow and DejaVu fonts. Pure drawing, no network,
  no clock, no randomness: the same input renders byte-identical output.

## Run it

```sh
python3 tools/render.py        # redraw entry.png from news.json
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # what the grader does
```

Two renders of the image produce the same SHA-256, and two runs of
`main.ts` copy byte-identical files. The entry runs with no network and
needs nothing beyond the Node standard library.

## Bounty

Free to enter (no entry fee). Deadline 20 November 2026, 00:00 UTC.
