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
        print(p.pattern)
        p.Possible(towels,0)
        if(p.possible):
            total += 1

    print("Part1:",total)

    ## Part 2, to start, ignore the ones with no possible solution
    for p in patterns:
        if(not p.possible):
            continue




