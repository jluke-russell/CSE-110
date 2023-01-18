""" 
Luke Russell
Lists of Numbers 
3/4/21
""" 
numbers = []
number = -1 
while number != 0:
    number = int(input('Please enter a number. Type "0" when finished: '))
    if number != 0:
        numbers.append(number)
for number in numbers:
    print(number)
total = 0 
for number in numbers:
    total += number
print(f"The sum is: {total}")
average = 0 
for number in numbers:
    count = len(numbers)
    average = total / count
print(f"The average is: {average:.2f}")

largest = 0 
for number in numbers: 
    if number > largest:
        largest = number 
print(f"The largest number is: {largest}")
smallest = 99999999999999999999999999999999999999
for number in numbers:
    if number > 0 and number < smallest:
        smallest = number
print(f"The smallest positive number is: {smallest}")

in_order = sorted(numbers)
print("The numbers in order are: ")
for number in in_order:
    print(number)