print("Python Tuples and Sets")
print("What is Tuple ?")
print("A Tuple is a Python Data Type, used to store Multiple values in Single Variable.") 
print("It's similar to a List but Difference between them is, Tuple cannot be Modified after it is created.")
print()

print("Example")
print("Python Tuple")
student = ("Ganesh", 23, "Male", 7.70)
print(student)
print()

print("List vs Tuple")
print("List is a Shopping List, We can Add or Remove in it.")
print("Tuple is a Date of Birth, Can't or Don't Change")
print()

print("Creating Tuples")
numbers = (12, 16, 46, 86, 92, 24, 64)
names = ("Hari", "Shiva", "Ram", "Krishna")
mixed = ("Gopi", 34, 7.70)
empty = ()
print(numbers)
print(names)
print(mixed)
print(empty)
print()

print("IMPORTANT: ',' is mandatory even Single Element in Tuple")
print("Example")
a = (10,)
print(type(a))
print()

print("Indexing Tuples")
fruits = ("Apple", "Banana", "Orange", "Papaya", "WaterMelon")
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[-3])
print(fruits[-2])
print(fruits[-1])
print()

print("Tuple Slicing")
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[2:4])
print(numbers[4])
print(numbers[:4])
print(numbers[2:])
print(numbers[::-1])
print()

print("Tuple Methods")
numbers = (5, 10, 15, 20, 25, 30, 35, 20, 40, 45)
print(numbers.count(20))
print(numbers.index(40))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(len(numbers))
print()
print()

print("Python Sets")
print("What is a Set  ?")
print("Set is a Python Data type, used to store Multiple Unique Values.")
print("IMPORTANT: Sets DON'T ALLOW DUPLICATE ELEMENTS")
print("Example")
numbers = {10, 20, 30, 20, 40}
print(numbers)
print()

print("Creating Sets")
numbers = {10, 20, 30, 40, 50, 60}
names = {"Ganesh", "Gopi", "Shankar", "Sagar"}
empty_set = set()
print(numbers)
print(names)
print(empty_set)
print()

print("Adding an Element")
fruits = {"Apple", "Banana"}
fruits.add("Carrot")
print(fruits)
veggies = {"Tomato", "Chillies"}
veggies.update(["Potato", "Onion"])
print(veggies)
print()

print("Removing an Element")
numbers = {10, 30, 50, 70, 60}
numbers.remove(60)
print(numbers)
numbers.discard(30)
print(numbers)
print()

print("Set Operations")
A = {10, 30, 50, 70, 20}
B = {20, 40, 60, 80, 30}
print(A.union(B))            #  print(A|B)
print(A.intersection(B))     #  print(A&B)
print(len(A | B)) 
print(A.difference(B))
print(A.symmetric_difference(B))
print()

print("Practical Assignments")
print("Assignment 1")
name = ("Ganesh", 23, "CSE", 7.70)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print()

print("Assignment 2")
numbers = (10, 20, 30, 20, 40, 20, 50)
print(len(numbers))
print(numbers.count(20))
print(numbers.index(40))
print(max(numbers))
print(min(numbers))
print()

print("Assignment 3")
numbers = [10, 20, 30, 20, 40, 10, 50, 30]
set_numbers = set(numbers)
print(set_numbers)
print()

print("Assignment 4")
python_students = {"Ganesh", "Ravi", "Abhi", "Gopi"}
java_students = {"Ravi", "Vishnu", "Ganesh", "Kiran"}
print(python_students & java_students)
print(python_students - java_students)
print((python_students | java_students))
print(java_students - python_students)
print()

print("Assignment 5")
print("Mini Project - Course Enrollment System")
python = {"Ganesh", "Gopi", "Raju", "Nani"}
full_stack = {"Hema", "Praveen", "Sunny", "Narendra"}
python.add("Karthik")
print(python)
python.remove("Nani")
print(python)
print(python | full_stack)
print(python & full_stack)
python_stu = python - full_stack
print(python_stu)
print()
print()

print("Knowledge Test")
print("Q1. Which symbol is used to create a Python tuple?")
print("()")
print("Q2. Can we modify a tuple after creating it?")
print("No")
print("Q3. Which method counts occurrences in a tuple?")
print("count()")
print("Q4. Which Python data type automatically removes duplicates?")
print("Set")
print("Q5. How do you create an empty set?")
print(set())
print("Q6. Which set operation returns common elements?")
print("Intersection")
print("Q7. What does A.difference(B) return?")
print("Elements in A but not B(Unique Values will be Printed Compared to A and B.)")
print()

print("Final Coding Test")
print("1. Create a tuple containing 5 numbers. Print the first and last elements.")
numbers = (1, 2, 3, 4, 5)
print(numbers[0])
print(numbers[4])
print()

print("2.Given A = {10, 20, 30, 40} and B = {30, 40, 50, 60}, print only the common elements.")
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print(A.intersection(B))
print(A & B)
print()

print("3. Given a list [10, 20, 10, 30, 20, 40, 50], convert it into a set and print the unique elements.")
A = [10, 20, 10, 30, 20, 40, 50]
print(set(A))
