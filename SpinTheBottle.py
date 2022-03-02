import random
list_of_names = []
list_of_names.append(input("Give the name of the 1st participant: "))
list_of_names.append(input("Give the name of the 2nd participant: "))
flag = True
while flag == True:
    answer = None
    while (answer != "Yes") and (answer != "yes") and (answer != "No") and (answer != "no"):
        answer = input("Do you want to add another name to the list? ")
    if (answer == "No") or (answer == "no"):
        flag = False
    else:
        name = input("Give a name: ")
        list_of_names.append(name)
flag = True
previous_answer = "affirmative"
while (len(list_of_names) > 1) and (flag == True):
    i = 0
    while (i < len(list_of_names)) and (flag == True):
        answer = None
        while (answer != "Yes") and (answer != "yes") and (answer != "No") and (answer != "no"):
            answer = input("Do you want to spin the bottle? ")
        if (answer == "No") or (answer == "no"):
            print("Player:", list_of_names[i], "has been kicked out of the game.")
            adjust = False
            if len(list_of_names) != i+1:
                adjust = True
                adjustment = i
            list_of_names.pop(i)
            previous_answer = "negative"
            if len(list_of_names) == 1:
                print("The game has ended.")
                flag = False
        else:
            if previous_answer == "negative":
                if adjust == True:
                    i = adjustment
                temp = list_of_names[i]
                list_of_names.pop(i)
                print("Player:", temp, "has to kiss:", random.choice(list_of_names))
                list_of_names.insert(i, temp)
                previous_answer = "affirmative"
            else:
                temp = list_of_names[i]
                list_of_names.pop(i)
                print("Player:", temp, "has to kiss:", random.choice(list_of_names))
                list_of_names.insert(i, temp)
        i += 1
print("The last person standing is:", list_of_names[0], "! Congratulations, you're the winner!")
