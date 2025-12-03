# Name: Inthat # Student ID: 68010545999

while True:
    try:
        negative = input("Enter a non-negative number: ")
        number = float(negative)
        if number < 0:
            print("Error: Cannot calculate the square root of a negative number.")

        else:
            sqr = number ** 0.5
            print(f"The square root of {number:.1f} is {sqr}.")
            break

    except ValueError:
        print("Error: Invalid input. Please enter a number.")