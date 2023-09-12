from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.a = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 275)
        self.write(f"Scoreboard: {self.a}", align="center", font=("Verdana", 15, "normal"))

    def update_score(self):
        self.clear()
        self.a += 1
        self.write(f"Scoreboard: {self.a}", align="center", font=("Verdana", 15, "normal"))


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.write("Game Over.", align="center", font=("Verdana", 15, "normal"))
