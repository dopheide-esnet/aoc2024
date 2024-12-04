#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

# Directions:
# 0 1 2
# 3 x 4
# 5 6 7

def FindXmas(map,y,x,letter,direction):
    xmas = ['X','M','A','S']
    max = len(map)

    if(map[y][x] == xmas[letter]):
        if(letter == len(xmas) - 1):
            # we're done
            return 1
        if(direction == 0) and (y-1 >= 0) and (x-1 >= 0):
            return FindXmas(map,y-1,x-1,letter+1,0)
        elif(direction == 1 and y-1 >= 0):
            return FindXmas(map,y-1,x,letter+1,1)
        elif(direction == 2 and (y-1 >= 0) and (x+1 < max)):
            return FindXmas(map,y-1,x+1,letter+1,2)
        elif(direction == 3 and x-1 >= 0):
            return FindXmas(map,y,x-1,letter+1,3)
        elif(direction == 4 and x+1 < max):
            return FindXmas(map,y,x+1,letter+1,4)
        elif(direction == 5 and (y+1 < max) and (x-1 >= 0)):
            return FindXmas(map,y+1,x-1,letter+1,5)
        elif(direction == 6 and (y+1 < max)):
            return FindXmas(map,y+1,x,letter+1,6)
        elif(direction == 7 and (y+1 < max) and (x+1 < max)):
            return FindXmas(map,y+1,x+1,letter+1,7)
        else:
            return 0
    else:
        return 0

def FindMas(map,y,x,letter,direction):
    xmas = ['M','A','S']
    max = len(map)

    if(map[y][x] == xmas[letter]):
        if(letter == len(xmas) - 1):
            # we're done
            if(direction == 0):
                return (y+1,x+1) # where the 'A' was
            elif(direction == 2):
                return (y+1,x-1)
            elif(direction == 5):
                return (y-1,x+1)
            elif(direction == 7):
                return (y-1,x-1)
            else:
                print("Error, shouldn't get here")
                exit(1)
        
        if(direction == 0) and (y-1 >= 0) and (x-1 >= 0):
            return FindMas(map,y-1,x-1,letter+1,0)

        elif(direction == 2 and (y-1 >= 0) and (x+1 < max)):
            return FindMas(map,y-1,x+1,letter+1,2)
        elif(direction == 3 and x-1 >= 0):
            return FindMas(map,y,x-1,letter+1,3)

        elif(direction == 5 and (y+1 < max) and (x-1 >= 0)):
            return FindMas(map,y+1,x-1,letter+1,5)

        elif(direction == 7 and (y+1 < max) and (x+1 < max)):
            return FindMas(map,y+1,x+1,letter+1,7)
        else:
            return (-1,-1)
    else:
        return (-1,-1)

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
        x = list(line)
        map.append(x)

    # Part 1
    total = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            for direction in range(8):
                result = FindXmas(map,y,x,0,direction)
                total += result
#                if result == 1:
#                    print("Found:",y,x,direction)
    print(total)

    # Part 2
    total = 0
    # same idea, we'll find all the "MAS's" and track the x,y coordinate for each 'A'.
    # we only need to check the diagonal directions.
    # Then any x,y that's been seen twice should be an X-MAS
    As = {}
    for y in range(len(map)):
        for x in range(len(map[0])):
            for direction in [0,2,5,7]:
                (ay,ax) = FindMas(map,y,x,0,direction)
                if(ay != -1):
                    if (ay,ax) not in As:
                        As[ay,ax] = 1
                    else:
                        As[ay,ax] += 1

#                total += result
#                if result == 1:
#                    print("Found:",y,x,direction)

    # Do something with ay,ax
#    print(As)
    for A in As:
        if(As[A] == 2):
            total += 1
    print(total)




