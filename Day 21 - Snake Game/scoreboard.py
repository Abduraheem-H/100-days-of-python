from turtle import Turtle

ALIGN = "center"
FONT = ("Cursive", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.update()

    def update(self):
        """Update the scoreboard with the current score"""
        self.clear()
        self.write(
            f"Score: {self.score}",
            move=False,
            align=ALIGN,
            font=FONT,
        )

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard"""
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(
            f"GAME OVER",
            move=False,
            align=ALIGN,
            font=FONT,
        )
