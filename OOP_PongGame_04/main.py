from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

WIDTH_SCR  = 800
HEIGHT_SCR = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH_SCR, height=HEIGHT_SCR)
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball     = Ball()

screen.listen()
screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(key="z",fun=l_paddle.go_up)
screen.onkey(key="s",fun=l_paddle.go_down)

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detec collision with wall and bounce
    if (ball.ycor()>280  or ball.ycor()<-280):
        ball.bounce_wall()

    # Detect collision with right paddle and bounce
    if (ball.distance(r_paddle) < 50 and ball.xcor()>330) or (ball.distance(l_paddle) < 50 and ball.xcor()<-330):
        ball.bounce_paddle()
    
    # Detect collision with both paddle and wall , then bounce
    if (ball.ycor()>280  or ball.ycor()<-280) and ((ball.distance(r_paddle) < 50 and ball.xcor()>320) or (ball.distance(l_paddle) < 50 and ball.xcor()<-320)): 
        ball.bounce_both()

    # Detect if the right paddle misses the ball
    if (ball.xcor()>400): 
        ball.reset_position()        

    if (ball.xcor()<-400):
        ball.reset_position()
        
screen.exitonclick()
