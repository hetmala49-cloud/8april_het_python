#25
#Write a Python program to convert a list to a tuple.
my_list = [10, 20, 30, 40, 50]

'''n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    elem = int(input("Enter an element: "))
    my_list.append(elem)'''#to get input from user.

my_tuple = tuple(my_list)

print(f"The tuple is: {my_tuple}")