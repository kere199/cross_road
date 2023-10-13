from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color = "black"
        self.hideturtle()
        self.penup()
        self.goto(-200,240)


    def print_level(self):
        self.clear()
        self.write(f"level:{self.level}", align= 'center' , font= FONT)


    def increase_level(self):
        self.level += 1
        self.print_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align= 'center' , font= FONT)