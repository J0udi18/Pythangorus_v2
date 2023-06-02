import random


def addition_game():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    guess = int(input(f"What is {num1} + {num2}? "))
    if guess == answer:
        print("Correct!")
    else:
        print(f"Sorry, the correct answer is {answer}.")


addition_game()
# This code will generate two random numbers between 1 and 10, add them together, 
# and ask the user to input their answer. If the user's answer matches the correct answer,
# it will print "Correct!" Otherwise, it will print the correct answer.
