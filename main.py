import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
guessed_states = []
screen.addshape(image)
score = 0
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
playing = True

while playing:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    print(answer_state)

    data = pd.read_csv('50_states.csv')
    response_answer = data[data["state"] == answer_state]
    if len(response_answer) == 1:
        if answer_state in guessed_states:
            print("you already guessed this")
        else:
            guessed_states.append(answer_state)
            score += 1
            x_cor = response_answer['x'].item()
            y_cor = response_answer['y'].item()

            writer.goto(x_cor,y_cor)
            writer.write(answer_state)


turtle.mainloop()

