Here's a step-by-step explanation of what happens in the code, in the order the lines are executed:

### Starting Point

1. **Line 78: `game = Game()`**
   - This line creates an instance of the `Game` class, invoking its `__init__` method.
   
2. **Line 79: `game.start()`**
   - This line calls the `start` method on the `game` instance, beginning the game loop.

### Game Class Initialization

3. **Line 57: `def __init__(self):`**
   - This is the constructor for the `Game` class. It initializes the game state.
   
4. **Line 58: `self.endGame = False`**
   - The `endGame` attribute is set to `False`, indicating that the game is not yet over.

5. **Line 59: `self.participant = Participant("John")`**
   - This creates a new `Participant` instance for "John", invoking the `Participant` class's `__init__` method.
   
6. **Line 2: `def __init__(self, name):`**
   - The constructor for the `Participant` class is called with the name "John".
   
7. **Line 3: `self.name = name`**
   - The `name` attribute is set to "John".
   
8. **Line 4: `self.points = 0`**
   - The `points` attribute is initialized to 0.
   
9. **Line 5: `self.choice = ""`**
   - The `choice` attribute is initialized to an empty string.
   
10. **Line 59: `self.secondParticipant = Participant("Jane")`**
    - This creates a new `Participant` instance for "Jane", following the same steps (2-9) as for "John".

### Starting the Game Loop

11. **Line 63: `def start(self):`**
    - The `start` method of the `Game` class is invoked.
    
12. **Line 64: `while not self.endGame:`**
    - The game loop starts and will continue until `self.endGame` is set to `True`.
    
13. **Line 65: `GameRound(self.participant, self.secondParticipant)`**
    - A new `GameRound` instance is created, invoking its `__init__` method.

### GameRound Class Initialization

14. **Line 26: `def __init__(self, p1, p2):`**
    - The constructor for the `GameRound` class is called with `p1` (John) and `p2` (Jane).
    
15. **Line 27-31: `self.rules = [...]`**
    - The `rules` attribute is initialized with a 2D list representing the game's rules.
    
16. **Line 32: `p1.choose()`**
    - The `choose` method of `Participant` `p1` (John) is called.

### John Makes a Choice

17. **Line 8: `def choose(self):`**
    - The `choose` method of the `Participant` class is invoked for John.
    
18. **Line 9: `valid_choices = {"rock", "paper", "scissor", "lizard", "spock"}`**
    - A set of valid choices is defined.
    
19. **Line 11-16: `while True:`**
    - A loop starts to prompt John to make a valid choice.
    
20. **Line 12: `self.choice = input(...).lower()`**
    - John is prompted to select rock, paper, scissor, lizard, or Spock. The input is converted to lowercase.
    
21. **Line 13: `if self.choice in valid_choices:`**
    - The input is checked against the set of valid choices.
    
22. **Line 14: `break`**
    - If the choice is valid, the loop breaks.
    
23. **Line 16: `print(...)`**
    - John's choice is printed.

### Jane Makes a Choice

24. **Line 33: `p2.choose()`**
    - The `choose` method of `Participant` `p2` (Jane) is called, following the same steps (17-23) as for John.

### Comparing Choices and Awarding Points

25. **Line 34: `result = self.compareChoices(p1, p2)`**
    - The `compareChoices` method is called to determine the result of the round.

26. **Line 40: `def compareChoices(self, p1, p2):`**
    - The `compareChoices` method is invoked.
    
27. **Line 41: `return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]`**
    - The method uses the `rules` matrix to determine the outcome of the round based on the numerical choices of `p1` and `p2`.
    
28. **Line 19: `def toNumericalChoice(self):`**
    - The `toNumericalChoice` method of `Participant` is called for `p1` (John).
    
29. **Line 20: `switcher = {...}`**
    - A dictionary mapping choices to numerical values is defined.
    
30. **Line 23: `return switcher[self.choice]`**
    - John's choice is converted to a numerical value.
    
31. **Line 19-23: `toNumericalChoice` is called for `p2` (Jane)**
    - Jane's choice is converted to a numerical value following the same steps as for John.

### Printing the Result

32. **Line 35: `print("Round resulted in a {result}".format(result=self.getResultAsString(result)))`**
    - The result of the round is printed using the `getResultAsString` method.

33. **Line 50: `def getResultAsString(self, result):`**
    - The `getResultAsString` method is invoked.
    
34. **Line 51: `res = {...}`**
    - A dictionary mapping results to strings is defined.
    
35. **Line 55: `return res[result]`**
    - The result is converted to a string and returned.

### Awarding Points

36. **Line 36: `self.awardPoints(result, p1, p2)`**
    - The `awardPoints` method is called to award points based on the result.

37. **Line 43: `def awardPoints(self, result, p1, p2):`**
    - The `awardPoints` method is invoked.
    
38. **Line 44-48: `if result > 0: ... elif result < 0: ... else: ...`**
    - Points are awarded to the winner of the round.

39. **Line 24: `def incrementPoint(self):`**
    - The `incrementPoint` method is called for the winning participant.

### Checking End Condition

40. **Line 66: `self.checkEndCondition()`**
    - The `checkEndCondition` method is called to determine if the game should continue.

41. **Line 68: `def checkEndCondition(self):`**
    - The `checkEndCondition` method is invoked.
    
42. **Line 69: `answer = input("Continue game y/n: ...")`**
    - The user is prompted to continue the game.
    
43. **Line 70-71: `if answer == '': answer = 'y'`**
    - If no input is given, the default answer is set to 'y'.
    
44. **Line 72: `if answer == 'y':`**
    - If the user wants to continue, a new round is started.
    
45. **Line 73: `GameRound(self.participant, self.secondParticipant)`**
    - A new `GameRound` instance is created, and the process from step 14 repeats.
    
46. **Line 74: `self.checkEndCondition()`**
    - The `checkEndCondition` method is called again.
    
47. **Line 75: `else:`**
    - If the user does not want to continue, the game ends.
    
48. **Line 76: `print("Game ended, ...")`**
    - The final scores are printed.
    
49. **Line 77: `self.determineWinner()`**
    - The `determineWinner` method is called to determine the overall winner.

### Determining the Winner

50. **Line 81: `def determineWinner(self):`**
    - The `determineWinner` method is invoked.
    
51. **Line 82-86: `if ... elif ... else ...`**
    - The winner is determined based on the final scores and a message is printed.

52. **Line 87: `self.endGame = True`**
    - The `endGame` attribute is set to `True`, ending the game loop.

### End of Game Loop

53. **Line 64: `while not self.endGame:`**
    - The game loop exits because `self.endGame` is now `True`.

### Conclusion

- The game ends, and the final winner is announced. The program stops execution.
