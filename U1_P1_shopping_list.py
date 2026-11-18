#####################################################################
## Becky Samson L1 : Data Types, Structures and Operators
## Storing and manipulating a list 
## Date 09/11/2026
#####################################################################

# Shopping list
# This program will demonstrate how we can store and manipulate a list (data structure)

# Assign shopping list values using square brackets:
shoppinglist1=["6 apples", "milk", "bread", "12 eggs"] # Assign list name and values
print("How many items are there on the shopping list?")
print(len(shoppinglist1)) # Print the number of items on the list using the len() function
shoppinglist1.sort() # Sort the list into alphabetical order
print(shoppinglist1) # Output what the variable holds (Note that the items with numbers will appear first on the list)

shoppinglist2=["cake", "biscuits", "chocolate"] # Variable name and assign value using brackets
shoppinglist2.sort(reverse=True) # Reverse alphabetical order of list items (remember True needs to start with a capital letter!)

for x in shoppinglist2: # Output all items one by one until exhausted, i.e. for all values of x
  print(x)

fulllist=shoppinglist1 + shoppinglist2 # Use + operator to join lists together and store in new variable named fulllist
print(fulllist) 

# Now sort the list alphabetically, list items one by one and print the number of items in the full list

fulllist.sort() # Sort the full list into alphabetical order

for x in fulllist: # Output all items one by one until exhausted, i.e. for all values of x
  print(x)

print("Number of items on full list is " + str(len(fulllist)))