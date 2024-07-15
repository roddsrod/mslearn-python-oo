import random  # Import the random module for computer choices

class Participant:
    # Class variable containing all valid choices
    CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

    def __init__(self, name, is_computer=False):
        self.name = name  # Player's name
        self.points = 0  # Player's score
        self.choice = ""  # Player's current choice
        self.is_computer = is_computer  # Flag to determine if it's a computer player

    def choose(self):
        if self.is_computer:
            # Computer randomly selects a choice
            self.choice = random.choice(self.CHOICES)
        else:
            while True:
                # Prompt human player for input
                self.choice = input(f"{self.name}, select {', '.join(self.CHOICES)}: ").lower()
                if self.choice in self.CHOICES:
                    break  # Exit loop if choice is valid
                print(f"Invalid choice. Please choose from: {', '.join(self.CHOICES)}")
        print(f"{self.name} selects {self.choice}")  # Announce the choice

    def add_point(self):
        self.points += 1  # Increment player's score

class Game:
    # Class variable containing all winning combinations
    RULES = {
        ("scissors", "paper"), ("paper", "rock"), ("rock", "lizard"),
        ("lizard", "spock"), ("spock", "scissors"), ("scissors", "lizard"),
        ("lizard", "paper"), ("paper", "spock"), ("spock", "rock"), ("rock", "scissors")
    }

    def __init__(self):
        self.p1 = Participant("You")  # Create human player
        self.p2 = Participant("Computer", is_computer=True)  # Create computer player

    def play_round(self):
        self.p1.choose()  # Human player makes a choice
        self.p2.choose()  # Computer player makes a choice
        self.determine_winner()  # Determine the winner of the round

    def determine_winner(self):
        if self.p1.choice == self.p2.choice:
            print("It's a tie!")  # If choices are the same, it's a tie
        elif (self.p1.choice, self.p2.choice) in self.RULES:
            print(f"{self.p1.name} wins!")  # If combination is in RULES, p1 wins
            self.p1.add_point()
        else:
            print(f"{self.p2.name} wins!")  # Otherwise, p2 wins
            self.p2.add_point()

    def play(self):
        while True:
            self.play_round()  # Play a round
            # Ask if player wants to continue
            if input("Play another round? (y/n): ").lower() != 'y':
                break  # Exit loop if answer is not 'y'
        self.print_result()  # Print final results

    def print_result(self):
        print(f"\nGame over! Final scores:")
        print(f"{self.p1.name}: {self.p1.points}")  # Print p1's score
        print(f"{self.p2.name}: {self.p2.points}")  # Print p2's score
        if self.p1.points > self.p2.points:
            print(f"{self.p1.name} wins the game!")  # p1 wins if they have more points
        elif self.p2.points > self.p1.points:
            print(f"{self.p2.name} wins the game!")  # p2 wins if they have more points
        else:
            print("The game is a tie!")  # It's a tie if points are equal

if __name__ == "__main__":
    game = Game()  # Create a new game
    game.play()  # Start the game
