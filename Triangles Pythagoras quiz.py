import random

score = 0


# displays instructions
def instructions():
    print("Instructions")
    print("\033[2;32;31m Hello \n")
    print("Welcome to the Pythagoras Quiz!")
    print("you will be given question about right triangles, and you need to find"
          "the length of the missing side.")
    print("let's start")
    print("Good luck and have fun!")

    return ""


# Main Routine goes here...
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y" or response == "pythagoras":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


want_instructions = yes_no("Would you like to read/see the instructions? ")

if want_instructions == "yes":
    instructions()


# Questions start here...

while True:
    # Gives numbers...
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = round((a ** 2 + b ** 2) ** 0.5)

    sides = [a, b, c]
    random.shuffle(sides)
    # Ask question
    print(f" {a} cm {b} cm ?")

    answer = input("What is the length of the missing side? (Enter 'q' to quit) ")

    if answer.lower() == "q":
        print(f"Your final score is {score}")
        break
    # check answer
    try:
        answer = int(answer)
        if answer == c:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {c} cm.")
        print("Your score is", score, "out of 10.")

    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

# This code generates random right triangles and prompts the user to find 
# the length of the missing side. It also keeps track of the score and allows
# the user to quit at any time by entering 'q
# I've removed the decimal in the calculation of the hypotenuse by rounding it to
# the nearest whole number.
