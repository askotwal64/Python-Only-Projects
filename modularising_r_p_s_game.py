import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {SCISSORS: "✂️", ROCK: "🪨", PAPER: "📃"}
choices = tuple(emojis.keys())


def user_choice():
    while True:
        user_input = input("Select any one from rock or paper or scissors r/p/s: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid Choice")

def printing_choices(user_input, computer_selection):
    print(f"Your choice: {emojis[user_input]}")
    print(f"Computer choice: {emojis[computer_selection]}")

def game_rules(user_input, computer_selection):
    if computer_selection == user_input:
        print(f"Oh! both got the same choice, Try again!")

    elif (  (computer_selection == SCISSORS and user_input == ROCK) or
            (computer_selection == ROCK and user_input == PAPER) or 
            (computer_selection == PAPER and user_input == SCISSORS)   ):
        print(f"You won")

    else:
        print(f"You lost")

def play_game():
    while True:
        user_input = user_choice()

        computer_selection = random.choice(choices)

        printing_choices(user_input, computer_selection)

        game_rules(user_input, computer_selection)

        to_continue = input("Want to continue y/n: ").lower()
        if to_continue == "y":
            continue
        elif to_continue == "n":
            break
        else:
            print("Please enter a valid choice!! (y/n)")
            to_continue = input("Renter y/n: ").lower()
            if to_continue == "n":
                break
            

play_game()
