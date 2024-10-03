# with open("Data/portfolio.csv", "rt") as file:
#     data = file.read()

# (data)

# reading a text file line by line

with open("Data/portfolio.csv", "rt") as file:
    for line in file:
        print(line, end="")
