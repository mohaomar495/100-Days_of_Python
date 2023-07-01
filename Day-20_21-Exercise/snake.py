from turtle import Turtle

STARTING_POSITION = [(0 , 0), (-25, 0), (-45, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)
    def extend_tail(self):
        self.add_segment(self.segments[-1].position())

    def mave(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_pos_x = self.segments[i - 1].xcor()
            new_pos_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_pos_x, new_pos_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)