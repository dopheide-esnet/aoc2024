#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class Array:
    def __init__(self):
        self.ants = []
        self.anodes = []
    def CalcAnodes(self,my,mx):
        for i in range(len(self.ants)):
            for j in range(i+1,len(self.ants)):
                (y1,x1) = self.ants[i]
                (y2,x2) = self.ants[j]
                y3 = y1 + 2*(y2 - y1)
                x3 = x1 + 2*(x2 - x1)
                if(y3 >= 0 and y3 < my) and (x3 >= 0 and x3 < mx):
                    if (y3,x3) not in self.anodes:
                        self.anodes.append((y3,x3))
                y4 = y1 - (y2 - y1)
                x4 = x1 - (x2 - x1)
                if(y4 >= 0 and y4 < my) and (x4 >= 0 and x4 < mx):
                    if (y4,x4) not in self.anodes:
                        self.anodes.append((y4,x4))             
    def CalcMoreAnodes(self,my,mx):
        for i in range(len(self.ants)):
            for j in range(i+1,len(self.ants)):
                (y1,x1) = self.ants[i]
                (y2,x2) = self.ants[j]
                # all are inline and are anodes themselves
                if (y1,x1) not in self.anodes:
                    self.anodes.append((y1,x1))
                if (y2,x2) not in self.anodes:
                    self.anodes.append((y2,x2))

                m = 2
                y3 = y1 + m*(y2 - y1)
                x3 = x1 + m*(x2 - x1)
                while(y3 >= 0 and y3 < my) and (x3 >= 0 and x3 < mx):
                    if (y3,x3) not in self.anodes:
                        self.anodes.append((y3,x3))
                    m += 1
                    y3 = y1 + m*(y2 - y1)
                    x3 = x1 + m*(x2 - x1)

                m = 1
                y4 = y1 - m*(y2 - y1)
                x4 = x1 - m*(x2 - x1)
                while(y4 >= 0 and y4 < my) and (x4 >= 0 and x4 < mx):
                    if (y4,x4) not in self.anodes:
                        self.anodes.append((y4,x4))  
                    m += 1
                    y4 = y1 - m*(y2 - y1)
                    x4 = x1 - m*(x2 - x1)

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
    arrays = {}
    y = 0
    for line in lines:
        row = list(line)
        x = 0
        for r in row:
            if r != '.':
                if r not in arrays:
                    arrays[r] = Array()
                arrays[r].ants.append((y,x))
            x += 1
        map.append(row)
        y += 1
    
    for r in arrays:
        # Part 1
        arrays[r].CalcAnodes(len(map),len(map[0]))  
        # Part 2
        arrays[r].CalcMoreAnodes(len(map),len(map[0]))

    all_anodes = []
    for r in arrays:
        for (y,x) in arrays[r].anodes:
            if (y,x) not in all_anodes:
                all_anodes.append((y,x))

    print(len(all_anodes))

    exit(1)
    for y in range(len(map)):
        for x in range(len(map[0])):
            for r in arrays:
                if (y,x) in arrays[r].anodes:
                    print('#',end='')
                    break
            else:
                print('.',end='')
        print()