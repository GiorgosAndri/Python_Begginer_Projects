import random

board = "| 1 | 2 | 3 |\n" \
        "|---|---|---|\n" \
        "| 4 | 5 | 6 |\n" \
        "|---|---|---|\n" \
        "| 7 | 8 | 9 |\n" \
        "|---|---|---|"
print(board)
while True:
  position = input("Do you want to begin first or second? 1 to begin first, 2 to begin second: ")
  if position == "1":
      user = "X"
      pc = "O"
      break
  elif position == "2":
      user = "O"
      pc = "X"
      break
  else:
      print("Invalid input. Try again")
      continue
userinputs = set()
pcinputs = set()
def player_win():
    if {"1", "2", "3"}.issubset(userinputs) or {"4", "5", "6"}.issubset(userinputs) or {"7", "8", "9"}.issubset(userinputs) or {"1", "4", "7"}.issubset(userinputs) or {"2", "5", "8"}.issubset(userinputs) or {"3", "6", "9"}.issubset(userinputs) or {"1", "5", "9"}.issubset(userinputs) or {"3", "5", "7"}.issubset(userinputs):
        return True
def computer_win():
    if {"1", "2", "3"}.issubset(pcinputs) or {"4", "5", "6"}.issubset(pcinputs) or {"7", "8", "9"}.issubset(pcinputs) or {"1", "4", "7"}.issubset(pcinputs) or {"2", "5", "8"}.issubset(pcinputs) or {"3", "6", "9"}.issubset(pcinputs) or {"1", "5", "9"}.issubset(pcinputs) or {"3", "5", "7"}.issubset(pcinputs):
        return True
def player():
    x = input("select a square: ")
    board2 = board
    while True:
        if x in board and x != "":
            board2 = board.replace(x, user)
            userinputs.add(x)
            return board2, userinputs
        else:
            print("invalid input")
            x = input("select a square: ")
            continue
def computer():
    x = str(random.randint(1, 9))
    while True:
        if x in board and x != "":
            board2 = board.replace(x, pc)
            pcinputs.add(x)
            return board2, pcinputs
        else:
            x = str(random.randint(1, 9))
            continue
count = 0
while True:
    if position == "1":
        k = player()
        board = k[0]
        if player_win():
            print("You won!")
            print(board)
            break
        count += 1
        if count == 5:
            print("It's a draw!")
            break
        print(count)
        b = computer()
        board = b[0]
        if computer_win():
            print("You lost!")
            print(board)
            break
        print(board)
    elif position == "2":
        b = computer()
        board = b[0]
        if computer_win():
            print("You lost!")
            print(board)
            break
        count += 1
        if count == 5:
            print("It's a draw!")
            print(board)
            break
        print(board)
        k = player()
        board = k[0]
        if player_win():
            print("You won!")
            print(board)
            break


