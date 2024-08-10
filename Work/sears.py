"""write a program to calculate the number of days it takes
 to exceed the height of the sears tower, if a dollar were to
 be stacked and each day thereafter, you go and double the bills 
"""

bill_thickness = 0.11 * 0.001
sears_height = 442

day = 1
num_of_bills = 1

while bill_thickness * num_of_bills < sears_height:
    print(day, bill_thickness * num_of_bills, num_of_bills)
    day += 1
    num_of_bills *= 2


print("On the {} day the size of the stacked bills exceeds the Sears tower".format(day))
