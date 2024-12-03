#!/usr/bin/env python3

import re

testcase = False
if testcase:
    file = "test2.txt"
else:
    file = "input.txt"

def TestWorks():
    return True


if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    line = ''.join(lines)

    total = 0
    mul_re = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    digit_re = re.compile(r'mul\((\d+),(\d+)\)')
#    for line in lines:
    matches = mul_re.findall(line)
    for match in matches:
        m = digit_re.search(match)
        if(m):
            total += int(m.group(1)) * int(m.group(2))

    print("Part 1:",total)

    do_re = re.compile(r'do\(\)')
    dont_re = re.compile(r'don\'t\(\)')
    do_i = []
    dont_i = []
#    for line in lines:
    do_matches = do_re.finditer(line)
    for do_match in do_matches:
        do_i.append(do_match.start())

    dont_matches = dont_re.finditer(line)
    for dont_match in dont_matches:
        dont_i.append(dont_match.start())
    
    enable = True
    total = 0

#    for line in lines:
    mul_matches = mul_re.finditer(line)
    for match in mul_matches:

        do_index = -1
        dont_index = -1

        if(len(do_i) > 0):
            while(match.start() > do_i[0]):
                do_index = do_i[0]
                del do_i[0]
                if(len(do_i)==0):
                    break
        if(len(dont_i) > 0):
            while(match.start() > dont_i[0]):
                dont_index = dont_i[0]
                del dont_i[0]
                if(len(dont_i)==0):
                    break 

#            print(do_index,dont_index)
        if(do_index != -1 and dont_index != -1):
            if(do_index > dont_index):
                enable = True
            else:
                enable = False
        elif(do_index != -1):
            enable = True
        elif(dont_index != -1):
            enable = False

        if(enable):
            m = digit_re.search(match.group())
            if(m):
                total += int(m.group(1)) * int(m.group(2))

    print("Part 2:",total)


