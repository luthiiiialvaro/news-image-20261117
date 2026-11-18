# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/luthiiiialvaro/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/luthiiiialvaro/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image that sums up the world's news of Tuesday 17 November 2026: a
newspaper front page, drawn as a single 1024×1024 PNG. The masthead names
the day, the lead story is the strike on the Kerch Bridge, and five more
stories plus a ticker cover the rest of the day across regions and fields.

## The stories in the image

- **Lead — Ukraine:** Ukraine struck the Kerch Bridge linking Crimea to
  Russia for a second straight day; verified footage showed a road section
  collapsed into the water, and Russia hit bridges in Kyiv in reply.
- **Asia-Pacific — Trump in Manila:** the US president met Quad leaders
  in Manila; a three-way summit with Xi Jinping and Vladimir Putin is set
  for Shenzhen on Thursday.
- **Japan:** Tokyo scrambled fighter jets after two suspected Russian
  aircraft entered its airspace early on Tuesday.
- **Middle East — Gaza:** Britain, Australia, Canada and Italy urged
  Israel to open crossings for aid; the UN warned of a winter emergency,
  with 1.7 million people displaced and 1.4 million facing acute hunger.
- **Europe:** five EU states (Austria, Denmark, Germany, Greece and the
  Netherlands) plan a Rwanda return hub for rejected asylum seekers.
- **Also today:** COP31 climate talks enter their decisive phase in
  Antalya; Mongolia's president resigns amid a corruption scandal; the US
  loses its measles elimination status; a US judge blocks limits on
  foreign students' stays.

## How the image was made

The four illustrations (bridge, summit hall, jets, aid convoy) were
generated as flat editorial art with no text in them, and the front page
— masthead, headlines, summaries and ticker — was composed over them in
crisp type, so every word a viewer reads is rendered exactly, with no
garbled text. The finished `entry.png` is 1024×1024 and under 1 MiB.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) checks that `entry.png`
is a whole PNG within the 1024×1024 and 1 MiB limits, then copies it to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`). It needs no network, so
both runs write the same bytes — verified locally: two runs produced
identical sha256 hashes.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
