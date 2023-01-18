temp_type = input('Please choose Fahrenheit or Celsius? ')
if temp_type .lower() == 'Fahrenheit':
    temperature_1 = float(input('What is the current temperature in degrees fahrenheit? '))
    celsius = (temperature_1 - 32) * 5 / 9
    print(f'The temperature in degrees celsius is {celsius:.1f} degrees.')
elif temp_type .lower() == 'Celsius':
    temperature_2 = float(input('What is the current temperature in degrees celsius? '))
    fahrenheit = temperature_2 * 9 / 5 + 32
    print(f'The temperature in degrees fahrenheit is {fahrenheit:.1f} degrees.')
else:
    print("It's a no for me dog.")
print('The End')