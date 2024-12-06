#!/usr/bin/env python3

import copy

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class Guard:
    def __init__(self,y,x):
        self.y = y
        self.x = x
        self.facing = 0 # 0 = up, 1 = right, etc
    def move(self,map):
        mx = len(map[0])
        my = len(map)
        if(self.facing == 0):
            if(self.y == 0):
                return 0 # we've left the Lab once we move
            elif(map[self.y - 1][self.x] == '^'):
                # We've been here before!  # Loop !
                return 2
            elif(map[self.y - 1][self.x] != '#'):
                self.y -= 1
                map[self.y][self.x] = '^' # mark that we've been here and the direction we were moving
                return 1
            else:
                self.facing = 1  # turn, but don't move yet
                return 1
        elif(self.facing == 1):
            if(self.x == mx - 1):
                return 0
            elif(map[self.y][self.x+1] == '>'):
                # We've been here before!  # Loop !
                return 2
            elif(map[self.y][self.x+1] != '#'):
                self.x += 1
                map[self.y][self.x] = '>'
                return 1
            else:
                self.facing = 2
                return 1
        elif(self.facing == 2):
            if(self.y == my - 1):
                return 0
            elif(map[self.y+1][self.x] == 'v'):
                # We've been here before!  # Loop !
                return 2
            elif(map[self.y+1][self.x] != '#'):
                self.y += 1
                map[self.y][self.x] = 'v'
                return 1
            else:
                self.facing = 3
                return 1
        elif(self.facing == 3):
            if(self.x == 0):
                return 0
            elif(map[self.y][self.x-1] == '<'):
                # We've been here before!  # Loop !
                return 2
            elif(map[self.y][self.x - 1] != '#'):
                self.x -= 1
                map[self.y][self.x] = '<'
                return 1
            else:
                self.facing = 0
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

    map = []
    for line in lines:
        row = list(line)
        if '^' in row:
            startx = row.index('^')
            row[startx] = 'X'  # replace ^ with a 'X' "i've been here" marker
            starty = len(map)
            guard = Guard(starty,startx)
        map.append(row)

    orig_map = copy.deepcopy(map)

    in_lab = True
    while(in_lab):
        in_lab = guard.move(map)

    total = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if(map[y][x] != '#' and map[y][x] != '.'):
                total += 1

    print("Part 1:",total)

    # Print Map
#    for y in map:
#        print(''.join(y))

    # Part 2:
    marked_map = map

    loops = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            # Only the current path is potential positions for a new blocker.
            # Otherwise the guard would never encounter it.
#            if(y != starty or x != startx):
            if(marked_map[y][x] != '.' and marked_map[y][x] != '#' and (y != starty or x != startx)):
                map = copy.deepcopy(orig_map)
                map[y][x] = "#"
                guard = Guard(starty,startx)
                in_lab = 1
                while(in_lab == 1):
                    # Now we can return three states:
                    #    In the lab, Off the map, or in a loop
                    in_lab = guard.move(map)
                    if(in_lab == 2):
                        loops += 1
#                        print("Block at:",y,x)
                        break
    
    print("Part 2:",loops)
