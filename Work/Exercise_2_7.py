import csv
import sys


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
    return portfolio



def read_prices(filename):
    with open(filename, "rt") as f:
        data = csv.reader(f)
        prices = {}
        for row in data:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

# reading args from the terminal
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"


# calling the function
portfolio = read_portfolio(filename)
print(portfolio)
