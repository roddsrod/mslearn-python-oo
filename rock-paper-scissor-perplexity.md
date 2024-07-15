Key improvements:

1. Simplified the `Participant` class:
   - Removed `toNumericalChoice` method.
   - Added an `is_computer` flag for computer players.
   - Simplified the `choose` method.

2. Removed the `GameRound` class and integrated its functionality into the `Game` class.

3. Simplified the rules:
   - Instead of a matrix, we now use a set of tuples representing winning combinations.

4. Improved the `Game` class:
   - Removed redundant `checkEndCondition` method.
   - Simplified the game loop in the `play` method.
   - Improved readability of the `determine_winner` method.

5. Used f-strings for better readability.

6. Added a computer player option, making the game playable by a single human player against the computer.

7. Improved input validation and error messages.

8. Added `if __name__ == "__main__":` to make the script both importable and executable.

This version is more concise, easier to read, and more maintainable while keeping all the core functionality of the original game.

