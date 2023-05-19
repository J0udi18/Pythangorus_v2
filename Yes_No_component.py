def yes_no(question):
    while True:
        response = input(question).strip().lower()
        if response == 'yes' or response == 'y':
            return True
        elif response == 'no' or response == 'n':
            return False
        else:
            print("Please enter 'Yes' or 'No'.")