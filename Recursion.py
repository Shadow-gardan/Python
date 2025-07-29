# Recursin simple code for Factorial

def factorial(n): # Function to find factorial of a number
    n = int(n)  # Convert input to integer for calculation
# base of Recursion 
    if n == 0 or n == 1: 
        return 1
    
    else:
        return n * factorial(n-1)
    

num = input("Enter the NUmber for it's Factorial : ") # Input from user
# Call the factorial function and print the result    
a = factorial(num)
print(a) 

# Recusion was a function which was call multiple  time when the base function is false

def main():
    num = input("Enter the Number for its Factorial: ")  # Input from user
    a = factorial(num)  # Call the factorial function
    print(f"The factorial of {num} is {a}")  # Print the result

if __name__ == "__main__":
    main()

# This code defines a main function to encapsulate the input and output logic
# and uses the factorial function to compute the factorial of a number provided by the user.

