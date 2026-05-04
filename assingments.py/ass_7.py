'''Write a Python program to find whether a given number is even or odd,
print out an appropriate message to the user.'''
a=int(input("Enter a number to check if it is even or odd: "))
if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")
