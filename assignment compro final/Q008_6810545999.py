# Name: Inthat # Student ID: 68010545999

size = int(input("Enter table size: "))
if size == 0 or size < 0:
    print("Invalid input")

for i in range(1, size+1):
    total = 0
    for j in range(size):
        total += i
        print(f'{total:>4}', end= '')
    print()