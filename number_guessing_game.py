# while True:


# generate any random no by comp
import random
num = random.randint(1,99)

while True:
    # ask user to guess no, if any non-integer is fed ask user to renter 
    try:
        user_guess = int(input("Enter any number between 0 and 100 to guess: "))

        if user_guess > num:
            print("Too high! Try Again...")
    
        elif user_guess < num:
            print("Too low! Try Again..")

        elif (user_guess == num):
            print("yeyy! you won!!")
            break
    
    except ValueError:
        print("Not an integer, Please enter a valid integer....")


