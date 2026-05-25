#17
#Write a Python program to check whether a list contains a sub list

def contains_sublist(main_list, sub_list):
    for item in sub_list:
        if item not in main_list:
            return False
    return True


main_list = [1, 2, 3, 4, 5]
sub_list = [2, 4]

print(contains_sublist(main_list, sub_list))