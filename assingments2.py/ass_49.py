#67
"""Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers."""
numbers = []

for i in range(5):
    num = float(input("Enter a decimal number: "))
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum number:", maximum)
print("Minimum number:", minimum)