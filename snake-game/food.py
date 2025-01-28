from turtle import Turtle
import random

colors = ["blue","red","orange","magenta","green","yellow"]
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.change_food_color()
        self.speed("fastest")
        self.refresh()

    def change_food_color(self):
        self.food_color = random.choice(colors)
        self.color(self.food_color)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.change_food_color()
        self.goto(random_x, random_y)