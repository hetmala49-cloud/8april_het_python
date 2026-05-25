#16
#Write a Python program to get unique values from a list

def get_unique_values(input_list):
    return list(set(input_list))

values = []

n = int(input("Enter the number of elements in the list: "))

for _ in range(n):
    num = int(input("Enter a number: "))
    values.append(num)

unique_values = get_unique_values(values)
print("Unique values:", unique_values)