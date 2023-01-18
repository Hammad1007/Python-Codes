import random   # import random library to use randint

n = random.randint(1, 100)
chances = 3

name = input("What is your name? ")
print(f"Hello {name} nice to meet you. Welcome to our game.")
print("Please guess a number to start. You only have 3 chances, so choose wisely😉")

while chances > 0:
  num = int(input("Enter your guess: "))
  chances = chances - 1
  if num == n:
    print("Hoorayyyyy, you guessed the number.")
    print(f"You guessed the number in {chances} chances.")
  elif num < n:
    print("Too Low!!")
  elif num > n:
    print("Too Highh!!")
  
if chances == 0:
  print(f"You couldn't guess the number. The number was {n}.")
