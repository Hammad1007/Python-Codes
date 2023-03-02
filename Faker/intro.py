# Code here

# !pip install faker

# from the library faker, import Faker the class
from faker import Faker

# make a fake object of class Faker
fake = Faker()

# create a fake name
name = fake.name()

# create a fake address
address = fake.address()

# print statements
print(name)
print(address)
