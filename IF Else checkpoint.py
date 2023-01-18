"""
Luke Russell 
If Else Checkpoint
2/2/2021
"""
print('Welcome to the comparison machine!')
print('Please fill in the following:')
first_number = float(input('What is the first number? '))
second_number = float(input('What is the second number? '))
if first_number > second_number:
    print('The first number is greater')
else: 
    print('The first number is not greater.')
if first_number == second_number:
    print('The numbers are the same.')
else: 
    print('The numbers are not the same.')
if second_number > first_number:
    print('The second number is greater.')
else:
    print('The second number is not greater.')
print()
animal = input('What is your favorite animal? ')
if animal.lower() == "chicken":
    print("No way! That's my favorite animal too!")
else: 
    print("Ahh, that one is not my favorite at all.")