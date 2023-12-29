import random
import string

def generate_password(minLength,numbers=True,specialCharacters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specialCharacters:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < minLength:
        newChar = random.choice(characters)
        pwd += newChar

        if newChar in digits:
            has_numbers = True
        elif newChar in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if specialCharacters:
            meets_criteria = has_special and meets_criteria

    return pwd

passLength = int(input("Enter the length of the passsword: \n"))
hasNum = input("Do you want numbers? (y/n)").lower() == "y"
hasSpecial = input("Do you want special characters? (y/n)").lower() == "y"

passwd = generate_password(passLength, hasNum, hasSpecial)
print("Your Password is: ", passwd)
