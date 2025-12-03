# Name: Inthat # Student ID: 68010545999

namelist = []
inventory = {}
num = int(input('How many items in inventory? '))

count = 1
while count <= num:
    print()
    print(f"Item {count}")
    while count <= num:
        name = str(input("Enter name: "))
        if count > 1 and name.upper() in namelist:      
            print("Invalid name, enter a different name")
            continue
        names = (name.upper())
        namelist.append(names)
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        count += 1
        data = []
        data.append(price)
        data.append(quantity)
        inventory[name] = data
        break
print()
print("Inventory Details:")
total = 0
for key, value in inventory.items():
    print(f'{key} - Price: {value[0]:.2f}, Quantity: {value[1]}, Subtotal: {(value[0] * value[1]):.2f}')
    total += value[0] * value[1]
print()
print(f'Total inventory value: {total:.2f}')