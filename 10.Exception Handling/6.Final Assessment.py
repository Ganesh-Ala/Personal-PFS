try:
    age = int(input("Enter Your Age: "))
    if age < 0:
        raise ValueError("Age cannot be a Negative.")
    elif age < 18:
         print("You are a Minor.")
    else:
         print("You are an Adult.")
except ValueError: ("Check Your Age Once Again.")
else:
    print("Age is Successfully Verified")
finally:
    print("You Age Verification Page was Ended")