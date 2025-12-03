# Name: Inthat # Student ID: 68010545999

height = int(input("Enter size of triangle: "))
pattern = input("Enter pattern string: ")

if height <= 0 or pattern == "":
    print("Invalid input")

pos = 0
for row_num in range(1, height + 1):
    line = ""
    for col_num in range(row_num):
        line += pattern[pos]
        pos = (pos + 1) % len(pattern)
    print(line)
