import random
response = "choose"
while response == "choose":
    list_of_names = []
    flag = True
    while flag:
        name = None
        while name is None:
            name = input("Give a name: ")
        list_of_names.append(name)
        answer = None
        while (answer != "Yes") and (answer != "yes") and (answer != "No") and (answer != "no"):
            answer = input("Do you want to add another name to the list? ")
        if (answer == "No") or (answer == "no"):
            flag = False
    print(random.choice(list_of_names), "has been chosen.")
    response = None
    while (response != "choose") and (response != "end"):
        response = input("Would you like to repeat the process?\nIf so type 'choose', if not type 'end'.")
print("The process has ended.")
