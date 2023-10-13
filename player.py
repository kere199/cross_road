from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
     super().__init__()
     self.penup()
     self.goto(STARTING_POSITION)
     self.shape("turtle")
     self.color("black")
     self.setheading(90)


    def move_up(self):
       self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def return_back(self):
       self.goto(STARTING_POSITION)


