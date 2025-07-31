import random

# Flag to control whether the dice should be rolled
yes = True

# Dice face functions
def dice1():
    print("|·|")  # Simple dot

def dice2():
    print("|··|")  # Two dots

def dice3():
    print("|:·|")  # Three dots

def dice4():
    print("|::|")  # Four dots

def dice5():
    print("|:·:|")  # Five dots

def dice6():
    print("|:::|")  # Six dots

# Function to roll the dice and print the corresponding face
def roll_dice():
    graphic = random.randint(1, 6)

    # match-case used like switch-case to call the correct face function
    match graphic:
        case 1:
            print("Result is:", graphic)
            dice1()

        case 2:
            print("Result is:", graphic)
            dice2()

        case 3:
            print("Result is:", graphic)
            dice3()

        case 4:
            print("Result is:", graphic)
            dice4()

        case 5:
            print("Result is:", graphic)
            dice5()

        case 6:
            print("Result is:", graphic)
            dice6()

# Run the dice roll if "yes" is True
if yes:
    roll_dice()
else:
    exit()
