# Name: Inthat # Student ID: 68010545999

integer = int(input("Enter a non-negative integer: "))
total_sum = 0

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for i in range(integer + 1):
    total_sum += factorial(i)

print(f'Factorial Sum is: {total_sum-1}')