import copy
import random
from enum import Enum
from typing import List, Generator


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
        row1 = "|".join([i.value for i in self._board[0]])
        row2 = "|".join([i.value for i in self._board[1]])
        row3 = "|".join([i.value for i in self._board[2]])
        return "\n".join([row1, row2, row3])

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
    def __init__(self, user_input_generator: Generator, ):
        """
        :param user_input_generator: Generates the user input - i.e. row, column pairs for where to put the tokens.
        """
        self._current_player = PlayerToken.X
        self._computer_player = PlayerToken.O
        self._user_input_generator = user_input_generator
        self._board = XOBoard.empty_board()

    def change_player(self):
        if self._current_player == PlayerToken.X:
            self._current_player = PlayerToken.O
            self._computer_player = PlayerToken.X
        else:
            self._current_player = PlayerToken.X
            self._computer_player = PlayerToken.O

    def current_player(self) -> PlayerToken:
        return self._current_player

    def get_winner(self) -> PlayerToken:
        if self._board.is_winning(X):
            return X
        elif self._board.is_winning(O):
            return O

    def play_game(self, n_moves: int):
        iterator = iter(self._user_input_generator)
        for i in range(n_moves):
            # Told for the user who is turn, collect a row and column from the user and try to put a play token there.
            print(f"Your turn")
            row, column = next(iterator)
            self._board.play_move(row, column, self._current_player)
            print(self._board)

            # The computer random choice
            print("The computer turn...")
            row, column = (random.randint(0, 2), random.randint(0, 2))
            self._board.play_move(row, column, self._computer_player)
            print(self._board)



def main():
    game = XOGame(iterate_user_input())
    game.play_game(100)
    if game.get_winner() is not None:
        print("Winner is:", game.get_winner().value)
    else:
        print("Draw")


if __name__ == '__main__':
    main()
