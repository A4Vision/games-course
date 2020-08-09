import copy
from enum import Enum
from typing import List, Generator
from random import randint


class PlayerToken(Enum):
    X = 'X'
    O = 'O'
    EMPTY = ' '


X = PlayerToken.X
O = PlayerToken.O


class XOBoard:
    EMPTY = PlayerToken.EMPTY

    def __init__(self, board: List[List[PlayerToken]]):
        self._board = copy.deepcopy(board)

    def __str__(self) -> str:
        board = ["|".join([i.value for i in row]) for row in self._board]
        return "\n".join(board)

    @staticmethod
    def empty_board():
        return XOBoard([[XOBoard.EMPTY] * 3 for i in range(3)])

    def play_move(self, row: int, column: int, player_token: PlayerToken):
        if self.is_move_legal(row, column):
            self._board[row][column] = player_token

    def is_winning(self, player_token: PlayerToken):
        win_lst = [player_token] * 3
        for row in self._board:
            if row == win_lst:
                return True

        for i in range(3):
            column = [row[i] for row in self._board]
            if column == win_lst:
                return True

        diagonal1 = [self._board[i][i] for i in range(3)]
        diagonal2 = [self._board[2 - i][i] for i in range(3)]
        if diagonal1 == win_lst or diagonal2 == win_lst:
            return True
        return False

    def is_move_legal(self, row: int, column: int):
        return 0 <= row < 3 and 0 <= column < 3 and self._board[row][column] == PlayerToken.EMPTY


def iterate_user_input():
    """
    Gets row and column from the user.
    """
    while True:
        text = input("Please select a row and a column to play (comma separated. for example, 0, 2). ")
        try:
            row, column = [int(coordinate) for coordinate in text.split(",")]
            yield row, column
        except Exception:
            print(f"Bad input: {text}")


class XOGame:
    def __init__(self, user_input_generator: Generator, vs_comp=False):
        """
        :param user_input_generator: Generates the user input - i.e. row, column pairs for where to put the tokens.
        """
        self._current_player = PlayerToken.X
        self._user_input_generator = user_input_generator
        self._board = XOBoard.empty_board()
        self._play_vs_comp = vs_comp

    def change_player(self):
        if self._current_player == PlayerToken.X:
            self._current_player = PlayerToken.O
        else:
            self._current_player = PlayerToken.X

    def current_player(self) -> PlayerToken:
        return self._current_player

    def get_winner(self) -> PlayerToken:
        for i in [X, O]:
            if self._board.is_winning(i):
                return i

    def play_game(self, n_moves: int):
        iterator = iter(self._user_input_generator)
        if not self._play_vs_comp:
            for i in range(n_moves):
                # Told for the user who is turn, collect a row and column from
                # the user and try to put a play token there.

                print(f"Now it's the turn of the player is play with {self._current_player.value}")
                while True:
                    row, column = next(iterator)

                    if self._board.is_move_legal(row, column):
                        self._board.play_move(row, column, self._current_player)

                        print(self._board)
                        break
                # Check if the current player in won.
                if self._board.is_winning(self._current_player) or " " not in str(self._board):
                    break
                self.change_player()
        else:
            i = 0
            while i < n_moves:
                # Told for the user who is turn, collect a row and column from the user and try to put a play token there.
                print("Your turn")
                while True:
                    row, column = next(iterator)
                    if self._board.is_move_legal(row, column):
                        self._board.play_move(row, column, self._current_player)
                        i += 1

                        print(self._board)
                        break

                if self._board.is_winning(self._current_player) or " " not in str(self._board):
                    break
                self.change_player()

                if not i < n_moves:
                    return
                ############################################################
                print("Now it's the computer turn...")
                row, column = (randint(0, 2), randint(0, 2))
                while not self._board.is_move_legal(row, column):
                    row, column = (randint(0, 2), randint(0, 2))

                self._board.play_move(row, column, self._current_player)
                i += 1
                print(self._board)

                if self._board.is_winning(self._current_player) or " " not in str(self._board):
                    break
                self.change_player()


def main():
    game = XOGame(iterate_user_input(), True)
    game.play_game(9)
    if game.get_winner() is not None:
        print("Winner is:", game.get_winner().value)
    else:
        print("Draw")


if __name__ == '__main__':
    main()
