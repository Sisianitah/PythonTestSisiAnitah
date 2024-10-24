# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.

# Solution for Question 3(i)
total_sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number

print(f"The sum of the numbers entered is: {total_sum}")




# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

#soln
for num in range(1, 101):
    if num % 2 != 0:
        print(num)



