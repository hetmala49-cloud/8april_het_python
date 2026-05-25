#12
"""Write a Python function that takes a list and returns a new list with unique
elements of the first list.
"""

def unique_elements(input_list):
    return list(set(input_list))

numbers = []

n = int(input("Enter the number of elements in the list: "))

for _ in range(n):
    element = input("Enter an element: ")
    numbers.append(element)


print("New list with unique elements:", unique_elements(numbers))

print("list:", numbers)