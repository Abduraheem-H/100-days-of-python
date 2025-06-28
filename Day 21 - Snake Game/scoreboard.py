from turtle import Turtle

ALIGN = "center"
FONT = ("Cursive", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as saved_score:
            self.high_score = int(saved_score.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.update()

    def update(self):
        """Update the scoreboard with the current score"""
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            move=False,
            align=ALIGN,
            font=FONT,
        )

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard"""
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as saved_score:
                self.high_score = self.score
                saved_score.write(f"{self.high_score}")

        self.score = 0
        self.update()
