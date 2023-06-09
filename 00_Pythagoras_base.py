import random
import time
from unittest import result


# Functions go here


# Function will print instructions when called
def instructions():
    statement_generator("Instructions", "|", "-")
    print("Welcome to the Pythagoras Quiz!")
    print("you will be given question about right triangles, and you need to find"
          "the length of the missing side.")
    print("let's start")
    print("Good luck!")
    return ""


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, exit_code=None, low=None, high=None):
    valid = False
    while not valid:
        try:
            # Checks if user inputs exit code
            response = input(question)
            if response == exit_code:
                return response
            else:
                response = num_type(response)

            # Checks if they inputted correct number
            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


# Checks for yes or no responses
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes / no")
            print()


# Definition that generates questions randomly and will call this function
def question(symbol, points_val):
    valid = False
    while not valid:

        # Question error if they input unexpected values
        q_error = "Please enter an integer between 0 - 1000 (dont be stupid)"

        # Generate random integer
        temp_int = random.randint(1, 10)
        int_i = random.randint(1, 10)
        int_ii = temp_int * int_i

        # Get answer and there answer to the question
        ans = eval(str(int_ii) + symbol + str(int_i))
        response = num_check("{} {} {} = ".format(int_ii, symbol, int_i), q_error, int, "xxx", -1, 1001)

        # If user quits
        if response == "xxx":
            print("You quit")
            result = "quit"
            return result

        # check if user got answer correct
        if response == ans and time.time() - start < seconds:
            statement_generator("You got it right! +{} points".format(points_val), "*", "~")
            result = "correct"
            print()
            return result
        elif response != ans:
            statement_generator("You got it wrong. -10 points", "|", "-")
            result = "incorrect"
            print()
            return result
        else:
            statement_generator("Time ran out no points", "|", "-")
            result = "quit"
            print()
            return result


# Gives statements decoration on sides and top
def statement_generator(statement, side_decoration, top_bottom_decoration):
    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Timer function stalls program and counts down
def timer(t):
    print("00 : {}".format(t))

    while t != 0:
        t -= 1
        time.sleep(1)
        print("00 : {}".format(t))


# Reset variables
questions_answered = 0
correct_questions = 0
incorrect_questions = 0
points = 0

# Main routine
print("\033[1;33;40m \n")
statement_generator("Welcome to Joudi's Math Quiz", "!", "=")

# define the saved points
save_points = 0

# Asks if user has played before
# If no print instructions
played_before = yes_no("did you know about this quiz before? ")
if played_before == "no":
    instructions()
print()
print("Enjoy!")

# Main quiz code
play_again = "yes"
while play_again == "yes":

    # Reset variables
    questions_answered = 0
    correct_questions = 0
    incorrect_questions = 0
    points = 0

    # Ask user for number of questions
    num_questions_error = "<error> enter an integer"
    num_questions = num_check("How many questions? ", num_questions_error, int, None, 0)

    # Ask user if they want a timer
    time_set = yes_no("Would you like a timer? ")

    if time_set == "yes":
        # Ask user for the amount of time they get for the questions
        seconds = num_check("how many seconds? ", "enter an number between 1, 59", int, None, 0, 60)
        print("Timer set! ")
        # Set start
        start = time.time()

    # No timer
    else:
        start = time.time() * 10000
        seconds = 1

    # Generate questions
    while time.time() - start < seconds and num_questions > 0:

        # Add number of correct and incorrect questions
        if result == "correct":
            correct_questions += 1
            points += num_points
        elif result == "incorrect":
            incorrect_questions += 1
            points -= 10
        else:
            questions_answered -= 1
            break

        # Add number of questions answered
        questions_answered += 1

        # number of questions left go down
        num_questions -= 1

    print(questions_answered)
    print(correct_questions)
    print(incorrect_questions)

    # **** Calculate Game Stats ****
    percent_correct = correct_questions / questions_answered * 100
    percent_incorrect = incorrect_questions / questions_answered * 100

    # Displays game stats with % values to the nearest whole number
    print()
    statement_generator("Quiz Statistics", "-", "*")
    print("Correct: {}: ({:.0f}%)\nIncorrect: {}: ({:.0f}%)".format(correct_questions, percent_correct,
                                                                    incorrect_questions, percent_incorrect))
    print()

    # Print and figure out new high score 
    if points > save_points:
        print("NEW HIGH SCORE")
        save_points = points
    else:
        print("Nice Job!")
    print("Total points: ", points)
    print()

    # Asks user if they want to see there history
    show_history = yes_no("would you like to see quiz history? ")

    # displays history if user says yes
    if show_history == "yes":
        print()
        statement_generator("Quiz History", "-", "*")
        for quiz in question:
            print(quiz)

        print()
        statement_generator("Thanks for doing the quiz", "!", "=")

    # Doesn't display history if user says no
    elif show_history == "no":
        print()
        statement_generator("Thank you for doing the quiz", "!", "=")

    # Ask user if they want to play again
    print()
    redo = yes_no("Would you like to play again? ")
    if redo == "yes":
        print()
        continue
    else:
        redo = "no"

print("\033[255;20;147m \n")
print("\033[255;20;147m Thanks for doing the quiz  \n")
255 - 20 - 147
