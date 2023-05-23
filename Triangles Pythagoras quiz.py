import random


# Class for coloured text, used for error generator
# (and other text colouring functions)
class Color_It():

    def __init__(self, red, green, blue, text):
        self.red = red
        self.green = green
        self.blue = blue
        self.text = text

    def get_color_escape(self, red, green, blue):
        return '\033[{};2;{};{};{}m'.format(38, red, green, blue)

    def print_colour(self):
        # the bit at the end resets the colour back to normal
        all_coloured = self.get_color_escape(self.red, self.green,
                                             self.blue) + self.text + '\033[0;0m'
        return all_coloured


score = 0


# displays instructions
def instructions():
    print("Instructions")
    print('''
- All the questions area about Pythagoras
- answer all of the questions  if you don't know guess
- answer should be provided decimal points.
       ''')
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


# Function to generate and run the quiz
def run_quiz():
    print("Welcome to the Pythagoras Quiz!")
    print("you will be given question about right triangles, and you need to find"
          "the length of the missing side.")
    print("let's start")


do_you_know_what_is_the_quiz_about = yes_no("do you know what is the quiz about? ")

if do_you_know_what_is_the_quiz_about == "no":
    instructions()

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
