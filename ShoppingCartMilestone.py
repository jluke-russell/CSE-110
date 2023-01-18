"""
Luke Russell
Shopping Cart Milestone
3/5/21
"""
print("Welcome to IKEA.com!")
print()
print("Please select one action from below: ")
print()
print("1. Add item")
print("2. View cart")
print("3. Remove item")
print("4. Show total")
print("5. Quit")
print()

action = 0
cart = []
prices = []
item = None
total = 0 
payment = 0

action = int(input("Please select one action to perform: "))
while action != 5:
    if action == 1:  
        item = input('Please enter what you want to add to the cart. ')
        price = float(input(f"What is the price of the {item}? "))
        if item != "Quit":
            print(f"{item} has been added to the cart!")
            cart.append(item)
            prices.append(price)
            action = int(input("Please select an action to perform: "))
    if action == 2: 
        print("Your cart has the following: " )
        for i in range(len(cart)):     
            print(f"{cart[i]} - ${prices[i]:.2f}")
        action = int(input("Please select an action to perform: "))      
    if action == 3:           
        remove = input("What item would you like to remove? ")
        i = cart.index(remove)
        del(cart[i])
        del(prices[i])
        action = int(input("Please select an action to perform: "))
    if action == 4:
        print("The total amount for the cart is: ")
        for i in range(len(cart)):
            total += prices[i]
        print(f"${total:.2f}")
        action = int(input("Please select an action to perform: "))
    if action == 5: 
        print(f"Your total is ${total:.2f}")
        payment = float(input("Please enter payment amount: $"))
        if payment == total:
            print() 
        print("Transaction Complete") 
        print("Thank You for shopping at IKEA!")