#####################################################################
## Becky Samson L3 : Scripting and OOP
## Command line arguments
## Date 12/11/2026
#####################################################################

# Customer profile program with 4 arguments passed from the command line
# customer_profile_2.py

import sys # import Python standard library sys module

fullname=sys.argv[1] # assign the first argument value to the variable fullname
age=sys.argv[2] # assign the second argument value to the variable age
heightincm=sys.argv[3] # assign the third argument value to the variable heightincm
homeowner=sys.argv[4] # assign the 4th argument value to the variable homeowner

# Print out each variable:
print("Name {}.".format(fullname)) 
print("Age {}.".format(age)) 
print("Height in cm {}.".format(heightincm))
print("Homeowner Y/N? {}.".format(homeowner))

