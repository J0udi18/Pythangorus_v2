# Function go here...
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
        print("please answer yes / no")


def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the quiz go here")
    print()
    return ""


# Main Routine goes here...
another_question = yes_no("did you know about this quiz before? ")

if another_question == "no":
    print("display")

print("program continues")