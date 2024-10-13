import random
import string

def generate_password(lenth):
    if lenth < 6:
        return "Password length must be at least 6 characters!!"
    
    lowercase_Char = string.ascii_lowercase
    uppercase_Char = string.ascii_uppercase
    digits = string.digits
    specialChar = string.punctuation

    password = [random.choice(lowercase_Char), random.choice(uppercase_Char),
                random.choice(digits), random.choice(specialChar)]
    
    allchartogether = lowercase_Char + uppercase_Char + digits + specialChar
    password += random.choices(allchartogether, k=lenth - len(password))
    random.shuffle(password)
    
    return ''.join(password)

password_length = random.randint(6, 10)
password = generate_password(password_length)
print("Generated password =", password)
