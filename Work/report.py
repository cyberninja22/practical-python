import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    "calculates the value of a portfolio"
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        portfolio = []
        headers = next(rows)
        for row in rows:
            try:
                name = row[0]
                nshares = int(row[1])
                price = float(row[2])
                value = (name, nshares, price)
                #creating the dict using zip operation
                record = dict(zip(headers,value))
            # this catches the int() and float() exceptions
            except:
                ("bad row", row)
            portfolio.append(record)
    return (portfolio)


# reading args from the terminal
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"


# calling the function
portfolio = read_portfolio(filename)
pprint(portfolio)
