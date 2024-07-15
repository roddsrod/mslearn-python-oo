class Participant:
    """
    Represents a participant in the game.
    """

    def __init__(self, name):
        """
        Initializes the participant with a name and sets default values for points and choice.

        Args:
            name (str): The name of the participant.
        """
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self, valid_choices=("rock", "paper", "scissors", "lizard", "spock")):
        """
        Prompts the participant to choose between valid options and validates the input.

        Args:
            valid_choices (tuple, optional): A tuple containing the valid choices for the game. Defaults to ("rock", "paper", "scissors", "lizard", "spock").
        """
        while True:
            self.choice = input(f"{self.name}, select rock, paper, scissor, lizard or Spock: ").lower()
            if self.choice in valid_choices:
                break
            else:
                print(f"Invalid choice, type one of the following: {', '.join(valid_choices)}")

        print(f"{self.name} selects {self.choice}")

    def increment_point(self):
        """
        Increments the participant's points by 1.
        """
        self.points += 1


class GameRound:
    """
    Represents a single round of the game.
    """

    def __init__(self, player1, player2):
        """
        Initializes a game round with two participants.

        Args:
            player1 (Participant): The first participant.
            player2 (Participant): The second participant.
        """
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
        ]

        player1.choose()
        player2.choose()

        result = self.compare_choices(player1, player2)
        print(f"Round resulted in a {self.get_result_as_string(result)}")
        self.award_points(result, player1, player2)

    def compare_choices(self, player1, player2):
        """
        Compares the choices of the two participants using the pre-defined rules matrix.

        Args:
            player1 (Participant): The first participant.
            player2 (Participant): The second participant.

        Returns:
            int: 1 for player1 win, -1 for player2 win, 0 for draw.
        """
        return self.rules[player1.choice.index("rock")][player2.choice.index("rock")]

    def award_points(self, result, player1, player2):
        """
        Awards points to the winner based on the round outcome.

        Args:
            result (int): 1 for player1 win, -1 for player2 win, 0 for draw.
            player1 (Participant): The first participant.
            player2 (Participant): The second participant.
        """
        if result > 0:
            player1.increment_point()
        elif result < 0:
            player2.increment_point()
        else:
            print("No points for anybody.")

    def get_result_as_string(self, result):
        """
        Converts numerical result to a human-readable string.

        Args:
            result (int): 1 for player1 win, -1 for player2 win, 0 for draw.

        Returns:
            str: "draw", "win", or "loss".
        """
        result_map = {0: "draw", 1: "win", -1: "loss"}
        return result_map[result]


class Game:
    """
    Represents a game instance with two participants.
    """

    def __init__(self):
        """
        Initializes the game with two default participants named John and Jane.
        """
        self.end_game = False
        self.player1 = Participant("John")
        self.player2 = Participant("Jane")

    def start(self):
        """
        Starts the game loop and continues until the user decides to quit.
        """
        while not self.end_game:
            GameRound(self.player1, self.player2)
            self.check_end_condition()

    def check_end_condition(self):
        """
        Prompts the user to continue or end the game.

        """
        answer = input("Continue game y/n: (pressing Enter without value will automatically count as 'y') ")

        if answer.lower() == "n":
            self.end_game = True
            print("Game ended, {p1name} has {p1points}, and {p2name} had {p2points}".format(
                p1name=self.player1.name, p1points=self.player1.points, p2name=self.player2.name, p2points=self.player2.points
            ))
            self.determine_winner()

    def determine_winner(self):
        """
        Determines the winner based on the final points and prints the result.
        """
        result_string = "It's a Draw"
        if self.player1.points > self.player2.points:
            result_string = f"Winner is {self.player1.name}"
        elif self.player1.points < self.player2.points:
            result_string = f"Winner is {self.player2.name}"
        print(result_string)


if __name__ == "__main__":
    game = Game()
    game.start()

