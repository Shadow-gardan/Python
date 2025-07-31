#Inheritance in python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Inheritance from Animal class

class Dog(Animal):
    def speak(self):
        return "Bark"   

 # Inheritance from Animal class

class Cat(Animal):
    def speak(self):
        return "Meow"   

# Objects of the classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")

# Type of Inheritance
# 1> Single Inheritance

# Example of Single Inheritance
class Bird(Animal):
    def speak(self):
        return "Chirp"


# 2> Multiple Inheritance
class Bat(Animal):
    def fly(self):
        return "Flies with wings"

class FlyingDog(Dog, Bat):
    def speak(self):
        return "Woof and flaps wings"
    

# 3> Multilevel Inheritance
class Puppy(Dog):
    def speak(self):
        return "Yip"    
    

# 4> Hierarchical Inheritance
class PersianCat(Cat):
    def speak(self):
        return "Purr"
    

# 5> Hybrid Inheritance
class HybridAnimal(Dog, Cat):
    def speak(self):
        return "Hybrid sound"
    
# objects of the classes
bird = Bird("Tweety")
flying_dog = FlyingDog("Sky")
puppy = Puppy("Tiny")
persian_cat = PersianCat("Fluffy")
hybrid_animal = HybridAnimal("Mixie")
print(f"{bird.name} says: {bird.speak()}")
print(f"{flying_dog.name} says: {flying_dog.speak()}")
print(f"{puppy.name} says: {puppy.speak()}")
print(f"{persian_cat.name} says: {persian_cat.speak()}")
print(f"{hybrid_animal.name} says: {hybrid_animal.speak()}")

