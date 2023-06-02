import random


# Define a function to ask a Pythagoras question and get a yes/no response from the user
def ask_question():
    # Generate random values for the legs and hypotenuse
    leg1 = random.randint(1, 10)
    leg2 = random.randint(1, 10)
    hypotenuse = random.randint(1, 10)

    # Ask the user the Pythagoras question
    print(f"What is the length of the hypotenuse of a right triangle with legs of length {leg1} and {leg2}?")

    # Get the user's answer
    user_answer = input("Enter your answer: ")

    # Check if the user's answer is correct
    if int(user_answer) == hypotenuse:
        print("🎉 Correct! 🎉")
        return 1
    else:
        print("❌ Incorrect. ❌")
        return 0


# Define a function to display the student's score
def display_score(score):
    print(f"Your score is {score} out of 10.")




