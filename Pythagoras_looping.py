import math


def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        try:
            response = int(input(question))
            if low is not None and response < low:
                print(error)
                continue
            if high is not None and response > high:
                print(error)
                continue
            return response
        except ValueError:
            print(error)


