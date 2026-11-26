# deadpan-forecast

[![make.fun · u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/nmlyz/deadpan-forecast/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/nmlyz/deadpan-forecast/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

A tiny program that writes a single deadpan weather forecast line to a
text file. The line is one sentence of at most 160 characters, a forecast
for an invented city, Hailmere, where pea-sized hail falls from 2 to 4
and the thawed peas are served at the village fete, as is tradition,
with mint. It is written to sound like a straight-faced broadcast line
for a place that does not exist.

## Run it

```sh
python3 main.py
```

It writes the forecast to `/output/entry.txt` (`OUTPUT_DIR` overrides
the directory). The program validates the line first — one line, between
1 and 160 characters — then writes it with a trailing newline and leaves
the file world-readable (mode 0644). Running it twice produces
byte-identical output.
