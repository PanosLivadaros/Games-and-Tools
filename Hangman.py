import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


playing = True
while playing:
    difficulty = None
    word = ""
    lives = 7
    wrong_letters = []
    while difficulty != "1" and difficulty != "2" and difficulty != "3":
        difficulty = input("Choose a level of difficulty.\nPress 1 for easy.\nPress 2 for medium.\nPress 3 for hard.\n")
    while len(word) < 3:
        word = input("Let you opponent choose a word for you to try to guess!\n")
    clear_screen()
    if difficulty == "1":
        guessed_word = word[0] + (len(word) - 2) * "_" + word[len(word)-1]
    elif difficulty == "2":
        guessed_word = word[0] + (len(word) - 1) * "_"
    else:
        guessed_word = len(word) * "_"
    while lives > 0 and word != guessed_word:
        letter = ""
        found = False
        print("So far, the word is:", guessed_word, "and you have:", lives, "lives remaining.\nThe letters guessed, but not in the word are:", wrong_letters)
        while len(letter) != 1:
            letter = input("Choose a letter to see if it exists inside the word.\n")
        for i in range(len(word)):
            if letter == word[i]:
                guessed_word = list(guessed_word)
                guessed_word[i] = letter
                guessed_word = "".join(guessed_word)
                found = True
        if not found:
            lives -= 1
            if letter not in wrong_letters:
                wrong_letters.append(letter)
        if word == guessed_word:
            print("You discovered the word:", word, "successfully and won!")
        elif lives == 0:
            print("You ran out of lives and lost! Better luck next time...")
    playing = None
    while playing != "Yes" and playing != "yes" and playing != "No" and playing != "no":
        playing = input("Would you like to play another game of Hangman?\n")
    if playing == "Yes" or playing == "yes":
        playing = True
    else:
        playing = False
print("That's enough Hangman for now.")
