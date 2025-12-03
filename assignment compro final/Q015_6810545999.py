# Name: Inthat # Student ID: 68010545999

import math
fx = {}
while True:
    line = input("Enter group name and coordinates (x y z) or 'done' to finish: ").strip()

    if line == "done":
        break

    part = line.split()
    if len(part) != 4:
        continue

    group_name = part[0]
    x = float(part[1])
    y = float(part[2])
    z = float(part[3])

    fx[group_name] = (x,y,z)

group_name = list(fx.keys())
distances = []

for i in range(len(group_name)):
    for j in range(i + 1, len(group_name)):
        group1 = group_name[i]
        group2 = group_name[j]
        x1, y1, z1 = fx[group1]
        x2, y2, z2 = fx[group2]

        a,b = sorted([group1, group2])
        distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))
        distances.append((a, b, distance))

distances.sort(key = lambda x: (x[2], x[0], x[1]))

print(" ")
print("Top minimum distance pairs (show only top-5):")

for i, (group1, group2, distance) in enumerate(distances[:5], start=1):
    print(f"{i}. {group1} to {group2}: {distance:.2f}")