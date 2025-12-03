# Name: Inthat # Student ID: 68010545999

records = []
total_income = 0
total_expense = 0

while True:
    item_name = input("Enter transaction description (or 'done' to finish): ")
    if item_name == "done":
        break

    value = float(input(f"Enter amount for {item_name}: "))
    if value == 0:
        continue

    records.append({"description": item_name, "amount": value})

total_income = sum(entry["amount"] for entry in records if entry["amount"] > 0)
total_expense = sum(entry["amount"] for entry in records if entry["amount"] < 0)
net_balance = total_income + total_expense

print()
print("--- FINANCIAL REPORT ---")
print("Transactions:")

for entry in records:
    sign = "+" if entry["amount"] > 0 else "-"
    print(f"{sign} {entry['description']}: {' ' * (13 - len(entry['description']))}${entry['amount']:8.2f}")

print("------------------------")
print(f"{'Total Income:':<16} ${total_income:8.2f}")
print(f"{'Total Expenses:':<16} ${total_expense:8.2f}")
print(f"{'Net Balance:':<16} ${net_balance:8.2f}")
print("------------------------")
