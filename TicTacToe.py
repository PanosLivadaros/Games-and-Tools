import re
import os


def check_for_win(a):
    for x in range(3):
        if a[x][0] == a[x][1] == a[x][2] != "" or a[0][x] == a[1][x] == a[2][x] != "":
            return True
    if a[0][0] == a[1][1] == a[2][2] != "" or a[0][2] == a[1][1] == a[2][0] != "":
        return True
    return False


def check_for_full_board(a):
    for x in range(3):
        for y in range(3):
            if a[x][y] == "":
                return False
    return True


def check_for_validity(n, x, y, a, s):
    if a[x-1][y-1] == "":
        a[x-1][y-1] = s
        return a
    x = y = " "
    while re.search(r"[^1-3]", x):
        print("Player", n, ", give the 1st coordinate for the", s, "to be placed in:\n")
        x = input()
    while re.search(r"[^1-3]", y):
        print("Player", n, ", give the 2nd coordinate for the", s, "to be placed in:\n")
        y = input()
    return check_for_validity(n, int(x), int(y), a, s)


playing = True
while playing:
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]
    win = False
    full = False
    i = 0
    for row in board:
        print(row)
    while not win:
        coord1 = coord2 = " "
        while re.search(r"[^1-3]", coord1):
            coord1 = input("Player 1, give the 1st coordinate for the X to be placed in:\n")
        while re.search(r"[^1-3]", coord2):
            coord2 = input("Player 1, give the 2nd coordinate for the X to be placed in:\n")
        board = check_for_validity(1, int(coord1), int(coord2), board, "X")
        i += 1
        for row in board:
            print(row)
        win = check_for_win(board)
        if check_for_full_board(board):
            full = True
            break
        if not win:
            coord1 = coord2 = " "
            while re.search(r"[^1-3]", coord1):
                coord1 = input("Player 2, give the 1st coordinate for the O to be placed in:\n")
            while re.search(r"[^1-3]", coord2):
                coord2 = input("Player 2, give the 2nd coordinate for the O to be placed in:\n")
            board = check_for_validity(2, int(coord1), int(coord2), board, "O")
            i += 1
            for row in board:
                print(row)
            win = check_for_win(board)
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
        playing = input("Would you like to play one more game of Tic-Tac-Toe?\n")
    playing = re.search(r"\b[yY][eE][sS]\b", playing)
    os.system('cls' if os.name == 'nt' else 'clear')
print("Game Over.")
