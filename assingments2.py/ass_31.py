#40
#Write a Python script to merge two Python dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

'''n = int(input("Enter the number of key-value pairs for the first dictionary: "))
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

n = int(input("Enter the number of key-value pairs for the second dictionary: "))
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict2[key] = value'''#to get data from user

merged_dict = {**dict1, **dict2}
print(merged_dict)