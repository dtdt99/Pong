from paddle import Paddle
from turtle import Turtle, Screen
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((450,-60))
l_paddle = Paddle((-450,-60))
ball = Ball()
scoreboard = Scoreboard()







screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(0.01)
    

    if ball.ycor() > 410 or ball.ycor() < -410:
        ball.bounce_y()
    
    for parts in r_paddle.paddle_parts:
        if ball.distance(parts) < 40 and ball.xcor() <= 445:
            ball.x_speed *= 1.05
            ball.bounce_x()
            
    
    for parts in l_paddle.paddle_parts:
        if ball.distance(parts) < 40 and ball.xcor() >= -445:
            ball.x_speed *= 1.05
            ball.bounce_x()
        
    if ball.xcor() > 450:
        scoreboard.l_scored()
        ball.reset()
    
    if ball.xcor() < -450:
        scoreboard.r_scored()
        ball.reset()
    screen.update()
        
    
    
    

screen.exitonclick()

