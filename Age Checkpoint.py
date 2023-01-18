"""
Luke Russell
Age Checkpoint 
1/19/2021
"""
print('Hello!')
age = int(input(f'Please enter your current age: '))
new_age = age + 1 
print(f'On your next birthday you will be {new_age}.')
print()
carton_count = int(input(f'How many egg cartons do you have? '))
egg_count = carton_count * 12 
print(f'You have {egg_count} eggs.')
print()
cookies = int(input('How many cookies do you have? '))
people = int(input('How many people are there? '))
cookies_per_person = cookies / people
print(f'Each person can have {cookies_per_person} cookies.')