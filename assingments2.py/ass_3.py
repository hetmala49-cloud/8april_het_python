#8
"""Write a Python program to remove duplicates from a list."""

numbers = []

n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    element = input("Enter an element: ")
    numbers.append(element)

print("Original list:", numbers)

def remove_duplicates(items):
    return list(set(items))

print("List without duplicates:", remove_duplicates(numbers))