import random


# Functions go here

# Function will print instructions when called
def instructions():
    print("\033[103;33;60m \n")
    statement_generator("Instructions", "|", "-")
    print("Welcome to the Pythagoras Quiz!")
    print("In this quiz, you will be shown the lengths of two sides of a right triangle.")
    print("Your task is to determine the length of the hypotenuse.")
    print("Each correct answer will earn you a certain number of points.")
    print("Each incorrect answer will deduct 10 points.")
    print("Let's get started!")

    return ""


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


print("\033[1;33;60m \n")
want_instructions = yes_no("would you like to read/see the instructions? ")
if want_instructions == "yes":
    instructions()


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


# Checks which questions user would like to answer
def question_checker(question):
    valid_responses = ["p", "m", "s", ""]
    response = input(question).lower()
    while response not in valid_responses:
        print(
            "<error> Please enter 'p' for Pythagorean triple questions, 'm' for Multiplication Challenge questions, "
            "'s' for Square Numbers Challenge questions, or press <enter> for all types of questions.")
        response = input(question).lower()
    return response


# Generate a Pythagorean triple question
def generate_pythagorean_question():
    # Generate random integer for n
    n = random.randint(1, 10)

    # Calculate the values of a and b based on n
    a = 2 * n + 1
    b = n * (2 * n + 1) + n

    # Get user's answer
    response = int(input(
        f"In a Pythagorean triple, if n = {n}, what is the length of the hypotenuse if the other two sides are {a} and {b}? "))

    # Check user's answer
    if response == a ** 2 + b ** 2:
        print("You got it right! +10 points")
        return 10
    else:
        print("You got it wrong. -10 points")
        return -10


# Generate a Multiplication Challenge question
def generate_multiplication_question():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Get user's answer
    response = int(input(f"What is the product of {num1} and {num2}? "))

    # Check user's answer
    if response == num1 * num2:
        print("You got it right! +5 points")
        return 5
    else:
        print("You got it wrong. -5 points")
        return -5


# Generate a Square Numbers Challenge question
def generate_square_number_question():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Get user's answer
    response = input(f"Is {num} a perfect square? (yes/no) ").lower()

    # Check user's answer
    if response == "yes" and int(num ** 0.5) ** 2 == num:
        print("You got it right! +5 points")
        return 5
    elif response == "no" and int(num ** 0.5) ** 2 != num:
        print("You got it right! +5 points")
        return 5
    else:
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
print("\033[103;33;60m \n")
statement_generator("Welcome to Joudi's Math Quiz", "!", "=")

points = 0
another_question = "yes"

while another_question == "yes":
    # Select question type
    question_type = question_checker(
        "Enter 'p' for Pythagorean triple questions, 'm' for Multiplication Challenge questions, 's' for Square "
        "Numbers Challenge questions, or press <enter> for all types of questions: ")

    # Call the respective question function based on the selected type
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

        # Ask if the user wants another question
        print()
    another_question = yes_no("Would you like another question? ")
    if another_question == "yes":
        print()
        continue
    else:
        another_question = "no"

print(f"Your total score is {points} points")
print("\033[1;35;40m \n")
print("Thank you for doing the quiz!")
