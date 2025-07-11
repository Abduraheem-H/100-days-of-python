from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        pos_x = self.xcor()
        pos_y = self.ycor()
        self.goto(pos_x, pos_y + MOVE_DISTANCE)

    def return_back(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
