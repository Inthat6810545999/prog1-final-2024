# Name: Inthat # Student ID: 68010545999

row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
matrix = []
for i in range(row):
    in_matrix = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(in_matrix)

print()
print("Transposed Matrix:")
for i in range(column):
    for j in range(row):
        print(matrix[j][i], end = " ")
    print()