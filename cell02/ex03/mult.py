#!/usr/bin/env python
first = int(input('Enter the first number:\n'))
second = int(input('Enter the second number:\n'))
product = first*second
print(f'{first} x {second} = {product}')
if not product: print('The result is positive and negative.')
elif product > 0:
    print('The result is positive.')
elif product < 0:
    print('The result is negative.')