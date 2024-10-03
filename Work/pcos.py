# reading the file first

with open("Data/portfolio.csv", "rt") as file:
    headers = next(file)
    total_cost = []
    for line in file:
        row = line.split(",")
        cost = int(row[1]) * float(row[2])
        total_cost.append(cost)
    tc = sum([x for x in total_cost])

print("Total cost ", tc)
