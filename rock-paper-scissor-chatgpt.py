class Participant:
    def __init__(self, name):
        # Initialize participant with a name, 0 points, and an empty choice
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        # Define valid choices
        valid_choices = {"rock", "paper", "scissor", "lizard", "spock"}
        # Keep asking for a valid choice until one is provided
        while True:
            self.choice = input(f"{self.name}, select rock, paper, scissor, lizard or Spock: ").lower()
            if self.choice in valid_choices:
                break
            else:
                print("Invalid choice, type one of the following: rock, paper, scissor, lizard or Spock")
        print(f"{self.name} selects {self.choice}")

    def to_numerical_choice(self):
        # Map choices to numerical values for easier comparison
        choices_map = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "lizard": 3,
            "spock": 4
        }
        return choices_map[self.choice]

    def increment_point(self):
        # Increment participant's points
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        # Define the rules matrix
        self.rules = [
            [0, -1, 1, 1, -1],    # Rock
            [1, 0, -1, -1, 1],    # Paper
            [-1, 1, 0, 1, -1],    # Scissor
            [-1, 1, -1, 0, 1],    # Lizard
            [1, -1, 1, -1, 0]     # Spock
        ]
        # Participants choose their options
        p1.choose()
        p2.choose()
        # Compare choices and print result
        result = self.compare_choices(p1, p2)
        print(f"Round resulted in a {self.get_result_as_string(result)}")
        # Award points based on result
        self.award_points(result, p1, p2)

    def compare_choices(self, p1, p2):
        # Compare the numerical choices of both participants
        return self.rules[p1.to_numerical_choice()][p2.to_numerical_choice()]

    def award_points(self, result, p1, p2):
        # Award points to the winning participant
        if result > 0:
            p1.increment_point()
        elif result < 0:
            p2.increment_point()
        else:
            print("No points for anybody.")

    def get_result_as_string(self, result):
        # Convert result to a string for printing
        result_map = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return result_map[result]


class Game:
    def __init__(self):
        # Initialize the game with two participants
        self.participant = Participant("John")
        self.second_participant = Participant("Jane")

    def start(self):
        # Start the game loop
        while True:
            GameRound(self.participant, self.second_participant)
            # Check if the game should end
            if not self.check_end_condition():
                break
        # Determine and print the winner
        self.determine_winner()

    def check_end_condition(self):
        # Ask if the user wants to continue the game
        answer = input("Continue game y/n: (pressing Enter without value will automatically count as 'y') ").strip().lower()
        if answer == '' or answer == 'y':
            return True
        else:
            print(f"Game ended, {self.participant.name} has {self.participant.points}, and {self.second_participant.name} has {self.second_participant.points}")
            return False

    def determine_winner(self):
        # Determine and print the winner of the game
        if self.participant.points > self.second_participant.points:
            result_string = f"Winner is {self.participant.name}"
        elif self.participant.points < self.second_participant.points:
            result_string = f"Winner is {self.second_participant.name}"
        else:
            result_string = "It's a Draw"
        print(result_string)


# Create and start the game
game = Game()
game.start()
