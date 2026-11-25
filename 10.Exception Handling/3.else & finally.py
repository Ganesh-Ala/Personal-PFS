print("else")
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot be divided by Zero.")
except ValueError:
    print("Enter Valid Number.")
else:
    print("Result: ", result)
    print("Program Executed Successfully.")
print()

print("finally")
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print (a / b)
except ZeroDivisionError:
    print("Cannot divide by Zero")
except ValueError:
    print("Invalid Input")
finally:
    print("Program Ended.")