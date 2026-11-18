#####################################################################
## Becky Samson L2 : Control Flow
## Functions
## Date 10/11/2026
#####################################################################

# validate password program
# User-defined function, built-in function, built-in module, and decision making using if, if not, if else.

import re # import built-in module named re which provides a set of powerful regular expression facilities

def validate_password(password): # user-defined function named validate_password
    
   # update password length to 10
    if len(password) < 10: # len is a built-in function 
        return False  
    if not re.search("[a-z]", password):  
        return False  
    if not re.search("[A-Z]", password):  
        return False  
    if not re.search("[0-9]", password):  
        return False  
    return True  
  
password = input("Create a new password")  
if validate_password(password):  
    print("Valid password")  
else:  
    print("Invalid password, try again. Choose a better password!!") # edited output for invalid password

