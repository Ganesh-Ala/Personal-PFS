print("Day-4: Lists and List Operations")

print()

print("List is a Python Data Type used to store Multiple Values in a Single Variable.")
print()

print("Without List")
marks1 = 95
marks2 = 89
marks3 = 92
marks4 = 85
marks5 = 97
print(marks1, marks2, marks3, marks4, marks5)
print()

print("With List")
marks = [95, 89, 92, 85, 97]
print(marks)
print()

print("Examples")
print("List of Numbers")
Numbers = [85, 90, 78, 92, 88]
print(Numbers)

print("List of Names") 
Names = ["Ganesh", "Ravi", "Abhi"]
print(Names)

print("List of Names and Numbers")
Strings = ["Ganesh",  23, "6-9-2003"]
print(Strings) 

print("Example of Indexing/Accessing the List Elements")
fruits = ["Banana", "Apple", "Orange", "Mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[0])
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[0])
print()

print("Updating Elements in List")
fruits = ["Mango", "Apple", "Guava"]
fruits[1] = "Grapes"
print(fruits)
print()

print("Adding Elements in List")
Games = ["Cricket", "Volleyball", "Kabadi"]
Games.append("Running Race")
print(Games)
print()

print("Inserting an Element at Particular Position")
Life = ["Birth", "School", "Skills", "Work", "Success", "Happy"]
Life.insert(2, "Degree")
print(Life)
print()

print("Adding Multiple Items")
Veggies = ["Tomato", "Chillies"]
Veggies.extend(["Onion", "Curry Leaves"])
print(Veggies)
print()

print("Removing Elements in the List")
Grades = ["A+", "A", "C", "B+", "B"]
Grades.remove("C")
print(Grades)
print()

print("Removing an Element by Indexing")
keyboard = ["Q", "W", "E", "R", "Z", "Y"]
keyboard.pop(4)
print(keyboard)
print()

print("Length of List")
numbers = [1, 2, 3, 4, 5]
print(len(numbers))
print()

print("Sum of List")
add = [1, 5, 9, 3, 7]
print(sum(add))
print()

print("Maximum Number of List")
digits = [10, 52, 95, 99, 85, 54]
print(max(digits))
print()

print("Minimum of List")
mark = [75, 82, 79, 95, 86]
print(min(mark))
print()

print("Sorting Elements in List")
CGPA = [8, 6, 9, 7, 10, 5]
print(sorted(CGPA))
print()

print("Sorting & Reversing")
CGPA = [8, 6, 9, 7, 10, 5]
CGPA.sort()
print(CGPA)
print("Reversing a List")
CGPA.sort(reverse=True)
print(CGPA)
CGPA.reverse()
print(CGPA)
print()

print("Looping through Lists")
names = ["Ganesh", "Gopi", "Vishnu"]
for boys in names:
    print(boys)
print()

marks = [85, 90, 78, 92, 88]
total = 0
for numbers in marks:
    total = total + numbers
print("Total Marks: ", total)
print("Average: ", total/len(marks))
print()
print()

print("Practical Assignments")
print("1.Student Marks")
marks = [95, 90, 84, 99, 92, 80, 70]
print(marks)
print(marks[0])
print(marks[6])
print(len(marks))
print()

print("2.Shopping List")
items = ["Rice", "Dal", "Oil", "Veggies", "Milk"]
items.append("Snacks")
print(items)
items.insert(1, "Sugar")
print(items)
items.remove("Oil")
print(items)
print()

print("3.Marks Calculator")
marks = [85, 90, 78, 92, 88]
a = sum(marks)
print(a)
print(a/len(marks))
print(max(marks))
print(min(marks))
marks.sort()
print(marks)
print()

print("4.Number Analysis")
numbers = [1, 7, 9, 5, 12, 3, 15, 17, 13, 19]
for digits in numbers:
    print(digits)

for digits in numbers:
    if digits % 2 == 0:
        print(digits)

total = 0

for digits in numbers:
    total = total + digits

print("Total:", total)
print()

print("5.Mini Project: Student Marks Assignment")
marks = []

for i in range(5):
    mark = int(input("Enter student marks: "))
    marks.append(mark)

print("Marks:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))

marks.sort()
print("Ascending Order:", marks)
print()
print()

print("Knowledge Test")
print("Q1. What is the index of the first element in a Python list ?")
print("0")
print()

print("Q2. Which method adds an element to the end of a list ?")
print("append")
print()

print("Q3. What does fruits[-1] return ?")
print("Last Item")
print()

print("Q4. Which method removes an item by its value ?")
print("remove()")
print()

print("Q5. What does len([10,20,30,40]) return ?")
print(4)
print()

print("Q6. Which method sorts a list in descending order ?")
print("sort(reverse=True)")
print()

print("Q7. Are Python lists mutable ?")
print("Yes")
print()

print("Final Tasks")
print("Even Number Finder")
numbers = [10, 15, 20, 25, 30, 35, 40]
for figures in numbers:
    if figures % 2 == 0:
        print(figures)
print()

print("Total and Average")
marks = [75, 85, 90, 65, 95]
total = 0
for mark in marks:
    total = total + mark
average = total/len(marks)
print(total)
print(average)
print()

marks = []

for i in range(5):
    mark = int(input("Enter Marks: "))
    marks.append(mark)

total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))