# Define the Participant class
class Participant:
    def __init__(self, name):
        # Initialize the participant's name, points, and choice
        self.name = name
        self.points = 0
        self.choice = ""

    def make_choice(self):
        # Define the valid choices
        valid_choices = {"rock", "paper", "scissor", "lizard", "spock"}
        # Loop until a valid choice is made
        while True:
            self.choice = input(f"{self.name}, select rock, paper, scissor, lizard or Spock: ").lower()
            # Check if the choice is valid
            if self.choice in valid_choices:
                break
            else:
                print("Invalid choice, type one of the following: rock, paper, scissor, lizard or Spock")
        print(f"{self.name} selects {self.choice}")

    def get_numerical_choice(self):
        # Map the choices to numerical values for comparison
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice]

    def add_point(self):
        # Increment the participant's points by 1
        self.points += 1

# Define the GameRound class
class GameRound:
    def __init__(self, p1, p2):
        # Define the rules of the game
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        # Have each participant make a choice
        p1.make_choice()
        p2.make_choice()
        # Compare the choices and determine the result
        result = self.compare_choices(p1, p2)
        print(f"Round resulted in a {self.get_result_as_string(result)}")
        # Award points based on the result
        self.award_points(result, p1, p2)

    def compare_choices(self, p1, p2):
        # Use the rules to determine the result of the comparison
        return self.rules[p1.get_numerical_choice()][p2.get_numerical_choice()]

    def award_points(self, result, p1, p2):
        # Award points based on the result of the comparison
        if result > 0:
            p1.add_point()
        elif result < 0:
            p2.add_point()
        else:
            print("No points for anybody.")

    def get_result_as_string(self, result):
        # Map the results to strings for printing
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]

# Define the Game class
class Game:
    def __init__(self):
        # Initialize the game with two participants
        self.end_game = False
        self.participant1 = Participant("John")
        self.participant2 = Participant("Jane")

    def start(self):
        # Start the game loop
        while not self.end_game:
            GameRound(self.participant1, self.participant2)
            self.check_end_condition()

    def check_end_condition(self):
        # Check if the game should end
        answer = input("Continue game y/n: (pressing Enter without value will automatically count as 'y') ")
        if answer == '':
            answer = 'y'
        if answer == 'y':
            # If the game should not end, start a new round
            GameRound(self.participant1, self.participant2)
            self.check_end_condition()
        else:
            # If the game should end, print the final scores and determine the winner
            print(f"Game ended, {self.participant1.name} has {self.participant1.points}, and {self.participant2.name} had {self.participant2.points}")
            self.determine_winner()
            self.end_game = True

    def determine_winner(self):
        # Determine the winner based on the final scores
        result_string = "It's a Draw"
        if self.participant1.points > self.participant2.points:
            result_string = f"Winner is {self.participant1.name}"
        elif self.participant1.points < self.participant2.points:
            result_string = f"Winner is {self.participant2.name}"
        print(result_string)

# Create a new game and start it
game = Game()
game.start()
