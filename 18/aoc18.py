#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2000)

testcase = False
if testcase:
    file = "test.txt"
    my = 6
    mx = 6
    steps = 12
else:
    file = "input.txt"
    my = 70
    mx = 70
    steps = 1024

def TestWorks():
    return True

def ShortestPath(paths,yx,my,mx,corrupted,score):
    (y,x) = yx

    if (y,x) not in paths:
        paths[(y,x)] = score
    else:
        if(score <= paths[(y,x)]):
            paths[(y,x)] = score
        elif(score > paths[(y,x)]):
            return
        if(y == my and x == mx):
            return


        # might not help to do this
#        if (my,mx) in paths:
#            if(score > paths[(my,mx)]):
#                return

    next = []
    if(y>0):
        next.append((y-1,x))
    if(y<my):
        next.append((y+1,x))
    if(x>0):
        next.append((y,x-1))
    if(x<mx):
        next.append((y,x+1))

#    print(next)

    for n in next:
        if n in corrupted:
            continue
        if n in paths:
            if(paths[n] <= score + 1):
                continue
        ShortestPath(paths,n,my,mx,corrupted,score+1)
    else:
        return        

if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    corrupted = []
    for line in lines:
        (y,x) = line.split(',')
        corrupted.append((int(y),int(x)))
    
    corrupted_steps = corrupted[:steps]

    paths = {}
    ShortestPath(paths,(0,0),my,mx,corrupted_steps,0)

#    print(paths)
    print("Part 1:",paths[(my,mx)])

#  Part 2: dumb way
    for i in range(steps,len(lines)):
        paths = {}
        ShortestPath(paths,(0,0),my,mx,corrupted[:i],0)
        if((my,mx) not in paths):
            print("Part 2",corrupted[i-1]) 
            break





