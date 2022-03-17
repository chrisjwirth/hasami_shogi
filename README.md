# Hasami Shogi
<hr>

A command line implementation of the Hasami Shogi game, using the traditional nine-piece variant (see "**Variant 1**" on [the Wikipedia page](https://en.wikipedia.org/wiki/Hasami_shogi)). It was created as my final project in CS162 - Introduction to Computer Science II at Oregon State University.  

Locations on the board are specified using "algebraic notation".

```
  1 2 3 4 5 6 7 8 9
a . . . . . B . . .
b . . . . . R . . .
c . . B R R . . . .
d B . . . . . . . .
e R . . . . . . . .
f R . . . . . . . .
g R . . . . . . . .
h . . . . . B . . .
i R B . . . . . . .
```

## Instructions

To start the game, initiate the HasamiShogiGame class.
```
game = HasamiShogiGame()
```

To print the current game board, run the print_board method.
```
game.print_board()
```

To get the current status of the game, print the return value of the get_game_state method.
```
print(game.get_game_state())
```

To determine who the active player is (BLACK or RED), print the return value of the get_active_player method.
```
print(game.get_active_player())
```

To move a piece, call the make_move method, providing the square moved from and the square moved to in algebraic notation. The method will return True if the move was invalid and False if it was not.
```
print(game.make_move(square_moved_from, square_moved_to))
```
