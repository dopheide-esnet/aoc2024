#!/usr/bin/env python3

import time

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

def PrintMap(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            print(map[y][x],end='')
        print()

def PrintMap2(boxes,walls,ry,rx,my,mx):
    for y in range(my):
        for x in range(mx):
            if( (y,x) in walls):
                print("#",end='')
            elif( (y,x) in boxes):
                print("[",end='')
            elif( (y,x-1) in boxes):
                print("]",end='')
            elif( (y,x) == (ry,rx)):
                print("@",end='')
            else:
                print(".",end='')
        print()

class Box:
    def __init__(self,y,x):
        self.x = x
        self.y = y
    def CanMove(self,boxes,walls,m,to_move):
        bx = self.x
        by = self.y

        if(by,bx) not in to_move:
            to_move.append( (by,bx))

        if(m == ">"):
            if( (by,bx+2) in walls):
                return False
            elif (by,bx+2) in boxes: # plus 2!
                return boxes[(by,bx+2)].CanMove(boxes,walls,m,to_move)
            else:
                return True # this space should be a '.'
        elif(m == "<"):
            if( (by,bx-1) in walls):
                return False
            elif (by,bx-2) in boxes: # minus 2!
                return boxes[(by,bx-2)].CanMove(boxes,walls,m,to_move)
            else:
                return True
        elif(m == "v"):
            if (by+1,bx) in walls or (by+1,bx+1) in walls:
                return False
            elif (by+1,bx) in boxes:
                # a box right underneath
                return boxes[(by+1,bx)].CanMove(boxes,walls,m,to_move)
            elif (by+1,bx-1) in boxes:
                if (by+1,bx+1) in boxes:
                    # two boxes underneath
                    return boxes[(by+1,bx-1)].CanMove(boxes,walls,m,to_move) and boxes[(by+1,bx+1)].CanMove(boxes,walls,m,to_move)
                else:
                    # one box to the left
                    return boxes[(by+1,bx-1)].CanMove(boxes,walls,m,to_move)
            elif (by+1,bx+1) in boxes:
                # one box to the right
                return boxes[(by+1,bx+1)].CanMove(boxes,walls,m,to_move)
            else:
                return True
        elif(m == "^"):
            if (by-1,bx) in walls or (by-1,bx+1) in walls:
                return False
            elif (by-1,bx) in boxes:
                # a box right above
                return boxes[(by-1,bx)].CanMove(boxes,walls,m,to_move)
            elif (by-1,bx-1) in boxes:
                if (by-1,bx+1) in boxes:
                    # two boxes above
                    return boxes[(by-1,bx-1)].CanMove(boxes,walls,m,to_move) and boxes[(by-1,bx+1)].CanMove(boxes,walls,m,to_move)
                else:
                    # one box to the left
                    return boxes[(by-1,bx-1)].CanMove(boxes,walls,m,to_move)
            elif (by-1,bx+1) in boxes:
                # one box to the right
                return boxes[(by-1,bx+1)].CanMove(boxes,walls,m,to_move)
            else:
                return True
            
    def Move(self,m):
        if(m == ">"):
            self.x += 1
        elif(m == "<"):
            self.x -= 1
        elif(m == "v"):
            self.y += 1
        elif(m == "^"):
            self.y -= 1

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
    moves = []
    y=0
    map2 = []
    boxes = {}
    walls = []
    for line in lines:
        new_row = []
        row = list(line)
        if('#' in row):
            if('@' in row):
                ry = y
                rx = row.index('@')
            map.append(row)
            x = 0
            for r in row:
                if(r == '@'):
                    new_row.extend(['@','.'])
                elif(r == "O"):
                    new_row.extend(['[',']'])
                    boxes[(y,x)] = Box(y,x)
                elif(r == '#'):
                    new_row.extend(['#','#'])
                    walls.extend([(y,x),(y,x+1)])
                else:
                    new_row.extend([r,r])
                x+=2
            map2.append(new_row)
        else:
            moves.extend(list(line))
        y+=1

    orig_ry = ry
    orig_rx = rx

    # Part 1
    for m in moves:
        if m == ">":
            y = ry
            # quick move
            if(map[y][rx+1] == '.'):
                map[ry][rx] = "."
                rx += 1
                map[ry][rx] = '@'
            else:
                for b in range(rx+1,len(map[0])):
                    # find the blocker
                    if(map[y][b] == '#'):
                        break
 #               print("blocker at",b)
                dot = rx
                for x in range(rx+1,b):
                    if(map[y][x] == '.'):
                        dot = x
                        break
                if(dot > rx):
                    # there is a free space, everything to the left of this to the robot can move right one space
                    for x in reversed(range(rx,dot+1)):
#                        print("Moving",map[y][x-1],"to",map[y][x])
                        map[y][x] = map[y][x-1]
                    # old robot location needs '.'
                    map[ry][rx] = "."
                    rx+=1
        elif m == "<":
            y = ry
            if(map[y][rx-1] == '.'):
                map[ry][rx] = '.'
                rx -= 1
                map[ry][rx] = '@'
            else:
                for b in reversed(range(0,rx)):
                    if(map[y][b] == '#'):
                        break
                dot = rx
                for x in reversed(range(b,rx)):
                    if(map[y][x] == '.'):
                        dot = x
                        break
                if(dot < rx):
                    for x in range(dot,rx):
                        map[y][x] = map[y][x+1]
                    map[ry][rx] = "."
                    rx -= 1
        elif( m == "v"):
            x = rx
            if(map[ry+1][x] == '.'):
                map[ry][rx] = '.'
                ry += 1
                map[ry][rx] = '@'
            else:
                for b in range(ry+1,len(map)):
                    if(map[b][x] == '#'):
                        break
                dot = ry
                for y in range(ry+1,b):
                    if(map[y][x] == "."):
                        dot = y
                        break
                if(dot > ry):
                    for y in reversed(range(ry,dot+1)):
                        map[y][x] = map[y-1][x]
                    map[ry][rx] = '.'
                    ry+=1
        elif( m == "^"):
            x = rx
            if(map[ry-1][x] == '.'):
                map[ry][rx] = '.'
                ry -= 1
                map[ry][rx] = '@'
            else:
                for b in reversed(range(0,ry)):
                    if(map[b][x] == '#'):
                        break
                dot = ry
                for y in reversed(range(b,ry)):
                    if(map[y][x] == '.'):
                        dot = y
                        break
                if(dot < ry):
                    for y in range(dot,ry):
                        map[y][x] = map[y+1][x]
                    map[ry][rx] = '.'
                    ry -= 1
#    PrintMap(map)
#        time.sleep(1)

    total = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if(map[y][x] == "O"):
                total += y * 100 + x

    print("Part 1",total)

    # Part 2
    rx = orig_rx * 2
    ry = orig_ry

    num = 1
    for m in moves:
#        print(m,"     ",num,end='')
        to_move = []
        canmove = False
        if(m == '>'):
            y = ry
            # quick move
            if( (y,rx+1) not in walls and (y,rx+1) not in boxes):
                rx += 1
            else:
                if (y,rx+1) in walls:
                    canmove = False
                elif (y,rx+1) in boxes:
                    canmove = boxes[(y,rx+1)].CanMove(boxes,walls,m,to_move)
                    if(canmove):
                        rx += 1
                        new_boxes = {}
                        for (by,bx) in to_move:
                            boxes[(by,bx)].Move(m)
                            new_boxes[(by,bx+1)] = boxes[(by,bx)]
                            del boxes[(by,bx)]
                            
                        # copy remaining
                        for b in boxes:
                            new_boxes[b] = boxes[b]
                        boxes = new_boxes

                else:
                    print("Error")
                    exit(0)
        elif(m == '<'):
            y = ry
            if( (y,rx-1) not in walls and (y,rx-2) not in boxes):
                rx -= 1
            else:
                if (y,rx-1) in walls:
                    canmove = False
                elif (y,rx-2) in boxes:
                    canmove = boxes[(y,rx-2)].CanMove(boxes,walls,m,to_move)
                    if(canmove):
                        rx -= 1

                        new_boxes = {}
                        for (by,bx) in to_move:
                            boxes[(by,bx)].Move(m)
                            new_boxes[(by,bx-1)] = boxes[(by,bx)]
                            del boxes[(by,bx)]
                            
                        # copy remaining
                        for b in boxes:
                            new_boxes[b] = boxes[b]
                        boxes = new_boxes

                else:
                    print("Error 2")
                    exit(0)

        elif(m == "v"):
            x = rx
            if( (ry+1,x) not in walls and (ry+1,x) not in boxes and (ry+1,x-1) not in boxes):
                ry += 1
            else:
                if (ry+1,x) in walls:
                    canmove = False
                elif (ry+1,x) in boxes:
                    # one box straight under
                    canmove = boxes[(ry+1,x)].CanMove(boxes,walls,m,to_move)
                elif (ry+1,x-1) in boxes:
                    # one box to the left
                    canmove = boxes[(ry+1,x-1)].CanMove(boxes,walls,m,to_move)
                else:
                    print("Error 3")
                    exit(0)
                if(canmove):
                    ry += 1

                    new_boxes = {}
                    for (by,bx) in to_move:
                        boxes[(by,bx)].Move(m)
                        new_boxes[(by+1,bx)] = boxes[(by,bx)]
                        del boxes[(by,bx)]
                    # copy remaining
                    for b in boxes:
                        new_boxes[b] = boxes[b]
                    boxes = new_boxes

        elif(m == "^"):
            x = rx
            if( (ry-1,x) not in walls and (ry-1,x) not in boxes and (ry-1,rx-1) not in boxes):
                ry -= 1
            else:
                if (ry-1,x) in walls:
                    canmove = False
                elif (ry-1,x) in boxes:
                    canmove = boxes[(ry-1,x)].CanMove(boxes,walls,m,to_move)
                elif (ry-1,x-1) in boxes:
                    canmove = boxes[(ry-1,x-1)].CanMove(boxes,walls,m,to_move)
                else:
                    print("Error 4")
                    exit(0)
#                print(canmove,'')
                if(canmove):
                    ry -= 1                    
                    new_boxes = {}
                    for (by,bx) in to_move:
                        boxes[(by,bx)].Move(m)
                        new_boxes[(by-1,bx)] = boxes[(by,bx)]
                        del boxes[(by,bx)]
                    # copy remaining
                    for b in boxes:
                        new_boxes[b] = boxes[b]
                    boxes = new_boxes
        else:
            print("WTF")
        num+=1
#        print()
#        if(num > 300):
    PrintMap2(boxes,walls,ry,rx,len(map2),len(map2[0]))
#            time.sleep(1)

    total = 0
    for (by,bx) in boxes:
        # closest edge or just 0,0?
        total += by*100 + bx

    print("Part 2",total)

    exit(1)




