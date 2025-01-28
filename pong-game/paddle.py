from turtle import Turtle
t = Turtle()
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.setposition(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

def dash_line():
    t.color("white")
    t.penup()
    t.hideturtle()
    t.goto(0, 300)
    t.setheading(270)
    for _ in range(15):
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(20)
    t.hideturtle()