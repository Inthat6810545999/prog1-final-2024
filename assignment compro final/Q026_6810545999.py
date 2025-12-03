# Name: Inthat # Student ID: 68010545999


import csv

csvfile = open("contacts.csv" , "w" , newline = "" , encoding = "utf-8")
writer = csv.writer(csvfile)
writer.writerow(["Name" , "Email" , "Phone"])

i = 0

while True:
    i += 1
    print(f"--- Enter Contact {i} ---")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    writer.writerow([name , email , phone])
    add = input("Add another contact? (yes/no): ")
    print()

    if add.lower() == "no":
        break
    else:
        continue

print("Contact list saved to contacts.csv.")
csvfile.close()