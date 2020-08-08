
from random import randint
t = ["Rock", "Paper", "Scissor"]
computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, Scissor?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        print("player=",player)
        if computer == "Paper":
            print("computer=",computer)
            print("You lose(*_*)")
        else:
            print("computer=",computer)
            print("You win(^_^)")
    elif player == "Paper":
        print("player=",player)
        if computer == "Scissor":
            print("computer=",computer)
            print("You lose(*_*)")
        else:
            print("computer=",computer)
            print("You win(^_^)")
    elif player == "Scissor":
        print("player=",player)
        if computer == "Rock":
            print("computer=",computer)
            print("You lose(*_*)")
        else:
           print("computer=",computer)
           print("You win(^_^)")
    else:
        print("Wrong move.check your spelling")
    player = False
    computer = t[randint(0,2)]
    print("Do you want to play again? (Y/N)") 
    ans = input() 
    if ans == 'n' or ans == 'N': 
        break
print("\nThanks for playing(ROCK=PAPER=SCISSOR)") 