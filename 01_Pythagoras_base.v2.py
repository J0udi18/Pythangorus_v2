import random


# Function to check which questions user would like to answer
def question_checker(question):
    valid_responses = ["p", ""]
    while True:
        response = input(question).lower()
        if response in valid_responses:
            return response
        else:
            print("<error> Please enter 'p' to generate a Pythagorean triple or press <enter> for all types of "
                  "questions.")


# Number checker to ensure correct user input
def num_check(question, error, num_type, exit_code="xxx", low=None, high=None):
    while True:
        try:
            response = input(question)
            if response == exit_code:
                return response
            else:
                response = num_type(response)

            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
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


# Function to check for yes or no responses
def yes_no(question):
    valid_responses = ["yes", "no", "y", "n"]
    while True:
        response = input(question).lower()
        if response in valid_responses:
            return response
        else:
            print("<error> Please say yes or no")
            print()


# Function to generate questions randomly
def generate_question(points_val):
    while True:
        n = random.randint(1, 10)
        a = 2 * n + 1
        b = n * (2 * n + 1) + n
        response = num_check("In a Pythagorean triple, if n = {}, what is the length of the hypotenuse "
                             "if the other two sides are {} and {}? ".format(n, a, b),
                             "<error> Please enter a number", float)

        if response == "xxx":
            print("You quit")
            return "quit"

        if abs(response - (a**2 + b**2) ** 0.5) <= 0.001:
            print("\033[1;32;40m \n")
            statement_generator("You got it right! +{} points".format(points_val), "*", "~")
            return "correct"
        else:
            print("\033[1;31;40m \n")
            statement_generator("You got it wrong. -10 points", "|", "-")
            return "incorrect"


# Function to print instructions
def instructions():
    print("\033[1;33;40m \n")
    statement_generator("Instructions", "|", "-")
    print("Welcome to the Pythagoras Quiz!")
    print("In this quiz, you will be shown the lengths of two sides of a right triangle.")
    print("Your task is to determine the length of the hypotenuse.")
    print("Each correct answer will earn you a certain number of points.")
    print("Each incorrect answer will deduct 10 points.")
    print("Let's get started!")


# Function to generate a formatted statement
def statement_generator(statement, deco_line, deco_char):
    print()
    print(deco_line * len(statement))
    print(statement)
    print(deco_char * len(statement))
    print()


# Main code
instructions()

points = 0
another_question = "yes"

while another_question == "yes":
    question_type = question_checker("Enter 'p' to generate a Pythagorean triple or press <enter> for all types of "
                                     "questions: ")
    if question_type == "p" or question_type == "":
        result = generate_question(10)
        print("\033[1;32;40m \n")
        if result == "correct":
            points += 10
        else:
            points -= 10

    another_question = yes_no("Do you want another question? (yes/no): ")

print("Your final score is:", points)
print("\033[1;35;40m \n")
print("Thank you for doing the Pythagoras Quiz!")