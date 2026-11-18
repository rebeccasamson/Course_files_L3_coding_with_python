#####################################################################
## Becky Samson U1 L3 : Scripting and OOP
## Classes and objects, methods, attributes
## Date 17/11/2026
#####################################################################

# Cat class example

# define a class
class Cat:
#	sound = "miaow"	# class attribute

# create an object from class
#cat1 = Cat()
#print(cat1.sound)

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    print(self.name)
    print(self.age)

cat1 = Cat("Fluffy", 5)
print(cat1.get_info()) 
class Cat:
	species  "Feline" # class attribute
	def _init_(self, name, age):
		self.name = name # object instance attribute
		self.age = age # object instance attribute
# Create an object of the Cat class
cat1 = Cat("Fluffy", 5)
print(cat1.name)
print(cat1.species)
print(cat1.age)
# define a method to increase age of cat by 1 year
  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

cat1 = Cat("Fluffy", 5)
cat1.celebrate_birthday()
