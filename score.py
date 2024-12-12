from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high-score.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highscore : {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.saveScore()
        else :
            self.score = 0
        self.updateScoreboard()

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def saveScore(self):
        with open("high-score.txt", mode="w") as file:
            file.write(str(self.highscore))
