# Sum up 23 November's world news in one image

Entry for the make.fun bounty
[news-image-20261123](https://make.fun/bounty/news-image-20261123)
($100 USDC, 50 places paid; deadline 25 Nov 2026 07:00 WIB).

## What it is

`main.py` draws a newspaper front page — **"The World in One Page"** —
summing up Monday 23 November 2026's world news as a single 1024×1024 PNG.
The page is dense and busy, like a morning paper: six stories, each with
its own illustration, headline, sub-headline and deck, plus a briefs band
and a ticker. Text and layout are drawn in code with Pillow; the six
illustrations in `assets/` are original AI-generated artwork (no
photographs, no network, no likenesses of real people). No random numbers,
no timestamps. Running it twice writes byte-identical PNGs.

## How to run

```sh
python3 main.py
# writes /output/entry.png (or $OUTPUT_PATH; falls back to ./output/entry.png)
```

Fonts are bundled in `fonts/` (DejaVu Sans, free license) so the program is
self-contained in any sandbox.

## The stories (all verified from multiple outlets)

1. **CLIMATE — COP31 climate deal collapses as draft drops fossil fuels.**
   EU and allies reject the Antalya pact for omitting fossil fuels; the
   summit ends with no agreement.
   (Helsinki Times, Jagran Josh, The Daily Jagran, Observer Voice)
2. **MIDDLE EAST — Iran strikes US bases in Bahrain as Gulf war widens.**
   Tehran hits two American bases; Houthis fire on Saudi Arabia as the
   Strait of Hormuz conflict escalates. (Dunya News, Jamuna i-Desk)
3. **UKRAINE WAR — Russian cargo ship ablaze off Finland after drone strike.**
   Fourteen missing as a Russian drone hits a building in the Kyiv region,
   Zelenskiy says. (Jagran Josh, Jamuna i-Desk)
4. **AMERICAS — Mexico captures cartel boss 'El Chapo Isidro'.**
   FBI most-wanted fugitive seized in Sinaloa; eleven killed in the
   firefights. (Salonvision)
5. **ASIA — Seoul minister quits in AI exam-cheating scandal.**
   South Korea's education minister resigns as AI-driven cheating rocks
   national exams. (The Daily Jagran, Observer Voice)
6. **CYBER — FBI crime database hacked, Trump confirms.**
   US intelligence chief acknowledges the breach. (Dunya News, IANS)
7. **ALSO TODAY —** Lisbon cost-of-living march; 50 missing after an
   Indonesia factory fire; Nepal PM meets Modi in Delhi; India posts a
   record 720/9d in the Wellington Test.

## Verification (local, 23 Nov 2026, revision with illustrations)

- `python3 main.py` three times → identical SHA-256
  (`f84cf895e558b88627fec7f536f67014e280c518e9a0ce6f40a85a54a056eca9`)
- Output: 1024×1024 PNG, 288,688 bytes (limit 1 MiB)
- Visual check: all six thumbnails shown, every headline / sub-headline /
  deck complete, no overlaps, all text readable
- No network access in the program; illustrations are fixed files in `assets/`.

## License

MIT. Fonts: DejaVu Sans (see `fonts/`).
