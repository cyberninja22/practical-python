# pcost.py
#
# Exercise 1.27

# with open("Data/portfolio.csv", "rt") as f:
#     headers = next(f)
#     total = 0
#     for row in f:
#         row_list = row.split(",")
#         sum = int(row_list[1]) * float(row_list[2])
#         total += sum

# print("Total cost is ", total)

# Exercise 1.30 and 1.31
# def portfolio_cost(filename):
#     total = 0
#     with open(filename, "rt") as f:
#         headers = next(f)
#         for file in f:
#             rowlist = file.split(",")
#             try:
#                 stock_sum = int(rowlist[1]) * float(rowlist[2])
#             except ValueError:
#                 print("The share field cannot be empty")
#             total += stock_sum

#     print("The total is ", total)

# Exercise 1.32
# import csv
# def portfolio_cost(filename):
#     total = 0
#     with open(filename) as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             try:
#                 stock_sum = int(row[1]) * float(row[2])
#             except ValueError:
#                 print("The share field cannot be empty")
#             total += stock_sum

#     print("The total is ", total)

# Exercise 1.33
import csv
import sys

import csv
def portfolio_cost(filename):
    total = 0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                stock_sum = int(row[1]) * float(row[2])
            except ValueError:
                print("The share field cannot be empty")
            total += stock_sum
    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("The total is ", cost)
