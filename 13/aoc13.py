#!/usr/bin/env python3

import re
import subprocess
import numpy as np
import sys

testcase = False
if testcase:
    file = "test5.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class Machine:
    def __init__(self,ax,ay,bx,by,px,py):
        self.a = (ax,ay)
        self.b = (bx,by)
        self.prize = (px,py)
    def Part1(self):
        # Do it the dumb way
        (ax,ay) = self.a
        (bx,by) = self.b
        (px,py) = self.prize

        max_a = min(min(int(px / ax),int(py / ay)),100)
        max_b = min(min(int(px / bx),int(py / by)),100)

        small = 0
        sa = 0
        sb = 0
        for a in range(1,max_a+1):
            for b in range(1,max_b+1):
                x = a * ax + b * bx
                y = a * ay + b * by
                if(px == x and py == y):
                    tokens = a*3 + b
                    if(small == 0):
                        small = tokens
                        sa = a
                        sb = b
                    elif(tokens < small):
                        small = tokens
                        sa = a
                        sb = b
        return small
    def Part2(self):
        # Wait a second... Math says these are linear equations, there is only one solution
        # where the lines cross.
        (ax,ay) = self.a
        (bx,by) = self.b
        (px,py) = self.prize
#        px = px + 10000000000000  # python still giving bad answers?
#        py = py + 10000000000000

## LULZ.. doesn't work cause python's int/float stuff is a bit wonky
# For example:
# Button A: X+94, Y+20
# Button B: X+57, Y+71
# Prize: X=14573, Y=8929
#
# A = 95.00000000000001

#        A = (px - ((bx * py) / by)) / (ax - ((bx * ay)/by))
#        print(A)

        res = subprocess.run(["./a.out",str(ax),str(ay),str(bx),str(by),str(px),str(py)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT, text=True)
        A = float(res.stdout)
        print("From C, A:",float(res.stdout))

        Astr = str(A)
        if(".00000" in Astr):
            Alist = Astr.split('.00000')
            A = int(Alist[0])
#        if(".99999" in Astr):
#            Alist = Astr.split('.99999')
#            A = int(Alist[0]) + 1

        if(A % 1 == 0):
            B = (px - (A * ax)) / bx
            return int(3*A + B)
        else:
            return 0
        
    def Part2LessMath(self):
        (ax,ay) = self.a
        (bx,by) = self.b
        (px,py) = self.prize


        px = px + 10000000000000  # python still giving bad answers?
        py = py + 10000000000000
        det = ax * by - bx * ay
        if(det == 0):
            print("Goddammit!")
            exit(1)

        foo = np.array([[ax,bx],[ay,by]])
        bar = np.array( [px,py])
        x = np.linalg.solve(foo, bar)
#        print(x)
        res = 3*x[0]+x[1]
        # print(res)

        # np.finfo(np.float32).eps = .001
        # np.finfo(np.float64).eps = .001
        res = round(res, 3)
        if(str(res).endswith(".0")):
            # print(f"ends with .0 {int(res)}")
            return(int(res))
        # elif(".000000000" in str(res)):
        #     return(int(res))
        # elif(".999999999" in str(res)):
        #     return(int(res)+1)

        # return int(res)

        return 0


if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    # Note:  There are no minuses, you can only move forward, that's huge
    # Button presses limited to 100

    machines = []
    for line in lines:
        if("Button A" in line):
            m = re.search(r'Button A: X\+(\d+), Y\+(\d+)',line)
            if(m):
                ax = int(m.group(1))
                ay = int(m.group(2))
        elif("Button B" in line):
            m = re.search(r'Button B: X\+(\d+), Y\+(\d+)',line)
            if(m):
                bx = int(m.group(1))
                by = int(m.group(2))
        elif("Prize" in line):
            m = re.search(r'Prize: X\=(\d+), Y\=(\d+)',line)
            if(m):
                px = int(m.group(1))
                py = int(m.group(2))
            machines.append(Machine(ax,ay,bx,by,px,py))

    total = 0
    total2 = 0
    for m in machines:
        res1 = m.Part1()
        total += res1
#        m.Part2LessMath()
        res2 = m.Part2LessMath()
        total2 += res2
        # if(res1 != res2):
            # wtf
            # print(m.a,m.b,m.prize)


    print("Part 1,2:",total, total2)



