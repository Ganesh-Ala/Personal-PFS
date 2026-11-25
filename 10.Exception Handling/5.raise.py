age = int(input("Enter Your Age here: "))
if age < 0:
    raise ValueError("You entered negative Number.")
print("Your age is Verified: ", age)