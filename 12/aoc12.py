#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class Plot:
    def __init__(self,veggie):
        self.veggie = veggie
        self.coords = []
        self.perimeter = 0
        self.area = 0
        self.sides = 0

def Explore(map,coords,veggie,y,x):
    if(y > 0):
        if(map[y-1][x] == veggie and (y-1,x) not in coords):
            coords.append( (y-1,x) )
            Explore(map,coords,veggie,y-1,x)
    if(y < len(map) - 1):
        if(map[y+1][x] == veggie and (y+1,x) not in coords):
            coords.append( (y+1,x) )
            Explore(map,coords,veggie,y+1,x)
    if(x > 0):
        if(map[y][x-1] == veggie and (y,x-1) not in coords):
            coords.append( (y,x-1) )
            Explore(map,coords,veggie,y,x-1)
    if(x < len(map[0]) - 1):
        if(map[y][x+1] == veggie and (y,x+1) not in coords):
            coords.append( (y,x+1) )
            Explore(map,coords,veggie,y,x+1)

def Perimeter(plot):
    fence = 0
    # any neighbor plot that isn't this veggie needs a fence
    for (y,x) in plot.coords:
        if (y-1,x) not in plot.coords:
            fence += 1
        if (y+1,x) not in plot.coords:
            fence += 1
        if (y,x-1) not in plot.coords:
            fence += 1
        if (y,x+1) not in plot.coords:
            fence += 1
    return fence

def SidesBroken(plot):
    # the first coord should be the top-right corner in all cases

    # Worry about:
    # .....
    # AAAAA
    #     A
    #     A
    (starty,startx) = plot.coords[0]
    y = starty
    x = startx
    sides = 1
    print(plot.veggie)
    facing = "east"
    going = False
    done = False
    while(going == False or done == False):
        going = True
    
        # sides doesn't increase unless we turn
        # EAST
        if(facing == "east"):
            print("east",sides)
            if(x<len(map[0])-1): # right, you can't go east if you're on the edge, but you could still BE there.
                if( (y,x+1) in plot.coords):
                    if(y>0):
                        if( (y-1,x+1) in plot.coords):
                            # we turn north
                            facing="north"
                            sides += 1
                            y = y - 1
                    x = x + 1 # still need to move east..
                    if(y == starty and x == startx):
                        done = True
                    continue                    
            if(y < len(map)-1 and (y+1,x) in plot.coords):
                print("here")
                facing="south"
                sides += 1
            elif(x > 0 and (y,x-1) in plot.coords): # pennisula?
                facing="west"
                sides += 2 # go around the edge.
            else:
#                print("Tiny Island??")
                return 4
    
        # NORTH
        elif(facing == "north"):
            print("north",sides)
            if(y > 0):
                if( (y-1,x) in plot.coords):
                    if(x > 0):
                        if( (y-1,x-1) in plot.coords):
                            facing="west"
                            sides += 1
                            x = x - 1
                    y = y - 1
                    if(y == starty and x == startx):
                        done = True
                    if(y == starty and x == startx and facing=="west"):
                        print("fuck")
                        sides += 1
                        done = True
                    continue
            if(x < len(map[0])-1 and (y,x+1) in plot.coords):
                facing="east"
                sides += 1
            elif(y < len(map[0])-1 and (y+1,x) in plot.coords):
                facing="south"
                sides += 2
            else:
                print("North nope")
                exit(1)

        # SOUTH
        elif(facing == "south"):
            print("south",sides)
            if(y<len(map)-1):
                if( (y+1,x) in plot.coords):
                    if(x < len(map[0])-1):
                        if( (y+1,x+1) in plot.coords):
                            facing="east"
                            sides += 1
                            x = x + 1
                    y = y + 1 # keep moving south
                    if(y == starty and x == startx):
                        done = True
                    continue
            if(x > 0 and (y,x-1) in plot.coords):
                facing="west"
                sides += 1
            elif(y > 0 and (y-1,x) in plot.coords):
                facing="north"
                sides += 2
            else:
                print("South nope")
                exit(1)

        # WEST
        elif(facing == "west"):
            print("west",sides)
            if(x > 0):
                if((y,x-1) in plot.coords):
                    if(y<len(map)-1):
                        if((y+1,x-1) in plot.coords):
                            facing="south"
                            sides += 1
                            y = y + 1
                    x = x - 1  # keep moving west
                    if(y == starty and x == startx):
                        done = True
                    continue
            if(y > 0 and (y-1,x) in plot.coords):
                facing="north"
                sides += 1
            elif(x < len(map[0])-1 and (y,x+1) in plot.coords):
                facing="east"
                sides += 2
            else:
                print("West nope")
        print(y,x,facing)
    return sides

def Sides(plot):
    if(plot.area == 1):
        return 4

    mx = -1
    Mx = -1
    my = -1
    My = -1
    for (y,x) in plot.coords:
        if(mx == -1 or x < mx):
            mx = x
        elif(Mx == -1 or x > Mx):
            Mx = x
        if(my == -1 or y < my):
            my = y
        elif(My == -1 or y > My):
            My = y

    sides = 0

    # Top/Bottom sides
    for y in range(my,My+1):
        on_top_edge = False
        on_bot_edge = False
        for x in range(mx,Mx+1):
            # if it's in coords and the one above it isn't, this is a fence.
            # then find the gaps... either one that does have something above, or one that's missing.
            if (y,x) in plot.coords:
                if (y-1,x) not in plot.coords:
                    if not on_top_edge:
                        sides += 1
                        on_top_edge = True
                else:
                    on_top_edge = False
                if (y+1,x) not in plot.coords:
                    if not on_bot_edge:
                        sides += 1
                        on_bot_edge = True
                else:
                    on_bot_edge = False
            else:
                on_top_edge = False
                on_bot_edge = False

    for x in range(mx,Mx+1):
        on_left_edge = False
        on_right_edge = False
        for y in range(my,My+1):
            if (y,x) in plot.coords:
                if (y,x-1) not in plot.coords:
                    if not on_left_edge:
                        sides += 1
                        on_left_edge = True
                else:
                    on_left_edge = False
                if (y,x+1) not in plot.coords:
                    if not on_right_edge:
                        sides += 1
                        on_right_edge = True
                else:
                    on_right_edge = False
            else:
                on_left_edge = False
                on_right_edge = False

    return sides

def FindPlots(map,plots):
    for y in range(len(map)):
        for x in range(len(map[0])):
            skip = False
            veggie = map[y][x]
            for p in plots:
                if veggie == p.veggie:
                    if (y,x) in p.coords:
                        skip = True
                        break
            if(skip == False):
                # we haven't seen this plot yet
                new_plot = Plot(veggie)
                new_coords = []
                new_coords.append((y,x))
                Explore(map,new_coords,veggie,y,x)
                new_plot.coords = new_coords
                new_plot.area = len(new_coords)
                new_plot.perimeter = Perimeter(new_plot)
#                if(veggie == "R"):
                new_plot.sides = Sides(new_plot)
                plots.append(new_plot)

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
        map.append(row)

    plots = []
    FindPlots(map,plots)

    total = 0
    for p in plots:
        total += p.area * p.perimeter

    print("Part 1:",total)

    total = 0
    for p in plots:
        total += p.area * p.sides
        print(p.veggie,p.sides)

    print('Part 2:',total)

