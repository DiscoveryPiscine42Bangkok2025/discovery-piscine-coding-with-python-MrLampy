#!/usr/bin/env python
import sys

for i in sys.argv[1:]:
    if 'ism' in i[-3:]:
        continue
    else:
        print(f'{i}ism')
