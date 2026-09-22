import random 

while True:

    choice = input("Enter y to roll a dice or n to stop the game: ").lower()

    if choice == "y":
        # if two dices i.e. die
        # d1 = random.randint(1,6)
        # d2 = random.randint(1,6)
        # print(f"({d1},{d2})")
        print(random.randint(1,6))
        
    elif choice == "n":
        print("Thanks for playing!")
        break
        
    else:
        print("Invalid Choice! try again...")
        

# further enhancements
# modify; so that user can specify how many times  they want to roll dice
# add a feature, how many times a user has rolled a dice during a session
