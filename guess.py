import random
from prettytable import PrettyTable
import easygui

# Generating a random number between 1 and 102
num = random.randint(1, 102)

# Setting up the table
table = PrettyTable()
table.field_names = ["Guess", "Result"]

# Main game loop
while True:
    # Getting user input
    guess = easygui.integerbox("Guess a number between 1 and 102:", lowerbound=1, upperbound=102)

    # Checking if the guess is within the valid range
    if guess is None:
        # User clicked cancel, exit the game
        easygui.msgbox("Game cancelled.")
        break
    elif guess < 1 or guess > 102:
        easygui.msgbox("Invalid input! Please enter a number between 1 and 102.")
        continue

    # Checking if the guess is correct
    if guess == num:
        table.add_row([guess, "Yeah! You won!"])
        easygui.msgbox(str(table))
        break
    elif guess < num:
        table.add_row([guess, "Too low!"])
        easygui.msgbox(str(table))
    else:
        table.add_row([guess, "Too high!"])
        easygui.msgbox(str(table))
