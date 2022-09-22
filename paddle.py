from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, which_side):
        """Set's the side of the paddle. 'left' or 'right'"""
        super().__init__()

        # creating the paddle
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.color("white")
        self.penup()

        if which_side == "left":
            side = -1
        elif which_side == "right":
            side = 1
        self.setx(350*side)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

    def object_collision(self, object):
        """Detects collision with said object"""
        if object
