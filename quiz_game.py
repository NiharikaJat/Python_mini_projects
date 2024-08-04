print("Welcome to Computer Quiz!")

playing=input("Want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! :)")
score=0
answer1= input("What does GPU stand for? ")
if answer1.lower() == "graphical processing unit":
    print('Correct!')
    score+= 1
else:
    print('Incorrect!')

answer2= input("What does CPU stand for? ")
if answer2.lower() == "central processing unit":
    print('Correct!')
    score+= 1
else:
    print('Incorrect!')

answer3= input("What does ROM stand for? ")
if answer1.lower() == "read only memory":
    print('Correct!')
    score+= 1
else:
    print('Incorrect!')

answer4= input("What does RAM stand for? ")
if answer1.lower() == "random access memoryYES":
    print('Correct!')
    score+= 1
else:
    print('Incorrect!')

answer5= input("What does PC stand for? ")
if answer1.lower() == "program counter":
    print('Correct!')
    score+= 1
else:
    print('Incorrect!')

print("Your final score is: ",score)