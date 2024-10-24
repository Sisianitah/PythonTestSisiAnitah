# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

#soln 

def calculate_grade(score):

    if 90 percentage >= 90:
        print ("A")
    elif  percentage >= 80:
        print ("B")
    elif  percentage >= 70:
        print ("C")
    elif  percentage >= 60:
        print ("D")
    elif  percentage <= 40:
        print ("E")
    else:
        print ("Fail")

def grade_students():

    num_students = int(input("Enter the number of students: "))

    for i in range(1, num_students + 1):

        score = float(input(f"Enter the score for student {i}: "))

        grade = calculate_grade(score)

        print(f"Student {i} - Score: {score} - Grade: {grade}")
grade_students()



