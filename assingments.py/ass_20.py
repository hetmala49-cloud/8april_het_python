''' Write a Python function that takes a list of words and returns the length
of the longest one.'''
data=[]
a=int(input("Enter the number of strings: "))
for _ in range(a):
    data.append(input("Enter a string: "))
    
print("The longest string has a length of:", max(len(s) for s in data))
a = max(len(s) for s in data)
print("The longest string is:", [s for s in data if len(s) == a][0])