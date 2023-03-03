# Code here for inheritance

class A:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def PrintFunc(self):
    print("{",self.a, "", self.b, "}")
  
  

class B(A):
  def __init__(self, a, b, c):
    super().__init__(a, b)
    self.c = c

  def PrintFunc(self):
    print("{",self.a, "", self.b, "", self.c, "}")

a = A(4, 5)
a.PrintFunc()

b = B(4, 5, 8)
b.PrintFunc()
