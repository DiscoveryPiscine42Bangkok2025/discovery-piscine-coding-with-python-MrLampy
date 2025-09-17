#!/usr/bin/env python
import sys
if not (len(sys.argv) >1 and sys.argv[1]):
    for i in range(11):
        print(f'Table de {i}: ',end='')
        for ii in range(11):
            print(f'{i*ii}',end=' ')
        print()

