import random
import time


# Functions go here

# Checks which questions user would like to answer
def question_checker(question):
    valid = False
    while not valid:

        response = input(question).lower()
        # set list  of the type of questions
        ques_type_list = ["p", ""]

        # Checks how long word is
        if response not in ques_type_list:
            print("<error> please enter 'p' to generate a Pythagorean triple\n"
                  "OR press <enter> for all types of questions")
            print()
            continue
        else:
            return response


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, exit_code="xxx", low=None, high=None):
    valid = False
    while not valid:
        try:
            # Checks if user inputs exit code
            response = input(question)
            if response == exit_code:
                return response
            else:
                response = num_type(response)

            # Checks if they inputted correct number
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


# Checks for yes or no responses
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes or no")
            print()


# Definition that generates questions randomly and will call this function
def question(points_val):
    valid = False
    while not valid:
        # Generate random integer for n
        n = random.randint(1, 10)

        # Calculate the values of a and b based on n
        a = 2 * n + 1
        b = n * (2 * n + 1) + n

        # Get user's answer
        response = num_check("In a Pythagorean triple, if n = {}, what is the length of the hypotenuse "
                             "if the other two sides are {} and {}? ".format(n, a, b),
                             "<error> please enter a number", float)

        # If user quits
        if response == "xxx":
            print("You quit")
            result = "quit"
            return result

        # Check if user's answer is correct
        if abs(response - (a**2 + b**2) ** 0.5) <= 0.001:
            statement_generator("You got it right! +{} points".format(points_val), "*", "~")
            result = "correct"
            print()
            return result
        else:
            print("\033[1;31;40m \n")
            statement_generator("You got it wrong. -10 points", "|", "-")
            result = "incorrect"
            print()
            return result


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
instructions()

points = 0
another_question = "yes"

while another_question == "yes":

    # Select question type
    colored_question("Enter 'p' to generate a Pythagorean triple or press <enter> for all types of questions: ")
    question_type = question_checker("")

     # ask uesr for number of questions
    num_questions_error = "<error> enter an interger"
    num_questions = num_check("How many questions? ", num_questions_error, int, None, 0)

    # Call the question function based on the selected type
    if question_type == "p" or question_type == "":
        result = question(10)
        print("\033[1;32;40m \n")
        if result == "correct":
            points += 10
        else:
            points -= 10

    another_question = yes_no("Do you want to have another question? (yes/no): ")

# Ask user if they want to see there history
show_history = yes_no("would you like to see the quiz history?")

# display history if user syays yes
if show_history == "yes":
    print()
    statement_generator("Quiz History", "-", "*")
    for quiz in question_type:
        print(quiz)


print("Your final score is:", points)
print("\033[1;35;40m \n")
print("Thank you for doing the Pythagoras Quiz!")