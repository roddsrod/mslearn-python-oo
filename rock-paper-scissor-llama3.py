class Participant:
    """
    Represents a participant in the game.
    """
    def __init__(self, name: str):
        """
        Initializes a participant with a name and zero points.
        Args:
            name (str): The participant's name.
        """
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self) -> None:
        """
        Asks the participant to choose a valid option.
        """
        valid_choices = {"rock", "paper", "scissor", "lizard", "spock"}
        while True:
            self.choice = input(f"{self.name}, select rock, paper, scissor, lizard or Spock: ").lower()
            if self.choice in valid_choices:
                break
            print("Invalid choice, type one of the following: rock, paper, scissor, lizard or Spock")
        print(f"{self.name} selects {self.choice}")

    def to_numerical_choice(self) -> int:
        """
        Converts the participant's choice to a numerical value.
        Returns:
            int: The numerical value of the participant's choice.
        """
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice]

    def increment_point(self) -> None:
        """
        Increments the participant's points.
        """
        self.points += 1


class GameRound:
    """
    Represents a round in the game.
    """
    def __init__(self, p1: Participant, p2: Participant):
        """
        Initializes a game round with two participants.
        Args:
            p1 (Participant): The first participant.
            p2 (Participant): The second participant.
        """
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compare_choices(p1, p2)
        print(f"Round resulted in a {self.get_result_as_string(result)}")
        self.award_points(result, p1, p2)

    def compare_choices(self, p1: Participant, p2: Participant) -> int:
        """
        Compares the choices of two participants.
        Args:
            p1 (Participant): The first participant.
            p2 (Participant): The second participant.
        Returns:
            int: The result of the comparison.
        """
        return self.rules[p1.to_numerical_choice()][p2.to_numerical_choice()]

    def award_points(self, result: int, p1: Participant, p2: Participant) -> None:
        """
        Awards points to the winner of the round.
        Args:
            result (int): The result of the comparison.
            p1 (Participant): The first participant.
            p2 (Participant): The second participant.
        """
        if result > 0:
            p1.increment_point()
        elif result < 0:
            p2.increment_point()
        else:
            print("No points for anybody.")

    def get_result_as_string(self, result: int) -> str:
        """
        Converts the result to a string.
        Args:
            result (int): The result of the comparison.
        Returns:
            str: The result as a string.
        """
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]


class Game:
    """
    Represents the game.
    """
    def __init__(self):
        """
        Initializes the game with two participants.
        """
        self.end_game = False
        self.participant = Participant("John")
        self.second_participant = Participant("Jane")

    def start(self) -> None:
        """
        Starts the game.
        """
        while not self.end_game:
            GameRound(self.participant, self.second_participant)
            self.check_end_condition()

    def check_end_condition(self) -> None:
        """
        Checks if the game should end.
        """
        answer = input("Continue game y/n: (pressing Enter without value will automatically count as 'y') ")
        if answer == '':
            answer = 'y'
        if answer == 'y':
            GameRound(self.participant, self.second_participant)
            self.check_end_condition()
        else:
            print(f"Game ended, {self.participant.name} has {self.participant.points}, and {self.second_participant.name} had {self.second_participant.points}")
            self.determine_winner()
            self.end_game = True

    def determine_winner(self) -> None:
        """
        Determines the winner of the game.
        """
        result_string = "It's a Draw"
        if self.participant.points > self.second_participant.points:
            result_string = f"Winner is {self.participant.name}"
        elif self.participant.points < self.second_participant.points:
            result_string = f"Winner is {self.second_participant.name}"
        print(result_string)


game = Game()
game.start()

