#Radhe Radhe
#This is  a mini project for making the "Snake-Water-Gun" game...
import random
continue_choice='y'
while(continue_choice=='y'):
    computer_choice=random.randint(0,2)
    print("Snake-0;Water-1;Gun-2")
    user_choice=int(input("Enter your choice...:"))
    print(f"Your Choice:{user_choice}")
    print(f"Computer's Choice:{computer_choice}")
    if(user_choice==0 and computer_choice==1):
        print("You Won!")
    
    elif(user_choice==1 and computer_choice==0):
        print("Computer Wins!")

    elif(user_choice==0 and computer_choice==2):
        print("Computer Wins!")

    elif(user_choice==2 and computer_choice==0):
        print("You Won!")

    elif(user_choice==1 and computer_choice==2):
        print("You Won!")

    elif(user_choice==2 and computer_choice==1):
        print("Computer Wins!")

    elif(user_choice==2 and computer_choice==0):
        print("You Won!")

    elif(user_choice==0 and computer_choice==2):
        print("Computer Wins!")

    elif(user_choice==computer_choice):
        print("Nice one buddy! But that's a DRAW...!!!")

    else:
        print("Aww! You entered an invalid choice...!")

    continue_choice=input("Do you want tto play again:(y/n)")
    if(continue_choice=='y'):
        continue
    else:
        break