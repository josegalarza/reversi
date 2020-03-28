# Reversi

Python implementation of [Reversi](https://en.wikipedia.org/wiki/Reversi)

## How to play

Run the Python script:

```bash
python reversi.py
```

The initial board will be shown and the players will start playing in turns:

```
Reversi - By @josegalarza (2020)

  1 2 3 4 5 6 7 8
a . . . . . . . .
b . . . . . . . .
c . . . . . . . .
d . . . O X . . .
e . . . X O . . .
f . . . . . . . .
g . . . . . . . .
h . . . . . . . .

Player X, where will you play next? 
```

Let's say player `X` plays a valid move, for example `c4`:

```bash
Player X, where will you play next? c4
```

The boardgame will be updated with the player's move, and the other player will go next:

```
Reversi - By @josegalarza (2020)

  1 2 3 4 5 6 7 8
a . . . . . . . .
b . . . . . . . .
c . . . X . . . .
d . . . X X . . .
e . . . X O . . .
f . . . . . . . .
g . . . . . . . .
h . . . . . . . .

Player O, where will you play next?
```

For the actual rulese on how to play this game, visit the Wikipedia site.

## Releases

## v1.0

- Players take turn to play
- Handler for bad input
- Evaluates an input move is valid or not
- Game ends when the board is full
- Game ends if one player has "dominated", the other player is not longer in the board

## TODO

- Handle cases where the game ends before the grid is ccompletely filled
