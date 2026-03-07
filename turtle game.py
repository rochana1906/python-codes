import turtle
import random

tim = turtle.Turtle()

colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","wheat","SlateGray","SeaGreen"]
directions = [0, 90, 180, 270]

tim.pensize(10)
tim.speed("fast")

for _ in range(200):
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colours))
    tim.forward(30)

screen = turtle.Screen()
screen.exitonclick()
