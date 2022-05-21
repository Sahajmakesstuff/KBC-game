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
options=[["a", "C", "c", "d"],
         ["C", "2", "3", "4"],
         ["I", "II", "III", "C"],
         ["C", "b", "c", "d"],
         ["1", "2", "C", "4"],
         ["I", "II", "C", "IV"],
         ["a", "C", "c", "d"],
         ["C", "2", "3", "4"],
         ["I", "II", "III", "C"],
         ["C", "2", "3", "4"]]

#Correct Options
correct_options=["C","C","C","C","C","C","C","C","C","C"]

#variable declaration for the final lists
final_questions=[]
final_options=[]
final_c_options=[]

#variable for question state
state=0

#variable for ensuring things stay in range
questions_chosen=0

#Flavour text
print("Welcome to this quiz! \nIt is made by Github user @Sahajmakesstuff")
print("\nThe Rules are simple: You will be asked a question with 4 options, answer with 1,2,3, or 4 and we'll see if you are correct")
print("\nThere are currently 5 questions to be answered")

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
    while state==question_no:

        #printing question no
        print("\nQuestion no",state+1)

        #printing the question and options
        print(final_questions[question_no],"\n")
        for displaying_options in final_options[question_no]:
            print(displaying_options)        

        #Taking Input from user
        option_chosen=input("\nWhich option will you choose? ")

        #Converting input to integer
        try:
            f_op_c=int(option_chosen)
            
            #correct answer
            if final_options[question_no][f_op_c-1]==final_c_options[question_no]:
                print("Correct Answer! Congratulations!\n")
                state+=1

            #Wrong Answer
            else:
                print("Incorrect Answer! Sorry!")
                print("\nYour final score is",state)
                break

        #Invalid Answer
        except ValueError as ve:
            print("Invalid Answer")


#Final text if you won
if state == 5:
    print("Congratulations!! \nYou won!!")

    
