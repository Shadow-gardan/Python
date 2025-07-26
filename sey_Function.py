s = {1, 2, 3, 4, 5}
print(s)  # Output: {1, 2, 3, 4, 5}

# Set operations
s.add(3)  # Adding an existing element has no effect
print(len(s))  # Output: 5
s.add(6)
print(s)  # Output: {1, 2, 3, 4, 5, 6}
s.remove(3)
print(s)  # Output: {1, 2, 4, 5, 6} 
s.discard(10)  # No error, even though 10 is not in the set
print(s)  # Output: {1, 2, 4, 5, 6}
s.union({7, 8})  # Returns a new set with elements from both sets
print(s)  # Output: {1, 2, 4, 5, 6}
s.intersection({2, 3, 6})  # Returns a new set with common elements
print(s)  # Output: {2, 6}
s.clear()  # Removes all elements from the set
print(s)  # Output: set()
# sey_Function.py
s = set()  # Creating an empty set
print(s)  # Output: set()   