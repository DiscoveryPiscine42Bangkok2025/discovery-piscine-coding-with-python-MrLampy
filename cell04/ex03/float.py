#!/usr/bin/env python
user = float(input('Give me a number: '))
if user.is_integer(): user = 'integer'
else: user = 'decimal'
print(f'This number is {user}.')