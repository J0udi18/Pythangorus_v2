import random

print("Welcome to the Pythagoras Quiz!")
print("Find the missing side of the right triangle.")

score = 0
for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = round((a ** 2 + b ** 2) ** 0.5, 2)
    print(f"Question {i + 1}:")
    print(f"Side A: {a}")
    print(f"Side B: {b}")
    answer = input("What is the length of Side C? (Round to 2 decimal places) ")
    if answer == str(c):
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The answer is {c}.")

print(f"Quiz complete. Your score is {score}/5.")
if score == 5:
    print("Perfect score! Great job!")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("Better luck next time. Keep practicing.")

# The quiz generates random values ​​for Side A and Side B of a right triangle, 
# and asks the user to input the length of Side C.
# The program then checks if the user's answer matches the calculated value of Side C,
# and keeps track of the score.
