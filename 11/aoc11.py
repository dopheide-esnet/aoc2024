#!/usr/bin/env python3

import copy

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

def Blink(stones):
    s = 0
    while(s < len(stones)):
        if(stones[s] == 0):
            stones[s] = 1
        elif(len(str(stones[s])) % 2 == 0):
            # even number of digits
            mid = int(len(str(stones[s]))/2)
            left = str(stones[s])[:mid]
            right = str(stones[s])[mid:]
            stones[s] = int(left)
            stones.insert(s+1,int(right))
            s += 1
        else:
            stones[s] = stones[s] * 2024
        s += 1

class Stone:
    def __init__(self,depth):
#        self.val = d
        self.depths = {depth: 1} # depth: score

#def Blink2(stones,known_stones,depth,max_depth):
#    s = 0
#    next_stones = copy.deepcopy(stones)
#    while(s < len(stones)):
#        if(depth == max_depth):
#            if(stones[s] not in known_stones):
#                known_stones.append(Stone(stones[s],depth))
#        else:
#            if(stones[s] == 0):
#                next_stones[s] = 1
#            elif(len(str(stones[s])) % 2 == 0):
#                mid = int(len(str(stones[s]))/2)                
#
#            else:
#                next_stones[s] = stones[s] * 2024
#        s += 1



def Blink3(stone,known_stones,depth,max_depth):
#    if(stone not in known_stones):
#        known_stones[stone]=Stone(depth)
    if(depth == max_depth):
        if(stone not in known_stones):
            known_stones[stone]=Stone(depth)
        else:
            known_stones[stone].depths[depth] = 1
        return
    else:
        if(stone == 0):
            # If it's in known_stones w/ this depth, just calculate the score
            if(stone in known_stones):
                if(depth in known_stones[stone].depths):
                    return
                else:
                    if(1 in known_stones and depth+1 not in known_stones[1].depths):
                        Blink3(1,known_stones,depth+1,max_depth)
                    elif(1 not in known_stones):
                        Blink3(1,known_stones,depth+1,max_depth)
                    known_stones[stone].depths[depth]=known_stones[1].depths[depth+1]
            else:
                known_stones[stone]=Stone(depth)
                if(1 in known_stones and depth+1 not in known_stones[1].depths):
                    Blink3(1,known_stones,depth+1,max_depth)
                elif(1 not in known_stones):
                    Blink3(1,known_stones,depth+1,max_depth)
                # correct the default depth score that was just created.
                known_stones[stone].depths[depth]=known_stones[1].depths[depth+1]

        elif(len(str(stone)) % 2 == 0):
            # If it's in known_stones w/ this depth, just calculate the score
            mid = int(len(str(stone))/2)
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            ### TODO, re-order so all of this left stuff happens first?
#            Blink3(int(left),known_stones,depth+1,max_depth)
#            Blink3(int(right),known_stones,depth+1,max_depth)

            if(stone in known_stones):
                if(depth in known_stones[stone].depths):
                    return
                else:
                    if(left in known_stones and depth+1 not in known_stones[left].depths):
                        Blink3(left,known_stones,depth+1,max_depth)
                    elif(left not in known_stones):
                        Blink3(left,known_stones,depth+1,max_depth)
                    if(right in known_stones and depth+1 not in known_stones[right].depths):
                        Blink3(right,known_stones,depth+1,max_depth)
                    elif(right not in known_stones):
                        Blink3(right,known_stones,depth+1,max_depth)
                    known_stones[stone].depths[depth]=known_stones[left].depths[depth+1] + known_stones[right].depths[depth+1]
            else:
                known_stones[stone]=Stone(depth)
                if(left in known_stones and depth+1 not in known_stones[left].depths):
                    Blink3(left,known_stones,depth+1,max_depth)
                elif(left not in known_stones):
                    Blink3(left,known_stones,depth+1,max_depth)
                if(right in known_stones and depth+1 not in known_stones[right].depths):
                    Blink3(right,known_stones,depth+1,max_depth)
                elif(right not in known_stones):
                    Blink3(right,known_stones,depth+1,max_depth)
                # correct the default depth score that was just created.
                known_stones[stone].depths[depth]=known_stones[left].depths[depth+1] + known_stones[right].depths[depth+1]

        else:
            # If it's in known_stones w/ this depth, just calculate the score
            next_stone = stone * 2024
            if(stone in known_stones):
                if(depth in known_stones[stone].depths):
                    return
                else:
                    if(next_stone in known_stones and depth+1 not in known_stones[next_stone].depths):
                        Blink3(next_stone,known_stones,depth+1,max_depth)
                    elif(next_stone not in known_stones):
                        Blink3(next_stone,known_stones,depth+1,max_depth)
                    known_stones[stone].depths[depth]=known_stones[next_stone].depths[depth+1]
            else:
                known_stones[stone]=Stone(depth)
                if(next_stone in known_stones and depth+1 not in known_stones[next_stone].depths):
                    Blink3(next_stone,known_stones,depth+1,max_depth)
                elif(next_stone not in known_stones):
                    Blink3(next_stone,known_stones,depth+1,max_depth)
                # correct the default depth score that was just created.
                known_stones[stone].depths[depth]=known_stones[next_stone].depths[depth+1]


if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    stones = lines[0].split(" ")
    stones = [ int(x) for x in stones ]

# Previous Part 1
#    for x in range(25):
#        Blink(stones)
#    print("Part 1:",len(stones))

    known_stones = {}
    total = 0
    for s in stones:
        Blink3(s,known_stones,0,75)
        total += known_stones[s].depths[0]
    print(total)

#    for s in known_stones:
#        print(s, known_stones[s].depths)
