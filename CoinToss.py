import random
import re
import os
response = "play"
while re.search(r"\b[pP][lL][aA][yY]\b", response):
    user_choice = ""
    while not re.search(r"\b[hH][eE][aA][dD][sS]\b", user_choice) and not re.search(r"\b[tT][aA][iI][lL][sS]\b", user_choice):
        user_choice = input("Which side of the coin do you choose, heads or tails?\n")
    user_choice = user_choice.lower()
    possible_outcomes = ["heads", "tails"]
    outcome = random.choice(possible_outcomes)
    print("The coin toss result is:", outcome, ".")
    if outcome == user_choice:
        print("You chose", user_choice, "and won!")
    else:
        print("You chose", user_choice, "and lost...")
    response = ""
    while not re.search(r"\b[pP][lL][aA][yY]\b", response) and not re.search(r"\b[eE][nN][dD]\b", response):
        response = input("Would you like to toss again?\nIf so type 'play', if not type 'end'.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
print("The game has ended.")
