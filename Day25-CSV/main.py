import turtle
import pandas


def draw_state_name_on_map(coords, user_guess):
    state_writer.goto(coords)
    state_writer.write(user_guess)


def check_state(user_guess):
    if user_guess in all_states:
        state = state_data[state_data.state == user_guess]
        return float(state.x), float(state.y)


def output_missed_states():
    missed_states = [state for state in all_states if state not in correct_guesses]
    pandas.DataFrame(missed_states).to_csv("statesResources/missed_states.csv")


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("U.S. States Game")
    image = "statesResources/blank_states_img.gif"
    screen.addshape(image)

    turtle.shape(image)
    state_writer = turtle.Turtle()
    state_writer.hideturtle()
    state_writer.penup()

    game_is_on = True
    score = 0
    correct_guesses = []

    state_data = pandas.read_csv("statesResources/50_states.csv")
    all_states = state_data.state.to_list()

    while game_is_on:
        user_guess = screen.textinput(title="Guess", prompt="Enter a U.S. state name:").title()

        if user_guess == "Exit":
            output_missed_states()
            break

        coords = check_state(user_guess=user_guess)
        if coords is not None:
            draw_state_name_on_map(coords, user_guess)
            score += 1
            correct_guesses.append(user_guess)

        if score == 50:
            game_is_on = False

    turtle.mainloop()
