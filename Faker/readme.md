## Python Library

#### Faker

Faker is basically a library which helps to generate fake data in python. 

#### How to install?

The command to install is as follows:
```python
!pip install faker
```
#### Working:
This library calls an object of faker class and then helps in making the fake data such as names, addresses, phone numbers. Also this can be called anywhere in the program. In a for loop, while loop, if else conditions switch statements and many more!
This is more helpful when working with data anlytics and generating data for testing purposes at a beginner level.

#### Importing in the main program

The command to use in the main is as follows:
```python
from faker import Faker
```

#### Making an object of Fake class

```python
fake = Faker()
```
#### Simple program to orint a fake name and a fake address

```python
from faker import Faker
fake = Faker()
name = fake.name()
address = fake.address()
print(name)
print(address)
```
