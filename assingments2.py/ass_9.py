#14
#Write a Python program to select an item randomly from a list.


from random import choice, random


def select_random_item(input_list):
    return choice(input_list)

items = []

n = int(input("Enter the number of items to select randomly: "))

for i in range(n):
    a = input("Enter an item: ")
    items.append(a)

print("Randomly selected item:", select_random_item(items))