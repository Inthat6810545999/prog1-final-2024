# Name: Inthat # Student ID: 68010545999

import csv

region_sales = {}

with open("sales.tsv" , "r" , newline = "" , encoding = "utf-8") as f:
    reader = csv.reader(f, delimiter = "\t")
    header = next(reader)

    for row in reader:
        if len(row) < 3:
            continue
        
        region = row[0].strip()
        sale = float(row[2].strip())
        if region in region_sales:
            region_sales[region] += sale
        else:
            region_sales[region] = sale

print("--- Regional Sales Summary ---")
for region, total in region_sales.items():
    print(f"{region}: ${total:.2f}")