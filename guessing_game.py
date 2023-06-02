import random

print("Welcome to the number guessing game!")
print("")

while True:
    level = input("Select difficulty level (easy, medium, hard): ").lower()
    if level in ["easy", "medium", "hard"]:
        break
    else:
        print("Invalid input. Please select either 'easy', 'medium', or 'hard'.")

if level == "easy":
    guess_range = 50
    guesses_allowed = 20
elif level == "medium":
    guess_range = 100
    guesses_allowed = 15
else:
    guess_range = 150
    guesses_allowed = 10

answer = random.randint(1, guess_range)

for i in range(guesses_allowed):
    userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
    guess = int(userInput)

    if guess == answer:
        print("Congratulations! You guessed the correct number. You win!")
        break
    elif guess < answer:
        print("The number is higher.")
    else:
        print("The number is lower.")

    if abs(guess - answer) <= 10:
        print("You're warm!")
    elif abs(guess - answer) <= 20:
        print("You're getting warmer.")
    elif abs(guess - answer) <= 30:
        print("You're cold.")
    else:
        print("You're freezing.")

    if i == guesses_allowed - 1:
        print("Sorry, you have run out of guesses. You lose!")
