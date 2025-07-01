# to fint the vaild age for vote

age = int(input("Enter your age: "))

if age >18:
    print("You are valid for vote.")

elif age == 18:
    print("Wait for few month")    
else:
    print("You are not valid.")

#To find the day

choice = int(input("Enter a number (1-7): "))

switch = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday", 
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

day = switch.get(choice)
print(day)

# Code for find the number of days in months

year = (int("enter the year"))
Years = year % 4 
months = (int(input("Enter the NUmber of Months 1-12")))
if Years == 0:
        if months == 2:
            print("29 days")

        elif months in [1, 3, 5, 7, 8, 10, 12]:
            print("31 days") 

        elif months in [4, 6, 9, 11]:
            print("30 days")
        else:
            print("Invalid month number.")        

else:
    if months == 2:
        print("29 days")
    elif months in [1, 3, 5, 7, 8, 10, 12]:
        print("31 days") 

    elif months in [4, 6, 9, 11]:
        print("30 days")
    else:
        print("Invalid month number.") 


#check character is vowel or consonant

chara = input("Enter a single character: ").lower()

if len(chara) == 1:
    if chara in 'aeiou':
        print("It is a vowel.")
    else:
        print("It is a consonant.")
else:
    print("Invalid input.")
