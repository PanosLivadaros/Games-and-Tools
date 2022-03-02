import random
response = "play"
while response == "play":
    flag = False
    while flag == False:
        user_choice = input("Which side of the coin do you choose, head or tails? ")
        if (user_choice == "head") or (user_choice == "tails"):
            flag = True
    possible_outcomes = ["head", "tails"]
    outcome = random.choice(possible_outcomes)
    print("The coin toss result is:", outcome, ".")
    if outcome == user_choice:
        print("You chose:", user_choice, "and won!")
    else:
        print("You chose:", user_choice, "and lost...")
    response = None
    while (response != "play") and (response != "end"):
        response = input("Would you like to toss again?\nIf so type 'play', if not type 'end'.")
print("The game has ended.")
