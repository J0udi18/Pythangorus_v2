import random
import time
from termcolor import colored

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

def yes_no(prompt):
    while True:
        answer = input(prompt + " (yes/no) ").lower()
        if answer in ["yes", "no"]:
            return answer
        print("Please enter either 'yes' or 'no'.")

def main():
    print(colored("Welcome to the Pythagorean Theorem Quiz!", "blue"))
    print("Instructions: In each round, a random right triangle will be generated.")
    print("You need to input the length of the hypotenuse (c).")
    print("After each answer, feedback will be provided on whether your answer was correct or not.")
    print()

    rounds = int(input("How many rounds would you like to play? "))

    time_set = yes_no("Would you like a timer? ")
    if time_set == "yes":
        time_limit = int(input("Enter the time limit (in seconds) per question: "))
    else:
        time_limit = float("inf")  # Set an infinite time limit

    correct_answers = 0

    for _ in range(rounds):
        question, answer = generate_question()
        print(question)

        start_time = time.time()
        user_answer = input("Your answer: ")
        end_time = time.time()

        elapsed_time = end_time - start_time
        if elapsed_time > time_limit:
            print(colored(f"Time limit exceeded! You took {elapsed_time:.2f} seconds.", "yellow"))
            continue

        if user_answer == answer:
            correct_answers += 1
            print_feedback(True)
        else:
            print_feedback(False)

    print(f"\nYou scored {correct_answers} out of {rounds} in the Pythagorean Theorem Quiz.")

    play_again = input("Do you want to take the quiz again? (yes/no) ")
    if play_again.lower() == "yes":
        print(f"\nYour score in the previous quiz was {correct_answers}/{rounds}.")
        main()
    else:
        print("Thank you for taking the Pythagorean Theorem Quiz!")
