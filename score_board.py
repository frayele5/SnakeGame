from turtle import Turtle


def get_high_score():
    file = open("high_score.txt", mode="r")
    content = file.read()
    if content.strip():
        high_score = int(content)
    else:
        high_score = 0
    file.close()
    return high_score


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.up()
        self.goto(-80, 270)
        self.color("white")
        self.hideturtle()
        self.write(arg=f"Score is: {self.score}   High score is: {self.high_score}", font=("Calibri", 16, "bold"))

    def upgrade(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score is: {self.score}   High score is: {self.high_score}", font=("Calibri", 16, "bold"))

    def game_over(self):
        self.goto(-60, 0)
        new_record = ""
        if self.score > self.high_score:
            new_record = f"You have a new record {self.score} !!!!"
            self.set_high_score()

        self.write(arg=f"GAME OVER\n  {new_record} ", font=("Calibri", 16, "bold"))

    def set_high_score(self):
        file = open("high_score.txt", mode="w")
        file.write(str(self.score))
        file.close()
