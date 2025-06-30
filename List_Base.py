#Write a Python program to remove duplicates from a list without using set() or built-in dict.fromkeys().
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

#Create a function that accepts a list of numbers and returns a new list containing only the prime numbers.
def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

def numbers(lst):
    return [num for num in lst if prime(num)]

#Given a list of integers, write a program to find all pairs whose sum is equal to a given number k.
def sum(list, k):
    pairs = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == k:
                pairs.append((list[i], list[j]))
    return pairs

#Write a Python program to rotate a list by k elements to the right.
def rotate(list, k):
    k = k % len(list) 
    return list[-k:] + list[:-k]

#Implement your own sorting function without using built-in .sort() or sorted().
def sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


