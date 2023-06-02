import random
import math


# checks if user knows algebra or
# have an idea what is the quiz is going to be about
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


# display instructions
def instructions():
    print("Instructions")
    print('''
- Expand
- Factor
- simplify
    ''')
    return""


