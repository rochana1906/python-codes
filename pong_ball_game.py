ball.py
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move =10
        self.y_move =10


    def move(self):
        new_x= self.xcor() + self.x_move
        new_y = self.xcor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -10


    def bounce_x(self):
        self.x_move *= -10

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

paddle.py
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


scoreboard.py
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()


main.py
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball= Ball()
scoreboard= Scoreboard()

screen=Screen()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"W")
screen.onkey(l_paddle.go_down,"S")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()

