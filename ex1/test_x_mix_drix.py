import unittest

from exercise_1_x_mix_drix import XOBoard, PlayerToken, XOGame

X = PlayerToken.X
O = PlayerToken.O


class TestXOBoard(unittest.TestCase):
    def test_check_win_row(self):
        board = XOBoard([[XOBoard.EMPTY] * 3, [X, X, X], [XOBoard.EMPTY] * 3, ])
        assert board.is_winning(X)

    def test_check_win_column(self):
        board = XOBoard([
            [XOBoard.EMPTY, XOBoard.EMPTY, X],
            [XOBoard.EMPTY, XOBoard.EMPTY, X],
            [XOBoard.EMPTY, XOBoard.EMPTY, X],
        ])
        assert board.is_winning(X)

    def test_check_win_diagonal1(self):
        board = XOBoard([[X, PlayerToken.EMPTY, O], [PlayerToken.EMPTY, X, PlayerToken.EMPTY], [O, PlayerToken.EMPTY, X]])
        assert board.is_winning(X)
        board = XOBoard([[X, PlayerToken.EMPTY, O], [PlayerToken.EMPTY, X, PlayerToken.EMPTY], [O, PlayerToken.EMPTY, O]])
        assert not board.is_winning(X)

    def test_check_win_diagonal2(self):
        board = XOBoard(
            [[XOBoard.EMPTY, XOBoard.EMPTY, X], [XOBoard.EMPTY, X, XOBoard.EMPTY], [X, XOBoard.EMPTY, XOBoard.EMPTY], ])
        assert board.is_winning(X)

    def test_check_not_win(self):
        board = XOBoard([[X, X, XOBoard.EMPTY], [XOBoard.EMPTY, X, X], [X, XOBoard.EMPTY, XOBoard.EMPTY], ])
        assert not board.is_winning(X)

    def test_print_board1(self):
        board = XOBoard([
            [X, X, X],
            [O, O, O],
            [XOBoard.EMPTY, XOBoard.EMPTY, XOBoard.EMPTY],
        ])
        assert 'X|X|X' in str(board)  # Calls board.__str__()
        assert 'O|O|O' in str(board)

    def test_print_board2(self):
        board = XOBoard([[X, PlayerToken.EMPTY, O],
                         [PlayerToken.EMPTY, O, X],
                         [O, O, X]
                         ])
        assert str(board).count("X") == 3
        assert str(board).count("O") == 4
        assert str(board)[1] == str(board)[3] == str(board)[7] == str(board)[9] == str(board)[13] == str(board)[15]
        assert str(board)[5] == str(board)[5] == str(board)[11]

    def test_illegal_moves_are_ignored(self):
        board = XOBoard([
            [X, X, O],
            [XOBoard.EMPTY, XOBoard.EMPTY, XOBoard.EMPTY],
            [XOBoard.EMPTY, XOBoard.EMPTY, XOBoard.EMPTY],
        ])
        assert not board.is_move_legal(0, 2)
        board.play_move(0, 2, X)
        assert not board.is_winning(X)

    def test_out_of_bound_is_illegal_move(self):
        board = XOBoard.empty_board()
        assert board.is_move_legal(0, 0)
        assert board.is_move_legal(2, 2)
        assert not board.is_move_legal(-1, 0)
        assert not board.is_move_legal(3, 0)
        assert not board.is_move_legal(0, 3)

    def test_changing_value_only_one_value_change(self):
        board = XOBoard.empty_board()

        board.play_move(0, 0, X)
        assert board.is_move_legal(1, 0)


class TestGame(unittest.TestCase):
    def test_change_player(self):
        game = XOGame([(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)])
        assert game.current_player() == X
        game.change_player()
        assert game.current_player() == O
        game.change_player()
        assert game.current_player() == X

    def test_play_game_X_wins(self):
        game = XOGame([(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)])
        game.play_game(5)
        assert game.get_winner() == X

    def test_play_game_O_wins(self):
        game = XOGame([(0, 0), (1, 0), (0, 1), (1, 1), (2, 2), (2, 0)])
        game.play_game(6)
        assert game.get_winner() == O
