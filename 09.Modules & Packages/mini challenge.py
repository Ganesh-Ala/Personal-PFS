import random
import string
characters = list(string.ascii_letters + string.digits + string.punctuation)
password = "".join(random.choices(characters, k=8))
print(f"Generated Password: {password}")
