#41
#Write a Python program to map two lists into a dictionary.

keys = []
values = []

n = int(input("Enter the number of keys: "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    keys.append(key)

m = int(input("Enter the number of values: "))

for j in range(m):
    value = input(f"Enter value {j+1}: ")
    values.append(value)

if n != m:
    print("The number of keys and values should be the same.")
else:

    result = dict(zip(keys, values))

    print(result)

