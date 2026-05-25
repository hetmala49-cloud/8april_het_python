#42
#Write a Python program to combine two dictionary adding values for common keys.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

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

for key, value in dict2.items():
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value

print(dict1)
