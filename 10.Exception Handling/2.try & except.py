try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print(a / b)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")