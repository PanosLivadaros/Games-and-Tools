from random import randint
from time import sleep

playing = True
while playing:
    player_1_score = 0
    player_2_score = 0
    turn = None
    while turn != "Yes" and turn != "yes" and turn != "No" and turn != "no":
        turn = input("Player 1, would you like to roll the dice?\n")
    if turn == "No" or turn == "no":
        player_1_score = -1
    else:
        print("Rolling...")
        sleep(3)
        first_dice = randint(1, 6)
        second_dice = randint(1, 6)
        player_1_score = first_dice + second_dice
        print("First dice is:", first_dice, "and second dice is:", second_dice, ". Player 1 scored:", player_1_score, "points!")
        turn = None
        while turn != "Yes" and turn != "yes" and turn != "No" and turn != "no":
            turn = input("Player 2, would you like to roll the dice?\n")
        if turn == "No" or turn == "no":
            player_2_score = -1
        else:
            print("Rolling...")
            sleep(3)
            first_dice = randint(1, 6)
            second_dice = randint(1, 6)
            player_2_score = first_dice + second_dice
            print("First dice is:", first_dice, "and second dice is:", second_dice, ". Player 2 scored:", player_2_score, "points!")
    if player_1_score > player_2_score:
        print("Player 1 has won this game of craps!")
    elif player_2_score > player_1_score:
        print("Player 2 has won this game of craps!")
    else:
        print("It's a draw!")
    playing = None
    while playing != "Yes" and playing != "yes" and playing != "No" and playing != "no":
        playing = input("Would you like to play another game of craps?\n")
    if playing == "Yes" or playing == "yes":
        playing = True
    else:
        playing = False
print("All games have ended.")
