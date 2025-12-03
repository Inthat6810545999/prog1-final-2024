# Name: Inthat # Student ID: 68010545999
import math
shapes = []

while True:
    types = input("Enter shape type (circle/rectangle/triangle) or 'done' to finish: ").lower()

    if types == "done":
        break

    if types == "circle":
        r = input("Enter radius: ")
        area = math.pi * float(r) * float(r)
        area = round(area,2)
        shapes.append({"type": "Circle" , "dimension": f"radius {r}" , "area": area})
        print(f"Circle area: {area:.2f}")
        print("")

    elif types == "rectangle":
        w = input("Enter width: ")
        h = input("Enter height: ")
        area = float(w) * float(h)
        area = round(area,2)
        shapes.append({"type": "Rectangle" , "dimension": f"width {w}, height {h}" , "area": area})
        print(f"Rectangle area: {area:.2f}")
        print("")

    elif types == "triangle":
        b = input("Enter base: ")
        h = input("Enter height: ")
        area = 0.5 * float(b) * float(h)
        area = round(area,2)
        shapes.append({"type": "Triangle" , "dimension": f"base {b}, height {h}" , "area": area})
        print(f"Triangle area: {area:.2f}")
        print("")

def get_area(x):
    return x["area"]

total_area = sum(s["area"] for s in shapes)
largest = max(shapes, key = get_area)
smallest = min(shapes, key = get_area)

print("")
print("--- SHAPE AREA REPORT ---")
print(f"Total area: {total_area:.2f}")
print(f"Largest shape: {largest["type"]} with {largest["dimension"]}, area: {largest["area"]:.2f}")
print(f"Smallest shape: {smallest["type"]} with {smallest["dimension"]}, area: {smallest["area"]:.2f}")
print("-----------------------------")

