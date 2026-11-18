#####################################################################
## Becky Samson L2 : Control Flow
## Loops, decision making
## Date 10/11/2026
#####################################################################

# "Guess the number" program
# uses while loops and decision making

mynumber=26 # assign the secret number

counter=0 # assign counter (number of guesses) to 0

print("Let's play a guessing game, what two-digit number am I thinking of?")
  
while True: # condition for while loop

 while counter <= 5: # maximum number of guesses allowed
    print("Number of guesses is at: " + str(counter))

    usernumber = int(input("Guess a number:")) # assign usernumber to the integer input by the user

    if usernumber < mynumber: # if less than the 'secret number'
        print("a little higher!") 
    elif usernumber > mynumber: # or if higher than the 'secret number'
        print("a little lower!")
    else: # otherwise, ie guess was correct 
        print("\nYou read my mind! It was " + str(mynumber) + ", well done!")
        break

    counter += 1  # Increments the counter by 1
 break 
print("Total number of guesses exceeds the maximum")