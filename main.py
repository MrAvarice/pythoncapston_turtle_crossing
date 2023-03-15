import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import car_manager

score = Scoreboard()

play = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(play.moving, "Up")

car = car_manager.CarManager()
# While loop will run the game
game_is_on = True
while game_is_on:
    time.sleep(0.9)
    screen.update()
    car.generate_move()
    # statement for respawn player after successfully crossing
    if play.ycor() > 290:
        play.spawn()
        score.add()
        print("yes")
        game_is_on = True
    # statement for generating car
    if play.ycor() < 290:
        car.generate_car()
    # loop for player and car contact
    for car in car.cars:
        if car.distance(play) < 20:
            game_is_on = False

screen.exitonclick()
screen.onclick()
