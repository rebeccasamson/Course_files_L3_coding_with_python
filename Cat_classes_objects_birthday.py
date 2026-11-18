#####################################################################
## Becky Samson U1 L3 : Scripting and OOP
## Classes and objects, methods, attributes
## Date 17/11/2026
#####################################################################

# Cat class example

# define a class
class Cat:
	species="Feline" # class attribute
	def __init__(self, name, age):
		self.name = name # object instance attribute
		self.age = age # object instance attribute
# Create an object of the Cat class

cat1 = Cat("Fluffy", 5)

print(cat1.name)
print(cat1.species)
print(cat1.age)

# define a method to increase age of cat by 1 year
#  def celebrate_birthday(self):
#    self.age += 1
#    print(f"Happy birthday! You are now {self.age}")

#cat1 = Cat("Fluffy", 5)
#cat1.celebrate_birthday()
