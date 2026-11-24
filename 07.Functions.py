print("Day 7 - Functions")

print("What is a Function?")
print("A function is a block of code designed to perform a particular task.")
print('''Real-life example:
Imagine a washing machine.
You press the Start button, and the machine performs several operations:
- Fill water
- Wash clothes
- Rinse
- Spin

You don't need to manually perform every operation each time. You simply call the machine's washing process.

In Python, a function works similarly.
Instead of writing the same code repeatedly, we create a function and call it whenever necessary.''')
print()

print("Without a Function")
print("Task: Print greetings 3 times")
print("Manually:")
print("Hello Ganesh!")
print("Welcome to Python.")
print("Hello Ganesh!")
print("Welcome to Python!")
print("Hello Ganesh!")
print("Welcome to Python.")
print()

print("With a Function")

def greet():
    print("Hello Ganesh!")
    print("Welcome to Python.")

greet()
greet()
greet()
print()

print("Creating a Function")
print("def is the keyword used to create a function.")

print("1. Example:")

def welcome():
    print("Welcome to Python Full Stack Course!")

welcome()

print("2. Example:")

def hello():
    print("Hello!")

hello()
print()

print("Functions with Parameters")
print("Example: Greet Different People.")

def greet(name):
    print("How are you,", name, "?")

greet("Ben")
greet("Kevin")
greet("Max")

print("name, which is present inside the parentheses, is called a Parameter.")
print("Names or values passed during function calling are called Arguments.")
print()

print("Functions with Multiple Parameters")
print("Addition Calculator")

def add(a, b):
    print("Addition:", a + b)

add(10, 20)
add(10, 99)
add(15, 20)
print()

print("Example 2:")
print("Student Details")

def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_details("Ganesh", 22, "PFS")
student_details("Tharun", 21, "JFS")
print()

print("Return Statement")
print("Sometimes we need a function to calculate something and send the result back so that we can use it somewhere else.")
print("That's where return comes in.")
print()

print("Using print()")

def sub(a, b):
    print("Subtraction of a and b:", a - b)

sub(100, 69)
print()

print("Using return")

def mul(a, b):
    return a * b

product = mul(10, 5)
print(product)

print("Example")

def marks(a, b, c):
    return a + b + c

all_marks = marks(85, 92, 98)

print("Total:", all_marks)
print("Double:", all_marks * 2)
print("Square:", all_marks ** 2)
print()

print("Real-World Example")
print("Billing Application")

def calculate_bill(price, quantity):
    return price * quantity

bill = calculate_bill(120, 4)
print("Your Bill is:", bill)
print()

print("Functions with Conditions")
print("Example")

def check_age(age):
    if age >= 18:
        return age, "You are Eligible to Vote."
    else:
        return age, "You are a Minor."

print("Your age is:", check_age(25))
print("Your age is:", check_age(17))
print()

print("Example 2")

def check_number(number):
    if number % 2 == 0:
        return number, "Yes, It is an Even Number."
    else:
        return number, "No, It is an Odd Number."

print(check_number(52))
print(check_number(7))
print()

print("Default Parameters")

def greet(name="Ganesh"):
    print("Hello", name)

greet()
greet("Raj")
print()

print("Another Example")

def calculate_bill(price, quantity=1):
    return price * quantity

print(calculate_bill(120, 4))
print(calculate_bill(50, 2))
print()

print("Keyword Arguments")

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student(age=23, course="PFS", name="Ala")
print()

print("Variable-Length Arguments")

def add_numbers(*numbers):
    total = sum(numbers)
    print("Total:", total)

add_numbers(10, 20)
add_numbers(20, 30, 50)
add_numbers(50, 100, 150)
add_numbers(50, 100, 150, 1)
print()

print("Function with a Loop")

def table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

table(15)
table(12)
table(20)
print()

print("Mini Project: Calculator")

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero."
        return a / b
    else:
        return "Invalid Operator."

print(calculator(5, 2, "+"))
print(calculator(5, 9, "-"))
print(calculator(10, 5, "/"))
print(calculator(6, 0, "/"))
print(calculator(0, 9, "/"))
print(calculator(50, 4, "*"))
print(calculator(12, 2, "5"))
print()
print()

print("Practical Assignments")

print("1. Welcome Function")

def greet():
    print("Welcome to Python Full Stack Development!")

greet()
greet()
greet()
print()

print("2. Personal Greeting")

def name(enter):
    print("Hello Bro", enter)

name("Ala")
name("Ganesh")
print()

print("3. Addition Function")

def add(a, b):
    return a + b

result = add(15, 10)
print(result)
print()

print("4. Student Details")

def student(name, age, course, city):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("City:", city)

student(name="Ganesh", age=23, course="PFS", city="HYD")
print()

print("5. Even or Odd")

def check_number(number):
    if number % 2 == 0:
        return "Number is Even"
    else:
        return "It is an Odd Number"

print(check_number(5))
print(check_number(254))
print()

print("6. Marks Calculator")

def student(m1, m2, m3, m4, m5):
    marks = (m1, m2, m3, m4, m5)

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest

total, average, highest, lowest = student(85, 92, 78, 95, 88)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print()

print("7. Default Arguments")

def bill(price, quantity=1):
    total = price * quantity
    return total

single_item_bill = bill(250)
print("Total Bill (default quantity 1):", single_item_bill)

multiple_items_bill = bill(250, 4)
print("Total Bill (quantity 4):", multiple_items_bill)
print()

print("8. Multiplication Table")

def table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

table(5)
print()

print("9. Simple Calculator")

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero."
        return a / b
    else:
        return "Invalid Operator."

print(calculator(5, 10, "+"))
print(calculator(56, 6, "-"))
print(calculator(60, 6, "/"))
print(calculator(15, 5, "*"))
print(calculator(0, 5, "/"))
print(calculator(0, 0, "/"))
print()

print("10. Employee Salary Calculator")

def calculate_salary(name, salary):
    hra = salary * 0.20
    da = salary * 0.10
    total = salary + hra + da

    return name, salary, hra, da, total

name, salary, hra, da, total = calculate_salary("Vinith", 35000)

print("Employee Name:", name)
print("Basic Salary:", salary)
print("HRA:", hra)
print("DA:", da)
print("Total Salary:", total)
print()
print()

print("Knowledge Test")

print("Which keyword is used to create a function in Python?")
print("Answer: def")

print('''What is the output?
def greet():
    print("Hello")

greet()
greet()''')

print("Hello")
print("Hello")

print('''In this code, identify the parameter and arguments.
def add(a, b):
    return a + b

add(10, 20)''')

print("Parameters: a, b")
print("Arguments: 10, 20")

print("What is the main difference between print() and return?")
print("print() displays output, while return sends a value back from the function so it can be reused in calculations.")

print('''What will this code output?
def multiply(a, b=2):
    return a * b

print(multiply(5))
print(multiply(5, 3))''')

print(10)
print(15)
print()
print()

print("Final Coding Challenge: Discount Calculator")

def calculate_discount(price, discount_percentage):
    discount = price * discount_percentage / 100
    final_price = price - discount

    return discount, final_price

discount, final_price = calculate_discount(1000, 10)

print("Original Price:", 1000)
print("Discount Amount:", discount)
print("Final Price:", final_price)