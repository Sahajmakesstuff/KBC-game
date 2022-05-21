import random
from lists import *

#variable declaration for the final lists
final_questions=[]
final_options=[]
final_c_options=[]

#variable for question state
state=0

#variable for ensuring things stay in range
questions_chosen=0

#choosing the questions
for question_choser in range(0,5):
    questions_chosen+=1

    #randomizing
    question_choser=random.randrange(0,10-questions_chosen)

    #appending
    final_questions.append(questions[question_choser])
    final_options.append(options[question_choser])
    final_c_options.append(correct_options[question_choser])

    #removing from old list
    questions.pop(question_choser)
    options.pop(question_choser)
    correct_options.pop(question_choser)
