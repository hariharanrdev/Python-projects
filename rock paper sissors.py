import random

user_wins=0
com_wins=0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options :
        continue
    random_number = random.randint(0,2)
    #rock:1,paper:1,scissors:2

    computer_pick = options[random_number]
    print("computer picked",computer_pick + ".")
    
    if user_input=="rock" and computer_pick=="scissors":
        print("you won")
        user_wins += 1
        continue

    elif user_input=="paper" and computer_pick=="rock":
        print("you won")
        user_wins += 1
        continue

    elif user_input=="scissors" and computer_pick=="paper":
        print("you won")
        user_wins += 1
        continue

    else:
        print("good boy!")
        com_wins += 1
print("you won", user_wins, "times.")
print("The computer Won",com_wins, "times.")
