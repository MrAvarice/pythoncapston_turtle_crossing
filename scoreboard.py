from turtle import Turtle

FONT = ("Courier", 24, "normal")


# class for keeping score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_display()

    # for displaying the total score
    def score_display(self):
        self.hideturtle()
        self.penup()
        self.goto(-260, 270)
        self.color("black")
        self.write(f"Score:{self.score}", True, align="left", font=(FONT))

    # for adding score
    def add(self):
        self.clear()
        self.score += 1

        self.write(f"Score:{self.score}", True, align="left", font=(FONT))
        self.goto(-260, 270)
