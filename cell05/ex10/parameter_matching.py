#!/usr/bin/env python
import sys
if len(sys.argv) == 2:
    user = input('What was the parameter? ')
    if user == sys.argv[1]:
        print('Good job!')
    else: print('Nope, sorry...')
else: print('none')