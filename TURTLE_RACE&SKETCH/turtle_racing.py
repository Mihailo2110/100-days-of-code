import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Whick turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = -150
all_turtles = []
for color in colors:

    new_turtle = Turtle(shape="turtle")
    new_turtle.color([color])
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    y += 60

if user_bet:
    is_race_on = True

while is_race_on:
    for new_turtle in all_turtles:
        if new_turtle.xcor() > 230:
            is_race_on = False
            winning_color = new_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")

            else:
                print(f"You've lost! The {winning_color} turtle is winner!")

        random_distance = random.randint(0, 10)
        new_turtle.forward(random_distance)


screen.exitonclick()