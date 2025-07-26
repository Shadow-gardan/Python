Tup = (1, 2, 3, 4, 5)
print(Tup[0])  # Output: 1
print(Tup[1])  # Output: 2
print(Tup[2])  # Output: 3
print(Tup[3])  # Output: 4
print(Tup[4])  # Output: 5

# Tuple Functions
print(len(Tup))  # Output: 5
print(Tup.count(1))  # Output: 1
print(Tup.index(3))  # Output: 2
print(Tup[1:4])  # Output: (2, 3, 4)
print(Tup[2:])  # Output: (3, 4, 5)
print(Tup[:3])  # Output: (1, 2, 3)

print(len(Tup))  # Output: 5
print(3 in Tup)  # Output: True
print(Tup.index(4))  # Output: 3

for i in Tup:
    print(i)  # Output: 1 2 3 4 5

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

tup3 = tup1 + tup2
print(tup3)  # Output: (1, 2, 3, 4, 5, 6)
tup4 = tup1 * 2
print(tup4)  # Output: (1, 2, 3, 1, 2, 3)

a,b = (1, 2)# Unpacking a tuple
print(a)  # Output: 1
print(b)  # Output: 2