# Program to find the quadratic roots
import cmath

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
print(f"The values of a, b and c are {a}, {b} and {c} respectively.")

disc = b**2 - 4 * a * c
root1 = (-b - cmath.sqrt(disc))/(2 * a)
root2 = (-b + cmath.sqrt(disc))/(2 * a)

print(f"The roots are {root1} and {root2}.")
