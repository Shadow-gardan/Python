# OOPs concepts 
# Class and Object
class Dog:
    # Class variable
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"  
    
# Object instantiation
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Accessing class and instance variables
print(f"{dog1.name} is a {dog1.species}.")
print(f"{dog2.name} is a {dog2.species}.")


# Accessing instance methods
print(dog1.description())
print(dog2.description())


# Calling the speak method  
print(dog1.speak("Woof"))
print(dog2.speak("Bark"))


# Accessing class variable directly from the class
print(f"All dogs belong to the species: {Dog.species}")


# Accessing class variable from an instance
print(f"{dog1.name} belongs to the species: {dog1.species}")


# Accessing instance variables directly
print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")


# Modifying instance variables
dog1.age = 6
print(f"{dog1.name} is now {dog1.age} years old.")


# Modifying class variable
Dog.species = "Canis lupus familiaris"
print(f"Updated species: {Dog.species}")
print(f"{dog1.name} now belongs to the species: {dog1.species}")    


# Deleting an instance variable
del dog1.age
print(f"{dog1.name} no longer has an age attribute.")  # This will raise an AttributeError if accessed


# Attempting to access deleted attribute    
try:
    print(dog1.age)
except AttributeError as e:
    print(f"Error: {e}")



# Deleting an instance
del dog2
print("dog2 has been deleted.")


# Attempting to access deleted instance
try:
    print(dog2.name)
except NameError as e:
    print(f"Error: {e}")    

