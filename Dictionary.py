# Dictionary.py
# This code demonstrates the use of dictionaries in Python.

a ={ # Dictionary to store student information
    "Name" : "Ray",
    "Class" : "11",
    "Stream" : "Science",
    "Age" : "17"
}

# Accessing values in the dictionary

print(a["Name"])
print(a["Class"])
print(a["Stream"])
print(a["Age"])


# Modifying the dictionary
a["Age"] = "18"  # Update the age
print(a.items())

# Displaying keys, values, and updating the dictionary
print(a)
print(a.keys())# Display keys
print(a.values())# Display values
a.update({"Age": "16"})# Update age again
print(a["Age"])# Display updated age
print(a.get("Name"))#   Get name using get method

b ={
    "Name" : "Ray",
    "marks" : {  # Nested dictionary for marks
        "Physics" : 95,
        "Math" : 90,
        "Science" : 85,
        "English" : 88
    }
}

# Accessing values in the nested dictionary
print(b["Name"])
print(b["marks"]["Math"])
print(b["marks"]["Science"])
print(b["marks"]["English"])
print(b["marks"]["Physics"])

c ={
    "Name" : "Ray",
    "list" : [1, 2, 3, 4, 5],# List in dictionary
    "tuple" : (6, 7, 8, 9, 10)# Tuple in dictionary
}

# Accessing values in the dictionary with list and tuple

print(c["Name"])
print(c["list"])
print(c["tuple"])