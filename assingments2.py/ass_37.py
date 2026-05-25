#47
#Write a Python program to combine values in python list of dictionaries. 

# List of dictionaries
data = [
    {"a": 10, "b": 20},
    {"a": 5, "b": 15},
    {"a": 2, "b": 8}
]

'''n = int(input("Enter the number of dictionaries to add: "))

for i in range(n):
    d = {}
    for key in ["a", "b"]:
        value = int(input(f"Enter value for key '{key}': "))
        d[key] = value
    data.append(d)
'''#to get data from user
result = {}

for d in data:
    for key, value in d.items():
        result[key] = result.get(key, 0) + value

print(result)