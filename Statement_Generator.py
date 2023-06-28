# Gives statements decoration on sides and top
def statement_generator(statement, side_decoration, top_bottom_decoration):
    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)


print("\033[103;33;30m \n")
statement_generator("Welcome to the Pythagoras Quiz", "!", "=")
statement_generator("Instructions", "|", "-")
print("\033[1;35;40m \n")
statement_generator("Thank you for doing the quiz!", "*", "*")
