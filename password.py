#####################################################################
## Becky Samson L1 : Data Types, Structures and Operators Continued
## Comparisom & assignment operators
## Date 09/11/2026
#####################################################################

# Password checking program
# using COMPARISON, LOGICAL and ASSIGNMENT operators
# password checker program

actual_password="password" # assignment operator
entered_password = str(input("Enter password ")) # assignment operator

if (entered_password!=actual_password): # relational operator 'not equal to'
    print("Invalid password")  
else:  
    print("Valid password") 