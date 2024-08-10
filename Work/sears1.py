"""write a program to calculate the number of days it takes
 to exceed the height of the sears tower, if a dollar were to
 be stacked and each day thereafter, you go and double the bills 
"""

bill_thickness = 0.11 * 0.001
sears_height = 442
stack_height = 0
day = 0

while stack_height < sears_height:
    day += 1
    day2 = 100
    stack_height = stack_height + bill_thickness * pow(2, day - 1)
    print(day, stack_height, pow(2, day - 1))


print("The stack got higher on the {} day".format(day))
print(day2)
