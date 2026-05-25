#23
'''Write a Python program to check whether an element exists within a
tuple.'''
my_tuple = ()

n = int(input("Enter the number of elements in the tuple: "))

for i in range(n):
    elem = int(input("Enter an element: "))
    my_tuple += (elem,)

element = int(input("Enter an element to check: "))

if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")