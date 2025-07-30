
# Constructor is a special Function in Python that is automatically called when an object is created from a class.

class student:
    # Constructor for the student class
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Method to display student information
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Deconstructor for the student class
    def __del__(self):
        print(f"Object {self.name} is being deleted")


# Creating an instance of the student class
Ray = student("Ray", 20)
Ray.display()

# Deleting the instance to trigger the destructor
del Ray