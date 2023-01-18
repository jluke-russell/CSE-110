"""
Luke Russell
While Loop Practice
2/16/21
"""
answer = ''
answer = input('May I have a piece of candy? ')
while answer.lower() == 'no':
    answer = input('May I have a piece of candy? ')
    
print("Ok fine, but don't tell your mom.")


number = int(input('Please enter a positve number: '))

while number < 0: 
    print('Sorry, that is a negative number. Please try again, or not...') 
    number = int(input('Please enter a postive number: '))
    print(f'The number is {number}.')