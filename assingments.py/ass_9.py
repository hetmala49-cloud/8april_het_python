'''Write a Python program to find the sum of three numbers, but if two of them are equal, the sum is 0.'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a == b or b == c or a == c:
    print("Sum is 0")
else:
    print("Sum is:", a + b + c)