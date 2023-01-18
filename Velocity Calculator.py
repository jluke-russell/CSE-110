import math
from sympy import symbols, solve

print('Welcome to the velocity calculator. Please enter the following: ')
m = float(input('Please enter the mass: '))
g = float(input('Please enter gravity: '))
t = int(input('Please enter the time in seconds: '))
p = float(input('Please enter the density: '))
A = float(input('Please enter the cross sectional area: '))
C = float(input('Please enter the drag constant: '))
print()
c = 1/2 * p * A * C
print(f'The inner value of c is: {c:.3f}')
velocity = math.sqrt(m * g / c) * (1 - math.exp((-1 * math.sqrt(m * g * c) / m) * t))
v_terminal = math.sqrt(m * g / c)
print(f'The terminal velocity is: {v_terminal:.3f} m/s')
print(f'The velocity is: {velocity:.3f} m/s')


'''
x = symbols('x')
expr = x - 4
sol = solve(expr) 
print(sol)
t = symbols('t')
expr = velocity - v_terminal 
sol = solve(expr)
'''