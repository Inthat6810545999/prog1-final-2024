# Name: Inthat # Student ID: 68010545999

dict = {}

count = 1
n = int(input('How many students? '))
while count <= n:
    print()
    name = str(input(f"Enter name for student {count}: "))
    score = list(map(float, (input(f'Enter scores for {name}: ').split())))
    dict[name] = score
    count += 1

print("Student Averages:")
for key, value in dict.items():
    print(f'{key}: {(sum(value)/len(value)):.2f}')

