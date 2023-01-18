"""
Luke Russell
Multiplication Table 
2/25/21
"""
import math
table_size = int(input("How many rows and columns do you want? "))
maximum = table_size * table_size
digits = int(math.log10(maximum)) + 1 
range_size = table_size + 1 
for row_amount in range(1, range_size):
    for column_amount in range(1, range_size): 
        value = column_amount * row_amount  
        print(f'{value:{digits}}', end=' ')
    print()

