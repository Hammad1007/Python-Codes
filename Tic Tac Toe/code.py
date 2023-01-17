# Code here

import random
board = []

# make the board
def makeboard():
  for i in range(3):
    r = []
    for j in range(3):
      r.append('-')
    board.append(r)

# printing the board
def printboard():
  for i in board:
    for j in i:
      print(j, end = " ")
    print()

# random position
def randompos():
  a = random.randint(0,1)
  return a

# swap player
def swapplayer(player):
  if player == 'X':
      return 'O'
  else:
      return 'X'

# spot of the player
def spot(r, c, player):
  board[r][c] = player

# board filled or not
def boardfilled():
  for i in board:
    for j in i:
      if j == '-':
        return False
  return True

# check for the winning conditions check if the player wins
def checkwin(player):
  flag = None
  n = len(board)
  # checks for rows
  for i in range(n):
    flag = True
    for j in range(n):
      if board[i][j] != player:
       flag = False
       break
    if flag:
      return flag

    # checks columns
    for i in range(n):
      flag = True
      for j in range(n):
        if board[j][i] != player:
          flag = False
          break
      if flag:
        return flag

    # checks for diagnol
    flag = True
    for i in range(n):
      if board[i][i] == player:
        flag = True
        break
    if not flag:
      return False

    for i in range(n):
      flag = True
      if board[i][n - 1 - i] == player:
        flag = True
        break
      if not flag:
        return False
    return False

# start function
def start():
  makeboard()
  player = 'X' if randompos() == 1 else 'O'

  while True:
    print(f"Player {player} turn.")
    printboard()
    # taking user input
    row = int(input("Enter the row and column: "))
    col = int(input("Enter the row and column: "))
    print("The row and col is: ", row, col)
    # fixing the spot
    spot(row - 1, col - 1, player)
    
    printboard()
    if checkwin(player):
      print(f"Player {player} wins")
      break

    # Draw condition
    if boardfilled():
      print("Draw.\n")
      break

    # swapping the turn
    player = swapplayer(player)
    # showing the final view of board
    print()
    #printboard()

# main function here
print("\t\tTic Tac Toe Game")
start()
print("\t\t The END")
