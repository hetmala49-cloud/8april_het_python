#22
#Write a Python program to convert a tuple to a string.

my_tuple = ()

n = int(input("Enter the number of elements in the tuple: "))

for i in range(n):
    elem = input("Enter an element: ")
    my_tuple += (elem,)


my_string = ", ".join(my_tuple)

print(my_string)