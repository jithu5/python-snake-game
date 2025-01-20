from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-80,260)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="left", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", move=False, align="center", font=('Arial', 24, 'normal'))
        self.hideturtle()