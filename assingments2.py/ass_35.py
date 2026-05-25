#45
#Write a Python program to create and display all combinations of letters,
#selecting each letter from a different key in a dictionary.

dict_1 = {'a': ['a1', 'a2'], 'b': ['b1', 'b2'], 'c': ['c1', 'c2']}

'''n = int(input("Enter the number of keys in the dictionary: "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    values = input(f"Enter values for key '{key}' (comma-separated): ")
    dict_1[key] = values.split(',')
'''#to get data from user
values = list(dict_1.values())

for i in values[0]:
    for j in values[1]:
        for k in values[2]:
            print(i + j + k)
