print("ReChallenge")

try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Addition:",a + b)
    print("Subraction:",a - b)
    print("Multiplication:",a * b)
    print("Division:",a / b)
except ValueError:
    print("Something Invalid You Entered")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
print()



#print("Mini Challenge")         #Selfly Tried but Wrong One.
#print('''Safe Calculator
#a = (input("Enter a Number: "))
#b = input("Enter b Number: ")
#if a == 10 or "ten" and b == 0 or "zero":
#    print(a + b)
#else:
#    print("Invalid Entry")
#if a == 10 or "ten" and b == 0 or "zero":
#    print(a - b)
#else:
#    print("Invalid Entry")
#if a == 10 or "ten" and b == 0 or "zero":
#    print(a * b)
#else:
#    print("Invalid Entry")
#if a == 10 or "ten" and b == 0 or "zero":
#    print(a / b)
#else:
#    print("Invalid Entry)''')