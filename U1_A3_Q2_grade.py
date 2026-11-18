#####################################################################
## Becky Samson L3 : Scripting and OOP
## Command line arguments
## Date 12/11/2026
#####################################################################

# Grade result assignment program
# grade.py

import sys # import Python standard library sys module

grade=sys.argv[1] # assign the first argument value to the variable grade

print("Grade {}.".format(grade)) # print grade

percentage = int(grade) # assign integer grade value to percentage variable

result = "" # assign an empty value to result variable

if percentage >= 70: # output different results depending on percentage value
    result = "distinction" 
elif percentage >= 60:
    result = "merit"
elif percentage >= 40:
    result = "pass"
else:
    result = "fail"

print ("You entered a percentage mark of " + str(percentage) + ". The result awarded is a " + str(result))



