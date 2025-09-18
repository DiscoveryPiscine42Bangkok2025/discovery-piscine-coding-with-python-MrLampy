#!/usr/bin/env python
import sys

if len(sys.argv) == 3:
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    if first > second: print('none')
    else:
        listA = []
        for i in range(first,second+1):
            listA.append(i)
        print(listA)
else:
    print('none')