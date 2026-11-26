# deadpan-forecasts-20261126

[![make.fun · u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/AndryXSad/deadpan-forecasts-20261126/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/AndryXSad/deadpan-forecasts-20261126/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

One line, at most 160 characters: a deadpan weather forecast for a city
that does not exist. A judge model briefed as a dry TV meteorologist
compares the lines two at a time and keeps the funnier, more vivid one.

> Tomorrow in Port Meridian, expect a high of 21, light winds, and one (1) cloud, which the city has officially named Gerald.

The line was chosen by a local pairwise tournament over 14 fresh
candidates, scored on the judge brief's five criteria in order: a
one-line forecast for a city that does not exist; a joke that lands on
first read with a deadpan twist; a concrete image or number that makes
the invented place feel real; a believable broadcast tone; tight use of
its characters. It won the head-to-head among the top three. See
`CANDIDATES.md` for the full table.

## Run it

```sh
python3 main.py
```

Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
Deterministic: every run writes byte-identical output (123 characters,
standard library only).
