# Author: Christopher Wirth
# Date: 12/02/2021
# Description: An implementation of the Hasami Shogi game, using the traditional nine-piece variant.


class HasamiShogiGame:
    """
    A representation of the Hasami Shogi game.
    This game is played according to the variant 1 rules, provided at https://en.wikipedia.org/wiki/Hasami_shogi.
    """

    def __init__(self):
        """
        Takes no parameters.
        Initializes the Hasami Shogi game.
        """
        self._game_state = "UNFINISHED"
        self._active_player = "BLACK"
        self._black_player_captures = 0
        self._red_player_captures = 0
        self._board = [
            [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["a", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
            ["b", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["c", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["d", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["e", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["f", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["g", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["h", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["i", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
        ]

    def get_game_state(self):
        """
        Takes no parameters.
        Returns the state of the game, which can be "UNFINISHED", "RED_WON", or "BLACK_WON".
        """
        return self._game_state

    def get_active_player(self):
        """
        Takes no parameters.
        Returns "BLACK" or "RED" to indicate whether the black or red player, respectively, is active.
        """
        return self._active_player

    def get_num_captured_pieces(self, player):
        """
        Takes as a parameter "BLACK" or "RED", corresponding to the black or red player, respectively.
        Returns the number of pieces that player has captured.
        """
        if player == "BLACK":
            return self._black_player_captures
        else:
            return self._red_player_captures

    def get_square_occupant(self, square):
        """
        Takes as a parameter a square in algebraic notation.
        Returns "BLACK", "RED", or "NONE" corresponding to a black, red, or no piece, respectively, in the square.
        """
        row, col = self._square_to_indexes(square)
        square_occupant = self._board[row][col]
        if square_occupant == "B":
            return "BLACK"
        elif square_occupant == "R":
            return "RED"
        else:
            return "NONE"

    def make_move(self, square_moved_from, square_moved_to):
        """
        Takes as parameters the squares a player is attempting to move from and to, respectively, in algebraic notation.
        Determines if the move is valid and legal.
        If it is not, returns False.
        If it is, moves the player, captures applicable pieces, sets the game state and active player, and returns True.
        """
        if self._game_state != "UNFINISHED":
            return False
        elif not self._legal_move(square_moved_from, square_moved_to):
            return False
        else:
            self._set_board("REMOVE", square_moved_from)
            self._set_board("ADD", square_moved_to)
            self._capture_pieces(square_moved_from, square_moved_to)
            self._set_game_state()
            self._set_active_player()
            return True

    def print_board(self):
        """
        Takes no parameters.
        Prints the board in an easy-to-read format.
        """
        for row in self._board:
            print(" ".join(row))

    @staticmethod
    def _square_to_indexes(square):
        """
        Takes as a parameter a square in algebraic notation.
        Returns the index of the row and column corresponding to the square.
        """
        row = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i"].index(square[0])
        col = int(square[1])
        return row, col

    @staticmethod
    def _rows_and_cols_to_squares(rows, cols):
        """
        Takes as parameters a list of rows and a list of columns, respectively.
        Converts the row and column at the same index in each list to a single square.
        Returns a list of the corresponding squares.
        """
        squares = []
        for row in rows:
            for col in cols:
                squares.append(str([" ", "a", "b", "c", "d", "e", "f", "g", "h", "i"][row]) + str(col))
        return squares

    def _set_game_state(self):
        """
        Takes no parameters.
        Sets the game state to "BLACK_WON" or "RED_WON", if applicable.
        If no player has won, the game state will remain "UNFINISHED".
        """
        if self._active_player == "BLACK" and self._black_player_captures >= 8:
            self._game_state = "BLACK_WON"
        elif self._active_player == "RED" and self._red_player_captures >= 8:
            self._game_state = "RED_WON"

    def _set_active_player(self):
        """
        Takes no parameters.
        Sets the active player to the previously-inactive player, effectively swapping the active player.
        """
        self._active_player = self._get_opponent_player()

    def _get_opponent_player(self):
        """
        Takes no parameters.
        Returns "BLACK" or "RED", representing the active player's opponent.
        """
        if self._active_player == "BLACK":
            return "RED"
        else:
            return "BLACK"

    def _set_num_captured_pieces(self, pieces_captured):
        """
        Takes as a parameter the number of pieces the active player captured.
        Increases the count of the active player's captured pieces accordingly.
        """
        if self._active_player == "BLACK":
            self._black_player_captures += pieces_captured
        else:
            self._red_player_captures += pieces_captured

    def _set_board(self, action, square):
        """
        Takes as parameters the action "REMOVE" or "ADD" and the corresponding square.
        If the action is "REMOVE", removes the player present in the provided square.
        If the action is "ADD", adds the active player to the provided square.
        """
        row, col = self._square_to_indexes(square)
        if action == "REMOVE":
            self._board[row][col] = "."
        elif action == "ADD":
            if self._active_player == "BLACK":
                self._board[row][col] = "B"
            else:
                self._board[row][col] = "R"

    def _player_direction(self, square_moved_from, square_moved_to):
        """
        Takes as parameters the squares a player is attempting to move from and to, respectively, in algebraic notation.
        Returns the direction of the player's movement.
        """
        row_moved_from, col_moved_from = self._square_to_indexes(square_moved_from)
        row_moved_to, col_moved_to = self._square_to_indexes(square_moved_to)

        if row_moved_from == row_moved_to:
            if col_moved_from < col_moved_to:
                return "Right"
            else:
                return "Left"
        elif col_moved_from == col_moved_to:
            if row_moved_from > row_moved_to:
                return "Up"
            else:
                return "Down"

    def _squares_to_check_for_legal_move(self, square_moved_from, square_moved_to):
        """
        Takes as parameters the squares a player is attempting to move from and to, respectively, in algebraic notation.
        Returns a list of the squares in the provided direction between the square moved from and the square moved to.
        """
        rows_to_check, cols_to_check = [], []

        player_direction = self._player_direction(square_moved_from, square_moved_to)
        row_moved_from, col_moved_from = self._square_to_indexes(square_moved_from)
        row_moved_to, col_moved_to = self._square_to_indexes(square_moved_to)

        if player_direction == "Right":
            rows_to_check.append(row_moved_from)
            cols_to_check += list(range(col_moved_from + 1, col_moved_to))
        elif player_direction == "Left":
            rows_to_check.append(row_moved_from)
            cols_to_check += list(range(col_moved_to, col_moved_from))
        elif player_direction == "Up":
            cols_to_check.append(col_moved_from)
            rows_to_check += list(range(row_moved_to, row_moved_from))
        elif player_direction == "Down":
            cols_to_check.append(col_moved_from)
            rows_to_check += list(range(row_moved_from + 1, row_moved_to))

        return self._rows_and_cols_to_squares(rows_to_check, cols_to_check)

    def _legal_move(self, square_moved_from, square_moved_to):
        """
        Takes as parameters the squares a player is attempting to move from and to, respectively, in algebraic notation.
        Returns True if the move is legal, else returns False.
        """
        if self.get_square_occupant(square_moved_from) != self._active_player:
            return False

        if square_moved_from == square_moved_to:
            return False

        row_moved_from, col_moved_from = self._square_to_indexes(square_moved_from)
        row_moved_to, col_moved_to = self._square_to_indexes(square_moved_to)
        if row_moved_from != row_moved_to and col_moved_from != col_moved_to:
            return False

        if self.get_square_occupant(square_moved_to) != "NONE":
            return False

        for square in self._squares_to_check_for_legal_move(square_moved_from, square_moved_to):
            if self.get_square_occupant(square) != "NONE":
                return False

        return True

    def _corner_capture(self, square_moved_to):
        """
        Takes as a parameter the square the active player moved to, in algebraic notation.
        Returns the active player's corner capture, if applicable.
        """
        corners_and_capture_locations = {"a1": ("a2", "b1"), "a9": ("a8", "b9"), "i1": ("h1", "i2"), "i9": ("h9", "i8")}

        for corner, capture_location in corners_and_capture_locations.items():
            if square_moved_to == capture_location[0]:
                if self.get_square_occupant(capture_location[1]) == self._active_player:
                    if self.get_square_occupant(corner) == self._get_opponent_player():
                        return corner
            elif square_moved_to == capture_location[1]:
                if self.get_square_occupant(capture_location[0]) == self._active_player:
                    if self.get_square_occupant(corner) == self._get_opponent_player():
                        return corner

    def _squares_to_check_for_non_corner_capture(self, direction_to_check, square_moved_to):
        """
        Takes as parameters the direction to check and the square the active player moved to, in algebraic notation.
        Returns a list of the squares in the provided direction between the square moved to and the edge of the board.
        """
        row_moved_to, col_moved_to = self._square_to_indexes(square_moved_to)

        rows_to_check, cols_to_check = [], []

        if direction_to_check == "Right":
            rows_to_check.append(row_moved_to)
            cols_to_check += list(range(col_moved_to + 1, 10))
        elif direction_to_check == "Left":
            rows_to_check.append(row_moved_to)
            cols_to_check += list(range(col_moved_to - 1, 0, -1))
        elif direction_to_check == "Up":
            rows_to_check += list(range(row_moved_to - 1, 0, -1))
            cols_to_check.append(col_moved_to)
        elif direction_to_check == "Down":
            rows_to_check += list(range(row_moved_to + 1, 10))
            cols_to_check.append(col_moved_to)

        return self._rows_and_cols_to_squares(rows_to_check, cols_to_check)

    def _directions_to_check_for_non_corner_capture(self, square_moved_from, square_moved_to):
        """
        Takes as parameters the squares the active player moved from and to, respectively, in algebraic notation.
        Returns a dictionary containing the squares to check for captures in each applicable direction.
        """
        player_direction = self._player_direction(square_moved_from, square_moved_to)
        directions_to_check = {"Right": [], "Left": [], "Down": [], "Up": []}

        if player_direction == "Right":
            del directions_to_check["Left"]
        elif player_direction == "Left":
            del directions_to_check["Right"]
        elif player_direction == "Up":
            del directions_to_check["Down"]
        elif player_direction == "Down":
            del directions_to_check["Up"]

        for direction in directions_to_check:
            directions_to_check[direction] = self._squares_to_check_for_non_corner_capture(direction, square_moved_to)

        return directions_to_check

    def _non_corner_capture(self, square_moved_from, square_moved_to):
        """
        Takes as parameters the squares the active player moved from and to, respectively, in algebraic notation.
        Returns the active player's non-corner captures, if applicable.
        """
        non_corner_captures = []

        directions_to_check = self._directions_to_check_for_non_corner_capture(square_moved_from, square_moved_to)

        for squares_to_check in directions_to_check.values():
            potential_captured_squares = []
            for square_to_check in squares_to_check:
                square_occupant = self.get_square_occupant(square_to_check)
                if square_occupant == self._get_opponent_player():
                    potential_captured_squares.append(square_to_check)
                elif square_occupant == self._active_player:
                    non_corner_captures += potential_captured_squares
                    break
                elif square_occupant == "NONE":
                    break

        return non_corner_captures

    def _capture_pieces(self, square_moved_from, square_moved_to):
        """
        Takes as parameters the squares the active player moved from and to, respectively, in algebraic notation.
        Determines whether any of the opponents pieces were captured following the legal move.
        If so, clears the pieces from the board and accordingly increases the active player's number of captured pieces.
        """
        captured_squares = []

        captured_corner = self._corner_capture(square_moved_to)
        if captured_corner:
            captured_squares.append(captured_corner)

        captured_non_corners = self._non_corner_capture(square_moved_from, square_moved_to)
        if captured_non_corners:
            captured_squares += captured_non_corners

        self._set_num_captured_pieces(len(captured_squares))

        for square in captured_squares:
            self._set_board("REMOVE", square)
