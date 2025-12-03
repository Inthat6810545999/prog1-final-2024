# Name: Inthat # Student ID: 68010545999

print("Enter coefficients for f(x) = a1x^2 + b1x + c1")
a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))

print("")
print("Enter coefficients for g(x) = a2x^2 + b2x + c2")
a2 = float(input("a2: "))
b2 = float(input("b2: "))
c2 = float(input("c2: "))

print("")
x_start = float(input("Enter the start of the interval (a): "))
x_end = float(input("Enter the end of the interval (b): "))
n_traps = int(input("Enter the number of trapezoids (n): "))

if x_start >= x_end:
    print("Error: The start of the interval must be less than the end.")

elif n_traps <= 0:
    print("Error: The number of trapezoids must be a positive integer")

else:
    delta_x = (x_end - x_start) / n_traps

    def func1(x):
        return (a1 * x * x) + (b1 * x) + c1

    def func2(x):
        return (a2 * x * x) + (b2 * x) + c2

    total_area = 0
    for k in range(n_traps):
        x_curr = x_start + k * delta_x
        x_next = x_curr + delta_x
        y_curr = abs(func1(x_curr) - func2(x_curr))
        y_next = abs(func1(x_next) - func2(x_next))
        total_area += (y_curr + y_next) * delta_x / 2

    print(" ")
    print(f"Approximate area: {total_area:.6f}")
