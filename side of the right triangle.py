import random

# Define the number of questions
num_questions = 10

# Define the range of values for the sides of the right triangle
min_value = 1
max_value = 20

# Define the answers dictionary
answers = {}

# Generate the questions and answers
for i in range(num_questions):
    # Generate the sides of the right triangle
    a = random.randint(min_value, max_value)
    b = random.randint(min_value, max_value)
    c = round((a**2 + b**2)**0.5, 2)
    
    # Generate the answer choices
    choices = [c, c-1, c+1, c+2]
    random.shuffle(choices)
    
    # Print the question and answer choices
    print(f"{i+1}. What is the length of the hypotenuse of a right triangle with sides {a} and {b}?")
    for j, choice in enumerate(choices):
        print(f"   {j+1}. {choice}")
    
    # Store the correct answer
    answer = choices.index(c) + 1
    answers[i+1] = answer
    
# Ask the user for their answers
score = 0
for i in range(num_questions):
    answer = int(input(f"Enter your answer"))
