#!/usr/bin/env python
from itertools import cycle
import os
import sys


BLACK="⚫️ "
WHITE="⚪️ "
EMPTY="   "
BACK_GREEN = "\x1b[0;30;42m"  # style=0=normal, front=30=black, back=42=green
RESET_COLOR = "\x1b[0m"


class Board():
    def __init__(self):
        self.board = [[EMPTY for i in range(8)] for i in range(8)]
        self.board[3][4] = WHITE
        self.board[3][3] = BLACK
        self.board[4][3] = WHITE
        self.board[4][4] = BLACK

    def __str__(self):
        b = self.board
        return f"""     1   2   3   4   5   6   7   8
   {BACK_GREEN}┼───┼───┼───┼───┼───┼───┼───┼───┼{RESET_COLOR}
 A {BACK_GREEN}│{b[0][0]}│{b[0][1]}│{b[0][2]}│{b[0][3]}│{b[0][4]}│{b[0][5]}│{b[0][6]}│{b[0][7]}│{RESET_COLOR} A
   {BACK_GREEN}┼───┼───┼───┼───┼───┼───┼───┼───┼{RESET_COLOR}
 B {BACK_GREEN}│{b[1][0]}│{b[1][1]}│{b[1][2]}│{b[1][3]}│{b[1][4]}│{b[1][5]}│{b[1][6]}│{b[1][7]}│{RESET_COLOR} B
   {BACK_GREEN}┼───┼───┼───┼───┼───┼───┼───┼───┼{RESET_COLOR}
 C {BACK_GREEN}│{b[2][0]}│{b[2][1]}│{b[2][2]}│{b[2][3]}│{b[2][4]}│{b[2][5]}│{b[2][6]}│{b[2][7]}│{RESET_COLOR} C
   {BACK_GREEN}┼───┼───┼───┼───┼───┼───┼───┼───┼{RESET_COLOR}
 D {BACK_GREEN}│{b[3][0]}│{b[3][1]}│{b[3][2]}│{b[3][3]}│{b[3][4]}│{b[3][5]}│{b[3][6]}│{b[3][7]}│{RESET_COLOR} D
   {BACK_GREEN}┼───┼───┼───┼───┼───┼───┼───┼───┼{RESET_COLOR}
 E {BACK_GREEN}│{b[4][0]}│{b[4][1]}│{b[4][2]}│{b[4][3]}│{b[4][4]}│{b[4][5]}│{b[4][6]}│{b[4][7]}│{RESET_COLOR} E
   {BACK_GREEN}┼───┼───┼───┼───┼───┼───┼───┼───┼{RESET_COLOR}
 F {BACK_GREEN}│{b[5][0]}│{b[5][1]}│{b[5][2]}│{b[5][3]}│{b[5][4]}│{b[5][5]}│{b[5][6]}│{b[5][7]}│{RESET_COLOR} F
   {BACK_GREEN}┼───┼───┼───┼───┼───┼───┼───┼───┼{RESET_COLOR}
 G {BACK_GREEN}│{b[6][0]}│{b[6][1]}│{b[6][2]}│{b[6][3]}│{b[6][4]}│{b[6][5]}│{b[6][6]}│{b[6][7]}│{RESET_COLOR} G
   {BACK_GREEN}┼───┼───┼───┼───┼───┼───┼───┼───┼{RESET_COLOR}
 H {BACK_GREEN}│{b[7][0]}│{b[7][1]}│{b[7][2]}│{b[7][3]}│{b[7][4]}│{b[7][5]}│{b[7][6]}│{b[7][7]}│{RESET_COLOR} H
   {BACK_GREEN}┼───┼───┼───┼───┼───┼───┼───┼───┼{RESET_COLOR}
     1   2   3   4   5   6   7   8"""

    def has_dominated(self, player):
        """
        Returns False if the other player is still on the board
        """
        for y in range(8):
           for x in range(8):
               if self.board[x][y] != EMPTY and self.board[x][y] != player.color:
                   return False
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
        try:
            return True if self._get_valid_moves(player) else False
        except Exception as e:
            return False

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
        x, y = move
        if x not in range(8) or y not in range(8):
            return False  # Off the board
        elif self.board[x][y] != EMPTY:
            return False  # Position to move is not empty
        else:
            return True if self._get_flips(player, move) else False

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

    def get_player_score(self, player):
        score = 0
        for y in range(8):
           for x in range(8):
               if self.board[x][y] == player.color:
                   score += 1
        return score


class Player():
    def __init__(self, color):
        self.color = color

    def get_move(self):
        # Input move
        move = input( \
            f"Where will you play next, {self.color}? "
        ).strip().replace(" ", "").replace(",", "").replace("|", "")
        if len(move) != 2:
            raise RuntimeError  # Invalid move
        # Parse move
        x, y = move[0].upper(), move[1].upper()
        # fix move
        if x in "12345678" and y.upper() in "ABCDEFGH":
            x, y = y, x
            x, y = ord(x.upper())-65, int(y)-1
        elif x in "ABCDEFGH" and y in "12345678":
            x, y = ord(x.upper())-65, int(y)-1
        else:
            raise RuntimeError  # Invalid move - can't parse
        return x, y


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(BLACK), Player(WHITE)]

    def print(self):
        """
        Prints the game: the header, notification(s) (if any) and the board
        """
        os.system("clear")
        header = "Reversi • By @josegalarza (2020)"
        p0 = self.players[0]
        p1 = self.players[1]
        p0_score = f"{p0.color}{'%2d' % self.board.get_player_score(p0)}"
        p1_score = f"{p1.color}{'%2d' % self.board.get_player_score(p1)}"
        render = f"""{header}

Score: {p0_score} vs. {p1_score}

{self.board}
"""
        print(render)

    def play(self):
        for player in cycle(self.players):
            self.print()
            if self.board.is_full() \
                or self.board.has_dominated(player):
                break
            if self.board.has_valid_moves(player):
                while True:
                    try:
                        move = player.get_move()
                        self.board.put_stone(player, move)
                        break
                    except KeyboardInterrupt:
                        sys.exit(1)
                    except RuntimeError as e:
                        pass
                    except Exception as e:
                        pass
        self.print()


if __name__ == '__main__':
    game = Game()
    game.play()
