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
timmyTur.pensize(10)
timmyTur.speed(10)

def random_walk():
    """Generates a random walk"""
    for i in range(200):
        timmyTur.color(random_color())
        timmyTur.forward(30)
        timmyTur.setheading(random.choice(random_walks))

random_walk()

screen = t.Screen()
screen.exitonclick()