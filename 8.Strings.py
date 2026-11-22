print("What is String")
print("A String is a sequence of characters enclosed within Quotation Marks")
print('''Letters: "Python"
Numbers: "1234"
Symbols: "!@#$%"
Spaces:  "Hello World"     
Combinations: "Ganes#@2003Online"
''')

print("Example:")
name = "Ala Ganesh"
age = "23"
print(name)
print(age)
print(type(name))
print(type(age))
print()

print("Creating Strings")
name = 'Ganesh'                 #Single Quote
print(name)
name = "Ala Ganesh"                #Double Quotes
print(name)
name = '''Hello Ganesh,
        Welcome to Python'''   #Triple Quotes
print(name)
print()

print("Strings Indexing")
name = "Ala Brahmendrarao"
print(name[10])
print(name[1])
print(name[6])
print(name[4])
city = "Hyderabad"
print(city[0])
print(city[2])
print(city[6])
print()

print("Negative Indexing")
party = "Congress"
print(party[-3])
print(party[-7])
print()

print("String Slicing")
name = "varalakshmi"
print(name[0:4])
print(name[4:11])
name = "venkateswarlu"
print(name[1:6])
print(name[6:12])
print()

print("Shortcut Slicing")
name = "lakshmi narasamma"
print(name[3:])
print(name[8:])
print(name[:7])
print(name[:12])
print()

print("Slicing with Steps")
name = "Asirvadham"
print(name[1:10:2])
print(name[0:9:3])
name = "vanajakshi"
print(name[::2])
print()

print("Reversing a String")
name = "hsenag"
print(name[::-1])
print(name[::-2])
print()

print("String Length")
name = "Pedda NarasimhaRao"
print(len(name))
print()

print("Changing Case")
name = "Mangamma"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print()

print("Removing an Extra Space")
name = "   Dadi Gopi    "
print(name)
print(name.strip())
print(name.rstrip())
print(name.lstrip())
print()

print("Replacing a String")
name = "veera kumari"
new_name = name.replace("veera", "dheera")
print(new_name)
language = "I Love Java"
update_language = language.replace("Java", "Python")
print(update_language)
print()

print("Search inside a String")
message = ("My name is Ganesh and learning Python")
print(message.find("Python"))
message2 = "I'm from Palnadu"
print(message2.find("Palnadu"))
print()

print("Counting Characters")
tech = "Python is Easy and Used in AI as AI"
print(tech.count("Python"))
print(tech.count("AI"))
fruit = "Pomegranate"
print(fruit.count("a"))
print()

print("Checking the Begining and Ending")
line = "Basically I like Coding"
print(line.startswith("Basically"))
print(line.startswith("like"))
print(line.endswith("Coding"))
print(line.endswith("I"))
print("Example")
filename = "Doc.pdf"
if filename.endswith(".pdf"):
    print("File Accepted.")
else:
    print("Choose Another File")
print()

print("Splitting a String")
course = "Python Full Stack"
print(course.split())
print(len(course))
details = "Ganesh,22,Python,Hyd"
print(details.split(","))
print(len(details))
print()

print("Joining Strings")
info = "Ganesh", "22", "Python", "Hyd"
print(" ".join(info))
print("-".join(info))
date = "6", "9", "2003"
print("-".join(date))
print("/".join(date))
print()

print("Checking String Contents")
name = "Ganesh"
print(name.isalpha())
number = "123456"
print(number.isdigit())
combo = "Ganesh2003"
print(combo.isalnum())
combo = "Ganesh@2003"
print(combo.isalnum())
space = "Ganesh Ala"
print(" ".isspace())
name = "ala ganesh"
print(name.islower())
print(name.isupper())
name = "ALA GANESH"
print(name.isupper())
print(name.islower())
print()

print("String Membership")
message = "I'm Learning Python and SQL"
print("Python" in message)
print("SQL" in message)
print("Java" in message)
print("Java" not in message)
validation = "ganesh@gmail.com"
if "@" in validation:
    print("Mail is Valid")
else:
    print("InValide Mail Address")
print()

print("String Concatenation")
first = "ALA"
second = "GANESH"
print(first + " " + second)
print("Joining Strings and Numbers")
age = 23
print("My age is:", age)
print("My age is: " + str(age))
print()

print("String Formatting and f-strings")
name = "Ala Ganesh"
age = 23
course = "Python Full Stack"
print(f"My name is {name}. I'm {age} years old.I choose {course} as My Carrer.")
price = 250
quantity = 4
total = price * quantity
print(f"Your price per Quantity is {price} then Your Quantity is {quantity} and Total Bill is {total}")
print()

