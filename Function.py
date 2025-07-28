def sum_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def subtract_numbers(a, b):
    return a - b

a = sum_numbers(5, 3)
b = multiply_numbers(5, 3)
c = subtract_numbers(5, 3)

print(f"Sum: {a}, Product: {b}, Difference: {c}")

def tell(name = "World"):
    return f"Hello, {name}!"

print(tell())
print(tell("Alice"))

def play():
    return "Playing a game!"

print(play())