name=input("Type your name: ")
print("Welcome ",name," to this adventure!")

answer=input("You are on a road,it came to end,you can go left or right: ").lower()

if answer=='left':
    answer=input("You came to a mountain,you can climb it or take ropeway: ").lower()
    if answer=='climb':
        print("You slided through mountain and got injured! ")
    elif answer=='ropeway':
        print("Congrates!You got on jackpot!")
    else:
        print('Not a valid option!')

elif answer=='right':
    answer=input("You want to cross bridge,yes or not: ").lower()
    if answer=='yes':
        print("Bridge broke down!Game Over")
    elif answer=='no':
        print("There is a long path across village,take over")
    else:
        print('Not a valid option!')

else:
    print('Not a valid option!')