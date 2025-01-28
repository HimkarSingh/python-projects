from turtle import Turtle,Screen
from paddle import Paddle,dash_line
from ball import Ball
from scoreboard import Scoreboard
import time

t = Turtle()
s = Screen()
s.setup(800,600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")
s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")


dash_line() # Middle Screen Line

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor()> 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect a paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

s.exitonclick()