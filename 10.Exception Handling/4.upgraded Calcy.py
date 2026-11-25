try:
    a = int(input("Enter Your First Number: "))
    b = int(input("Enter Your Second Number: "))
    print("Addition:", a+b)
    print("Subtraction: ", a-b)
    print("Multiplication: ", a*b)
    print("Division: ", a/b)
except ValueError:
    print("This is Invalid Input.")
except ZeroDivisionError:
    print("Cannot be Divided by Zero.")
else:
    print("Numbers are Valid.")
finally:
    print("Calcy Program Ended.")