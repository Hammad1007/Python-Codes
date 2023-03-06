from faker import Faker

# An object of Faker class
fake = Faker()

# Faker can be used in for loop as well, just like any other library
for i in range(0, 10):
  name = fake.name()
  print(name)

# While loop as well
print("\n")
i = 0
while i < 10:
  name = fake.name()
  print(name)
  i = i + 1
