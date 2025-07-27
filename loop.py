# while loop
i = 0
while i < 5:
    print(i)
    i += 1

# for loop
for j in range(5):
    print(j)

for k in [0, 1, 2, 3, 4]:
    print(k)

# nested loop
for m in range(3):
    for n in range(2):
        print(f"Outer: {m}, Inner: {n}")       

# list comprehension
squares = [x**2 for x in range(10)]  # generates a list of squares
print(squares)         

# using a loop with a condition
for o in range(10):
    if o % 2 == 0:
        print(o)

# using a loop with a break statement
for p in range(10):
    if p == 5:
        break
    print(p)    

# using a loop with a continue statement
for q in range(10):
    if q % 2 != 0:
        continue
    print(q)

# using a loop with an else clause
for r in range(5):
    print(r)
else:
    print("Loop completed")