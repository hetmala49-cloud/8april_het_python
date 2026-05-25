#34
#Write a Python script to concatenate following dictionaries to create a new one.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

'''n = int(input("Enter the number of dictionaries to concatenate: "))

for i in range(n):
    new_dict = {}
    for j in range(3):
        key = input(f"Enter the key for dictionary {j+1}: ")
        value = int(input(f"Enter the value for dictionary {j+1}: "))
        new_dict[key] = value
    print(f"Dictionary {i+1}:", new_dict)
'''#to get information from user
new_dict = {**dict1, **dict2, **dict3}
print(new_dict)