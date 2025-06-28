from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.tracer(0)

screen.setup(width=800, height=600)
canvas = screen.getcanvas()
window = canvas.winfo_toplevel()
window.geometry("+300+25")
screen.bgcolor("black")
screen.title("Pong")

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_right()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(True)

    if (
        ball.distance(paddle_r) < 50
        and ball.xcor() > 320
        or ball.distance(paddle_l) < 50
        and ball.xcor() < -320
    ):
        ball.bounce()

    elif ball.xcor() > 380:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce()
        scoreboard.left_point()

    elif ball.xcor() < -380:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce()
        scoreboard.right_point()

    # Here you would typically update the game state, e.g., move the ball, check for collisions, etc.


screen.mainloop()
