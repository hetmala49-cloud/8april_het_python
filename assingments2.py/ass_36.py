#46
#Write a Python program to find the highest 3 values in a dictionary
dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

'''n = int(input("Enter the number of values to add in the dictionary: "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = int(input(f"Enter value for key '{key}': "))
    dict1[key] = value
'''#to get data from user
highest_values = sorted(dict1.values(), reverse=True)[:3]

print(f"The highest {3} values are:", highest_values)