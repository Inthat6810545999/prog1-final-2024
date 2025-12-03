# Name: Inthat # Student ID: 68010545999

def read_input():
    first, second, third = map(int, input("Enter three integers: ").split())
    return first, second, third

def sum(f, s, t):
    sum = f + s + t
    if sum == 0:
        sum = 'Zero'
    elif sum % 2 == 0:
        sum = "Even"
    else:
        sum = 'Odd'
    return sum

def max(f, s, t):
    list = []
    list.append(f)
    list.append(s)
    list.append(t)
    list = sorted(list, reverse=True)
    return list[0]

def min(f, s, t):
    list = []
    list.append(f)
    list.append(s)
    list.append(t)
    list = sorted(list)
    return list[0]

f, s, t = read_input()
print(f"Sum: {sum(f, s, t)}")
print(f'Max: {max(f, s, t)}')
print(f'Min: {min(f, s, t)}')