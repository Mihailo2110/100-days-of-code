import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
score = 0

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
data = pandas.read_csv("50_states.csv")

data_state_list = data.state.to_list()
correct_guesses = []
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in data_state_list if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_on = False
        break
    elif answer_state in data_state_list:
        correct_guesses.append(answer_state)
        position = (int(data.x[data.state == answer_state]), int(data.y[data.state == answer_state]))
        text = turtle.Turtle()
        text.penup()
        text.color("black")
        text.hideturtle()
        text.goto(position)
        text.write(f"{answer_state}", align=ALIGNMENT, font=FONT)
        screen.update()
        score += 1
        print(correct_guesses)
    else:
        game_on = True
    if score == 50:
        game_on = False
        print("Well done!")






