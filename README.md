# Reversi

Python implementation of [Reversi](https://en.wikipedia.org/wiki/Reversi)

## How to play

Run the Python script:

```bash
python reversi.py
```

The initial board will be shown and the players will start playing in turns:

```
Reversi • By @josegalarza (2020)

Score: ⚫️  2 vs. ⚪️  2

    1  2  3  4  5  6  7  8
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 A │  │  │  │  │  │  │  │  │ A
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 B │  │  │  │  │  │  │  │  │ B
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 C │  │  │  │  │  │  │  │  │ C
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 D │  │  │  │⚫️│⚪️│  │  │  │ D
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 E │  │  │  │⚪️│⚫️│  │  │  │ E
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 F │  │  │  │  │  │  │  │  │ F
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 G │  │  │  │  │  │  │  │  │ G
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 H │  │  │  │  │  │  │  │  │ H
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
    1  2  3  4  5  6  7  8

Where will you play next, ⚫️ ?
```

Let's say player `⚫️` plays a valid move, for example `F4`:

```bash
Where will you play next, ⚫️ ? F4
```

The boardgame will be updated with the player's move, and the other player will go next:

```
Reversi • By @josegalarza (2020)

Score: ⚫️  4 vs. ⚪️  1

    1  2  3  4  5  6  7  8
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 A │  │  │  │  │  │  │  │  │ A
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 B │  │  │  │  │  │  │  │  │ B
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 C │  │  │  │  │  │  │  │  │ C
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 D │  │  │  │⚫️│⚪️│  │  │  │ D
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 E │  │  │  │⚫️│⚫️│  │  │  │ E
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 F │  │  │  │⚫️│  │  │  │  │ F
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 G │  │  │  │  │  │  │  │  │ G
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
 H │  │  │  │  │  │  │  │  │ H
   ┼──┼──┼──┼──┼──┼──┼──┼──┼
    1  2  3  4  5  6  7  8

Where will you play next, ⚪️ ?
```

For the actual rulese on how to play this game, visit the Wikipedia site.

## Releases

## v1.0

- Players take turn to play
- Handler for bad input
- Evaluates an input move is valid or not
- Game ends when the board is full
- Game ends if one player has "dominated", the other player is not longer in the board

## v1.1

- Better UI - colored board, emojis and score count
- Fix bug of invalid input moves

## TODO

- Handle cases where the game ends before the grid is completely filled
- Python2 compatible
