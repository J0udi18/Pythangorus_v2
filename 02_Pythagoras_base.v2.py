import random
from termcolor import termcolor
termcolor


# Function will print instructions when called
def instructions():
    print("\033[1;33;40m \n")
    statement_generator("Instructions", "|", "-")
    print("Welcome to the Pythagoras Quiz!")
    print("In this quiz, you will be shown the lengths of two sides of a right triangle.")
    print("Your task is to determine the length of the hypotenuse.")
    print("Each correct answer will earn you a certain number of points.")
    print("Each incorrect answer will deduct 10 points.")
    print("Let's get started!")


# Checks for yes or no responses
def yes_no(question):
    valid_responses = ["yes", "no", "y", "n"]
    while True:
        response = input(question).lower()
        if response in valid_responses:
            return response
        else:
            print("<error> Please say yes or no")
            print()


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, exit_code="xxx", low=None, high=None):
    while True:
        try:
            response = input(question)
            if response == exit_code:
                return response
            else:
                response = num_type(response)

            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response >= low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


# Checks which questions user would like to answer
def question_checker(question):
    valid_responses = ["p", "m", "s", ""]
    while True:
        response = input(question).lower()
        if response in valid_responses:
            return response
        else:
            print("<error> Please enter 'p' for Pythagorean triple questions, 'm' for Multiplication Challenge "
                  "questions, 's' for Square Numbers Challenge questions, or press <enter> for all types of questions.")


# Generate a Pythagorean triple question
def generate_pythagorean_question():
    n = random.randint(1, 10)
    a = 2 * n + 1
    b = n * (2 * n + 1) + n
    response = num_check(f"In a Pythagorean triple, if n = {n}, what is the length of the hypotenuse if the other two "
                         f"sides are {a} and {b}? ",
                         "<error> Please enter a valid number.", int)
    if response == a ** 2 + b ** 2:
        print("\033[1;32;40m \n")
        print("You got it right! +10 points")
        return 10
    else:
        print("\033[1;31;40m \n")
        print("You got it wrong. -10 points")
        return -10


# Generate a Multiplication Challenge question
def generate_multiplication_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    response = num_check(f"What is the product of {num1} and {num2}? ",
                         "<error> Please enter a valid number.", int)
    if response == num1 * num2:
        print("\033[1;32;40m \n")
        print("You got it right! +5 points")
        return 5
    else:
        print("\033[1;31;40m \n")
        print("You got it wrong. -5 points")
        return -5


# Generate a Square Numbers Challenge question
def generate_square_number_question():
    num = random.randint(1, 10)
    response = yes_no(f"Is {num} a perfect square? (yes/no) ")
    if (response == "yes" and int(num ** 0.5) ** 2 == num) or (response == "no" and int(num ** 0.5) ** 2 != num):
        print("\033[1;32;40m \n")
        print("You got it right! +5 points")
        return 5
    else:
        print("\033[1;31;40m \n")
        print("You got it wrong. -5 points")
        return -5


# Function to generate a formatted statement
def statement_generator(statement, deco_line, deco_char):
    print()
    print(deco_line * len(statement))
    print(statement)
    print(deco_char * len(statement))
    print()


# Function to generate a formatted colored question
def colored_question(question):
    print("\033[1;34m" + question + "\033[0m")


# Main code
colored = "\033[1;33;40m \n"
statement_generator("Welcome to Joudi's Math Quiz", "!", "=")

points = 0
another_question = "yes"

while another_question == "yes":
    if yes_no("Would you like to read/see the instructions? ") == "yes":
        instructions()

    num_of_questions = num_check("How many questions would you like to answer? ",
                                 "<error> please enter a valid number.", int, low=1)

    question_type = question_checker("Enter 'p' for Pythagorean triple questions, 'm' for Multiplication Challenge "
                                     "questions, 's' for Square Numbers Challenge questions, or press <enter> for all"
                                     " types of questions: ")

    if question_type == "p":
        points += generate_pythagorean_question()
    elif question_type == "m":
        points += generate_multiplication_question()
    elif question_type == "s":
        points += generate_square_number_question()
    else:
        points += generate_pythagorean_question()
        points += generate_multiplication_question()
        points += generate_square_number_question()

    another_question = yes_no("Would you like another question? ")
    print()

print(f"Your total score is {points} points")
print("\033[1;35;40m \n")
print("Thank you for doing the quiz!")
