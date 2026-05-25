#18
#Write a Python program to split a list into different variables.

numbers = []

n = int(input("Enter the number of elements in the list(3 values only): "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)


a, b, c = numbers

print("a =", a)
print("b =", b)
print("c =", c)