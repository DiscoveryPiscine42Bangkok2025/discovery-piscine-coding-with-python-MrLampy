#!/usr/bin/env python
import sys

param = len(sys.argv) - 1
if param == 0: 
    print('none')
    exit()
print(f'parameters: {param}')
for i in sys.argv[1:]:
    print(f'{i}: {len(i)}')