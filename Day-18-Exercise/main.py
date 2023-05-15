import random
import turtle as t

timmyTur = t.Turtle(shape="turtle", visible=False)

"""I extracted these below rgb colors from the pic in the file using colorgram"""

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60),
              (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]


timmyTur.pensize(20)
timmyTur.pencolor("white")
timmyTur.speed(0)

screen = t.Screen()
screen.colormode(255)

timmyTur.setheading(225)
timmyTur.fd(300)
timmyTur.setheading(0)
timmyTur.penup()
#timmyTur.hideturtle()

number_of_dots = 100


def painting(dots):
    """returns a full dot painting wall, based on the number of dots passed"""
    for dot_count in range(1, dots + 1):
        #screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
        timmyTur.dot(20, random.choice(color_list))
        timmyTur.fd(50)
        if dot_count % 10 == 0:
            timmyTur.setheading(90)
            timmyTur.fd(50)
            timmyTur.setheading(180)
            timmyTur.fd(500)
            timmyTur.setheading(0)
painting(number_of_dots)


screen = t.Screen()
screen.exitonclick()