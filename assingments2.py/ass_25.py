#31
#Write a Python program to convert a list of tuples into a dictionary.
my_list = [('a', 1), ('b', 2), ('c', 3)]

'''n = int(input("Enter the number of tuples in the list: "))

for i in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    my_list.append((key, value))'''#to get information form user.

my_dict = dict(my_list)
print(my_dict)