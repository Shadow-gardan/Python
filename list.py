anyThing = ["Apple",4,True,"Banana",3.14,False,"Cherry",42]

print(anyThing[0])  # Output: Apple
print(anyThing[1])  # Output: 4
print(anyThing[2])  # Output: True
print(anyThing[3])  # Output: Banana
print(anyThing[4])  # Output: 3.14
print(anyThing[5])  # Output: False
print(anyThing[6])  # Output: Cherry
print(anyThing[7])  # Output: 42

# list Functions
print(len(anyThing))  # Output: 8
print(anyThing.count("Apple"))  # Output: 1
print(anyThing.index("Banana"))  # Output: 3
print(anyThing[2:5])  # Output: [True, 'Banana', 3.14]
print(anyThing[1:])  # Output: [4, True, 'Banana', 3.14, False, 'Cherry', 42]
print(anyThing[:3])  # Output: ['Apple', 4, True]
print(anyThing[-1])  # Output: 42
print(anyThing.reverse())  # This will also raise an error because the list contains mixed types
print(anyThing)  # Output: ['Apple', 4, True, 'Banana', 3.14, False, 'Cherry', 42]
print(anyThing.append("Date"))  # Adds "Date" to the end of the list
print(anyThing)  # Output: ['Apple', 4, True, 'Banana', 3.14, False, 'Cherry', 42, 'Date']
print(anyThing.insert(2, "Orange"))  # Inserts "Orange" at index    2
print(anyThing)  # Output: ['Apple', 4, 'Orange', True, 'Banana', 3.14, False, 'Cherry', 42, 'Date']
print(anyThing.pop())  # Removes and returns the last item: 'Date'  
print(anyThing)  # Output: ['Apple', 4, 'Orange', True, 'Banana', 3.14, False, 'Cherry', 42]
print(anyThing.remove("Banana"))  # Removes 'Banana' from the list
print(anyThing)  # Output: ['Apple', 4, 'Orange', True, 3.14, False, 'Cherry', 42]
print(anyThing.clear())  # Clears the list