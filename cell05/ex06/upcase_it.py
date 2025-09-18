#!/usr/bin/env python
import sys

if len(sys.argv) == 2:
    user = sys.argv[1]
    print(user.upper())
else: 
    print('none')