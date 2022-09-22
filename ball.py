from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(60)

    def move(self):
        """Moves the ball and updates its position"""
        self.forward(3)
        self.track()

    def track(self):
        """Updates the ball position into self.position attribute"""
        self.position = self.pos()

    def collisions(self):
        """Detects collisions with the upper and lower walls,
        and calls the bounce function"""
        if self.position[1] > 280 or self.position[1] < -280:
            self.bounce()

    def bounce(self):
        """Bounces the ball at the opposite angle in which it came from. Based on True plane"""
        self.setheading(360 - self.heading())

