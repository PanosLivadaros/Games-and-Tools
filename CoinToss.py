import random
response = "play"
while response == "play":
    flag = True
    while flag:
        user_choice = input("Which side of the coin do you choose, heads or tails?\n")
        if (user_choice == "heads") or (user_choice == "tails"):
            flag = False
    possible_outcomes = ["heads", "tails"]
    outcome = random.choice(possible_outcomes)
    print("The coin toss result is:", outcome, ".")
    if outcome == user_choice:
        print("You chose:", user_choice, "and won!")
    else:
        print("You chose:", user_choice, "and lost...")
    response = None
    while (response != "play") and (response != "end"):
        response = input("Would you like to toss again?\nIf so type 'play', if not type 'end'.\n")
print("The game has ended.")
