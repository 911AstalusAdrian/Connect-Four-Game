import unittest
from Board.board import Board, BoardException
from Player.player import Player


class TestBoard(unittest.TestCase):
    def setUp(self):
        self._board = Board()

    def test_chip_moves(self):
        player_one = Player(1)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 5)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 4)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 3)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 2)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 1)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 0)
        self.assertRaises(BoardException, self._board.add_chip, player_one, 0)
        self.assertRaises(BoardException, self._board.add_chip, player_one, -1)

    def test_win_horizontal(self):
        """
        The winning chips are placed on a horizontal line
        |=========================================================|
        |winning_chip | winning_chip | winning_chip | winning_chip|
        |=========================================================|
        :return: -
        """
        player_one = Player(1)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 5)
        row_index = self._board.add_chip(player_one, 1)
        self.assertEqual(row_index, 5)
        row_index = self._board.add_chip(player_one, 2)
        self.assertEqual(row_index, 5)
        row_index = self._board.add_chip(player_one, 3)
        self.assertEqual(row_index, 5)
        self.assertTrue(self._board.check_player_win(player_one))

    def test_win_vertical(self):
        """
        The winning chips are placed on a horizontal line
         ____________
        |winning_chip|
        |------------|
        |winning_chip|
        |------------|
        |winning_chip|
        |------------|
        |winning_chip|
        |------------|
        :return: -
        """
        player_one = Player(1)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 5)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 4)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 3)
        row_index = self._board.add_chip(player_one, 0)
        self.assertEqual(row_index, 2)
        self.assertTrue(self._board.check_player_win(player_one))

    def test_win_main_diagonal(self):
        """
        The winning chips are placed on a 'main' diagonal
        ______________
        |winning_chip|
        |------------|------------|
        | other_chip |winning_chip|
        |------------|------------|------------|
        | other_chip | other_chip |winning_chip|
        |------------|------------|------------|------------|
        | other_chip | other_chip | other_chip |winning_chip|
        |---------------------------------------------------|
        :return: -
        """
        player_one = Player(1)
        player_two = Player(2)
        self._board.add_chip(player_two, 0)
        self._board.add_chip(player_two, 0)
        self._board.add_chip(player_two, 0)
        self._board.add_chip(player_one, 0)
        self._board.add_chip(player_two, 1)
        self._board.add_chip(player_two, 1)
        self._board.add_chip(player_one, 1)
        self._board.add_chip(player_two, 2)
        self._board.add_chip(player_one, 2)
        self._board.add_chip(player_one, 3)
        self.assertTrue(self._board.check_player_win(player_one))

    def test_win_secondary_diagonal(self):
        """
        The winning chips are placed on a 'secondary' diagonal
                                               ______________
                                               |winning_chip|
                                  |------------|------------|
                                  |winning_chip| other_chip |
                     |------------|------------|------------|
                     |winning_chip| other_chip | other_chip |
        |------------|------------|------------|------------|
        |winning_chip| other_chip | other_chip | other_chip |
        |---------------------------------------------------|
        :return:
        """
        player_one = Player(1)
        player_two = Player(2)
        self._board.add_chip(player_two, 3)
        self._board.add_chip(player_two, 3)
        self._board.add_chip(player_two, 3)
        self._board.add_chip(player_one, 3)
        self._board.add_chip(player_two, 2)
        self._board.add_chip(player_two, 2)
        self._board.add_chip(player_one, 2)
        self._board.add_chip(player_two, 1)
        self._board.add_chip(player_one, 1)
        self._board.add_chip(player_one, 0)
        self.assertTrue(self._board.check_player_win(player_one))

    def test_no_win(self):
        self.assertFalse(self._board.check_player_win(Player(2)))

    def test_board_full(self):
        player = Player(1)
        self.assertFalse(self._board.check_board_full())
        for column in range(7):
            for each_count in range(6):
                self._board.add_chip(player, column)
        self.assertTrue(self._board.check_board_full())
        self._board.clear()
        self.assertFalse(self._board.check_board_full())

    def test_ui_look(self):
        player = Player(1)
        self._board.add_chip(player, 0)
        display = "+---+---+---+---+---+---+---+\n" \
                  "| 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n" \
                  "+===+===+===+===+===+===+===+\n" \
                  "| 0 | 0 | 0 | 0 | 0 | 0 | 0 |\n" \
                  "+---+---+---+---+---+---+---+\n" \
                  "| 0 | 0 | 0 | 0 | 0 | 0 | 0 |\n" \
                  "+---+---+---+---+---+---+---+\n" \
                  "| 0 | 0 | 0 | 0 | 0 | 0 | 0 |\n" \
                  "+---+---+---+---+---+---+---+\n" \
                  "| 0 | 0 | 0 | 0 | 0 | 0 | 0 |\n" \
                  "+---+---+---+---+---+---+---+\n" \
                  "| 0 | 0 | 0 | 0 | 0 | 0 | 0 |\n" \
                  "+---+---+---+---+---+---+---+\n" \
                  "| 1 | 0 | 0 | 0 | 0 | 0 | 0 |\n" \
                  "+---+---+---+---+---+---+---+" \

        board = str(self._board)
        self.assertEqual(board, display)
