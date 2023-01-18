"""
Luke Russell
Loan Checkpoint
2/9/21
"""
print('Welcome to Broke Boi Bank, we specialize in loans among other things.')
loan = input('Would you like to apply for a loan today? Please enter YES or NO: ')

if loan.lower() == 'yes':
    print('Please answer the following on a scale between 1-10: ')
    amount = int(input('How big is your loan? '))
    credit = int(input('How good is your credit history? '))
    income = int(input('How high is your income? '))
    down_payment = int(input('How high is your down payment? '))
else: 
    print('Have a great day! Thank you for choosing Broke Boi Bank!')          

qualify = False
if amount >= 6:
    if credit >= 7 and income >= 7:
        qualify = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 8:
            qualify = True
        else: 
            qualify = False
    else: 
        qualify = False
else:
    if credit < 4:
        qualify = False
    else: 
        if income >= 7 or down_payment >= 7:
            qualify = True
        elif income >= 4 and down_payment >=4:
            qualify = True
        else:
            qualify = False
if qualify:
    print('You are approved for your loan! Thank you for choosing Broke Boi Bank! Have a nice day.')
else:
    print('Unfortunetly you do not qualify for a loan. We hope to see you again soon. Thank you for choosing Broke Boi Bank! Have a nice day.')
                                   
