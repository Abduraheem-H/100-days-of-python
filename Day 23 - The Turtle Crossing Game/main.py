import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
canvas = screen.getcanvas()
window = canvas.winfo_toplevel()
window.geometry("+300+25")
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 6) == 1:
        car.generate_car()
    car.move_cars()

    # detect colision with cars
    for each_car in car.cars:
        if player.distance(each_car) < 23:
            scoreboard.game_over()
            game_is_on = False

    # detect level pass
    if player.ycor() > 280:
        player.return_back()
        car.incement_car_speed()
        scoreboard.increment_level()
screen.exitonclick()
