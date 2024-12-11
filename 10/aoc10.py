#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class Trailhead:
    def __init__(self,y,x):
        self.y = y
        self.x = x
        self.score = 0
        self.nines = []

def TrailSearch(y,x,map):
    results = []
    current = map[y][x]
    next = current + 1
#    print("Searching from:",y,x,next)
    if(y > 0):
        # check up
#        print("check up")
        if(map[y-1][x] == next):
            if(next == 9):
                results.append((y-1,x))
            else:
                results.extend(TrailSearch(y-1,x,map))
    if(y < len(map) - 1):
        # check down
#        print("check down")
        if(map[y+1][x] == next):
            if(next == 9):
                results.append((y+1,x))
            else:
                results.extend(TrailSearch(y+1,x,map))
    if(x > 0):
        # check left
#        print("check left")
        if(map[y][x-1] == next):
            if(next == 9):
                results.append((y,x-1))
            else:
                results.extend(TrailSearch(y,x-1,map))
    if(x < len(map[0]) - 1):
        # check right
        if(map[y][x+1] == next):
            if(next == 9):
                results.append((y,x+1))
            else:
                results.extend(TrailSearch(y,x+1,map))

    return results

if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    map = []
    trails = []
    y = 0
    for line in lines:
        row = list(line)
        row = [ int(x) for x in row ]
        for x in range(len(row)):
            if row[x] == 0:
                trails.append(Trailhead(y,x))
        map.append(row)
        y += 1
    

    total = 0
    total2 = 0
    for t in trails:
        # Make sure results are unique
#        results = list(set(TrailSearch(t.y,t.x,map)))
        results = TrailSearch(t.y,t.x,map)
        total2 += len(results)
        part1_results = list(set(results))
        t.nines = part1_results
        t.score = len(part1_results)
        total += t.score

    print("Part1:",total)
    print("Part2:",total2)







