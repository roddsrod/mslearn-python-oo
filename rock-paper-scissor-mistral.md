Changes made:

1. Added comments to explain what each part of the code does.
2. Renamed some methods to be more descriptive of their functionality.
3. Used f-strings for formatting strings, which is a more modern and readable way to do it.
4. Moved the game loop to the `Game` class, which makes more sense since it's the game that's being managed, not the rounds.
5. Added a check for an empty input in `check_end_condition()`, which allows the user to press Enter to continue the game.
6. Renamed some variables to be more descriptive of their contents.
7. Added a docstring to the `Game` class to explain what it does.
8. Added a `self.end_game` attribute to the `Game` class to keep track of whether the game should end.
9. Moved the creation of the game and the call to `start()` to the bottom of the script, which is a common convention in Python.
