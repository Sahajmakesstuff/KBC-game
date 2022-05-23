import random
from listing import *

#variable declaration for the final lists
final_questions=[]
final_options=[]
final_c_options=[]

#variable for ensuring things stay in range
questions_chosen_e=0
questions_chosen_m=0
questions_chosen_h=0

questions_choser_e=0
questions_choser_m=0
questions_choser_h=0

#choosing the questions for easy
def easy_q():
    for choser_e in range(0,5):
        questions_chosen_e=choser_e+1

        #randomizing
        question_choser_e=random.randrange(0,10-questions_chosen_e)

        #appending
        final_questions.append(easy_questions[question_choser_e])
        final_options.append(easy_options[question_choser_e])
        final_c_options.append(easy_correct_options[question_choser_e])

        #removing from old list
        easy_questions.pop(question_choser_e)
        easy_options.pop(question_choser_e)
        easy_correct_options.pop(question_choser_e)

#choosing the questions for medium
def medium_q():
    for choser_m in range(0,3):
        questions_chosen_m=choser_m+1

        #randomizing
        question_choser_m=random.randrange(0,6-questions_chosen_m)

        #appending
        final_questions.append(mid_questions[question_choser_m])
        final_options.append(mid_options[question_choser_m])
        final_c_options.append(mid_correct_options[question_choser_m])

        #removing from old list
        mid_questions.pop(question_choser_m)
        mid_options.pop(question_choser_m)
        mid_correct_options.pop(question_choser_m)

#choosing the questions for hard
def hard_q():
    for choser_h in range(0,2):
        questions_chosen_h=choser_h+1

        #randomizing
        question_choser_h=random.randrange(0,4-questions_chosen_h)

        #appending
        final_questions.append(hard_questions[question_choser_h])
        final_options.append(hard_options[question_choser_h])
        final_c_options.append(hard_correct_options[question_choser_h])

        #removing from old list
        hard_questions.pop(question_choser_h)
        hard_options.pop(question_choser_h)
        hard_correct_options.pop(question_choser_h)

