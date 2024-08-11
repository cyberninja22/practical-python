# turning pcost to a function
"""Take the code you wrote for the pcost.py program in Exercise 1.27 and
turn it into a function portfolio_cost(filename). 
This function takes a filename as input, reads the portfolio data in that file,
and returns the total cost of the portfolio as a float"""


def portfolio_cost(filename):
    "calculates the value of a portfolio"
    with open(filename, "rt") as f:
        total = 0
        headers = next(f)
        for row in f:
            row_list = row.split(",")
            try:
                nshares = int(row_list[1])
                price = float(row_list[2])
                sum = nshares * price
            # this catches the int() and float() exceptions
            except:
                ("bad row", row)
            total += sum
    return float(total)


cost = portfolio_cost("Data/portfolio.csv")
print("Total cost is ", cost)
