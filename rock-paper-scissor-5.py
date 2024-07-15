class Participant:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        valid_choices = {"rock", "paper", "scissor", "lizard", "spock"}
        while True:
            self.choice = input("{name}, select rock, paper, scissor, lizard or Spock: ".format(name=self.name)).lower() # added trigger to lower cases to match values present in switcher to avoid unnecessary errors and script crash
            if self.choice in valid_choices: # added if statement requesting a valid choice as original code did not have it, so that entering a non valid choice would crash the script
                break
            else:
                print("Invalid choice, type one of the following: rock, paper, scissor, lizard or Spock")
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))

    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice]
    
    def incrementPoint(self):
        self.points += 1

class GameRound:

    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("Round resulted in a {result}".format(result=self.getResultAsString(result)))
        self.awardPoints(result, p1, p2) # added this line in order to call the function

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    
    def awardPoints(self, result, p1, p2): # added proper code for this entry as the original left it blank and was running from GameRound class init
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
        else:
            print("No points for anybody.")

    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]

class Game:

    def __init__(self):
        self.endGame = False
        self.participant = Participant("John") # changed names to more generic ones, as original had the same value for a name as for a choice, leading to confusion in reading the code 
        self.secondParticipant = Participant("Jane")

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: (pressing Enter without value will automatically count as 'y') ") # added blank entry to count as 'y' to not have to type it everytime we want to go to next round
        if answer == '':
            answer = 'y'
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} had {p2points}".format(p1name=self.participant.name, p1points=self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)

game = Game()
game.start()

