from turtle import Screen, Turtle
from PONG_GAME.paddle import Paddle
from PONG_GAME.ball import Ball
from PONG_GAME.scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
score_1 = Scoreboard((300, -250))
score_2 = Scoreboard((-300, -250))

screen.listen()
screen.onkeypress(paddle_1.go_up, "Up")
screen.onkeypress(paddle_1.go_down, "Down")
screen.onkeypress(paddle_2.go_up, "w")
screen.onkeypress(paddle_2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    elif ball.distance(paddle_1) > 50 and ball.xcor() > 380:
        score_2.increase_score()
        ball.home()
        ball.move_speed = 0.1
        ball.bounce_x()
    elif ball.distance(paddle_2) > 50 and ball.xcor() < -380:
        score_1.increase_score()
        ball.home()
        ball.move_speed = 0.1
        ball.bounce_x()



screen.exitonclick()