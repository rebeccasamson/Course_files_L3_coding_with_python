#####################################################################
## Becky Samson L3 : Scripting and OOP
## Command line arguments
## Date 12/11/2026
#####################################################################

# Hello, how are you? program
# helloname.py

import sys # import Python standard library sys module

# print("argument list", sys.argv) # print argument list

name=sys.argv[1] # assign argument 1 (input by user on command line) to variable name

print("Hello, {}. How are you?".format(name)) 
