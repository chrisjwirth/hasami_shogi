import unittest
from hasami_shogi_game import HasamiShogiGame


class MyTestCase(unittest.TestCase):

    # --- TEST GAME INFORMATION ---

    def test_get_active_player(self):
        test_game = HasamiShogiGame()
        active_player_turn_one = test_game.get_active_player()
        self.assertEqual("BLACK", active_player_turn_one)
        test_game.make_move("i1", "h1")
        active_player_turn_two = test_game.get_active_player()
        self.assertEqual("RED", active_player_turn_two)
        test_game.make_move("a1", "b1")
        active_player_turn_three = test_game.get_active_player()
        self.assertEqual("BLACK", active_player_turn_three)
        test_game.make_move("b1", "c1")
        active_player_after_red_player_moved_twice = test_game.get_active_player()
        self.assertEqual("BLACK", active_player_after_red_player_moved_twice)

    def test_get_square_occupant(self):
        test_game = HasamiShogiGame()
        empty_square_occupant = test_game.get_square_occupant("e5")
        self.assertEqual("NONE", empty_square_occupant)
        black_square_occupant = test_game.get_square_occupant("i5")
        self.assertEqual("BLACK", black_square_occupant)
        red_square_occupant = test_game.get_square_occupant("a5")
        self.assertEqual("RED", red_square_occupant)

    def test_game_state_unfinished(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "b1")
        test_game.make_move("a2", "b2")
        test_game.make_move("i3", "b3")
        game_state = test_game.get_game_state()
        self.assertEqual("UNFINISHED", game_state)

    def test_game_state_black_won(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "b1")
        test_game.make_move("a2", "b2")
        test_game.make_move("i2", "h2")
        test_game.make_move("a3", "b3")
        test_game.make_move("i3", "h3")
        test_game.make_move("a4", "b4")
        test_game.make_move("i4", "h4")
        test_game.make_move("a5", "b5")
        test_game.make_move("i5", "h5")
        test_game.make_move("a6", "b6")
        test_game.make_move("i6", "h6")
        test_game.make_move("a7", "b7")
        test_game.make_move("i7", "h7")
        test_game.make_move("a8", "b8")
        test_game.make_move("i9", "b9")
        test_game.make_move("a1", "a2")
        test_game.make_move("b1", "a1")
        test_game.make_move("a9", "a3")
        test_game.make_move("h4", "a4")
        game_state = test_game.get_game_state()
        self.assertEqual("BLACK_WON", game_state)

    def test_game_state_red_won(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i2", "h2")
        test_game.make_move("a1", "h1")
        test_game.make_move("i3", "h3")
        test_game.make_move("a2", "b2")
        test_game.make_move("i4", "h4")
        test_game.make_move("a3", "b3")
        test_game.make_move("i5", "h5")
        test_game.make_move("a4", "b4")
        test_game.make_move("i6", "h6")
        test_game.make_move("a5", "b5")
        test_game.make_move("i7", "h7")
        test_game.make_move("a6", "b6")
        test_game.make_move("i8", "h8")
        test_game.make_move("a9", "h9")
        test_game.make_move("i1", "i2")
        test_game.make_move("h1", "i1")
        test_game.make_move("i9", "i3")
        test_game.make_move("b4", "i4")
        game_state = test_game.get_game_state()
        self.assertEqual("RED_WON", game_state)

    # --- TEST INVALID MOVES ---

    def test_same_player_moving_twice(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "h1")
        move = test_game.make_move("h1", "g1")
        self.assertEqual(False, move)

    def test_moving_to_occupied_square(self):
        test_game = HasamiShogiGame()
        move = test_game.make_move("i1", "a1")
        self.assertEqual(False, move)

    def test_moving_to_same_square(self):
        test_game = HasamiShogiGame()
        move = test_game.make_move("i1", "i1")
        self.assertEqual(False, move)

    def test_moving_both_horizontally_and_vertically(self):
        test_game = HasamiShogiGame()
        move = test_game.make_move("i1", "h2")
        self.assertEqual(False, move)

    def test_jump_move(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "b1")
        move = test_game.make_move("a1", "c1")
        self.assertEqual(False, move)

    def test_move_after_game_over(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "b1")
        test_game.make_move("a2", "b2")
        test_game.make_move("i2", "h2")
        test_game.make_move("a3", "b3")
        test_game.make_move("i3", "h3")
        test_game.make_move("a4", "b4")
        test_game.make_move("i4", "h4")
        test_game.make_move("a5", "b5")
        test_game.make_move("i5", "h5")
        test_game.make_move("a6", "b6")
        test_game.make_move("i6", "h6")
        test_game.make_move("a7", "b7")
        test_game.make_move("i7", "h7")
        test_game.make_move("a8", "b8")
        test_game.make_move("i9", "b9")
        test_game.make_move("a1", "a2")
        test_game.make_move("b1", "a1")
        test_game.make_move("a9", "a3")
        test_game.make_move("h4", "a4")
        move_after_game_over = test_game.make_move("h3", "h4")
        self.assertEqual(False, move_after_game_over)

    # --- TEST CAPTURES ---

    def test_normal_capture_one_square(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "b1")
        test_game.make_move("a2", "b2")
        test_game.make_move("i3", "b3")
        num_captured_pieces_black = test_game.get_num_captured_pieces("BLACK")
        self.assertEqual(1, num_captured_pieces_black)
        square_occupant = test_game.get_square_occupant("b2")
        self.assertEqual("NONE", square_occupant)

    def test_normal_capture_multiple_squares(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "c1")
        test_game.make_move("a2", "b2")
        test_game.make_move("c1", "b1")
        test_game.make_move("a3", "b3")
        test_game.make_move("i4", "b4")
        num_captured_pieces_black = test_game.get_num_captured_pieces("BLACK")
        self.assertEqual(2, num_captured_pieces_black)
        square_occupant_capture_one_of_two = test_game.get_square_occupant("b2")
        square_occupant_capture_two_of_two = test_game.get_square_occupant("b3")
        self.assertEqual("NONE", square_occupant_capture_one_of_two)
        self.assertEqual("NONE", square_occupant_capture_two_of_two)

    def test_corner_capture(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "b1")
        test_game.make_move("a2", "b2")
        test_game.make_move("i2", "h2")
        test_game.make_move("b2", "b3")
        test_game.make_move("h2", "a2")
        num_captured_pieces_black = test_game.get_num_captured_pieces("BLACK")
        self.assertEqual(1, num_captured_pieces_black)
        square_occupant = test_game.get_square_occupant("a1")
        self.assertEqual("NONE", square_occupant)

    def test_num_captured_pieces_one(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "b1")
        test_game.make_move("a2", "b2")
        test_game.make_move("i3", "b3")
        num_captured_pieces_black = test_game.get_num_captured_pieces("BLACK")
        num_captured_pieces_red = test_game.get_num_captured_pieces("RED")
        self.assertEqual(1, num_captured_pieces_black)
        self.assertEqual(0, num_captured_pieces_red)

    def test_num_captured_pieces_all(self):
        test_game = HasamiShogiGame()
        test_game.make_move("i1", "b1")
        test_game.make_move("a2", "b2")
        test_game.make_move("i2", "h2")
        test_game.make_move("a3", "b3")
        test_game.make_move("i3", "h3")
        test_game.make_move("a4", "b4")
        test_game.make_move("i4", "h4")
        test_game.make_move("a5", "b5")
        test_game.make_move("i5", "h5")
        test_game.make_move("a6", "b6")
        test_game.make_move("i6", "h6")
        test_game.make_move("a7", "b7")
        test_game.make_move("i7", "h7")
        test_game.make_move("a8", "b8")
        test_game.make_move("i9", "b9")
        test_game.make_move("a1", "a2")
        test_game.make_move("b1", "a1")
        test_game.make_move("a9", "a3")
        test_game.make_move("h4", "a4")
        num_captured_pieces_black = test_game.get_num_captured_pieces("BLACK")
        num_captured_pieces_red = test_game.get_num_captured_pieces("RED")
        self.assertEqual(9, num_captured_pieces_black)
        self.assertEqual(0, num_captured_pieces_red)


if __name__ == '__main__':
    unittest.main()
