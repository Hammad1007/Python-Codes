# Class A 
class A:
  a = 10

# Class B
class B:
  b = 20

# An object of class A calling the variable of class A
x = A()
print(x.a)  # prints 10

# An object of class B calling the variable of class B
y = B()
print(y.b)    # prints 20
