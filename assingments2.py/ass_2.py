#7
"""Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.
"""
strings = []

n = int(input("Enter the number of strings: "))

for i in range(n):
    s = input("Enter a string: ")
    strings.append(s)

count = 0

for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Number of matching strings:", count)