from turtle import Turtle
import random
class Food(Turtle):
    colors = ["red", "blue", "yellow", "green", "orange", "white", "purple"]
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(self.colors))
        self.speed("fastest")
        self.create_food()
    def  create_food(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)