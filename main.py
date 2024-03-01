from turtle import Screen
from paddle import Peddle
from pongball import Pong_ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game New")
screen.tracer(0)

r_peddle = Peddle((370, 0))
l_peddle = Peddle((-370, 0))

pong_ball = Pong_ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_peddle.go_up, "Up")
screen.onkey(r_peddle.go_down, "Down")
screen.onkey(l_peddle.go_up, "w")
screen.onkey(l_peddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    # Detect the collision of walls
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    # Detect collision with peddle
    if pong_ball.distance(r_peddle) < 50 and pong_ball.xcor() > 340 or pong_ball.distance(l_peddle) < 50 and \
            pong_ball.xcor() < -340:
        pong_ball.bounce_x()

    # Detect when r peddle misses
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.l_point()

    # Detect when r peddle misses
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
