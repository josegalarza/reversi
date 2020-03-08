#!/usr/bin/env python

import os
import sys


EMPTY = "-"
BLACK = "◎"
WHITE = "◉"


class Board():

  def __init__(self, map_file='boards/square.txt'):
    self.board = self.load_map(map_file)

  def load_map(self, map_file):
    with open(map_file) as f:
      lines = [line[:-1] for line in f.readlines()]
      return [[cell for cell in line] for line in lines]

  def render(self):
    return '\n'.join([' '.join(line) for line in self.board])

  def count_stones(self, color):
    score = 0
    for line in self.board:
      score += len([x for x in line if x == color])
    return score

  def position(self, position):
    #return self.board[position]
    x, y = position
    return self.board[y][x]

  def put_stone(self, position, color):
    #self.board[position] = color
    x, y = position
    self.board[y][x] = color
    # TODO: reverse other stones

  def can_put_stone(self, position, color):
    x, y = position
    try:
      if self.board[y][x] != EMPTY:
        return False
      else:
        # TODO: check if player can actually put a stone in this position
        return True
    except IndexError:
      return False


class Reversi:

  def __init__(self):
    self.board = Board()
    self._current_player = BLACK

  def play(self):
    while True:
      player = self._current_player
      self.render()
      if self.board.count_stones(EMPTY) == 0:
        self.game_over()
      while True:
        position = self._input_move()
        if self.board.can_put_stone(position, player):
          self.board.put_stone(position, player)
          self._next_player()
          break

  def _next_player(self):
    # TODO: check if other player can actually play
    self._current_player = BLACK if self._current_player == WHITE else WHITE

  def render(self):
    score_white = self.board.count_stones(WHITE)
    score_black = self.board.count_stones(BLACK)
    render = f"""Reversi - by @josegalarza 2019
Playing: {self._current_player} | Score: {WHITE} = {score_black} vs {BLACK} = {score_black}
{self.board.render()}"""
    os.system('clear')
    print(render)

  def _input_move(self):
    while True:
      move = input(f'Enter move (x,y) (:q to quit) > ')
      if move == ':q':
        sys.exit(0)
      else:
        x,y = tuple(move.replace(' ', '').split(','))
        try:
          if int(x.strip()) in range(8) and int(y.strip()) in range(8):
            return int(x), int(y)
        except:
          continue
    # TODO get line(s) from movement. and try flip

  def game_over(self):
    print(f"Game over.")
    sys.exit(0)

  def _flip(line):
    # Returns a new line flipped (or not) and a `did_flip` indicator True/False
    did_flip = False
    new_line = line[:]

    try:
      player = line[0]
      rest_of_line = line[1:]
    except IndexError:
      return False, new_line

    count_flip = _get_flip_count(player, rest_of_line)

    if count_flip:
      did_flip = True
      for i in range(count_flip):
        new_line[i+1] = player

    return new_line

  def _get_flip_count(player, rest_of_line):
    # 1, [] -> Error
    if not rest_of_line:
      return 0

    try:
      # 1, [111] -> 0
      if rest_of_line[0] == player:
        return 0

      # 1, [01] -> 1
      # 1, [001] -> 2
      if rest_of_line[0] != player and rest_of_line[1] == player:
        return 1
    except IndexError:
      # 1, [1] -> 0
      return 0

    # 1, [0001] -> 3
    # 1, [0000] -> 0
    if rest_of_line[0] != player:
      return 1 + get_flip_count(player, rest_of_line[1:])


if __name__ == '__main__':
  game = Reversi()
  game.play()
