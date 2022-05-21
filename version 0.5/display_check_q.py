from chosing_q import *

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
