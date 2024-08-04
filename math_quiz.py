import random
import time

operators=['+','-','*','/']
min_operand=2
max_operand=20
total_problems=10

def generate_problem():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator=random.choice(operators)

    exp=str(left)+" "+operator+" "+str(right)
    answer=eval(exp)

    return exp,answer


score=0
input("Press enter to start!")
print("---------------------------------------------")

start_time=time.time()

for i in range(total_problems):
    exp,answer=generate_problem()
    guess=eval(input("Problem number "+str(i+1)+" : "+exp+" = "))
    if answer==guess:
        score+=1
        print("Correct!")
    else:
        print("Incorrect !")
        break

end_time=time.time()

print("Total time taken by you(in seconds): ",round((end_time-start_time),2))
print("Your score is: ",score)
print("---------------------------------------------")