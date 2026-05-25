#21
#Write a Python program to create a tuple with numbers.

numbers = ()

N = int(input("Enter the number of elements in the tuple: "))

for i in range(N):
    elem = int(input("Enter a number: "))
    numbers += (elem,)

print(numbers)