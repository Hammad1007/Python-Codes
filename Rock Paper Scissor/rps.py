# Code here

import random   # import the random library

c = ['R', 'P', 'S']   # rock, paper, scissor

# returns any random index from the computer
def computergenerate():
  return c[random.randint(0, 2)]

def start(countplay, countcomp):
  comp = computergenerate()
  player = input("Select any one of the R, P, S--> ")
  print("Computer chose: ", comp)
  print("Player chose: ", player)
  if comp == player:
    print("Draw.\n")
  elif comp == 'R':
    if player == 'S':
      print("Computer wins!\n")
      countcomp = countcomp + 1
    elif player == 'P':
      print("Player wins!\n")
      countplay = countplay + 1
  elif comp == 'S':
    if player == 'P':
      print("Computer wins!\n")
      countcomp = countcomp + 1
    elif player == 'R':
      print("Player wins!\n")
      countplay = countplay + 1
  elif comp == 'P':
    if player == 'R':
      print("Computer wins!\n")
      countcomp = countcomp + 1
    elif player == 'S':
      print("Player wins!\n")
      countplay = countplay + 1

# printing the score on the screen
def printscore(councomp, countplay):
  print(f"The computer scored: {countcomp} points")
  print(f"The player scored: {countplay} points")

# check for a winner
def winner():
  if countcomp > countplay:
    print("Computer Wins!!!\n")
  elif countcomp == countplay:
    print("The Game was a Draw!!!\n")
  else:
    print("Player Wins!!!\n")

# exit or not from the game
def exit():
  printscore(countcomp, countplay)
  winner()

# Main here
choice = 5
while choice > 0:
   countplay = 0
   countcomp = 0
   start(countplay, countcomp)
   choice = choice - 1

#exit()
