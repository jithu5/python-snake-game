from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_high_score()
        self.penup()
        self.hideturtle()
        self.goto(-160,260)
        self.color("white")
        self.update_score()

    def read_high_score(self):
        with open("previous_high_scores.txt","r") as file:
            self.high_score = int(file.read()) or 0

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} | High Score : {self.high_score}", move=False, align="left", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.save_high_score()
        self.update_score()
    
    def save_high_score(self):
        with open("previous_high_scores.txt","w") as file:
            file.write(str(self.high_score))