#33
#Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

'''n = int(input("Enter the number of items in the dictionary: "))
for _ in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    my_dict[key] = value'''#to get information from user

# (ascending)
sorted_ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Ascending order:", sorted_ascending)

# (descending)
sorted_descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending order:", sorted_descending)