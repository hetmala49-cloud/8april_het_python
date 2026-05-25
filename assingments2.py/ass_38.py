#48
#Write a Python program to create a dictionary from a string.
text = "w3resource"

'''n = int(input("Enter the number of characters to add: "))

for i in range(n):
    ch = input(f"Enter character {i+1}: ")
    text += ch
'''#to get data from user
count = {}

for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)