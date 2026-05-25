#5
"""Write a Python function to get the largest number, smallest num and sum
of all from a list."""

num = []

n = int(input("Enter the number of elements in the list: "))

for _ in range(n):
    element = int(input("Enter an number: "))
    num.append(element)

def list_info(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)

    return largest, smallest, total


largest, smallest, total = list_info(num)

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum:", total)