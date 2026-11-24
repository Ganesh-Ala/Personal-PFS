print("Day-6: Dictionaries")
print("What is a Dictionary ?")
print("A Python Dictionary stores Data in Key-Value Pairs.")
print("Example:")
print("Instead of printing above Variables, Dictionary can print at a Time.")
student = {
    "name" : "Ala Ganesh",
    "age" : 23,
    "course" : "Python Full Stack",
    "city" : "Hyderabad"
}
print(student)
print()

print("Accessing Dictionary Values")
student = {
    "name" : "Vikram",
    "age" : 25,
    "path" : "IT"
}
print(student["name"])
print(student["age"])
print(student["path"])
print("Alternatice Code")
print(student.get("name"))
print(student.get("age"))
print(student.get("age"))
print(student.get("marks"))
print()

print("Adding and Updating Elements")
student = {
    "name" : "venkat",
    "age" : 28,
    "city" : "HYD"
}
student["status"] = "Enrolled"
print(student)
student["name"] = "Shiva"
print(student)
student.pop("name")
print(student)
print('Some Other Methods')
student.popitem()
print(student)
del student ["age"]
print(student)
student.clear()
print(student)
stu_copy = student.copy()
print(stu_copy)
print()

print("Examples")
student = {
    "name": "Ganesh",
    "age": 22,
    "city": "Hyderabad"
}
print(student.keys())
print(student.values())
print(student.items())
print()

print("Looping through Dictionaries")
student = {
    "name": "Ganesh",
    "age": 22,
    "city": "Hyderabad"
}
print("Loops for Keys")
for key in student:
    print(key)
print("Loops for Values")
for value in student.values():
    print(value)
print("Loops for both Key and Value")
for key, value in student.items():
    print(key, ":", value)
print()

print("Practical Example")
student = {
    "name" : "Ganesh",
    "python" : 95,
    "sql" : 92,
    "html" : 98,
    "css" : 94,
    "js" : 98
}
total = student["python"] + student["sql"] + student["html"] + student["css"] + student["js"]
print(student["name"])
print("Total Marks: ", total)
print("Average is: ", total/5)
print()
print()

print("Practical Assignment")
print("1.Employee Details")
employee_details = {
    "name" : "Suraj",
    "id" : "4765",
    "age" : 27,
    "department" : "Software",
    "salary" : 50000
}
print(employee_details["name"])
print(employee_details["id"])
print(employee_details["age"])
print(employee_details["department"])
print(employee_details["salary"])
print("or")
for value in employee_details.values():
    print(value)
print()

print("2.Product Management")
product = {
    "name" : "milk",
    "price" : 80,
    "quantity" : "1litre"
}
product["category"] = "Dairy"
print(product)
product["price"] = 90
print(product)
product.update({"price" : 95, "quantity" : "500ml"})
print(product)
print()

print("3.Contact Book")
contacts = {
    "Jio" : 99,
    "Airtel" : 95,
    "V!" : 97
}
contacts["BSNL"] = 90
print(contacts)
contacts["Jio"] = 98
print(contacts)
contacts.pop("Airtel")
print(contacts)
print()

print("4.Student Marks")
subjects = {
    "eng" : 95,
    "sci" : 92,
    "soc" : 90,
    "math" : 98,
    'gk' : 98
}
total = subjects["eng"] + subjects["sci"] + subjects["soc"] + subjects["math"] + subjects["gk"]
print(total)
average = total/5
print(average)
print(max(subjects.values()))
print(min(subjects.values()))
print()

print("Mini Project: Student Management System")
student = {
    "name" : "vishnu",
    "roll number" : "101",
    "mark1" : 99,
    "mark2" : 98
}
print(student)
student["mark1"] = 9999
print(student)
average = (student["mark1"] + student["mark2"]) / 2
print(average)
print()

print("Knowledge Test")
print("Which brackets are used to create a Python dictionary?")
print("{}")
print("How do you access the value of the key 'name'?")
print("student", "[" "name" "]")
print("Which method returns all key-value pairs?")
print(".items()")
print("What happens when you use get() with a missing key and no default value?")
print("None")
print("Which method removes all dictionary elements?")
print("Clear()")