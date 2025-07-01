# Count the frequency of each character in a string using a dictionary

def frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

string = "game"
print(frequency(string))

# Create a dictionary from two lists (one for keys, one for values) 

keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(dict(zip(keys, values)))

# Read a sentence and return a dictionary with the count of each word

def count(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

sentence = "Let go go"
print(count(sentence))

# Make a dictionary of students with their marks, then sort by marks

def sort(students):
    return dict(sorted(students.items(), key=lambda item: item[1], reverse=True))

students = {
    'Alice': 88,
    'Bob': 95,
    'Charlie': 78,
    'Diana': 85
}
print(sort(students))

# Create a nested dictionary for student details and display the average marks

def average(students):
    total = 0
    count = 0
    for student in students.values():
        total += student['marks']
        count += 1
    return total / count if count != 0 else 0

students = {
    'student1': {'name': 'Alice', 'age': 20, 'marks': 88},
    'student2': {'name': 'Bob', 'age': 21, 'marks': 95},
    'student3': {'name': 'Charlie', 'age': 19, 'marks': 78}
}

print(f"Average Marks: {average(students):.2f}")
