#20
#Write a Python program to create a tuple with different data types.

my_tuple = ()

n = int(input("Enter the number of elements in the tuple: "))

for i in range(n):
    elem = input("Enter an element: ")
    my_tuple += (elem,)

print(my_tuple)