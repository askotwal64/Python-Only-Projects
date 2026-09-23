
import random

choices = ('s','p','r') 
emojis = {'s': "✂️", 'r': "🪨", 'p': "📃"}

while True:

    user_input = input("Select any one from rock or paper or scissors r/p/s: ").lower()
    if user_input not in choices:
        print("Invalid Choice")
        continue

    computer_selection =  random.choice(choices)

    print(f"Your choice: {emojis[user_input]}")
    print(f"Computer choice: {emojis[computer_selection]}")


    if computer_selection == user_input:
        print(f"Oh! both got the same choice, Try again!")

    elif (computer_selection == 's' and user_input == 'r') or (computer_selection == 'r' and user_input == 'p') or (computer_selection == 'p' and user_input == 's'):
        print(f"You won")

    else:
        print(f"You lost")

    to_continue = input("Want to continue y/n: ").lower()
    if to_continue == 'n':
        break
