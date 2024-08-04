import random

us= random.randint(1,100)
guesses=0

while True:
    guesses+=1
    user =int(input("Guess a number between 1 and 100 "))
    
    if user<1 or user>100:
        print("Out of range!")
        

    elif user==us:
        print("Correct guess!")
        break
    
    else:
        print("Incorrect guess!")

print('You got it in ',guesses,' guess')
