import random

def askQuestion():
    repeat = "Yes"
    while repeat == "Yes":
        question = str(input("Ask me a yes or no question!"))

        answers = ['It is certain.', 'Definitely no.', 'Reply hazy, try again.']
        ball_answer = random.randint(0,2)

        print(answers[ball_answer])

        repeat = str(input('Do you want to ask another question? Type Yes or No: '))



askQuestion()

