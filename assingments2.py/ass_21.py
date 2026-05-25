#27
#Write a Python program to replace last value of tuples in a list.
my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

'''n = int(input("Enter the number of tuples in the list: "))

for i in range(n):
    elem = tuple(int(x) for x in input("Enter the elements of the tuple separated by space: ").split())
    my_list.append(elem)'''#to get input from user.

# Replace the last value of each tuple with a new value
new_value = int(input("Enter the new value to replace the last element of each tuple: "))

for i in range(len(my_list)):
    my_list[i] = my_list[i][:-1] + (new_value,)

print(f"The modified list is: {my_list}")