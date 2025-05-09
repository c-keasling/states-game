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
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
data = pd.read_csv('50_states.csv')
while playing:

    print(answer_state)


    response_answer = data[data["state"].str.lower() == answer_state.lower()]
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
            answer_state = screen.textinput(title="Guess the State", prompt=f"Current score {score}.What's "
                                                                            f"another state's name?")
    else:
        playing = False
        answer_state = screen.textinput(title="Guess the State", prompt=f"Sorry {answer_state} is "
                                                                        f"not a state you lose")
        turtle.exitonclick()
    if len(guessed_states) == 50:
        answer_state = screen.textinput(title="Guess the State", prompt=f"You Guessed them all right")
        playing=False
        turtle.exitonclick()


turtle.mainloop()

