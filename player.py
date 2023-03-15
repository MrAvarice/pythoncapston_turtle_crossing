from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# class for making player avatar and moving and respawning
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    # for moving player
    def moving(self):
        self.forward(20)

    # for respawning
    def spawn(self):
        self.goto(0, -280)
