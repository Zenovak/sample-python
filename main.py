from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

game_is_on = True
title = "The Pong"

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title(title)
screen.tracer(0)

# Left side paddle
l_paddle = Paddle("left")

# Right side paddle
r_paddle = Paddle("right")

ball = Ball()


screen.listen()
# Left side paddle controls
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)
# Right side paddle controls
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)


while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    ball.collisions()
    print(ball.position)

screen.exitonclick()
