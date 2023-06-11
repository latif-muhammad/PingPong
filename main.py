from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)


r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
score = Scoreboard()

# Key Bindings
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()

in_game = True
while in_game:
    screen.update()
    ball.move()
#     Collision
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        score.l_scored()
        if score.endGame():
            in_game = False
            screen.update()

    if ball.xcor() < -380:
        ball.reset()
        score.r_scored()
        if score.endGame():
            in_game = False
            screen.update()
        print("out")

screen.exitonclick()
