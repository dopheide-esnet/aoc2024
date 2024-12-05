#!/usr/bin/env python3

import re
import functools

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

global rules

def TestWorks():
    return True

def SortbyRules(a,b):
    if( (a,b) in rules):
        return -1
    elif (b,a) in rules:
        return 1

if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    order = []
    rules = []
    total = 0
    total2 = 0
    for line in lines:
        m = re.search(r'^(\d+)\|(\d+)',line)
        if(m):
            a = int(m.group(1))
            b = int(m.group(2)) 
            rules.append((a,b))
        elif ',' in line:
            pages = line.split(',')
            pages = [ int(x) for x in pages ]
            ordered = sorted(pages,key=functools.cmp_to_key(SortbyRules))
#            print(ordered)
            if(ordered == pages):
                total += pages[int(len(pages)/2)]
            else:
                total2 += ordered[int(len(ordered)/2)]

    print(total)
    print(total2)
