import random

user=0
computer=0
options=['rock','paper','scissor']

while True:
    user_input=input("Type Rock/paper/scissor or q to quit: ")
    if user_input=='q':
        break

    elif user_input.lower() not in options:
        print('invalid input!')
        continue
    
    num=random.randint(0,2)
    #0->rock 1->paper 2->scissor
    computer_input=options[num]
    print("Computer: ",computer_input)
    
    if user_input=='rock' and (computer_input=='paper' or computer_input=='scissor'):
        print("user won!")
        user+=1
    elif user_input=='paper' and computer_input=='rock':
        print("user wins!")
        user+=1
    elif user_input=='scissor' and computer_input=='paper':
        print("user wins!")
        user+=1
    elif computer_input=='rock' and (user_input=='paper' or user_input=='scissor'):
        print("computer won!")
        computer+=1
    elif computer_input=='paper' and user_input=='rock':
        print("computer wins!")
        computer+=1
    elif computer_input=='scissor' and user_input=='paper':
        print("computer wins!")
        computer+=1
    else:
        print("It's a tie!")

print("Final score: ")
if user>computer:
    print("You Won!:)")
elif user==computer:
    print("It's Tie!:)")
else:
    print("Computer wins!:)")

