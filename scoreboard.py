from turtle import Turtle
score = 0


class ScoreBoard(Turtle):
    def __init__(self):
        global score
        super().__init__()
        self.goto(0, 250)
        self.pendown()
        self.pencolor("white")
        self.hideturtle()
        self.clear()
        self.write_score()
        self.scoring()

    def write_score(self):
        self.write(f"Score: {score}", False, "center", ("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 16, "normal"))

    def scoring(self):
        global score
        score += 10
