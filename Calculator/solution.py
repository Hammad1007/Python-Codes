# Simple Calculator in Python

# Adding the two values
def add(x, y):
  return x + y

# Subtracting the two values
def subtract(x, y):
  return x - y

# Multiplying the two values
def multiply(x, y):
  return x * y

# Dividing the two values
def divide(x, y):
  return x // y

# Modulus of two values
def modulo(x, y):
  return x % y

# start function to begin with the calculations
def start():
  a = int(input("Enter the value of a: "))
  b = int(input("Enter the value of b: "))
  print("Value of a is: ", a)
  print("Value of b is: ", b)
  print("The sum of a and b is: ", add(a, b))
  print("The difference of a and b is: ", subtract(a, b))
  print("The product of a and b is: ", multiply(a, b))
  print("The dividend of a and b is: ", divide(a, b))
  print("The modulus of a and b is: ", modulo(a, b))
  print("If you wish to exit, press '0'. ")
  #c = int(input("Enter 0 to exit.\n"))

start()

