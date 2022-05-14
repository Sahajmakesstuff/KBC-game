#importing module
import random

#list of questions
questions=["Question 1",
           "Question 2",
           "Question 3",
           "Question 4",
           "Question 5",
           "Question 6",
           "Question 7",
           "Question 8",
           "Question 9",
           "Question 10"]

#lists of options
options=[["a", "b", "c", "d"],
         ["1", "2", "3", "4"],
         ["I", "II", "III", "IV"],
         ["a", "b", "c", "d"],
         ["1", "2", "3", "4"],
         ["I", "II", "III", "IV"],
         ["a", "b", "c", "d"],
         ["1", "2", "3", "4"],
         ["I", "II", "III", "IV"],
         ["1", "2", "3", "4"]]

#variable declaration for the final lists
final_questions=[]
final_options=[]

#variable for ensuring things stay in range
questions_chosen=0

#choosing the questions
for question_choser in range(0,5):
    questions_chosen+=1

    #randomizing
    question_choser=random.randrange(0,10-questions_chosen)

    #adding to the final list and removing from old one to ensure no repeats
    final_questions.append(questions[question_choser])
    final_options.append(options[question_choser])
    questions.pop(question_choser)
    options.pop(question_choser)

#displaying them
for displaying_questions in range(0,5):
    print(final_questions[displaying_questions],"\n")
    for displaying_options in final_options[displaying_questions]:
        print(displaying_options)
    print("\n")
    
