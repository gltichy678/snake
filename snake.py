from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.head = 0
        self.create_snake()
        self.a = -20

    def create_snake(self):
        for i in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(positions[i])
            self.segments.append(segment)
            self.head = self.segments[0]

    def increase_length(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.increase_length(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def right(self):
        self.segments[0].right(90)

    def left(self):
        self.segments[0].left(90)

    def top(self):
        self.segments[0].left(90)

    def bottom(self):
        self.segments[0].right(90)

    def check_collision(self):
        for i in range(1, len(self.segments) - 1):
            if self.head.pos() == self.segments[i].pos():
                return 1
