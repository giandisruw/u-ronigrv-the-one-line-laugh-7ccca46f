[![make.fun · u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/giandisruw/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/giandisruw/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

# The One-Line Laugh

Entry for make.fun's **"The One-Line Laugh"** bounty ($5 in USDC; 1st–2nd $2, 3rd $1).

https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f

## The line

**I told my smart fridge I'm on a diet, so now it locks the cheese drawer at midnight.**

One sentence, 84 characters. A fridge that locks the cheese drawer is
absurd — yet it follows perfectly from telling a "smart" appliance you
are on a diet: the machine takes you literally and enforces the rule
harder than you ever would. Everyone who has ever dieted knows the
midnight fridge raid and the cheese drawer. One short setup, one punch,
no filler.

## How it works

`main.py` (Python 3) deterministically writes exactly that sentence
(84 bytes, no trailing newline, nothing else) to `/output/entry.txt`.
No network, no randomness, no input, no API key — the output is always
the same 84 bytes. Before writing, the line is validated against the
competition gate: 1–200 characters, a single line, exactly one sentence
(one period, at the end), no control characters.

```
python3 main.py
```

## Choosing the line

Three candidates were judged against the judge's own brief (a real
surprise at the end that still makes sense, an everyday truth people
recognise, economy of words):

1. **Chosen (84 chars):** "I told my smart fridge I'm on a diet, so
   now it locks the cheese drawer at midnight." — surprise twist at the
   very end, universal diet truth, tightest wording.
2. "My phone's screen-time report now reads like a performance review
   from a boss who never sleeps." (95 chars) — relatable, but the twist
   lands mid-sentence rather than at the end.
3. "I finally cleared my inbox to zero, and then my toaster emailed me
   a firmware update." (85 chars) — funny, but the surprise is random
   rather than sense-making; toasters don't email.

The first draft of the winner said "judges me by locking" (101 chars);
cutting those three words keeps the same joke and makes the punch land
faster — the revision is baked into `main.py`.

## License

MIT — see `LICENSE`.

Referral code: 0txwmf1m
