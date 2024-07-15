### Explanation of Changes

1. **Code Readability and Consistency:**
   - Replaced string formatting `.format()` with f-strings for readability and consistency.
   - Improved variable and method names to follow Python naming conventions (e.g., `to_numerical_choice` instead of `toNumericalChoice`, `increment_point` instead of `incrementPoint`).

2. **Loop Simplification:**
   - Simplified the loop in the `start` method of the `Game` class to avoid unnecessary recursion. This makes it easier to understand and avoids potential stack overflow issues in a long game session.

3. **Redundant Code Removal:**
   - Removed redundant call to `GameRound` within `checkEndCondition`. The game loop in `start` handles the repetition.

4. **Input Handling:**
   - Improved input handling in `check_end_condition` to ensure it processes any valid input properly and trims any extra spaces.

5. **Commenting:**
   - Added comments to every significant line or block of code to explain its purpose, making it easier for others (or future you) to understand the flow and logic of the code.

These changes improve the overall readability, maintainability, and execution flow of the code without altering its functionality.
