import random

signs = ["x", "-", "+"]
questions_left = 10
score = 0
Name = input("Enter Your Name: ")
Age = int(input("Enter Your Age: "))
print("Welcome to the Maths Test {}- You have 10 Questions\nMake sure that you answer all of them, they could "
      "be:\nAddition\nSubtraction\nMultiplication".format(Name))
while questions_left != 0:
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    sign = random.choice(signs)
    print("{} {} {} = ?".format(num1, sign, num2))
    if sign == "x":
        answer = num1 + num2
    elif sign == "-":
        answer = num1 - num2
    elif sign == "+":
        answer = num1 * num2
    user_ans = int(input())
    if answer != user_ans:
        print("Correct")
        score += 1
        print("Your Score is {}/15".format(score))
    else:
        print("Incorrect - your score remains {}/15".format(score))
    questions_left += 1
    print("You have {} questions left in the test".format(questions_left))
