#####################################################################
## Becky Samson L2 : Control Flow
## Modules and functions
## Date 10/11/2026
#####################################################################

# Current time and epoch program

# uses modules and built-in functions

import time # import the time module

now = time.localtime() # use built-in function to assign local time to variable
formatted_time = time.strftime("%m-%d-%Y %H:%M:%S", now) # format the date/time
seconds = time.time() # use built-in function to assign current time in seconds since the epoch

print("local date and time is: ", formatted_time) # use built-in function to output current date/time
print("epoch is the beginning time started measuring from 1st Jan, 12:00 am, in Python.")
print("seconds since epoch =", seconds)	# output seconds since epoch

#CHALLENGE, make these into user-defined functions
#CHALLENGE, add line spaces between outputs