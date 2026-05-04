# Write a Python function to insert a string in the middle of a string.
a = input("Enter a string: ")
b = input("Enter the string to insert in the middle: ")
def insert_middle(a, b):
    return a[:len(a)//2] + b + a[len(a)//2:]
result = insert_middle(a, b)
print(result)