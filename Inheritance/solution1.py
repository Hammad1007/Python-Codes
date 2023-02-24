# Code here

# Parent class is Person class
class Person:
  def __init__(self, name, age):
    self.name = name;
    self.age = age
    
  def printdet(self):
    print(self.name, self.age)

# Child class
class Student(Person):
  def __init__(self, name, age, gender, degree):
    super().__init__(name, age)   # super method is basically using the parent class contructor
    self.gender = gender
    self.degree = degree
      
  def printdet(self):
    print(self.name, self.age, self.gender, self.degree)
    
# Main here
s = Student("Hammad", 22, "Male", "BsCS")
s.printdet()
    
