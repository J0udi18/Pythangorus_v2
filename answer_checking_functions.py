import random

from Tools.demo.beer import n


# Functions go here

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

    return a, b


# Check if the answer for a Pythagorean triple question is correct
def check_pythagorean_answer(a, b, response):
    return response == (a ** 2 + b ** 2)


# Generate a Multiplication Challenge question
def generate_multiplication_question():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    return num1, num2


# Check if the answer for a Multiplication Challenge question is correct
def check_multiplication_answer(num1, num2, response):
    return response == num1 * num2


# Generate a Square Numbers Challenge question
def generate_square_number_question():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    return num


# Check if the answer for a Square Numbers Challenge question is correct
def check_square_number_answer(num, response):
    return response == (int(num ** 0.5) ** 2)


# Main code

print("Welcome to the Quiz!")
points = 0
another_question = "yes"

while another_question == "yes":
    # Select question type
    question_type = question_checker(
        "Enter 'p' for Pythagorean triple questions, 'm' for Multiplication Challenge questions, 's' for Square "
        "Numbers Challenge questions, or press <enter> for all types of questions: ")

    # Call the respective question function based on the selected type
    if question_type == "p":
        a, b = generate_pythagorean_question()
        response = int(input(
            f"In a Pythagorean triple, if n = {n}, what is the length of the hypotenuse if the other two sides are {a} and {b}? "))
        if check_pythagorean_answer(a, b, response):
            print("You got it right! +10 points")
            points += 10
        else:
            print("You got it wrong. -10 points")
            points -= 10
    elif question_type == "m":
        num1, num2 = generate_multiplication_question()
        response = int(input(f"What is the product of {num1} and {num2}? "))
        if check_multiplication_answer(num1, num2, response):
            print("You got it right! +5 points")
            points += 5
        else:
            print("You got it wrong. -5 points")
            points -= 5
    elif question_type == "s":
        num = generate_square_number_question()
        response = input(f"Is {num} a perfect square? (yes/no) ")
        if check_square_number_answer(num, response):
            print("You got it right! +7 points")
            points += 7
        else:
            print("You got it wrong. -7 points")
            points -= 7
    else:
        # If no specific type is selected, generate all types of questions
        a, b = generate_pythagorean_question()
        num1, num2 = generate_multiplication_question()
        num = generate_square_number_question()

        response1 = int(input(
            f"In a Pythagorean triple, if n = {n}, what is the length of the hypotenuse if"
            f" the other two sides are {a} and {b}? "))
        if check_pythagorean_answer(a, b, response1):
            print("You got it right! +10 points")
            points += 10
        else:
            print("You got it wrong. -10 points")
            points -= 10

        response2 = int(input(f"What is the product of {num1} and {num2}? "))
        if check_multiplication_answer(num1, num2, response2):
            print("You got it right! +5 points")
            points += 5
        else:
            print("You got it wrong. -5 points")
            points -= 5

        response3 = input(f"Is {num} a perfect square? (yes/no) ")
        if check_square_number_answer(num, response3):
            print("You got it right! +7 points")
            points += 7
        else:
            print("You got it wrong. -7 points")
            points -= 7

    play_again = input("Do you want another question? (yes/no): ").lower()

print("Your final score is:", points)
print("Thank you for doing the Quiz!")
