set1 = {13,54,65,34,65,34}
set2 ={54,76,334,67,54,34,67,23}

# 1. Find the common elements between two sets 

comman = set1 & set2
print(comman)

# 2. Create two sets: odd and even numbers between 1–20
odd = set(range(1, 21, 2))
even = set(range(2, 21, 2))
print(odd)
print(even)

# Perform union, intersection, and difference
union = set1 | set2
print(union)
intersection = set1 & set2
print(intersection)
difference = set1 - set2 
print(difference)

# 3. Find all unique characters from a string using a set
def unique_characters(s):
    s = set2(set1)
    print(s)
# 4. Check whether set A is a subset of set B

    A = (set1.issubset(set2))
    print(A)

# 5. Eliminate duplicate words from a sentence
word = {"game","ram","team","game","ram","sam"}
def unique(word):
    words = word.split()
    return print (words)