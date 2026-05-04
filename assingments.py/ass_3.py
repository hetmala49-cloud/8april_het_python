#Write a Python program to get the Fibonacci series of given range.
n = int(input("Enter how many numbers you want: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b