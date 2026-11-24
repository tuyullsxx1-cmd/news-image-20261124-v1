# One Day of World News — Tuesday 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/tuyullsxx1-cmd/news-image-20261124-v1/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/tuyullsxx1-cmd/news-image-20261124-v1/reward.svg)](https://make.fun/bounty/news-image-20261124)

A single front page that sums up Tuesday 24 November 2026: 33 verified
stories from 6 regions, drawn as a flat-vector newspaper in the style of
the 22 November final winner. The three biggest stories lead — Russia
firing 96 drones at Ukraine overnight (73 downed by 08:00), Libya
demanding answers over the sunken Russian warship Merkury as the UN
mission seeks an independent probe, and Asia's chip stocks soaring on
Jensen Huang's return to Nvidia — followed by ten secondary cards, a
day-in-UTC timeline on a dark navy band, the day in six big red numbers,
a dotted world map with numbered pins, a twenty-story "also on Tuesday"
list, a six-panel "day in pictures" strip, and a red DATE CHECK box
naming the stories left out because they happened on another day (the
COP31 collapse, the Merkury sinking itself, 15 killed at Dymer, Huang's
reinstatement, the Jabalia strike). Every story carries a certainty tag
(CONFIRMED, REPORTED or CLAIM), so nothing is shown as fact that was
only claimed.

## How the program works

`main.py` (Python 3.13 standard library only) copies the pre-rendered
`entry.png` (1024×1024, 192,755 bytes) to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR/entry.png`), after checking the PNG magic bytes
and the 1 MiB size cap. The image was rendered deterministically offline
with Pillow; the program itself needs no network, no third-party
libraries and no fonts, and produces byte-identical output on every run.
