# pcost.py
#
# Exercise 1.27

with open("Data/portfolio.csv", "rt") as f:
    headers = next(f)
    total = 0
    for row in f:
        row_list = row.split(",")
        sum = int(row_list[1]) * float(row_list[2])
        total += sum

print("Total cost is ", total)
