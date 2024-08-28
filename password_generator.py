import random
import string

def generate_password(length, include_numbers=True):

    # define characters
    letters = string.ascii_letters
    numbers = string.digits

    # create character pool
    character_pool = letters

    if include_numbers:
        character_pool = letters + numbers
    
    # create password
    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

# get user inputs
length = int(input("Enter desired password length (minimum 10): "))
include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"

# validate length
if length < 10:
    print("Password must be minimum 10 characters long")
else:
    password = generate_password(length, include_numbers)
    print("success, password is " + password)
