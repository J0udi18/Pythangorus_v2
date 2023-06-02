import random

number = random.randint(1, 100)
print("spoiler alert: ", number)
print()
print("I'm thinking of a number between 1 and 100. ")
guesses_taken = 0

while guesses_taken < 5:
    guess = input("Enter a guess: ")
    guess = int(guess)
    guesses_taken = guesses_taken + 1
    if guess < number:
        print("That was too low.")
    elif guess > number:
        print("That was Too high!")
    else:
        break
if guess == number:
    print("Winner Winner, chicken dinner!🐔")
    print("You guessed the correct number!")
else:
    print("You lose, better luck next time.The right number was", number)
    print()
