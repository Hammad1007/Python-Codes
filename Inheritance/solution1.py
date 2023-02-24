# Code here

# Parent class is Person class
class Person:
  def __init__(self, name, age):
    self.name = name;
    self.age = age
    
  def printdet(self):
    print("Name is: ", self.name)
    print("Age is: ", self.age)

class Student(Person):
  def __init__(self, name, age, gender, degree):
    super().__init__(name, age)
    self.gender = gender
    self.degree = degree
    
    
