#####################################################################
## Becky Samson L1 : Data Types, Structures and Operators
## Comparison & assignment operators
## Date 09/11/2026
#####################################################################

# Password and username checking program
# using COMPARISON, LOGICAL and ASSIGNMENT operators

actual_password="password" # assignment operator
entered_password=str(input("Enter your password: ")) # assignment operator

if (entered_password!=actual_password): # relational operator 'not equal to'
    print("Invalid password")  
else:  
    print("Valid password") 

# CHALLENGE: Now let's incorporate a username and logical operators:
actual_username="becky" # assignment operator
entered_username=str(input("Enter your username: ")) # assignment operator

if (entered_password!=actual_password) or (entered_username!=actual_username): # logical operator 'or'
    print("Invalid username or password")  
else:  
    print("Valid username and password") 
