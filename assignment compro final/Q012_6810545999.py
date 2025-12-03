# Name: Inthat # Student ID: 68010545999

size = int(input("Enter an odd number for the size: "))
if size <= 0 or size % 2 == 0:
    print("Error: Please enter a positive odd number.")
else:
    symbol = input("Enter the character to use: ")

    mid = size // 2

    for row in range(mid + 1):
        if row == mid:
            print(symbol * size)
        else:
            outer_space = mid - row
            if row == 0:
                print(" " * outer_space + symbol)
            else:
                inner_space = 2 * row - 1
                print(" " * outer_space + symbol + " " * inner_space + symbol)
    
    for row in range(mid - 1, -1, -1):
        outer_space = mid - row
        if row == 0:
            print(" " * outer_space + symbol)
        else:
            inner_space = 2 * row - 1
            print(" " * outer_space + symbol + " " * inner_space + symbol)
