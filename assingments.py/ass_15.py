#Write a Python program to count occurrences of a substring in a string.
text = input("Enter the main string: ")
sub = input("Enter the substring to check occurrence: ")
count = text.count(sub)
print("Occurrences:", count)