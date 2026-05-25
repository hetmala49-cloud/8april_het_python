#51
#Write a Python function to check whether a number is perfect or not.
# Function to check perfect number
def perfect_number(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n:
        print(n, "is a Perfect Number")
    else:
        print(n, "is not a Perfect Number")

n = int(input("Enter a number: "))
perfect_number(n)