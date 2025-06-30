import turtle
import pandas as pd

screen = turtle.Screen()
t = turtle.Turtle()
screen.title("U.S. State Game")
image = "blank_states_img(1).gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
found_state = []
score = 0

data = pd.read_csv("50_states.csv")


while game_is_on:
    user_answer = screen.textinput(
        title=f"{score}/{len(data.state)} Guess the state",
        prompt="What is the next State?",
    )
    if user_answer.title() == "Exit":
        break
    row = data[data.state == user_answer.title()]

    if user_answer.title() not in found_state and not row.empty:
        t.penup()
        t.hideturtle()
        x = int(row.x.iloc[0])
        y = int(row.y.iloc[0])
        state_name = row.state.iloc[0]

        t.goto(x, y)
        t.write(f"{state_name}", align="center")

        found_state.append(state_name)
        score += 1
    else:
        pass

    if len(found_state) == len(data.state):
        game_is_on = False


states_to_learn = {
    "states": [state for state in data.state if state not in found_state]
}
pd.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
