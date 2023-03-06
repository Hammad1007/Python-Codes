from faker import Faker

def funcA():
  # Function to generate fake data
  fake = Faker()
  name = fake.name()
  address = fake.address()
  print(name, " ", address)

funcA()
