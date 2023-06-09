import random
import time
from termcolor import colored


def instructions():
    print(colored("Welcome to the Pythagorean Theorem Quiz!", "blue"))
    print("Instructions: In each round, a random right triangle will be generated.")
    print("You need to input the length of the hypotenuse (c).")
    print("After each answer, feedback will be provided on whether your answer was correct or not.")
    print()

# Timer function stalls program and counts down
def timer(t):
    time_set = yes_no("Would you like a timer? ")
    if time_set == "yes":
        time_limit = int(input("Enter the time limit (in seconds) per question: "))
    else:
        time_limit = float("inf")  # Set an infinite time limit


# checks how many round had the player played
def check_rounds(round_error=None):
    while True:
        response = input("How many rounds: ")

        rounds_error = "please type either <enter> or an " \
                       "integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(rounds_error)
                    continue

              except ValueError:
                print(round_error)
                continue
            return response


            # If response is not an integer go back to
            # start of loop


def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = int((a ** 2 + b ** 2) ** 0.5)  # Calculate the hypotenuse

    question = f"What is the length of the hypotenuse (c) in a right triangle with sides a = {a} and b = {b}? "
    answer = str(c)
    return question, answer


def print_feedback(correct):
    if correct:
        feedback = colored("Correct!", "green")
    else:
        feedback = colored("Incorrect.", "red")
    print(feedback)


def yes_no(question, error, num_type, exit_code=None, low=None, high=None):
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

        print("Thank you for taking the Pythagorean Theorem Quiz!")
