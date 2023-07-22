from random import randint
from time import sleep
import re
playing = True
while playing:
    player_1_score = 0
    player_2_score = 0
    turn = ""
    while not re.search(r"\b[yY][eE][sS]\b", turn) and not re.search(r"\b[nN][oO]\b", turn):
        turn = input("Player 1, would you like to roll the dice?\n")
    if re.search(r"\b[nN][oO]\b", turn):
        player_1_score = -1
    else:
        print("Rolling...")
        sleep(3)
        first_dice = randint(1, 6)
        second_dice = randint(1, 6)
        player_1_score = first_dice + second_dice
        print("First dice is:", first_dice, "and second dice is:", second_dice, ". Player 1 scored:", player_1_score, "points!")
        turn = ""
        while not re.search(r"\b[yY][eE][sS]\b", turn) and not re.search(r"\b[nN][oO]\b", turn):
            turn = input("Player 2, would you like to roll the dice?\n")
        if re.search(r"\b[nN][oO]\b", turn):
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
    playing = ""
    while not re.search(r"\b[yY][eE][sS]\b", playing) and not re.search(r"\b[nN][oO]\b", playing):
        playing = input("Would you like to play another game of craps?\n")
    playing = re.search(r"\b[yY][eE][sS]\b", playing)
print("All games have ended.")
