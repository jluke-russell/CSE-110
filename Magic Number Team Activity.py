"""
Luke Russell 
Magic Number Team Activity
2/18/21
"""
import random

#magic_number = int(input('What is the magic number? '))
magic_number = random.randint(1,100)
print(magic_number)
guess = int(input('What is your guess? '))

while guess != magic_number:
    guess = int(input('What is your guess? '))
    if guess < magic_number:
        print('Higher')
    elif guess > magic_number: 
        print('Lower')
    else:
        print('You got it!')