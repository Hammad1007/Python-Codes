# Program to linearly search a number in an array
import cmath

a = []
arr = []
n = int(input("Enter the size of array: "))

# function to search
def Search_Linearly(arr, key, n):
  for i in range(n):
    if arr[i] == key:
      print("Match found.\n")
    else:
      print("Mathc not found.\n")

# Input function to see 
def Input(a):
  
  for i in range(n):
    l = int(input())
    a.append(l)
  print("The array is: ", a)    # dipslay the array

Input(a)
k = int(input("Enter the number you want to search for: "))
print("The key is: ", k)
Search_Linearly(a, k, n)



