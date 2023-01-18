"""
Luke Russell
Bank Account team activity
3/11/21
"""
account_name = []
account_balance = []
name = None
balance = 0
print("Please enter the following information. Type 'quit' to stop.")
while name != "quit":
    name = input("Please enter the name of the account: ")
    if name != 'quit':
        balance = float(input("Please enter the balance of the above account: "))
        account_name.append(name)
        account_balance.append(balance)
total = 0
print()
print("Account Information: ")
for i in range(len(account_name)):
    print(f"{account_name[i]} - ${account_balance[i]:.2f}")
    total += account_balance[i]
average = total / len(account_balance)
print()
print(f"Total Balance: ${total:.2f}")
print(f"Average Balance: ${average:.2f}")