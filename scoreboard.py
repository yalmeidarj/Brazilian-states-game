from turtle import Turtle
style = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.ht()
        self.penup()
        self.goto(-180.0, -31.0)
        self.color("black")
        self.write(arg=f"Score: {self.points}/27  ", align='center', font=style)

    def update_score(self):
        self.clear()
        self.points += 1
        self.write(arg=f"Score: {self.points}/27  ", align='center', font=style)

