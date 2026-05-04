'''Write a Python program to get a string made of the first 2 and the last 2
chars from a given a string. Ifthe string length islessthan 2,return instead
of the empty string.'''
text = input("Enter a string: ")
if len(text) <= 2:
    print("")
else:
    print(text[:2] + text[-2:])


