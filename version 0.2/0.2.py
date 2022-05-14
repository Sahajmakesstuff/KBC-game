#importing module
import random

#list of questions
questions=["Placeholder 1",
           "Placeholder 2",
           "Placeholder 3",
           "Placeholder 4",
           "Placeholder 5",
           "Placeholder 6",
           "Placeholder 7",
           "Placeholder 8",
           "Placeholder 9",
           "Placeholder 10"]

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

correct_options=["b","1","IV","a","3","III","b","1","IV","1"]

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

    #adding to the final list
    final_questions.append(questions[question_choser])
    final_options.append(options[question_choser])
    final_c_options.append(correct_options[question_choser])

    #removing from old list
    questions.pop(question_choser)
    options.pop(question_choser)
    correct_options.pop(question_choser)

#displaying them
for question_no in range(0,5):
    print(final_questions[question_no],"\n")
    for displaying_options in final_options[question_no]:
        print(displaying_options)
    print()

    #Increasing the question no
    state +=1

    #Taking Input from user
    option_chosen=int(input("Which option will you choose? "))

    #checking for invalid answer
    if option_chosen>0 and option_chosen<5:

        #Checking if answer is correct
        option_converted=final_options[question_no][option_chosen-1]
        
        #correct answer
        if option_converted==final_c_options[question_no]:
            print("Correct Answer! Congratulations!\n")

        #wrong answer
        else:
            print("Incorrect Answer! Sorry!")
            break
        
    #invalid answer
    else:
        print("Invalid Answer")
        break
    
