import random

# Functions go here

# Checks which questions user would like to answer
def question_checker(question):
    valid_responses = ["p", "m", ""]
    response = input(question).lower()
    while response not in valid_responses:
        print("<error> Please enter 'p' for Pythagorean triple questions, 'm' for Multiplication Challenge questions, or press <enter> for all types of questions.")
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
    response = int(input(f"In a Pythagorean triple, if n = {n}, what is the length of the hypotenuse if the other two sides are {a} and {b}? "))

    # Check user's answer
    if response == a**2 + b**2:
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

# Main code

print("Welcome to the Quiz!")
points = 0
another_qesution = "yes"

while another_qesution == "yes":
    # Select question type
    question_type = question_checker("Enter 'p' for Pythagorean triple questions, 'm' for Multiplication Challenge questions, or press <enter> for all types of questions: ")

    # Call the respective question function based on the selected type
    if question_type == "p":
        points += generate_pythagorean_question()
    elif question_type == "m":
        points += generate_multiplication_question()
    else:
        points += generate_pythagorean_question() + generate_multiplication_question()

    another_qesution = input("Do you want to have another question? (yes/no): ").lower()

print("Your final score is:", points)
print("Thank you for doing the Quiz!")