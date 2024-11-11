from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=7, stretch_wid=1.2)
        self.color("White")
        self.speed(0)
        self.penup()
        self.setheading(90)
        self.player = player
        self.new_round()

    def new_round(self):
        if self.player == "left":
            self.goto(-370, 0)
        else:
            self.goto(370, 0)

    def go_up(self):
        if self.position()[1] < 215:
            self.goto(self.position()[0], self.position()[1] + 3)

    def go_down(self):
        if self.position()[1] > -215:
            self.goto(self.position()[0], self.position()[1] - 3)

    def collision(self, cords: tuple) -> None:
        if (
            self.position()[0] > 0
            and self.position()[0] - cords[0] < 30
            and abs(self.position()[1] - cords[1]) < 80
        ):
            return True
        if (
            self.position()[0] < 0
            and self.position()[0] - cords[0] > -30
            and abs(self.position()[1] - cords[1]) < 80
        ):
            return True
