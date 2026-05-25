#28
#Write a Python program to find the repeated items of a tuple
my_tuple = (10, 20, 30, 20, 40, 10, 50)

'''n = int(input("Enter the number of elements in the tuple: "))

for i in range(n):
    elem = int(input("Enter an element: "))
    my_tuple += (elem,)'''#to get input from user.

repeated_items = []
for item in my_tuple:
    if my_tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

print(f"The repeated items in the tuple are: {repeated_items}")