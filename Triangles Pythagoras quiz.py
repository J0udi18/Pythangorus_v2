import random

score = 0


# displays instructions
def instructions():
    print("Instructions")
    print('''
- All the questions area about Pythagoras
- answer all of the questions  if you dont know guess
- answer should be without a decimal
       ''')
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


do_you_know_what_is_the_quiz_about = yes_no("do you know what is the quiz about? ")

if do_you_know_what_is_the_quiz_about == "no":
    instructions()

print("let start")

print("Welcome to the Pythagoras Quiz!")
print("You will be given a questions about right triangle and you need to find "
      "the length of the missing side.")

while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = round((a ** 2 + b ** 2) ** 0.5)

    sides = [a, b, c]
    random.shuffle(sides)

    print(f" {a} cm {b} cm ?")

    answer = input("What is the length of the missing side? (Enter 'q' to quit) ")

    if answer.lower() == "q":
        print(f"Your final score is {score}")
        break

    try:
        answer = float(answer)
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
