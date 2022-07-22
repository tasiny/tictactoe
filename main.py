from os import system, name
title = r"""  _____ _        _____            _____          
 |_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___ 
   | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \
   | | | | (__    | | (_| | (__    | | (_) |  __/
   |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___|"""
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
game_over = False


def clear():
    """clears console to prevent clutter"""
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def board():
    """prints a tic-tac-toe board"""
    print(row1)
    print(row2)
    print(row3)


def check_win():
    """checks for win condition of three in a row for all cases"""
    if "".join(row1) == "XXX" or "".join(row2) == "XXX" or "".join(row3) == "XXX":
        print("Player X wins")
        return True
    elif "".join(row1[0] + row2[0] + row3[0]) == "XXX" or "".join(row1[1] + row2[1] + row3[1]) == "XXX" or "".join(row1[2] + row2[2] + row3[2]) == "XXX":
        print("Player X wins")
        return True
    elif "".join(row1[0] + row2[1] + row3[2]) == "XXX" or "".join(row1[2] + row2[1] + row3[0]) == "XXX":
        print("Player X wins")
        return True
    elif "".join(row1) == "OOO" or "".join(row2) == "OOO" or "".join(row3) == "OOO":
        print("Player O wins")
        return True
    elif "".join(row1[0] + row2[0] + row3[0]) == "OOO" or "".join(row1[1] + row2[1] + row3[1]) == "OOO" or "".join(row1[2] + row2[2] + row3[2]) == "OOO":
        print("Player O wins")
        return True
    elif "".join(row1[0] + row2[1] + row3[2]) == "OOO" or "".join(row1[2] + row2[1] + row3[0]) == "OOO":
        print("Player O wins")
        return True
    else:
        return False


def check_draw():
    """checks if there are any empty spaces on board and ends game if none are available"""
    if " " not in "".join(row1 + row2 + row3):
        print("Game has ended in a draw. ")
        return True
    else:
        return False


def x_choice():
    """determines player choice and places choice on board for X"""
    player_choice_row = input("Player X choose a row 1, 2 , or 3: ").lower()
    player_choice_column = input("Player X choose a column 1, 2, 3: ").lower()
    if player_choice_row == "1" and player_choice_column in ("1", "2", "3"):
        row1[int(player_choice_column) - 1] = "X"
    elif player_choice_row == "2" and player_choice_column in ("1", "2", "3"):
        row2[int(player_choice_column) - 1] = "X"
    elif player_choice_row == "3" and player_choice_column in ("1", "2", "3"):
        row3[int(player_choice_column) - 1] = "X"
    else:
        print("Incorrect input. Try again")
        return False


def o_choice():
    """determines player choice and places choice on board for O"""
    player_choice_row = input("Player O choose a row 1, 2 , or 3: ").lower()
    player_choice_column = input("Player O choose a column 1, 2, 3: ").lower()
    if player_choice_row == "1" and player_choice_column in ("1", "2", "3"):
        row1[int(player_choice_column) - 1] = "O"
    elif player_choice_row == "2" and player_choice_column in ("1", "2", "3"):
        row2[int(player_choice_column) - 1] = "O"
    elif player_choice_row == "3" and player_choice_column in ("1", "2", "3"):
        row3[int(player_choice_column) - 1] = "O"
    else:
        print("Incorrect input. Try again")
        return False


print(title)
board()
while not game_over:
    x_choice()
    clear()
    print(title)
    board()
    if check_win():
        game_over = True
    if check_draw():
        game_over = True
    else:
        o_choice()
        clear()
        print(title)
        board()
        if check_win():
            game_over = True
        if check_draw():
            game_over = True

