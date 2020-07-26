import copy
from enum import Enum
from typing import List, Generator


class PlayerToken(Enum):
    X = 'X'
    O = 'O'
    EMPTY = ' '


class XOBoard:
    EMPTY = PlayerToken.EMPTY

    def __init__(self, board: List[List[PlayerToken]]):
        self._board = copy.deepcopy(board)

    def __str__(self) -> str:
        """
        Prints the board in a human-readable way.
        """
        pass

    @staticmethod
    def empty_board():
        return XOBoard([[XOBoard.EMPTY] * 3 for i in range(3)])

    def play_move(self, row: int, column: int, player_token: PlayerToken):
        """
        Does nothing if the move is illegal
        """
        pass

    def is_winning(self, player_token: PlayerToken):
        """
        Returns true if the given player won the game.
        """
        pass

    def is_move_legal(self, row: int, column: int):
        """
        Returns true if the location of the given coordinates
        """
        pass


def iterate_user_input():
    """
    Gets row and column from the user.
    """
    while True:
        text = input("Please select a row and a column to play (comma separated. for example, 0, 2.")
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
        self._user_input_generator = user_input_generator
        self._board = XOBoard.empty_board()

    def change_player(self):
        """
        Changes the current player.
        """
        pass

    def current_player(self) -> PlayerToken:
        """
        Returns the token of the current player.
        """
        pass

    def get_winner(self) -> PlayerToken:
        """
        Returns the token of the winning player if any of the player won.
        Otherwise, returns None.
        """
        pass

    def play_game(self, n_moves: int):
        """
        Plays n_moves turns of the game.
        """
        # Hint: take input from the user using next(self._user_input_generator)
        pass


def main():
    game = XOGame(iterate_user_input())
    game.play_game(100)
    if game.get_winner() is not None:
        print("Winner is:", game.get_winner())
    else:
        print("Draw")


if __name__ == '__main__':
    main()
