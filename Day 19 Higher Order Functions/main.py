from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(500, 400)

start = False

user_bet = screen.textinput(
    prompt="Which turtle will win? Enter a color", title="Make your guess"
)
colors = ["red", "yellow", "green", "blue", "purple", "orange"]
turtles = []
y_cor = -100
for color in colors:
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(color)
    my_turtle.penup()
    my_turtle.goto(x=-230, y=y_cor)
    turtles.append(my_turtle)
    y_cor += 40
if user_bet:
    start = True

while start:
    for turtle in turtles:
        if turtle.xcor() > 230:
            start = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
