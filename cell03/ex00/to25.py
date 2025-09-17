#!/usr/bin/env python
user = int(input('Enter a number less than 25\n'))
if user < 25:
    while user <= 25:
        print(f'Inside the loop, my variable is {user}')
        user += 1
else: print('Error')