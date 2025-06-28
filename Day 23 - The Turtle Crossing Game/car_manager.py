from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=1.4, stretch_wid=0.7)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        pos_x = 300
        pos_y = random.randint(-250, 250)
        new_car.goto(pos_x, pos_y)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            new_x_cor = car.xcor() - self.car_speed
            car.goto(new_x_cor, car.ycor())

    def incement_car_speed(self):
        self.car_speed += MOVE_INCREMENT
