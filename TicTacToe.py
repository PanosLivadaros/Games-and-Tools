def check_for_win(a, s):
    for x in range(3):
        if a[x][0] == a[x][1] == a[x][2] == s or a[0][x] == a[1][x] == a[2][x] == s:
            return True
    if a[0][0] == a[1][1] == a[2][2] == s or a[0][2] == a[1][1] == a[2][0] == s:
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
    x = y = 0
    while x != 1 and x != 2 and x != 3:
        print("Player", n, ", give the 1st coordinate for the", s, "to be placed in:\n")
        x = int(input())
    while y != 1 and y != 2 and y != 3:
        print("Player", n, ", give the 2nd coordinate for the", s, "to be placed in:\n")
        y = int(input())
    return check_for_validity(n, x, y, a, s)


playing = True
while playing:
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    win = False
    full = False
    coord1 = coord2 = i = 0
    while not win:
        while coord1 != 1 and coord1 != 2 and coord1 != 3:
            coord1 = int(input("Player 1, give the 1st coordinate for the X to be placed in:\n"))
        while coord2 != 1 and coord2 != 2 and coord2 != 3:
            coord2 = int(input("Player 1, give the 2nd coordinate for the X to be placed in:\n"))
        board = check_for_validity(1, coord1, coord2, board, "X")
        i += 1
        print(board)
        win = check_for_win(board, "X")
        if check_for_full_board(board):
            full = True
            break
        if not win:
            while coord1 != 1 and coord1 != 2 and coord1 != 3:
                coord1 = int(input("Player 2, give the 1st coordinate for the O to be placed in:\n"))
            while coord2 != 1 and coord2 != 2 and coord2 != 3:
                coord2 = int(input("Player 2, give the 2nd coordinate for the O to be placed in:\n"))
            board = check_for_validity(2, coord1, coord2, board, "O")
            i += 1
            print(board)
            win = check_for_win(board, "O")
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
    playing = None
    while playing != "Yes" and playing != "yes" and playing != "No" and playing != "no":
        playing = input("Would you like to play another game of Tic-Tac-Toe?\n")
    if playing == "Yes" or playing == "yes":
        playing = True
    else:
        playing = False
print("Game Over.")
