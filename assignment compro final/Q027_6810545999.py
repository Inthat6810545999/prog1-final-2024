# Name: Inthat # Student ID: 68010545999

import csv

categ = input("Enter category to filter by: ")
category_lower = categ.lower()
inventoryfile = open('inventory.csv', 'r', newline='', encoding='utf‐8')
reader = csv.reader(inventoryfile)

next(reader)

items = []

for row in reader:
    item_name = row[1]
    item_category = row[2]
    stock = row[3]

    if item_category.lower() == categ.lower():
        items.append((item_name , stock))

if items:
    print(f"Items in category '{categ}': ")
    for item_name, stock in items:
        print(f"Item: {item_name}, Stock: {stock}")

else:
    print(f"No items found in category '{categ}'.")

inventoryfile.close()