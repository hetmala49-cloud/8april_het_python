#52
# Write a Python function to check whether a string is a palindrome or not.

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")