#24
# Write a Python program to find the length of a tuple.

my_tuple = (10, 20, 30, 40, 50)

'''n = int(input("Enter the number of elements in the tuple: "))

    for i in range(n):
        elem = int(input("Enter an element: "))
        my_tuple += (elem,)
'''#to get input from user.
length = len(my_tuple)

print(f"The length of the tuple is: {length}")