import random
import re
import os
playing = True
while playing:
    user_action = ""
    while not re.search(r"\b[rR][oO][cC][kK]\b", user_action) and not re.search(r"\b[pP][aA][pP][eE][rR]\b", user_action) and not re.search(r"\b[sS][cC][iI][sS][sS][oO][rR][sS]\b", user_action):
        user_action = input("Enter your choice: rock, paper or scissors:\n")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    user_action = user_action.lower()
    print("You chose:", user_action, ", computer chose:", computer_action, ".")
    if user_action == computer_action:
        print("Both players selected:", user_action, ". It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")
    playing = ""
    while not re.search(r"\b[yY][eE][sS]\b", playing) and not re.search(r"\b[nN][oO]\b", playing):
        playing = input("Would you like to play another round of rock paper scissors?\n")
    playing = re.search(r"\b[yY][eE][sS]\b", playing)
    os.system('cls' if os.name == 'nt' else 'clear')
print("Goodbye.")
