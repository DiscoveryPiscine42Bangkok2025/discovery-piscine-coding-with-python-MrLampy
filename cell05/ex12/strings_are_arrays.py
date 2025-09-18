#!/usr/bin/env python
import sys
found = 0
if len(sys.argv) == 2:
    for i in sys.argv[1]:
        if i == 'z':
            found = 1
            print('z',end='')
if not found: print('none')