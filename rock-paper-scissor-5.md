Step-by-step explanation of the code execution, describing which line of code runs after each other and how the flow of control moves through the program.

### Explanation of Code Execution Order

#### Initialization of the `Game` class and Starting the Game

1. **Line 99**: `game = Game()`
    - A new instance of the `Game` class is created.
    - This triggers the `__init__` method of the `Game` class.

2. **Line 68**: `def __init__(self):`
    - Initializes the game:
    - **Line 69**: `self.endGame = False` sets the `endGame` attribute to `False`.
    - **Line 70**: `self.participant = Participant("John")` creates a new `Participant` named John, triggering the `__init__` method of the `Participant` class.
    - **Line 4**: `def __init__(self, name):`
        - Initializes the `Participant`:
        - **Line 5**: `self.name = name` sets the `name` attribute to "John".
        - **Line 6**: `self.points = 0` initializes `points` to 0.
        - **Line 7**: `self.choice = ""` initializes `choice` to an empty string.
        - **Line 8**: Returns `None`, completing the initialization of John.
    - **Line 71**: `self.secondParticipant = Participant("Jane")` creates a new `Participant` named Jane, triggering the `__init__` method of the `Participant` class again.
    - **Line 4-8**: The same steps as above are repeated for Jane.
    - **Line 72**: Returns `None`, completing the initialization of the `Game` instance.

3. **Line 73**: `game.start()`
    - Calls the `start` method of the `Game` class.
    - **Line 74**: `def start(self):`
        - Starts the game loop:
        - **Line 75**: `while not self.endGame:` starts a loop that continues as long as `endGame` is `False`.

#### First Round of the Game

4. **Line 76**: `GameRound(self.participant, self.secondParticipant)`
    - A new instance of the `GameRound` class is created with John and Jane as participants.
    - This triggers the `__init__` method of the `GameRound` class.

5. **Line 28**: `def __init__(self, p1, p2):`
    - Initializes the game round:
    - **Line 29-35**: `self.rules = [...]` initializes the rules matrix.
    - **Line 36**: `p1.choose()` calls the `choose` method for participant John (p1).
    - **Line 11**: `def choose(self):`
        - Executes the `choose` method for John:
        - **Line 12**: `valid_choices = {"rock", "paper", "scissor", "lizard", "spock"}` defines valid choices.
        - **Line 13**: `while True:` starts an input loop.
        - **Line 14**: `self.choice = input("{name}, select rock, paper, scissor, lizard or Spock: ".format(name=self.name)).lower()` prompts John for input and converts it to lowercase.
        - If the choice is valid:
            - **Line 15**: `if self.choice in valid_choices:` checks if the choice is valid.
            - **Line 16**: `break` exits the loop.
        - If the choice is invalid:
            - **Line 18**: `else:` enters the invalid choice branch.
            - **Line 19**: `print("Invalid choice, type one of the following: rock, paper, scissor, lizard or Spock")` prints an error message.
        - **Line 20**: Prints the chosen option: `print("{name} selects {choice}".format(name=self.name, choice=self.choice))`.
        - **Line 21**: Returns `None`, completing John's choice.

6. **Line 37**: `p2.choose()` calls the `choose` method for participant Jane (p2).
    - **Line 11-21**: The same steps as above are repeated for Jane.

7. **Line 38**: `result = self.compareChoices(p1, p2)` calls the `compareChoices` method.
    - **Line 40**: `def compareChoices(self, p1, p2):`
        - Compares the choices:
        - **Line 41**: `return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]` returns the result based on the rules matrix.
        - **Line 23**: `def toNumericalChoice(self):`
            - Converts the choice to a numerical value:
            - **Line 24**: `switcher = {...}` defines the conversion dictionary.
            - **Line 25**: `return switcher[self.choice]` returns the numerical choice for John.
        - **Line 23-25**: The same steps are repeated for Jane.
        - **Line 42**: Returns the result.

8. **Line 39**: `print("Round resulted in a {result}".format(result=self.getResultAsString(result)))`
    - Prints the result of the round.
    - **Line 53**: `def getResultAsString(self, result):`
        - Converts the result to a string:
        - **Line 54**: `res = {...}` defines the result conversion dictionary.
        - **Line 55**: `return res[result]` returns the result as a string.
        - **Line 56**: Returns the result string.

9. **Line 39**: Calls `self.awardPoints(result, p1, p2)`
    - **Line 45**: `def awardPoints(self, result, p1, p2):`
        - Awards points based on the result:
        - If result > 0:
            - **Line 46**: `if result > 0:` checks if John wins.
            - **Line 47**: `p1.incrementPoint()` increments John's points.
            - **Line 26**: `def incrementPoint(self):`
                - **Line 27**: `self.points += 1` increments points by 1.
                - **Line 28**: Returns `None`.
        - If result < 0:
            - **Line 48**: `elif result < 0:` checks if Jane wins.
            - **Line 49**: `p2.incrementPoint()` increments Jane's points.
            - **Line 26-28**: The same steps are repeated for Jane.
        - If result == 0:
            - **Line 50**: `else:` enters the draw branch.
            - **Line 51**: `print("No points for anybody.")` prints no points message.
        - **Line 52**: Returns `None`.

10. **Line 44**: Returns `None`, completing the game round.

#### Checking End Condition

11. **Line 77**: `self.checkEndCondition()` calls `checkEndCondition`
    - **Line 78**: `def checkEndCondition(self):`
        - Checks if the game should continue:
        - **Line 79**: `answer = input("Continue game y/n: (pressing Enter without value will automatically count as 'y') ")` prompts for input.
        - **Line 80**: `if answer == '':` checks if input is empty.
        - **Line 81**: `answer = 'y'` sets default to 'y'.
        - **Line 82**: `if answer == 'y':` checks if input is 'y'.
        - **Line 83**: `GameRound(self.participant, self.secondParticipant)` starts a new round.
        - **Line 28-44**: The same steps as above are repeated for the new round.
        - **Line 84**: `self.checkEndCondition()` recursively checks the end condition.
        - **Line 78-84**: The same steps are repeated.
        - **Line 85**: `else:` enters the game end branch.
        - **Line 86**: `print("Game ended, {p1name} has {p1points}, and {p2name} had {p2points}".format(p1name=self.participant.name, p1points=self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))` prints the final points.
        - **Line 87**: `self.determineWinner()` calls `determineWinner`
        - **Line 89**: `def determineWinner(self):`
            - Determines the winner:
            - **Line 90**: `resultString = "It's a Draw"` sets default result string.
            - **Line 91**: `if self.participant.points > self.secondParticipant.points:` checks if John wins.
            - **Line 92**: `resultString = "Winner is {name}".format(name=self.participant.name)` sets winner string to John.
            - **Line 93**: `elif self.participant.points < self.secondParticipant.points:` checks if Jane wins.
            - **Line 94**: `resultString = "Winner is {name}".format(name=self.secondParticipant.name)` sets winner string to Jane.
            - **Line 95

**: `print(resultString)` prints the result string.
            - **Line 96**: Returns `None`.
        - **Line 87**: `self.endGame = True` sets `endGame` to `True`.
        - **Line 88**: Returns `None`.

12. **Line 75**: The loop in the `start` method ends as `endGame` is now `True`.
13. **Line 73**: The `start` method completes and returns `None`.

This step-by-step explanation should help you understand the flow of execution in your code. Each line is described in the order it is executed, showing the interactions between methods and classes.

