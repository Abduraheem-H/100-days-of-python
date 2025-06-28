from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_go_direction = 10
        self.y_go_direction = 10
        self.move_speed = 0.1

    def move_left(self):
        self.goto(self.xcor() - self.x_go_direction, self.ycor() - self.y_go_direction)

    def move_right(self):
        self.goto(self.xcor() + self.x_go_direction, self.ycor() + self.y_go_direction)

    def bounce(self, is_y: bool = False):
        if is_y:
            self.y_go_direction *= -1
        else:
            self.x_go_direction *= -1
            self.move_speed *= 0.9
