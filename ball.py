from turtle import Turtle
from random import randint, choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color("white")
        self.speed(1)
        self.penup()
        self.goto(0, 0)
        if choice([1, 2]) == 1:
            self.right_initial_angle()
        else:
            self.left_initial_angle()

    def right_initial_angle(self):
        self.setheading(randint(-60, 60))

    def left_initial_angle(self):
        self.setheading(randint(120, 240))

    def bounce_angle(self):
        if self.heading() <= 90 and self.heading() >= 0:
            self.setheading(360 - self.heading() + randint(0, 5))
        elif self.heading() <= 180 and self.heading() >= 90:
            self.setheading(360 - self.heading() + randint(-5, 0))
        elif self.heading() <= 270 and self.heading() >= 180:
            self.setheading(360 - self.heading() + randint(0, 5))
        elif self.heading() <= 360 and self.heading() >= 270:
            self.setheading(360 - self.heading() + randint(-5, 0))

    def paddle_bounce(self):
        self.setheading(180 - self.heading() + randint(-20, 20))

    def move(self):
        self.forward(3)

    def round_over(self, right_won):
        self.goto(0, 0)
        if right_won:
            self.left_initial_angle()
        else:
            self.right_initial_angle()
