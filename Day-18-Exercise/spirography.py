import turtle as t
import random

timmyTur = t.Turtle()
t.colormode(255)

def random_color():
    """Returns a random color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

random_walks = [0, 90, 180, 270]
timmyTur.pensize(1)
timmyTur.speed(0)

def Draw_spirography(num_of_gabs):
    """Returns a spirograph shape"""
    for i in range(int(360 / num_of_gabs) ):
        timmyTur.color(random_color())
        timmyTur.circle(100)
        timmyTur.setheading(timmyTur.heading() + num_of_gabs)
Draw_spirography(5)

screen = t.Screen()
screen.exitonclick()