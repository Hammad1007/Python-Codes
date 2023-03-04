## Python Library

#### Faker

Faker is basically a library which helps to generate fake data in python. 

#### How to install?

The command to install is as follows:
```python
!pip install faker
```

The output of this line is something like given below:
<img
  src="https://github.com/Hammad1007/Python-Codes/blob/Faker/Faker/img/img.jpg"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
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
#### Simple program to print a fake name and a fake address

```python
from faker import Faker
fake = Faker()
name = fake.name()
address = fake.address()
print(name)
print(address)
```
The output of this line is something like given below:

<img
  src="https://github.com/Hammad1007/Python-Codes/blob/Faker/Faker/img/out.jpg"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
