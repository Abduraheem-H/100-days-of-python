from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.moving = True

    def create_snake(self):
        """Create the initial snake with 3 segments"""
        for position in STARTING_POSSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at a given position"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def extend(self):
        """Extend the snake by adding a new segment at the end"""
        self.add_segment(self.snake[-1].pos())

    def move(self):
        if not self.moving:
            return
        """Make the snake move after its the object is created"""
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def stop(self):
        """Stop the snake movement"""
        self.moving = False

    def start(self):
        """Start the snake movement"""
        self.moving = True
