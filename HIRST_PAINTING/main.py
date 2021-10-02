import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# angles = 360
# sides = 3
#
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]

#
# for _ in range(5):
#     tim.pencolor(random.choice(colors))
#     for turn in range(sides):
#         tim.forward(100)
#         tim.right(angles/sides)
#
#     sides += 1
color = ()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# i = 0
# rand_num = [1, 2, 3]
# while i < 50:
#     tim.speed(10)
#     tim.pensize(15)
#     tim.pencolor(random_color())
#     tim.forward(50)
#     tim.right(random.choice(rand_num) * 90)
#     i += 1


for _ in range(72):
    tim.pencolor(random_color())
    tim.speed(0)
    tim.circle(100, 360)
    tim.left(5)




screen = Screen()
screen.exitonclick()
