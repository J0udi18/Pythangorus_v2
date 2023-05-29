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

# Define a function to play the Pythagoras Quiz
def play_quiz():
    # Display instructions for the quiz
    print("Welcome to the Pythagoras Quiz! 😃")
    print("You will be asked 10 questions about the Pythagorean theorem.")
    print("For each question, enter the length of the hypotenuse.")
    print("You will receive a point for each correct answer.")
    print("Good luck! 🍀")

    # Use a for loop to ask 10 questions and track the student's score
    score = 0
    for i in range(10):
        score += ask_question()

    # Display the student's score
    display_score(score)

# Use a while loop to allow the user to play the Pythagoras Quiz multiple times
play_again = "yes"
while play_again.lower() == "yes":
    play_quiz()
    play_again = input("Do you want to play again? (yes/no): ")
print("Thanks for playing the Pythagoras Quiz!")