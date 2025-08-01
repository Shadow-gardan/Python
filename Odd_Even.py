# With Using the If-else or loop we can find the odd or even
n = 4
odev = ["Even" , "Odd"]
print(odev[n%2])

# With the help of the if-else

nu = 4
if nu % 2 == 0 :
    print(f"It was a Even Number : {nu}")

else :
    print(f"It was a odd number : {nu}")    

# using the Function ot find the ODD or EVEN

def ODEV(num):
        if num % 2 == 0 :
            print(f"It was a Even Number : {num}")

        else :
            print(f"It was a odd number : {num}") 

ODEV(5)            