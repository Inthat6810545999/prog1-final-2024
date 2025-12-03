# Name: Inthat # Student ID: 68010545999

def triangle_area(base, height):
    area = base * height * 1/2
    return area
def read_input():
    base, height = map(float, input("Enter base and height: ").split())
    return base, height

b, h = read_input()
if b < 0 or h < 0:
    print("Input incorrect")
else:
    print(f"Area: {triangle_area(b, h):.2f}")
    