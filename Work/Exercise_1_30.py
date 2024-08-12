# turning pcost to a function
"""Take the code you wrote for the pcost.py program in Exercise 1.27 and
turn it into a function portfolio_cost(filename). 
This function takes a filename as input, reads the portfolio data in that file,
and returns the total cost of the portfolio as a float"""


import csv
import sys

def portfolio_cost(filename):
    "calculates the value of a portfolio"
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        total = 0
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                sum = nshares * price
            # this catches the int() and float() exceptions
            except:
                ("bad row", row)
            total += sum
    return float(total)

#modifying to accept filename from command line

if len(sys.argv) == 2:
    filename= sys.argv[1]
else:
    filename = "Data/portfolio.csv"


cost = portfolio_cost(filename)
print("Total cost is ", cost)
