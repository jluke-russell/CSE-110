"""
Luke Russell
Team assignment: Grader Code
2/4/21
"""
print("Hello, and welcome to the Grade Calculator! Let's see how you did in the class!")
final_grade = int(input('Please enter your final semester grade: '))
if final_grade >= 90:
    letter = 'A'
elif final_grade >= 80:
    letter = 'B'
elif final_grade >= 70:
    letter = 'C'
elif final_grade >= 60:
    letter = 'D'
elif final_grade < 60:
    letter = 'F'
last_digit = final_grade % 10
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""
print(f'Your final letter grade is {letter}{sign}')
if final_grade >= 90:
    print("You're a genius! Einstein would be proud of you!")
elif final_grade >= 80:
    print("Congradulations!! You're smarter than you think!")
elif final_grade >= 70: 
    print("Congradulations!! C's get degrees!")
else:
    print("Get pranked.")