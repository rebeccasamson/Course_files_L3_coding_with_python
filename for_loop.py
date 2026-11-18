#####################################################################
## Becky Samson L2 : Control Flow
## for loop
## Date 10/11/2026
#####################################################################

# Use for loop to generate a list of numbers from 9 to 50 divisible by 2.
for i in range(9, 51):
    # divide each number by 2
    if i%2==0: # if divisible by 2 ie remainder=0
        print(i)