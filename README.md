# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/ilham270207/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/ilham270207/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

`main.py` draws a newspaper front page — **"The World in One Page"** — summing up Monday 23 November 2026's world news as a single 1024×1024 PNG. The page is dense and busy, like a morning paper: six stories, each with its own photorealistic AI-generated illustration, headline, sub-headline and deck, plus a briefs band and a BY THE NUMBERS strip. Text and layout are drawn in code with Pillow; the six illustrations in `assets/` are original AI-generated artwork (no photographs, no network, no likenesses of real people). No random numbers, no timestamps. Running it twice writes byte-identical PNGs.

## Run it

```sh
python3 main.py
# writes /output/entry.png (or $OUTPUT_PATH; falls back to ./output/entry.png)
```

---

Entered on [make.fun](https://make.fun/?ref=vs40zhzs&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards

## The stories (all verified from multiple outlets)

1. **CLIMATE — COP31 climate deal collapses as draft drops fossil fuels.** 194 delegations; fossil fuels dropped from all drafts despite 100+ countries objecting; the longest COP, the first to fail since Copenhagen 2009. (CNN, Le Monde, AP, WSJ)
2. **MIDDLE EAST — Iran strikes US bases in Bahrain as Gulf war widens.** IRGC claims two US Patriot radars hit in Al-Riffa and Awali; two injured, a factory burned in Sitra; the US says its forces were unharmed. (Reuters, Madhyamam, Geneva Times)
3. **UKRAINE WAR — Russian cargo ship Sparta II ablaze off Finland after drone strike.** Two drones hit the 121 m ship bound for Kaliningrad; 16 crew evacuated (one lightly injured); Finland, Estonia and Russia fought the fire together. (CNN, Reuters, ISW)
4. **AMERICAS — Mexico captures cartel boss 'El Chapo Isidro'.** 11 killed in the raid to capture him — four soldiers and seven cartel members in Guasave; eight arrested, flown to Mexico City, with US intelligence help. (CNN, AP, Times Now)
5. **ASIA — Seoul minister quits in AI exam-cheating scandal.** Education minister Choi Kyo-jin (72) resigns; the trigger was a tax accountant exam top scorer cheating with a mini camera and AI; 111 device violations detected. (Reuters, Korea JoongAng Daily, TBS)
6. **CYBER — FBI crime database hacked, Trump confirms.** The NCIC holds warrants, fingerprints and missing-person records; unclear what data was taken; the second breach after ShinyHunters (September); the USDA was hit the same day. (AP / SecurityWeek, The Times, CNN)
7. **ALSO TODAY —** Lisbon cost-of-living march; 50 missing after an Indonesia factory fire; Nepal PM meets Modi in Delhi; India posts a record 720/9d in the Wellington Test.

## Verification (local, 23 Nov 2026, revision 3)

- `python3 main.py` three times → identical SHA-256 (`378010a3dd6d7a409003e2b59dd2b8e4abe9f0b9b5b186b9671ca5b7f2e8921d`)
- Output: 1024×1024 PNG, 305,516 bytes (limit 1 MiB)
- Visual check: all six photorealistic thumbnails shown, every headline / sub-headline / deck complete, no overlaps, all text readable
- No network access in the program; illustrations are fixed files in `assets/`.

## License

MIT. Fonts: DejaVu Sans (see `fonts/`).
