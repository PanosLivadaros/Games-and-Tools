import re
import os


def vertical_check(a):
    for j in range(7):
        for k in range(3):
            if a[k][j] == a[k + 1][j] == a[k + 2][j] == a[k + 3][j] != "":
                return True
    return False


def horizontal_check(a):
    for k in range(6):
        for j in range(4):
            if a[k][j] == a[k][j + 1] == a[k][j + 2] == a[k][j + 3] != "":
                return True
    return False


def diagonal_check(a):
    for k in range(1, 4):
        for j in range(4 - k):
            if a[j][k + j] == a[j + 1][k + j + 1] == a[j + 2][k + j + 2] == a[j + 3][k + j + 3] != "" or a[5 - j][k + j] == a[5 - j - 1][k + j + 1] == a[5 - j - 2][k + j + 2] == a[5 - j - 3][k + j + 3] != "":
                return True
    for k in range(5, 2, -1):
        for j in range(k - 2):
            if a[j][k - j] == a[j + 1][k - j - 1] == a[j + 2][k - j - 2] == a[j + 3][k - j - 3] != "" or a[5 - j][k - j] == a[5 - j - 1][k - j - 1] == a[5 - j - 2][k - j - 2] == a[5 - j - 3][k - j - 3] != "":
                return True
    return False


def check_for_full_board(a):
    for j in range(6):
        for k in range(7):
            if a[j][k] == "":
                return False
    return True


def check_for_validity(n, x, a, s):
    for j in range(6):
        if a[5-j][x-1] == "":
            a[5-j][x-1] = s[0]
            return a
    x = " "
    while re.search(r"[^1-7]", x):
        print("Player", n, ", give the column where you'd like to drop your", s, " checker:\n")
        x = input()
    return check_for_validity(n, int(x), a, s)


playing = True
while playing:
    board = [["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""]]
    win = False
    full = False
    i = 0
    for row in board:
        print(row)
    while not win:
        place = " "
        while re.search(r"[^1-7]", place):
            place = input("Player 1, give the column where you'd like to drop your Yellow checker:\n")
        board = check_for_validity(1, int(place), board, "Yellow")
        i += 1
        for row in board:
            print(row)
        win = vertical_check(board) or horizontal_check(board) or diagonal_check(board)
        if check_for_full_board(board):
            full = True
            break
        if not win:
            place = " "
            while re.search(r"[^1-7]", place):
                place = input("Player 2, give the column where you'd like to drop your Red checker:\n")
            board = check_for_validity(2, int(place), board, "Red")
            i += 1
            for row in board:
                print(row)
            win = vertical_check(board) or horizontal_check(board) or diagonal_check(board)
            if check_for_full_board(board):
                full = True
                break
    if win:
        if i % 2 == 1:
            print("Congratulations player 1! You are the winner of this round!")
        else:
            print("Congratulations player 2! You are the winner of this round!")
    elif full:
        print("This round is a tie. There is no winner.")
    playing = ""
    while not re.search(r"\b[yY][eE][sS]\b", playing) and not re.search(r"\b[nN][oO]\b", playing):
        playing = input("Would you like to play one more game of Connect Four?\n")
    playing = re.search(r"\b[yY][eE][sS]\b", playing)
    os.system('cls' if os.name == 'nt' else 'clear')
print("Game Over.")
