#  Make a Constructor and a Super Method
# Constructor is a special method that is automatically called when an object of a class is created.
# The super() function allows you to call methods from a parent class.

class Animal:
    def __init__(self, name): # Constructor
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):# Constructor with super method
        # Call the constructor of the parent class
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Bark"


#objects of the classes
dog = Dog("Buddy", "Golden Retriever")
print(f"Dog Name: {dog.name}, Breed: {dog.breed}")
print(f"Dog Sound: {dog.speak()}")

cat = Animal("Whiskers")
print(f"Cat Name: {cat.name}")
print(f"Cat Sound: {cat.speak()}")
