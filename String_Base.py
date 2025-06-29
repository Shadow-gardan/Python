# 1. Count vowels, consonants, digits, and special characters
s = (input("Enter a string: "))

vowels = consonants = digits = special = 0

for ch in s:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)

# 2. Check if the string is a palindrome
cleaned = s.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

# 3. Remove duplicate characters
duplicates = ""
for ch in s:
    if ch not in duplicates:
        duplicates += ch
print("Without duplicates:",duplicates)

# 4. Most frequent character
max_count = 0
most_char = ''
for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        most_char = ch
print("Most frequent character:", most_char)

# 5. Check if two strings are anagrams
str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("They are anagrams.")
else:
    print("They are not anagrams.")
