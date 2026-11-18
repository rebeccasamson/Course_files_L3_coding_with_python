#####################################################################
## Becky Samson L2 : Control Flow
## Loops, decision making, operators and functions
## Date 10/11/2026
#####################################################################

# Calculate the average program
# Uses for loops, decision making, operators and built-in functions

numbers = [15, 20, 35, 45, 55] # assign values to list 'numbers'
sum = 0 # assign sum=0
listsize = len(numbers) # calculate number of items in list 'numbers' using len function

for i in numbers: # loop runs 5 times because the list 'numbers' contains 5 items
    sum = sum + i # sum the numbers in the list 'numbers'
average = sum / listsize # divide by the listsize to give the average and output
print("The average calculated is " + str(average))

# odd/even numbers within the list 'numbers'
for i in numbers: # decision making within a for loop
    if i % 2 == 0: # if divisible by 2
        print("Even number: " + str(i)) # output 'Even number', and the number value
    else: # if not it is odd! Therefore output 'Odd number', and the number value
        print("Odd number: " + str(i))


# Use for loop to output a list of numbers from 9 to 50 divisible by 2:
for i in range(9, 51): # use built-in function range which returns a sequence of numbers incrementing by 1 (by default).to set upper and lower boundaries
    if i%2==0: # if the number is divisible by 2
        print(i)