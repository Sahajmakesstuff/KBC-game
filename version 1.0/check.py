#importing modules and other files
import random
from chose import *

#variable for question no.
question_no=0

#displaying questions
def displayandask():
    
    #question state to ensure that the question is over before we move to next
    state=0

    for question_no in range(0,10):
        while state==question_no:

            #flavour text for easy, medium and hard questions starting at 1,6,9 respectively
            if state==0:
                print("\nThe Easy Questions")
            elif state==5:
                print("\nThe Medium Questions")
            elif state==8:
                print("\nThe Hard Questions")
            
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

                #to remove invalid answers
                if f_op_c>0 and f_op_c<6:

                    #for lifelines
                    if f_op_c==5:
                        
                        #printing remaining lifelines
                        print("The Lifelines are:")
                        for i in lifelines:
                            print(i)

                        #input for lifeline
                        lifeline_chosen=input("\nWhich Lifeline would you like to choose? \nEnter number between 1 and "+str(len(lifelines))+" ")

                        #to remove invalid lifeline
                        try:
                            final_ll=int(lifeline_chosen)
                            
                            if final_ll>0 and final_ll<len(lifelines)+1:

                                #chosing lifeline
                                ll_chosen=lifelines[final_ll-1]

                                #Phone a friend
                                if ll_chosen=="Phone a Friend":
                                    print("You have chosen Phone a Friend Lifeline \nCalling Friend...")

                                    #done with phone a friend
                                    chosen_friend_option=0
                                    
                                    while chosen_friend_option==0:

                                        #chosing wrong option to display
                                        other_opt_f=random.choice(final_options[question_no])

                                        #if it is not same as the correct
                                        if other_opt_f!=final_c_options[question_no]:
                                            opt_friend=[final_c_options[question_no],other_opt_f]
                                            chosen_friend_option=1

                                    #sorting the list so that people do not get suspicious      
                                    f_opt_f=sorted(opt_friend)

                                    #displaying
                                    print("I think maybe one of these two")
                                    for d_friend in f_opt_f:
                                        print(d_friend)

                                    #removing from the list
                                    lifelines.remove("Phone a Friend")

                                #50 50 pretty much same as phone a friend
                                elif ll_chosen=="50-50":
                                    print("You have chosen 50-50 lifeline \nTwo remaining options are...")
                                    
                                    chosen_50=0
                                    while chosen_50==0:
                                        
                                        other_opt_5=random.choice(final_options[question_no])
                                        
                                        if other_opt_5!=final_c_options[question_no]:
                                            opt_50=[final_c_options[question_no],other_opt_5]
                                            chosen_50=1
                                            
                                    f_opt_50=sorted(opt_50)
            
                                    for d_50 in f_opt_50:
                                        print(d_50)

                                    lifelines.remove("50-50")

                                #Expert Advice
                                elif ll_chosen=="Expert Advice":
                                    print("You have chosen Expert Advice Lifeline \nCalling Expert...")

                                    #for chance
                                    chance_ea=random.randrange(1,101)

                                    #removing from lifelines
                                    lifelines.remove("Expert Advice")
                                    
                                    #for correct answer
                                    if chance_ea !=50:
                                        print("I think the Answer should be",final_c_options[question_no])

                                    #for wrong answer
                                    else:
                                        print("I think the Answer should be",random.choice(final_options[question_no]))
                                        
                                #Expert Advice
                                elif ll_chosen=="Audience Poll":
                                    print("You have chosen Audience Poll Lifeline \nAudience is voting...")

                                    #for chance
                                    chance_ap=random.randrange(1,1001)

                                    #removing from lifelines
                                    lifelines.remove("Audience Poll")

                                    #for correct answer
                                    if chance_ea !=500:
                                        print("Audience has voted for",final_c_options[question_no])

                                    #for wrong answer
                                    else:
                                        print("Audience has voted for",random.choice(final_options[question_no]))
                                
                            else:
                                print("Invalid Lifeline")
                            
                        except ValueError as ve:
                            print("Invalid Lifeline")
                    
                    #correct answer
                    elif final_options[question_no][f_op_c-1]==final_c_options[question_no]:
                        print("Correct Answer! Congratulations!")
                        state+=1
                    
                    #Wrong Answer
                    else:
                        print("Incorrect Answer! Sorry!")
                        print("\nYour final score is",state)
                        state="done"
                        break

                else:
                    print("Invalid Answer")

            #Invalid Answer
            except ValueError as ve:
                print("Invalid Answer")
        
    if state==10:
        print("Congratulations! You Won!")
