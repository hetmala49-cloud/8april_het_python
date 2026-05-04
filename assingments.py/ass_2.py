#Write a Python program to get the Factorial number of given number.
num = int(input("Enter a number: "))
fact = 1
if num < 0:
    print("Factorial is not possible for negative numbers")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print(f"Factorial is:{fact}")