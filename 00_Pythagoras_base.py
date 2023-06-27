import random
import time
from termcolor import colored


# Functions go here

# Function will print instructions when called
def instructions():
    print(colored("\nInstructions", "yellow"))
    print("Welcome to the Pythagoras Quiz!")
    print("In this quiz, you will be shown the lengths of two sides of a right triangle.")
    print("Your task is to determine the length of the hypotenuse.")
    print("Each correct answer will earn you a certain number of points.")
    print("Each incorrect answer will deduct 10 points.")
    print("Let's get started!")
    print("Good Luck!\n")


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, exit_code=None, low=None, high=None):
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
            print("<error> Please say yes/no")
            print()


# Definition that generates questions randomly and will call this function
# Checks which questions user would like to choose
def question_checker(question):
    # 'p' is for pythagorean triple questions
    # 'm' is for multiplication questions
    # 's' is for square number questions
    # set list of the type of questions
    valid_responses = ["p", "m", "s", ""]
    while True:
        response = input(question).lower()
        if response in valid_responses:
            return response
        else:
            print("<error> Please enter 'p' for Pythagorean triple questions, 'm' for Multiplication Challenge "
                  "questions, 's' for Square Numbers Challenge questions, or press <enter> for all types of questions.")

        # If user quits
        if response == "xxx":
            print("You quit")
            result = "quit"
            return result


def generate_question(question_type):
    if question_type == "p":
        # Generate a Pythagorean triple question
        n = random.randint(1, 10)
        a = 2 * n + 1
        b = n * (2 * n + 1) + n
        response = num_check(f"In a Pythagorean triple, if n = {n}, what is the length of the hypotenuse if the other "
                             f"two sides are {a} and {b}? ",
                             "<error> Please enter a valid number.", int)
        correct_answer = a ** 2 + b ** 2
    elif question_type == "m":
        # Generate a Multiplication Challenge question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        response = num_check(f"What is the product of {num1} and {num2}? ",
                             "<error> Please enter a valid number.", int)
        correct_answer = num1 * num2
    elif question_type == "s":
        # Generate a Square Numbers Challenge question
        num = random.randint(1, 10)
        response = num_check(f"What is the square of {num}? ",
                             "<error> Please enter a valid number.", int)
        correct_answer = num ** 2

    return response, correct_answer


# Main code goes here

print(colored("Welcome to the Pythagoras Quiz!", "green"))
print()
print(colored)

# Show instructions
instructions()

# Ask if user wants to play
want_to_do_quiz = yes_no("Do you want to do the quiz? (yes/no): ")
if want_to_do_quiz == "no":
    print("Okay, maybe next time!")
    exit()

# Ask which type of questions the user wants
question_type = question_checker("What type of questions would you like to choose? (p/m/s): ")

# Set the number of questions
num_questions = num_check("How many questions would you like to answer? (1-10): ",
                          "<error> Please enter a number between 1 and 10.", int, low=1, high=10)

# Set the point values
correct_points = 10
incorrect_points = -10

# Initialize variables
total_score = 0
correct_count = 0
incorrect_count = 0

# Generate and ask questions
for i in range(num_questions):
    print(f"\nQuestion {i + 1}:")
    response, correct_answer = generate_question(question_type)

    if response == "quit":
        break

    # Check if the response is correct
    if response == correct_answer:
        print("Correct!")
        total_score += correct_points
        correct_count += 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer}.")
        total_score += incorrect_points
        incorrect_count += 1

    time.sleep(1)  # Add a delay before showing the next question

# Print final score and statistics
print("\nQuiz Finished!")
print(f"Total Score: {total_score}")
print(f"Number of Correct Answers: {correct_count}")
print(f"Number of Incorrect Answers: {incorrect_count}")
