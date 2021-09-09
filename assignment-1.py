from random import randint

print("Welcome to Rock-Paper-Scissors game!\n")
print("Rules of the game \n-Rock beats Scissors \n-Scissors beats Paper \n-Paper beats Rock")

choices =["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0
round_history = dict() # round_history={'round 1': [player_choice, computer_choice, winner}, ...., 'round n': []} 

print("\nSCOREBOARD \t Player: {} \t Computer: {}".format(player_score, computer_score))

for i in range (1, 11):
    print("\nRound {}".format(i))
    computer_choice = choices[randint(0, 2)]
    player_index = int(input("Enter your choice (0- Rock, 1- Paper, 2- Scissors): "))
    player_choice = choices[player_index]
    
    if computer_choice == player_choice:
        print("Tie!")
        round_winner= "Both"
    elif computer_choice == "Rock":
        if player_choice == "Paper":
            player_score = player_score + 1
            round_winner= "Player"
        if player_choice == "Scissors":
            computer_score = computer_score + 1
            round_winner= "Computer"
    elif computer_choice == "Paper":
        if player_choice == "Rock":
            computer_score = computer_score + 1
            round_winner= "Computer"
        if player_choice == "Scissors":
            player_score = player_score + 1
            round_winner= "Player"
    elif computer_choice == "Scissors":
        if player_choice == "Rock":
            player_score = player_score + 1
            round_winner= "Player"
        if player_choice == "Paper":
            computer_score = computer_score + 1
            round_winner= "Computer"
    
    print("Your choice: {}, Computer choice: {}".format(player_choice, computer_choice))
    round_history[i]= [player_choice, computer_choice, round_winner]

winner = "Player" if player_score > computer_score else "Computer"
if player_score == computer_score:
    winner = "Both!"

print("\nThe winner is {}!! \n".format(winner))
print("\nSCOREBOARD \t Player: {} \t Computer: {}".format(player_score, computer_score))

while input("\nDo you want to see round history?(y/n)") == "y":
    ind= int(input("Enter the round for which you need the information: "))
    print("\nPlayer choice = {} \nComputer choice = {} \n{} won Round {}".format(round_history[ind][0], round_history[ind][1], round_history[ind][2], ind))
