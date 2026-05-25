#15
#Write a Python program to find the second smallest number in a list.

def find_second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]

numbers = [5, 2, 8, 1, 9]

n = int(input("Enter the number of elements in the list: "))

for _ in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

second_smallest = find_second_smallest(numbers)
print("Second smallest number:", second_smallest)