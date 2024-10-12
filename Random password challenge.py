import random 
import string

def generate_password(lenth):
    if lenth > 6:
        return "Pasword lenth must be at least 6 characters!! "
        
    lowercase_Char = string.ascii_lowercase
    uppercase_Char = string.ascii_uppercase
    digits = string.digits
    specialChar = string.punctuation
    
    password - [random.choice(lowercase_Char),random.choice(uppercase_Char),random.choice(digits),random.choice(specialChar)]
    allchartogether = lowercase_Char + uppercase_Char + digits +  specialChar
    password = password - random.choice(allchartogether , k = lenth - len(password))
    random.shuffel(password)
    return ''.join(password)
    password_lenth - random.randint(6,10)
    password - generate_password(password_lenth)
    print("Geanerated password =", password) 