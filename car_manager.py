import random
from turtle import Turtle, Screen

screen = Screen()
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LIST_A = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


# this class will be for making and moving cars
class CarManager:

    def __init__(self):
        self.cars = []
        self.generate_car()

    # make random car
    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            tn = random.randint(0, 5)
            tc = COLORS[tn]
            x = 300
            y = random.randint(-250, 250)
            tim = Turtle(shape="square")
            tim.shapesize(stretch_wid=1, stretch_len=2)
            tim.color(tc)
            tim.penup()
            tim.goto(x, y)
            tim.setheading(180)
            self.cars.append(tim)

    # for moving cars
    def generate_move(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
