'''Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add 'ly'
insteadif the string length of the given string is less than 3, leave it
unchanged.'''
a = input("Enter a string: ")

if len(a) < 3:
    result = a
elif a.endswith("ing"):
    result = a + "ly"
else:
    result = a + "ing"

print("Result:", result)