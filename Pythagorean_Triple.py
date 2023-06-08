import math


def generate_pythagorean_triple(n):
    a = 2 * n + 1
    b = n * (2 * n + 1) + n
    c = math.sqrt(a ** 2 + b ** 2)
    return a, b, c


def quiz():
    print("Welcome to the Pythagoras Quiz!")
    print("-------------------------------")
    print("Find the hypotenuse given the following values:")
    score = 0
    total_questions = 5

    for i in range(total_questions):
        n = i + 1
        a, b, c = generate_pythagorean_triple(n)

        print(f"\nQuestion {i + 1}:")
        print(f"a = {a}")
        print(f"b = {b}")
        user_answer = input("What is the value of the hypotenuse? ")

        try:
            user_answer = float(user_answer)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if math.isclose(user_answer, c, rel_tol=1e-09, abs_tol=1e-09):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {c}")

    print("\nQuiz complete!")
    print(f"You scored {score}/{total_questions}")