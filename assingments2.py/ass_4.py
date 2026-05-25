#9
'''Write a Python program to check a list is empty or not.'''

my_list = []

'''a = input("Enter elements for the list: ")
my_list.append(a)''' #if you want to test program by adding elements to list.

def check_empty(my_list):
    if not my_list:
        print("List is empty")
    else:
        print("List is not empty")



check_empty(my_list)