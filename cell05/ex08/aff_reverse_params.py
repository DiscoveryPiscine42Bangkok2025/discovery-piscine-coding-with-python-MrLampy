#!/usr/bin/env python
import sys
x = sys.argv
if len(x[1:]) >= 2:
    for i in reversed(x[1:]):
        print(i)
else: print('none')