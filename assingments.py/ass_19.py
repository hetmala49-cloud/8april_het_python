'''Write a Python program to find the first appearance of the substring 'not'
and 'poor' froma given string, if 'not' follows the 'poor', replace the whole
'not'...'poor'substring with 'good'. Return the resulting string.'''
a = input("Enter a string: ")
if 'not' in a and 'poor' in a and a.find('not') < a.find('poor'):
    a = a.replace(a[a.find('not'):a.find('poor')+4], 'good')
print(a)