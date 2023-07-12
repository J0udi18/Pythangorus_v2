import math
import random
import time


# Functions go here

# Function will print instructions when called
def instructions():
    print("\033[103;33;30m \n")
    statement_generator("Instructions", "|", "-")
    print("Welcome to the Pythagoras Quiz!")
    print("In this quiz, you will be shown the lengths of two sides of a right triangle.")
    print("Your task is to determine the length of the hypotenuse.")
    print("When writing your answer for 'p' please round your answer!!")
    print("Each correct answer will earn you a certain number of points.")
    print("Each incorrect answer will deduct 10 points.")
    print("Let's get started!")
    print("Good Luck!\n")


# Gives statements decoration on sides and top
def statement_generator(statement, side_decoration, top_bottom_decoration):
    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, exit_code="xxx", low=None, high=None):
    valid = False
    while not valid:
        try:
            # Checks if user inputs exit code
            responses = input(question)
            if responses == exit_code:
                return responses
            elif responses == "":
                print("No input detected. Using default value.")
                return 3  # Set a default value here

            responses = num_type(responses)

            # Checks if they inputted correct number
            if low is not None and high is not None:
                if low < responses < high:
                    return responses
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if responses > low:
                    return responses
                else:
                    print(error)
                    print()
                    continue

            else:
                return responses

        except ValueError:
            print(error)
            print()


# Checks for yes or no responses
def yes_no(question):
    valid = False
    while not valid:
        responses = input(question).lower()

        if responses == "yes" or responses == "y":
            responses = "yes"
            return responses

        elif responses == "no" or responses == "n":
            responses = "no"
            return responses

        else:
            print("\033[1;31;40m \n")
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
        responses = input(question).lower()
        if responses in valid_responses:
            return responses
        elif responses == "xxx":
            print("you quit")
            exit()
            print("\033[1;31;40m \n")
            print("<error> Please enter 'p' for Pythagorean triple questions, 'm' for Multiplication Challenge "
                  "questions, 's' for Square Numbers Challenge questions.")
            print()

        # If user quits
        if responses == "xxx":
            print("You quit")
            result = "quit"
            return result


def generate_question(question_type):
    responses = None  # Default value for responses

    if question_type == "p":
        # Generate a Pythagorean triple question
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = round(math.sqrt(a ** 2 + b ** 2))
        responses = num_check(
            f"In a Pythagorean triple, if the lengths of two sides are {a} and {b}, what is the length of the "
            f"hypotenuse? ",
            "<error> Please enter a valid number.", int)

        correct_answers = round(math.sqrt(a ** 2 + b ** 2))
        correct_answer_text = f"√({a}^2 + {b}^2)"
    elif question_type == "m":
        # Generate a Multiplication Challenge question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        responses = num_check(f"What is the product of {num1} and {num2}? ",
                              "<error> Please enter a valid number.", int)
        correct_answers = num1 * num2
    elif question_type == "s":
        # Generate a Square Numbers Challenge question
        num = random.randint(1, 10)
        responses = num_check(f"What is the square of {num}? ",
                              "<error> Please enter a valid number.", int)
        correct_answers = num ** 2

    return responses, correct_answers


# Main code goes here

exit_code = "xxx"

# it should print yellow code
print("\033[103;33;30m \n")
statement_generator("Welcome to the Pythagoras Quiz", "!", "=")

# Ask if it wants to see instructions
want_instructions = yes_no("Do you want to see the instructions? (yes/no): ")
if want_instructions == "yes":
    # Show instructions
    instructions()

# Ask if user wants to play
# it should print it white gray
print("\033[1;37;40m \n")
want_to_do_quiz = yes_no("Do you want to do the quiz? (yes/no): ")
if want_to_do_quiz == "no":
    print("\033[38;5;214m \n")
    print("Okay, maybe next time!")
    exit()

# Ask which type of questions the user wants
question_type = question_checker("What type of questions would you like to choose? (p/m/s): ")

# warn them about the deduction
print("\033[38;5;214m \n")
statement_generator("WARNING: If you left the quiz early 10 points will deduct from your total score.", "!", "!")

# Set the number of questions
print("\033[1;37;40m \n")
num_questions = num_check("How many questions would you like to answer? (1-10): ",
                          "<error> Please enter a number between 1 and 10.", int, low=1, high=10)

# Check if the user chose to quit
if num_questions == "xxx":
    print("You quit")
    exit()

# Set the point values
print("\033[1;32;40m \n")
correct_points = 10
print("\033[1;31;40m \n")
incorrect_points = -10

# Initialize variables
total_score = 0
print("\033[1;32;40m \n")
correct_count = 0
print("\033[1;31;40m \n")
incorrect_count = 0

# Generate and ask questions
for i in range(num_questions):
    print("\033[1;37;40m \n")
    print(f"\nQuestion {i + 1}:")
    response, correct_answer = generate_question(question_type)

    # Check if the response is "xxx"
    if str(response).lower() == "xxx":
        print("You quit")
        total_score -= 10  # Deduct 10 point for leaving early
        break

    # Check if the response is correct
    if response == correct_answer:
        print("\033[1;32;40m \n")
        print("Correct!")
        total_score += correct_points
        correct_count += 1
    else:
        print("\033[1;31;40m \n")
        print(f"Incorrect! The correct answer is {correct_answer}.")
        total_score += incorrect_points
        incorrect_count += 1

    time.sleep(1)  # Add a delay before showing the next question

# Print final score and statistics
# it should print blue code
print("\033[1;34m \n")
print("\nQuiz Finished!")
print(f"Total Score: {total_score}")
# it should print green code
print("\033[1;32;40m \n")
print(f"Number of Correct Answers: {correct_count}")
print("\033[1;31;40m \n")
# it should print red code
print(f"Number of Incorrect Answers: {incorrect_count}")
# it should print purple code
print("\033[1;35;40m \n")
statement_generator("Thank you for doing the quiz!", "*", "*")
