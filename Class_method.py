# It is a class method which is bound to the class and not the object of the class.
# It can be called on the class itself, rather than on instances of the class.

class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print(f"Called on class: {cls.__name__}")

# Object of the class is not required to call this method.
# It can be called directly on the class.

print( MyClass.class_method())
print(MyClass.class_method.__doc__)

# @getter and @setter decorators can also be used with class methods.
class MyClassWithGetterSetter:
    _value = 0

    @classmethod
    def get_value(cls):
        return cls._value

    @classmethod
    def set_value(cls, value):
        cls._value = value

# Example usage of getter and setter
MyClassWithGetterSetter.set_value(10)
print(MyClassWithGetterSetter.get_value())
print(MyClassWithGetterSetter.get_value.__doc__)        