print("String Immmutability")
name = "Sai Janesh"
new_name = "G" + name[5:]
print(new_name)
name2 = "AshtaLakshmi"
new_name2 = "Vara" + name2[5:]
print(new_name2)
print()

print("Combining Everything")
first = input("Enter Your First Name: ")
second = input("Enter Your Second Name: ")
birth = input("Enter Your Birth Year ")
details = first.strip().title() + second.strip().title() + birth
print(details)
print()
print()

print("Practical Assignments")
print("1. Basic String")
name = "Ganesh"
college = "Bharath University"
course = "Python Full Stack"
city = "Chennai"
print(name)
print(college)
print(course)
print(city)
print()

print("2. String Indexing")
name = "PYTHON"
print(name[1])
print(name[3])
print(name[5])
print(name[-2])
print()

print("3. String Slicing")
name = "PYTHON PROGRAMMING"
print(name[0:6])
print(name[8:18])
print(name[0:3])
print(name[-4:])
print(name)
print(name[::-1])
print()

print("4. String Methods")
name = "   ala ganesh   "
print(name.strip())
print(name.upper())
print(name.lower())
print(name.title())
print(len(name.strip()))
print()

print("5. Replace")
message = "I am learning Java"
new_one = message.replace("Java", "Python")
print(new_one)
print()

print("6. Character Counting")
word = "banana"
print(len(word))
print(word.count("a"))
print(word.count("n"))
print(word.find("b"))
print()

print("Email Checker")
mail = "alaganesh@gmail.com"
if ("@") in mail and mail.endswith (".com"):
    print("Valid")
else:
    print("Check the mail")
print()

print("Split and Join")
words = "Ala Ganesh Python Full Stack"
words2 = words.split()
print(words2)
print(words2)
print("-".join(words2))
print()

print("9. Username Generator")
first_name = input("Enter Your Initial: ")
second_name = input("Enter Your Name: ")
birth_year = input("Enter Your Birth Year: ")
user = first_name.strip() + second_name.strip()
username = user.lower() + birth_year.strip()
print("Username:", username)
print()

print("10. Password Analyzer")
password = "Ganesh69"
if len(password) >= 8:
    print("Yes, It Contains 8 Characters")
else:
    print("Minimum 8 Characters are Required")
if any(char.isdigit() for char in password):
    print("Contains Numbers")
else:
    print("Add Numbers")
if password.isalpha():
    print("Yes, It contains Alphabets")
else:
    print("Add Alphabets ")
if password.isupper():
    print("Yes, It contains Uppercase")
else:
    print("Update with Uppercase Letters")
if password.islower():
    print("Contains Lowercase")
else:
    print("No Lowercase Letters")
print()
print()

print("Knowledge Test")
print("What is String ?")
print("A String is a Data Type in Python and assigns to a Variable as a Value with Quote Marks(" ").")
print('''What is the output?
name = "PYTHON"
print(name[2])
''')
print("T")
print('''What is the output?
name = "GANESH"
print(name[-1])''')
print("H")
print('''What is the difference between:
name[0:3]
name[:3]''')
print("Both are same because Indicating 0 will start the Index from 0 and :3 also starts the indexing from 0.")
print('''What is the output?
word = "Python"
print(word[::-1])''')
print("nohtyp")
print("What does len() do?")
print("Tells the Length of a Value")
print("What is the difference between upper() and lower()?")
print("Makes the Letter to Total UPPER CASE and lower case.")
print("What does strip() do?")
print("Removes the Unwanted Spaces.")
print('''What is the output?
text = "banana"
print(text.count("a"))''')
print("3")
print("What is the difference between split() and join()?")
print("split is used to make the senstence into seperate words and join is used to add the seperate words as a sentence")
print('''What does this return?
print("12345".isdigit())''')
print("True")
print('''What is the output?
name = "Ganesh"
age = 22
print(f"My name is {name} and my age is {age}.")''')
print("My name is Ganesh and my age is 22.")
print("Are Python strings mutable or immutable?")
print("Immutable")
print('''What is the output?
text = "Python Programming"
print("Python" in text)
print("Java" in text)''')
print('''True
False''')
print('''What happens when you run this?
name = "Ganesh"
name[0] = "A"''')
print("TypeError: 'str' object does not support item assignment")
print()
print()

print("Final Coding Challenge")
word = input("Enter your Word: ")
print(word.lower().lower())
print(word[::-1])
print(word and word[::-1])
if word == word[::-1]:
    print("It is a Palindrome.")
else:
    print("Not a Palindrome.")