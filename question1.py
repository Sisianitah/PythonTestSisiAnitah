# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).

#soln

import math

# Input: Coordinates of the two points
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the distance using the distance formula
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Output the result
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")






# Question 1(ii)
# Write a Python program to find maximum between three numbers.

#soln

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum using conditional statements
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3

# Output the result
print(f"The maximum number among {num1}, {num2}, and {num3} is: {max_num}")


