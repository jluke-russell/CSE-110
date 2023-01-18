"""
Luke Russell 
Milestone: Menu
1/23/2021
"""
print("Welcome to McDonalds!")
print()
print("All drinks are $1.00 and all sides are $2.00")
print()
print('Please input your order below: ')
kids_meal = float(input(f"Please enter the Kid's Meal price: "))
adult_meal = float(input(f"Please enter the Adult Meal price: "))
kid_count = int(input(f'Please enter the number of Kids: '))
adult_count = int(input(f'Please enter the number of adults: '))
drink_count = int(input(f'Please enter the number of drinks ($1.00 each): '))
sides_count = int(input(f'Please enter the number of sides ($2.oo each): '))
tax = float(input(f'Please enter the Sales Tax: '))
kid_cost = kids_meal * kid_count
adult_cost = adult_meal * adult_count
drink_cost = drink_count * 1
sides_cost = sides_count * 2
subtotal = adult_cost + kid_cost + sides_cost + drink_cost
sales_tax = subtotal * (tax / 100)
total = subtotal + sales_tax
print()
print(f'Kids Meals: ${kid_cost:.2f}')
print(f'Adult Meals: ${adult_cost:.2f}')
print(f'Drinks: ${drink_cost:.2f}')
print(f'Sides: ${sides_cost:.2f}')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')
print()
payment = float(input(f'What is the payment amount? $'))
change = payment - total
print()
print(f'Your change is ${change:.2f}.') 
print('Please take your receipt below.')
print('Thank you and have a nice day!')