a = 5 # This is an integer
b = 10.5 + a # This is a float, as it adds an integer to a float
c = a + b # This is a float, as it adds an integer to a float
str(c)  # This will convert c to a string


# This code demonstrates type casting in Python
print("a : ",a, "type of a : ", type(a))
print("b : ",b, "type of b : ", type(b))
print("c : ",c, "type of c : ", type(c))

str(a)  # This will convert a to a string
float(a)  # This will convert a to a float
int(b)  # This will convert b to an integer
int(c)  # This will convert c to an integer
float(b)  # This will convert b to a float
float(c)  # This will convert c to a float

print(a, b, c)  # Printing the values of a, b, and c

# Demonstrating type casting in Python
print("Type casting demonstration:")

print("a:", a, "type:", type(a))
print("b:", b, "type:", type(b))
print("c:", c, "type:", type(c))
print("c as string:", str(c), "type:", type(str(c)))
print("End of type casting demonstration.")