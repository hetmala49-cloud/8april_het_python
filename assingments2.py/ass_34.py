#43
#Write a Python program to print all unique values in a dictionary.
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}

'''n = int(input("Enter the number of key-value pairs for the dictionary: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value
'''#to get data from user

unique_values = set(dict1.values())

print("Unique values:", unique_values)