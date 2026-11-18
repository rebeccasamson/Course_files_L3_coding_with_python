#####################################################################
## Becky Samson L1 : Data Types, Structures and Operators
## Variables, data types and inputs
## Date 09/11/2026
#####################################################################

# Customer profile information using different data types
# This program will demonstrate how we can create variables, use data types and obtain inputs

# Declare variables and assign values:
fullname="Becky Samson" # string
age=46 # integer  
heightincm=165.0 # float   
homeowner=False # boolean. Note that True or False MUST start with uppercase!

# Print out each variable:
print(fullname) 
print(age)
print(heightincm)
print(homeowner)  

print("My name is " + fullname) 
print("My age is " + str(age))
print("My height in cm is " + str(heightincm))
print("True or False, I am a homeowner?! " + str(homeowner)) 

# Now try asking for a new input from the user to make program interactive:
pet=input("Do you own a pet?")  
print(pet) # Output user response
