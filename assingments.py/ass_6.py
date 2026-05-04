'''Write python program that swap two number with temp variable and
without temp variable.'''
n1 = int(input("Enter a number A: "))
n2 = int(input("Enter another number: "))
a=n1
n1=n2
n2=a
print(f"After swapping: A = {n1}, B = {n2}")
