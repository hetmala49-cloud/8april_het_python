#39
# Write a Python program to check multiple keys exists in a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

'''m = int(input('Enter the number of keys to add to the dictionary: '))

for _ in range(m):
    key = input(f"Enter key {_+1}: ")
    value = input(f"Enter value for key '{key}': ")
    my_dict[key] = value
'''#to get data from user
n = int(input('Enter the number of keys to check: '))

keys_to_check = []
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    keys_to_check.append(key)

if all(key in my_dict for key in keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Some keys do not exist in the dictionary.")