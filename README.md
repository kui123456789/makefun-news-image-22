[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/kui123456789/makefun-news-image-22/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/kui123456789/makefun-news-image-22/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# The World Today — Sunday 22 November 2026

One image that sums up the world's news of Sunday 22 November 2026, drawn
as a newspaper front page. Entry for the make.fun bounty
[news-image-20261122](https://make.fun/bounty/news-image-20261122).

Built with make.fun — referral code `8g8e3fkv`.

## The image

`entry.png` (1024×1024) is a front page: a masthead dated **Sunday 22
November 2026**, an original code-drawn illustration (night sky, Mercury and
the BepiColombo spacecraft on its orbit), and six stories with headlines and
short summaries, plus an "Also today" strip.

1. **Climate** — COP31 ends with no deal: the UN climate summit in Antalya,
   Turkey, collapsed on Sunday after nearly 200 nations failed to agree; the
   EU, Britain, Panama and climate-vulnerable states rejected a final draft
   that never mentioned fossil fuels.
2. **Gulf** — Iran strikes Bahrain site: Iranian projectiles hit a civilian
   industrial facility in Sitra, Bahrain, starting a fire and injuring two
   people; Iran also struck three tankers near the Strait of Hormuz.
3. **Ukraine** — Drone flattens flats near Kyiv: a Russian drone destroyed
   part of a five-storey apartment block in Dymer, north of Kyiv, overnight
   into Sunday; 2 killed, 4 wounded, 14 missing under the rubble.
4. **Libya** — Sea drones hit Russian warship: suspected Ukrainian sea drones
   struck the Russian corvette Merkury at Benghazi naval base, causing an
   explosion and a brief fire.
5. **Space** — BepiColombo reaches Mercury: after an eight-year journey, the
   ESA–JAXA probe slipped into orbit around Mercury, only the third
   spacecraft ever to visit the planet; a thruster burn ran short, but the
   spacecraft is safe.
6. **Disaster** — Factory fire in Indonesia: a fire tore through a candy
   factory in Cikande, Banten, killing three workers; 37 people are still
   unaccounted for.

Also today: a fire at a power station near Basra, Iraq, killed at least 4
and injured 35; Israeli settlers torched 12 vehicles in four West Bank
villages, and Israel opened an inquiry.

## How it works

- `draw.py` draws `entry.png` from scratch with Pillow (no external images,
  no network). Re-run it to regenerate the image.
- `main.py` (the entry point) only copies the repository's `entry.png` to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`), byte for byte, so the two
  grader runs produce identical output.

## Reproduce

```sh
python3 draw.py        # regenerate entry.png
python3 main.py        # writes /output/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
