print("What is Module  ?")
print("A Module is a Python File, containing Code, that we can reuse it in Another Python File.")
print("Python Built-in Modules")
print('''math
random
date and time
os
statistics''')
print("import Statement")
print("To Use a Module, Firstly have to import it")
print("import math")
print("import random")
print("import datetime")
print("import os")
print("import statistics")
print()

print("math Module")
import math
print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))
print(math.ceil(4.2))
print(math.floor(4.8))
print()

print("Random Module")
print("Random")
import random
print(random.randint(1, 125))

print("Choice")
import random
fruits = ["Apple", "Banana", "Carrot"]
print(random.choice(fruits))

print("Shuffle")
import random
number = [1, 2, 3, 4, 5]
random.shuffle(number)
print(number)

print("datetime")
import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print("Today's Date:", today)
print("Current Date and Time:", now)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print()

print("Importing Specific Functions")
print("from module_name import function_name")
from math import sqrt
print(sqrt(81))

import math
print(math.sqrt(64))

from math import sqrt, factorial, pi
print(sqrt(121))
print(factorial(10))
print(pi)
print()

print("Alias (as)")
print("Module name as alias")
import math as m
print(m.factorial(6))
print(m.sqrt(36))
print(m.pi)
print("Real Examples")
print("import pandas as pd")
print("import Numpy as np")
print("matplotlib.pyplot as plt")
print()

print("Modules vs Packages")
print('''Module are Single Python File
Example: calculator.py
contains functions, variables, classes
            vs
Package is a Collection of Related Module
Example: mypackage/
organises multiple modules together''')
print()
print()

print("Practice Assignments")
print("1.Math Module")
import math
print(sqrt(144))
print(factorial(6))
print(pi)
print(math.ceil(8.3))
print(math.floor(8.9))
print()

print("2.Random Number Generator")
import random
print(random.randint(1, 50))
print(random.randint(100, 999))
print()

print("3.Random Choice")
import random
veggies = ["Tomato", "Chilly", "Onion", "Leaves", "Garlic"]
print(random.choice(veggies))
print()

print("4.Date information")
import datetime
current = datetime.date.today()
print(current)
print(current.year)
print(current.month)
print(current.day)
print()

print("5.Alias")
import math as m
print(m.sqrt(225))
print(m.factorial(4))
print(m.pi)
print()

print("Own Module")
print('''def addition(a, b):
    return a + b
def subraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b''')

print('''import calculator
print(calculator.add(10, 5))
print(calculator.subract(50, 20))
print(calculator.multiply(6, 5))
print(calculator.divide(150, 15))''')
print()

print("Knowledge Test")
print('''1. What is a Python module?
Module is a Python File which can be reused at Anywhere in the Project.
2. Why do we use modules?
Instead writing the same Code we required to, We can call it to save Time.
3. What is the purpose of import?
The import statement allows us to use modules and their functions in our Python program.
4. What does math.sqrt(49) return?
Returns 7
5. Which module generates random numbers?
import random Module
6. What does random.choice() do?
chooses the random pick in List[].
7. Which module is used for date and time?
import datetime
8. What is the difference between import math and from math import sqrt?
Both work. The difference is how we access the function.
9. What is an alias in Python?
An alias is an alternative name given to a module or function using the as keyword.
10. What is the difference between a module and a package?
module is a python file and package is a collection of multiple modules''')