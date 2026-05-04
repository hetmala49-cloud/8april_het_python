#Write a python program to sum of the first n positive integers.
a = int(input("Enter a number to find its sum of positive integers: "))
sum=0
if a >= 0:
 for i in range(1, a + 1):
    sum += i
    print(f"The sum of positive integers up to {a} is: {sum}")
else:
    print("Please enter a positive integer.")