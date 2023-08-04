import random
import re
import os
playing = True
while playing:
    list_of_names = []
    list_of_names.append(input("Give the name of the 1st participant:\n"))
    list_of_names.append(input("Give the name of the 2nd participant:\n"))
    answer = ""
    while not re.search(r"\b[nN][oO]\b", answer):
        answer = ""
        while not re.search(r"\b[yY][eE][sS]\b", answer) and not re.search(r"\b[nN][oO]\b", answer):
            answer = input("Do you want to add another name to the list?\n")
        if re.search(r"\b[yY][eE][sS]\b", answer):
            list_of_names.append(input("Give the name of the participant:\n"))
    flag = True
    previous_answer = True
    while (len(list_of_names) > 1) and flag:
        i = 0
        while (i < len(list_of_names)) and flag:
            answer = ""
            while not re.search(r"\b[yY][eE][sS]\b", answer) and not re.search(r"\b[nN][oO]\b", answer):
                answer = input("Do you want to spin the bottle?\n")
            if re.search(r"\b[nN][oO]\b", answer):
                print("Player:", list_of_names[i], "has been kicked out of the game.")
                adjust = False
                if len(list_of_names) != i+1:
                    adjust = True
                    adjustment = i
                list_of_names.pop(i)
                previous_answer = False
                if len(list_of_names) == 1:
                    print("The game has ended.")
                    flag = False
            else:
                if not previous_answer:
                    if adjust:
                        i = adjustment
                    temp = list_of_names[i]
                    list_of_names.pop(i)
                    print("Player:", temp, "has to kiss:", random.choice(list_of_names))
                    list_of_names.insert(i, temp)
                    previous_answer = True
                else:
                    temp = list_of_names[i]
                    list_of_names.pop(i)
                    print("Player:", temp, "has to kiss:", random.choice(list_of_names))
                    list_of_names.insert(i, temp)
            i += 1
    print("The last person standing is:", list_of_names[0], "! Congratulations, you're the winner!")
    playing = ""
    while not re.search(r"\b[yY][eE][sS]\b", playing) and not re.search(r"\b[nN][oO]\b", playing):
        playing = input("Would you like to play a new round of Spin The Bottle?\n")
    playing = re.search(r"\b[yY][eE][sS]\b", playing)
    os.system('cls' if os.name == 'nt' else 'clear')
print("So long friends.")
