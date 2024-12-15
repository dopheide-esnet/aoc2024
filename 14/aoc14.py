#!/usr/bin/env python3

import re

testcase = False
if testcase:
    file = "test.txt"
    Mx = 11
    My = 7
else:
    file = "input.txt"
    Mx = 101
    My = 103

def TestWorks():
    return True

class Robot:
    def __init__(self,x,y,vx,vy):
        self.sx = x
        self.sy = y
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def Move(self):
        self.x += self.vx
        self.y += self.vy

        if(self.x == Mx):
            self.x == 0
        if(self.y == My):
            self.y == 0
        while(self.x > Mx):
            self.x -= Mx
        while(self.y > My):
            self.y -= My
        while(self.x < 0):
            self.x += Mx
        while(self.y < 0):
            self.y += My
    def Move2(self,howmany):
        self.x += howmany * self.vx
        self.y += howmany * self.vy
        negx = False
        negy = False
        if(self.x < 0):
            negx = True
            self.x = self.x * -1
        if(self.y < 0):
            negy = True
            self.y = self.y * -1
        self.x = self.x % Mx
        self.y = self.y % My
        if(negx):
            self.x = Mx + self.x * -1
            if(self.x == Mx):
                self.x = 0
        if(negy):
            self.y = My + self.y * -1
            if(self.y == My):
                self.y = 0

if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    # p=29,20 v=25,-55
    robots = []
    robot_re = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')
    for line in lines:
        m = robot_re.search(line)
        if(m):
            robots.append(Robot(int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4))))


#    for x in range(100):
#        for r in robots:
#            r.Move()
    for r in robots:
        r.Move2(100)
    
    midx = int(Mx/2)
    midy = int(My/2)
    quads = [0,0,0,0]
    for r in robots:
#        print(r.x,r.y,r.sx,r.sy)
        if(r.x < midx and r.y < midy):
            quads[0] += 1
        elif(r.x > midx and r.y < midy):
            quads[1] += 1
        elif(r.x < midx and r.y > midy):
            quads[2] += 1
        elif(r.x > midx and r.y > midy):
            quads[3] += 1

    print("Part1:",(quads[0] * quads[1] * quads[2] * quads[3]))

    # Reset
    for r in robots:
        r.x = r.sx
        r.y = r.sy
#        r.Move2(690)
        # 471
        # 572
        # 673
        # 784

        # Find with most are within the middle range?

    for x in range(10000):

        tree = True
        outliers = 0
        for r in robots:
            r.x = r.sx
            r.y = r.sy
            r.Move2(x)
            if(r.x < 20 and r.y < 20):
                outliers += 1
            if(outliers > 6):
                tree = False
                break

        # Print Map
#        if(outliers < 5):
#            tree = True

        if(tree):
            print(x)
            for y in range(My):
                for x in range(Mx):
                    count = 0
                    for r in robots:
                        if(r.x == x and r.y == y):
                            count += 1
                    if(count == 0):
                        print(".",end='')
                    else:
                        print("X",end='')
                print()
        
