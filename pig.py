import random

def roll():
    min=1
    max=6
    roll=random.randint(min,max)

    return roll

while True:
    players=input("Enters the number of players between 2 and 4: ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            print('Not accepted')
            break 
    else:
        print('Invalid!')

max_score=20
player_score=[0 for _ in range(players)]

while max(player_score)<max_score:

    for i in range(players):
        print("\nPlayer number ",i+1," has just started")
        print("\nTill now, total score is ",player_score[i],"\n")
        current_score=0

        while True:
            should_roll=input("wanna roll dice,type y: ").lower()
            if should_roll!='y':
                break 

            value=roll()
            if value==1:
                current_score=0
                print("You rolled a one,turn done!")
                break
            else:
                current_score+=value
                print("You rolled a ",value)

            print("Your score is: ",current_score)
        
        player_score[i]+=current_score
        print("Your total score is: ",player_score[i])

max_score=max(player_score)
print("The clear winner is: ",player_score.index(max_score)+1," with a score of ",max_score)