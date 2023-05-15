import turtle as t
import random

timmyTur = t.Turtle()
t.colormode(255)

def random_color():
    """Returns random colors"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

random_walks = [0, 90, 180, 270]
timmyTur.pensize(5)
timmyTur.speed(10)

def Draw_shape(num_sides):
    """Returns a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon"""
    angle = 360 / num_sides
    for num in range(num_sides):
        timmyTur.forward(100)
        timmyTur.right(angle)
for num_sides in range(3, 11):
    timmyTur.color(random_color())
    Draw_shape(num_sides)

screen = t.Screen()
screen.exitonclick()