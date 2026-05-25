#10
'''Write a Python function that takes two lists and returns true if they have
at least one common member.'''

list1 = []
list2 = []

n = int(input("Enter the number of elements for the first list: "))
for _ in range(n):
    element = int(input("Enter an element for the first list: "))
    list1.append(element)

m = int(input("Enter the number of elements for the second list: "))
for _ in range(m):
    element = int(input("Enter an element for the second list: "))
    list2.append(element)

def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


print(common_member(list1, list2))