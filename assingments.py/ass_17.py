'''Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.'''
a = input("Enter first string: ")
b = input("Enter second string: ")

new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]

result = new_a + " " + new_b
print("Result:", result)