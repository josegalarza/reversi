#!/usr/bin/env python
from itertools import cycle
import os
import sys


WHITE="X"
BLACK="O"
EMPTY="."


class Board():
    def __init__(self):
        self.board = [[EMPTY for i in range(8)] for i in range(8)]
        self.board[3][4] = WHITE
        self.board[3][3] = BLACK
        self.board[4][3] = WHITE
        self.board[4][4] = BLACK

    def __str__(self):
        # return '\n'.join([' '.join(line) for line in self.board])  # TODO fix, it outputs YX, instead of XY
        result = "y"
        for y in range(8, 0, -1):
            # print y axis
            result += f"\n{y} "
            #print stone
            for x in range(8):
                result += f"{self.board[x][y-1]} "
        result += "\n"
        # print x axis
        for x in range(8+1):
            result += f"{x} "
        result += " x"
        return result

    def has_dominated(self, player):
        """
        Returns False if the other player is still on the board
        """
        for y in range(8):
           for x in range(8):
               if self.board[x][y] != EMPTY and self.board[x][y] != player.color:
                   return False
        print("Dominated!")
        input()
        return True

    def is_full(self):
        """
        Returns True/False if the board is/isn't full.
        """
        for y in range(8):
           for x in range(8):
               if self.board[x][y] == EMPTY:
                   return False
        return True

    def has_valid_moves(self, player):
        return True if self._get_valid_moves(player) else False

    def _get_valid_moves(self, player):
        valid_moves = []
        for y in range(8):
            for x in range(8):
                move = x, y
                if self.is_valid_move(player, move):
                    valid_moves.append(move)
        return valid_moves

    def is_valid_move(self, player, move):
        """
        Returns True/False if the player can/cannot play the move.
        """
        try:
            result = False
            x, y = move
            if x not in range(8) or y not in range(8):
               result = False  # Off the board
            if self.board[x][y] != EMPTY:
                result = False  # Position to momve is not empty
            result = True if self._get_flips(player, move) else False
        except:
            pass
        finally:
            return result

    def _get_flips(self, player, move):
        """
        Return a list of tuples that represents stones (x,y positions) to flip.
        """
        flips = []
        flips += self._get_flips_in_direction(player, move, direction=( 0,  1))  # up
        flips += self._get_flips_in_direction(player, move, direction=( 0, -1))  # down
        flips += self._get_flips_in_direction(player, move, direction=( 1,  0))  # right
        flips += self._get_flips_in_direction(player, move, direction=(-1,  0))  # left
        flips += self._get_flips_in_direction(player, move, direction=( 1,  1))  # up-right
        flips += self._get_flips_in_direction(player, move, direction=(-1,  1))  # up-left
        flips += self._get_flips_in_direction(player, move, direction=( 1, -1))  # down-right
        flips += self._get_flips_in_direction(player, move, direction=(-1, -1))  # down-left
        return flips

    def _get_flips_in_direction(self, player, move, direction):
        flips = []
        x, y = move
        xd, yd = direction
        line = self._get_line_in_direction(move, direction)
        rest_of_line = line[1:]  # line[0] would be where the player just put their stone
        flips_count = self._get_flip_count(player, rest_of_line)
        for i in range(flips_count):
            next_position = x + xd*(i+1), y + yd*(i+1)
            flips.append(next_position)
        return flips

    def _get_line_in_direction(self, position, direction):
        """
        Returns a list (line) of stones in a direction.
        """
        xp, yp = position
        if xp not in range(8) or yp not in range(8):
            return []
        else:
            xd, yd = direction
            next_position = xp + xd, yp + yd
            return [self.board[xp][yp]] + self._get_line_in_direction(next_position, direction)

    def _get_flip_count(self, player, rest_of_line):
        if player.color not in rest_of_line:
            # X, [O, O, O]
            # X, []
            return 0
        if not rest_of_line:
            # X, []
            return 0
        if player.color == rest_of_line[0]:
            # X, [X, ...]
            return 0
        if rest_of_line[0] == EMPTY:
            return 0
        # X, [O, ..., X]
        return 1 + self._get_flip_count(player, rest_of_line[1:])

    def put_stone(self, player, move):
        """
        Checks if the move is valid, and if so, puts the stone and flip others.
        """
        if not self.is_valid_move(player, move):
            raise RuntimeError("Invalid move")
        x, y = move
        self.board[x][y] = player.color
        for xi, yi in self._get_flips(player, move):
            self.board[xi][yi] = player.color


class Player():
    def __init__(self, color):
        self.color = color

    def get_move(self):
        return tuple([int(z)-1 for z in input(f"Player {self.color}, where to play? (x,y) ").strip().replace(' ', '').split(',')])


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(WHITE), Player(BLACK)]
        self.notification = ""

    def print(self):
        """
        Prints the game: the header, notification(s) (if any) and the board
        """
        os.system("clear")
        print(f"""Reversi - By @josegalarza (2020)
{self.notification if self.notification else ''}
{self.board}
""")
        if self.notification:
            self.notification = ""

    def play(self):
        for player in cycle(self.players):
            self.print()

            if self.board.is_full() or self.board.has_dominated(player):
                break  # game over TODO: get counts

            if self.board.has_valid_moves(player):
                try:
                    move = player.get_move()
                    self.board.put_stone(player, move)
                except KeyboardInterrupt:
                    sys.exit(1)
                except RuntimeError as e:
                    self.notification = f"{e}"
                    pass
                except Exception as e:
                    self.notification = f"Invalid move"


if __name__ == '__main__':
    game = Game()
    game.play()
