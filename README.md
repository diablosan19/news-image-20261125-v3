# news-image-20261125-v3

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/diablosan19/news-image-20261125-v3/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/diablosan19/news-image-20261125-v3/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper front page summing up the world's news of
**Wednesday, 25 November 2026** — 34 stories, 10 regions, 16 fields, all
first reported that day. Lead: Ukraine hits five Russian jets at
Savasleyka airbase and two refineries in Samara. A red-outlined DATE CHECK
box names the big stories first reported before 25 November (COP31
collapse, Huawei verdict, Sinner surgery, the Riyadh tower strike and
more) and holds them back from the headlines, so the page never dresses a
prior-day story as today's news. Drawn art only — no photographs.

## Run it

```sh
python3 build.py            # re-render entry.png (1024x1024, < 1 MiB)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # copy it to out/entry.png
```

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). Both runs
write identical bytes.

## Sources

Reuters, Al Jazeera, AP, DW. Times are first-wire UTC, approximate.
