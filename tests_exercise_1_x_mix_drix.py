    def test_the_computer_put_tokens1(self):
        game = XOGame([(0, 0), (0, 1), (1, 0), (2, 2), (2, 1), (1, 2)], True)

        for i in range(6):
            game.play_game(1)
            game.change_player()

        game.change_player()
        for i in range(3):
            game.play_game(1)
            game.change_player()

        assert game.get_winner() == O

    def test_the_computer_put_tokens2(self):
        game = XOGame([(0, 0), (0, 1), (1, 0), (2, 2), (2, 1), (1, 2)], True)

        for i in range(7):
            game.change_player()
            game.play_game(1)

        assert game.get_winner() == O
