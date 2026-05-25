#66
# Write a Python program to returns sum of all divisors of a number
def sum_of_divisors(n):
    total = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
            
    return total

num = int(input("Enter a number: "))

print("Sum of divisors:", sum_of_divisors(num))