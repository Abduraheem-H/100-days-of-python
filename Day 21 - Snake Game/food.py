from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.refresh()

    def refresh(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.goto(x=pos_x, y=pos_y)
