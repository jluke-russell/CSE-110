"""
Luke Russell 
Amusment Park Requirements
2/11/21
"""
access = False

height_1 = int(input('Please input the height of the first rider in inches: '))
age_1 = int(input('Please enter the age of the first rider: '))
rider = input('Is there a second rider? (YES or NO): ')

if rider.lower() == 'yes':
    age_2 = int(input('Please enter the age of the second rider: '))
    height_2 = int(input('Please enter the height of the second rider in inches: '))
    if height_1 < 36 or height_2 < 36:
        access = False
    else:
        if age_1 >= 18 or age_2 >= 18:
            access = True
        else: 
            access = False
            if age_1 >= 12 and age_2 >= 12 and height_1 >= 52 and height_2 >= 52: 
                access = True
            else:
                access = False
else:
    if height_1 >= 62 and age_1 >= 18:
        access = True
    else:
        access = False
if access:
    print('Welcome aboard!')
else:
    print('Access denied.')