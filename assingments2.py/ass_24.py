#30
#Write a Python program to unzip a list of tuples into individual lists.
n = int(input("Enter number of tuples: "))

pairs = []

for i in range(n):
    a = input("Enter first value: ")
    b = input("Enter second value: ")
    pairs.append((a, b))

num, alpha = zip(*pairs)

print("First list:", list(num))
print("Second list:", list(alpha))