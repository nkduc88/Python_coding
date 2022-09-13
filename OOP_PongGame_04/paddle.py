from turtle import Turtle


SHAPE  = "square"
COLOR  = "white"
WIDTH  = 5
LENGTH = 1
UP     = 90
DOWN   = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self,xcor_init,ycor_init):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid= WIDTH, stretch_len= LENGTH)
        self.penup()
        self.goto(xcor_init,ycor_init)

    def go_up(self):
        if self.ycor() + 50 < (600/2):
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(),new_y)

    def go_down(self):
        if self.ycor() - 50 > (-600/2):
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(),new_y)
