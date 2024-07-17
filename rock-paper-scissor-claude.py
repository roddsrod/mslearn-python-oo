# Import the random module for generating random choices
import random

# Define the Participant class
class Participant:
    # Initialize a participant with a name
    def __init__(self, name):
        self.name = name    # Participant's name
        self.points = 0     # Participant's score
        self.choice = ""    # Participant's current choice

    # Method for the participant to make a choice
    def choose(self):
        # List of possible choices
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        # Randomly select a choice
        self.choice = random.choice(choices)
        # Print the participant's choice
        print(f"{self.name} selects {self.choice}")

    # Method to increment the participant's score
    def add_point(self):
        self.points += 1

# Define the Game class
class Game:
    # Initialize the game
    def __init__(self):
        # Create two participants
        self.p1 = Participant("John")
        self.p2 = Participant("Jane")
        # Define the rules of the game as a dictionary
        self.rules = {
            ("scissors", "paper"): True,
            ("paper", "rock"): True,
            ("rock", "lizard"): True,
            ("lizard", "spock"): True,
            ("spock", "scissors"): True,
            ("scissors", "lizard"): True,
            ("lizard", "paper"): True,
            ("paper", "spock"): True,
            ("spock", "rock"): True,
            ("rock", "scissors"): True
        }

    # Method to play a single round
    def play_round(self):
        # Both participants make their choices
        self.p1.choose()
        self.p2.choose()
        
        # Determine the winner of the round
        if self.p1.choice == self.p2.choice:
            print("It's a tie!")
        elif (self.p1.choice, self.p2.choice) in self.rules:
            print(f"{self.p1.name} wins!")
            self.p1.add_point()
        else:
            print(f"{self.p2.name} wins!")
            self.p2.add_point()

    # Method to play the entire game
    def play_game(self):
        # Continue playing rounds until the player chooses to stop
        while True:
            self.play_round()
            if input("Play another round? (y/n): ").lower() != 'y':
                break
        
        # Print the final scores
        print(f"\nGame over! Final scores:")
        print(f"{self.p1.name}: {self.p1.points}")
        print(f"{self.p2.name}: {self.p2.points}")
        
        # Determine and announce the overall winner
        if self.p1.points > self.p2.points:
            print(f"{self.p1.name} wins the game!")
        elif self.p2.points > self.p1.points:
            print(f"{self.p2.name} wins the game!")
        else:
            print("It's a tie!")

# If this script is run directly (not imported), start the game
if __name__ == "__main__":
    game = Game()
    game.play_game()
