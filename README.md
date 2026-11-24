# One Word, One Username, One Reward

[![Bounty](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/cervus-snoopy/sleepy-username-fern-6k2p/rank.svg)](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/cervus-snoopy/sleepy-username-fern-6k2p/reward.svg)](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

A tiny Python program that writes the account owner's own make.fun handle — exactly one word, no spaces, no explanation — to `entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

The program writes `entry.txt` (UTF-8 text, 1–30 characters, no trailing newline) into `MAKEFUN_OUTPUT_DIR` (default `/output`), using only the Python standard library and no network access.

## How it works

`main.py` builds the handle from its two name parts joined by a hyphen, validates that it is a single word of 1–30 characters, writes it with no trailing newline, sets mode `0644`, then reads the file back and verifies the bytes and mode match before exiting.

