# X Flags Game - Theory and Strategy
**Author**: Dimitrios Petridis

---

## Introduction

The X Flags game is a simple mathematical strategy game where two players take turns picking up flags from a pile. The game's objective is to be the one to pick up the last flag. Players must strategize and anticipate their opponent's moves to win. This document outlines the underlying theory and the optimal strategy for the game.

---

## Basic Rules

1. There is a pile of `n` flags to start with.
2. Players alternate turns, picking up at least 1 flag and at most `m` flags in a single turn.
3. The player who picks up the last flag wins.

---

## Optimal Strategy

The optimal strategy is based on the mathematical properties of the game and can be described in terms of modular arithmetic.

### The Winning Position

If the number of flags left at the start of a player's turn is congruent to 0 modulo (`m + 1`), i.e.,

\[ n \equiv 0 \ (\text{mod} \ m + 1) \]

then the player is in a winning position. Conversely, if

\[ n \not\equiv 0 \ (\text{mod} \ m + 1) \]

the player is in a losing position.

### Player Strategy

1. **Winning Position**: If a player is in a winning position (the remainder of `n` divided by `m + 1` is not zero), they should always pick flags such that the remaining flags are a multiple of `m + 1`. This forces the opponent into a losing position.

2. **Losing Position**: If a player finds themselves in a losing position, there isn't a deterministic optimal strategy. In our game simulation, a player in a losing position picks a random number of flags between 1 and `m` (unless there are fewer than `m` flags remaining).

---

## Conclusion

The X Flags game, while simple in concept, has underlying mathematical properties that dictate an optimal strategy. Recognizing these properties is crucial for a player aiming to win consistently. In the case where a player is in a losing position, the randomness of their choices can add unpredictability to the game, making it more engaging for both players.
