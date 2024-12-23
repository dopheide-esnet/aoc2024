#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class Pattern:
    def __init__(self,pattern):
        self.pattern = pattern
        self.towels = []
        self.possible = False
        self.ways = {0: 1}
    def Possible(self,towels,i):
        p = self.pattern

        if(self.possible == True):
            return
#        print("i",i)
        for t in towels:
            lt = len(t)
            new_i = i + lt
#            print("towel",t, "sub-pattern:",p[i:new_i])
            
            if(new_i <= len(p) and p[i:new_i] == t):
#                print("match: sub-pattern",p[i:new_i],"towel",t)
                if(new_i == len(p)):
                    self.possible = True
#                    print("done")
                    break
#                    print("match new_i",new_i, "sub-pattern",p[i:new_i],"towel",t)
#                    print("done")
                    return
#                print("next",new_i)
                self.Possible(towels,new_i)
    def NextPossible(self,towels,i):
        p = self.pattern

        counts = {}
        for t in towels:
            lt = len(t)
            new_i = i + lt
            if(new_i <= len(p) and p[i:new_i] == t):
#                if(new_i == len(p)):
#                    print("at the end, but don't break")
                if(new_i in counts):
                    counts[new_i] += 1
                else:
                    counts[new_i] = 1
        for c in counts:
            if(c in self.ways):
                self.ways[c] += counts[c] * self.ways[i]
            else:
                self.ways[c] = counts[c] * self.ways[i]
#        print(self.ways)

                

if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    towels = lines[0].split(', ')
    for t in range(len(towels)):
        towels[t] = list(towels[t])
    patterns = []
    for line in lines[2:]:
        patterns.append(Pattern(list(line)))

    total = 0
    for p in patterns:
        p.Possible(towels,0)
        if(p.possible):
            total += 1

    print("Part1:",total)

    ## Part 2, to start, ignore the ones with no possible solution
    total = 0
    for p in patterns:
#        print(p.pattern)
        if(not p.possible):
            continue
        for i in range(len(p.pattern)):
            if(i in p.ways):
                p.NextPossible(towels,i)

#        print("Result:",p.ways[len(p.pattern)])
        total += p.ways[len(p.pattern)]

    print("Part2:",total)

        # for each index, count up the number of way to get there and multiply it forward.


        

    # rrbgbr
#    0 1 2
#    r r b
#       rb  

#    paths to 2 (2)

#    2  3  4
#    b  g  b
#         gb
#       g  br
    
#    from 2, there are 2 paths to 4    2*2 = 4
#                      1 path  to 5    2*1 = 2   == 6






