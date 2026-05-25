#35
#Write a Python script to check if a given key already exists in a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

'''n = int(input("Enter the number of items in the dictionary: "))
    for _ in range(n):
        key = input("Enter the key: ")
        value = int(input("Enter the value: "))
        my_dict[key] = value
'''#to get information from user
key_to_check = input("Enter the key to check: ")

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")