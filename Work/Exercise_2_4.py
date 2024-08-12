# creating a function to read prices
import csv
import sys


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


# modifying to accept filename from command line
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/prices.csv"

prices = read_prices(filename)
