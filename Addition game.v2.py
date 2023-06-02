import random


def addition_game():
    score = 0
    rounds = 0
    play_again = True

    while play_again:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2
        guess = input(f"What is {num1} + {num2}? (Type 'q' to quit) ")

        if guess.lower() == "q":
            play_again = False
        else:
            try:
                guess = int(guess)
                if guess == answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Sorry, the correct answer is {answer}.")
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")

        rounds += 1

    print(f"Thanks for playing! Your final score is {score} out of {rounds} rounds.")

# the game is played in a while loop that runs until the user chooses to quit by typing "q".
# Each round, the code generates two random numbers, calculates the correct answer, and asks the user for their guess.
# If the user's guess is correct, their score is increased by one. After each round,
# the code also checks if the user has entered a valid input (either a number or "q" to quit)
# and provides appropriate feedback.
