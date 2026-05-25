#50
#Write a Python function to check whether a number is in a given range

def check_range(num, start, end):
    if num >= start and num <= end:
        print("Number is in the range")
    else:
        print("Number is not in the range")

num = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

check_range(num, start, end)