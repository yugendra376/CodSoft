import string
import random

# Prompt the user to enter the desired password length
password_length = int(input("Enter the desired length of the password: "))

# Generate the password
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(password_length))

# Display the generated password
print("Your generated password is:", password)
