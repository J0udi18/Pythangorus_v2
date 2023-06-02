import random
from time import sleep


# This function will either generates question or print end game stats
def quest_gen(rounds, mode, a, b, answer, cor,incor):
    if rounds < 1:  # If player is out of rounds, game will show stats
        print("\nGameOver, Out of rounds!")
        print("***Stats - Correct: {} || Incorrect: {}***\n".format(cor, incor))
        try:
            cont = int(input("Continue? (1).Yes (2).No : "))    # Asks whether the player wants to continue or not.
            if cont == 1:  # New game. . .
                ask_rounds()
            elif cont == 2:  # Game ends. . .
                print("\n----------------")
                sleep(1)
                print("\nEnding game")
                print(".")
                sleep(.5)
                print(".")
                sleep(.5)
                quit()
            else:
                print("\n***Invalid input, Enter (1) to continue or (2) to exit.***\n")
                print("----------------")
                quest_gen(rounds, mode, a, b, answer, cor, incor)
        except ValueError:
            print("\n***Invalid input, Enter (1) to continue or (2) to exit.***\n")
            quest_gen(0, mode, a, b, answer, cor, incor)
    else:  # If there are more than 0 rounds, game will generate a new question.
        numbers = list(range(5, 20))
        print(numbers)
        a = random.choice(numbers)
        b = random.choice(numbers)
        answer = a + b
    if mode == 0:  # Unlimited rounds mode
        ask_quest(rounds, a, b, answer, mode, cor, incor)
    else:  # Limited rounds mode
        rounds -= 1
        ask_quest(rounds, a, b, answer, mode, cor, incor)


# This function asks the user the generated question followed by user feedback.
def ask_quest(rounds, a, b, answer, mode, cor, incor):
    try:
        quest = int(input("\nWhat is {} + {}? ".format(a, b)))
        if quest == answer:  # IF NUMBERS == ANSWER
            print("Correct!")
            cor += 1
        elif mode == 0 and quest == 000:  # ENDS UNLIMITED ROUNDS MODE
          print("\nEnding unlimited rounds..")
          sleep(2)
          ask_rounds()
        elif quest == 0:  # IF NUMBER == 0 OR LOWER THAN 0
            print("Enter a number higher than 0!")
            ask_quest(rounds, a, b, answer, mode, cor, incor)
        elif quest != answer:  # IF NUMBER INCORRECT
            print("Incorrect!")
            incor += 1
        print("\n----------------")
        quest_gen(rounds, mode, a, b, answer, cor, incor)

    except ValueError:
        print("Enter a integer!")
        ask_quest(rounds, a, b, answer, mode, cor, incor)


# Asks user how many rounds they want or what mode they want to play.
def ask_rounds():
    while True:
        try:
            print("\n**Enter 0 for unlimited rounds.**\n")
            rounds = int(input("How many rounds? "))
            if rounds == 0:
                print("\n----------------")
                quest_gen(3, 0, 0, 0, 0, 0, 0)  # rounds, mode, a, b, answer, correct, incorrect
            else:
                print("\n----------------")
                quest_gen(rounds, 1, 0, 0, 0, 0, 0)  # rounds, mode, a, b, answer, correct, incorrect

        except ValueError:
            print("Invalid input!")


# Main Routine and intro instructions
print("How to play -\n")
sleep(2)
print("Enter the amount of rounds you want to play. After this you will be given randomly generated math questions.\n")
sleep(3)
print(
    "Answer until you run out rounds. When you run out you will be given your end game stats and a option to continue")
sleep(3)
print("To get out unlimited mode, type '000'")
print("\n----------------------------")
ask_rounds()
