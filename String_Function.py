import pprint


sen = "The first word for string is string"

print(sen.split(" ", 1)[0])  # Output: The
print(sen.split(" ", 1)[1])  # Output: first word for string

print(type(sen))  # Output: <class 'str'>
print(sen.split(" ", 1))  # Output: ['The', 'first word for string']

print(sen.split(" ", 1)[0].upper())  # Output: THE
print(sen.split(" ", 1)[1].lower())  # Output: first word for string
print(sen.split(" ", 1)[0].capitalize())  # Output: The 

print(sen[2:4:6]) # Output: first word for string
print(sen[2:4])  # Output: first
print(sen[2:4:2])  # Output: first
print(sen[0:2])  # Output: The

# Function of the string
print(sen.isalnum())  # Output: False (contains spaces)
print(len(sen))  # Output: 36 (length of the string including spaces)
print(sen.endswith("string"))  # Output: True (checks if the string ends with 'string')
print(sen.startswith("The"))  # Output: True (checks if the string starts with 'The')
print(sen.find("word"))  # Output: 8 (index of the first occurrence of 'word')
print(sen.replace("string", "text"))  # Output: The first word for text
print(sen.count("string"))  # Output: 2 (counts occurrences of 'string')


a = input("Enter a string: ") # This will take input from the user
print(a)# Output: (user input will be displayed)

print(a.split(" ", 1)[0])  # Output: (first word of user input)
print(a.split(" ", 1)[1])  # Output: (rest of user input)