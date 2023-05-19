import turtle as t

adde = t.Turtle()

screen = t.Screen()

def Forward():
    """moves in forward direction from where it's at"""
    adde.forward(10)

def Backwards():
    """moves in backward direction from where it's at"""
    adde.backward(10)

def Counter_Clockwise():
    """Draws in Anti-clockwise direction or moves in Anti-clockwise direction"""
    direction = adde.heading() + 10
    adde.setheading(direction)

def Clockwise():
    """Draws in clockwise direction or moves in clockwise direction"""
    direction = adde.heading() - 10
    adde.setheading(direction)

def Home():
    """resets the arrow to center or the origin"""
    adde.clear()
    adde.penup()
    adde.home()
    adde.pendown()

def Sketch():
    """Sketches things you try to sketch"""
    screen.onkey(Forward, key="F")
    screen.onkey(Backwards, key="B")
    screen.onkey(Counter_Clockwise, key="A")
    screen.onkey(Clockwise, key="C")
    screen.onkey(Home, key="H")

screen.listen()
screen.onkey(Sketch, key="S")

screen.exitonclick()
