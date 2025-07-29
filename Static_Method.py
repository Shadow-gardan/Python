
# Static Method is used when you want to define a method that belongs to the class rather than any instance of the class.
# This method does not require an instance of the class to be called and can be called on the class itself.


class Employee:
    # Class variable
    company_name = "Tech Corp"

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance method
    def details(self):
        return f"Name: {self.name}, Position: {self.position}, Company: {Employee.company_name}"

    # Static method
    @staticmethod
    def company_info():
        return f"Company Name: {Employee.company_name}"


# Object instantiation
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")

# Accessing instance methods
print(emp1.details())
print(emp2.details())

# Calling the static method
print(Employee.company_info())