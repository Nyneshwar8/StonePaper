import random

play_score = 0
computer_score = 0

def computers():
    computers_choose = random.randint(1, 3)
    if computers_choose == 1:
        choice = 'r'
    elif computers_choose == 2:
        choice = 'p'
    elif computers_choose == 3:
        choice = 's'
    return choice

def players():
    while True:
        players_choose = input('Enter rock, paper, or scissors: ').lower()
        if players_choose in ['rock', 'r']:
            return 'r'
        elif players_choose in ['paper', 'p']:
            return 'p'
        elif players_choose in ['scissors', 's']:
            return 's'
        else:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

while True:
    user = players()
    computer = computers()

    if user == computer:
        print("It's a tie!")
    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        print("You won!")
        play_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print("Player Score: " + str(play_score))
    print("Computer Score: " + str(computer_score))

    game_on = input("Do you want to continue playing? (Y/N) ")
    if game_on.lower() != 'y':
        break

print("________________________________________________")
print("Game over")