# Pythagoras Quiz with Instructions, Yes/No Component, and Looping Component

print("Welcome to the Pythagoras Quiz!")
print("Answer the following questions to test your knowledge of the Pythagorean theorem.")


# Define a function to ask a Pythagoras question and get a yes/no response from the user
def ask_question():
    # Ask the user for the lengths of the legs
    leg1 = int(input("What is the length of the first leg? "))
    leg2 = int(input("What is the length of the second leg? "))

    # Ask the user for the length of the hypotenuse
    hypotenuse = int(input("What is the length of the hypotenuse? "))

    # Check if the user's answer is correct
    if hypotenuse ** 2 == leg1 ** 2 + leg2 ** 2:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {hypotenuse} cm. ")

    # Ask the user if they want to try another question
    another_question = input("Do you want to try another question? (yes/no) ")

    # Return True if the user wants to try another question, False otherwise
    if another_question.lower() == "yes" or "y":
        return True
    else:
        return False


# Use a while loop to keep asking questions until the user doesn't want to try anymore
while True:
    # Ask a question and get the user's response
    if ask_question():
        continue
    else:
        break

print("Thanks for playing the Pythagoras Quiz!")
