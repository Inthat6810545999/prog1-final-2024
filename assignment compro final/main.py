# Name: Inthat # Student ID: 68010545999

f = open('greeting.txt', 'w')
name = str(input("Enter your name: "))
f.write(f'Hello, {name}! Welcome to file handling.')
f.close()
print("Greeting saved to greeting.txt")
