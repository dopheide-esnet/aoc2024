#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

def IsSafe(levels):
    increasing = True
    if(levels[0] > levels[1]):
        increasing = False

    safe = True
    for j in range(len(levels)-1):
        if(abs(levels[j]-levels[j+1]) > 3):
            safe = False
            break
        if(increasing and levels[j] >= levels[j+1]):
            safe = False
            break
        if(not increasing and levels[j] <= levels[j+1]):
            safe = False
            break
    return safe,j


if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    reports = []
    for line in lines:
        levels = line.split(' ')
        for i in range(len(levels)):
            levels[i] = int(levels[i])
        reports.append(levels)
    #print(reports)

# Part 1
    total = 0
    skip_total = 0

    for i in range(len(reports)):
        levels = reports[i]
        (safe,j) = IsSafe(levels)
        problems = 0
        if safe:
            total += 1
            skip_total += 1

        if not safe and problems==0:
#            print(levels[:j] + levels[j+1:])
            if(j == 1):
                print(levels[1:])
                (safeone,k) = IsSafe(levels[1:])
                print(levels[:j] + levels[j+1:])
                (safetwo,k) = IsSafe(levels[:j] + levels[j+1:])
            else:
                (safeone,k) = IsSafe(levels[:j] + levels[j+1:])
                (safetwo,k) = IsSafe(levels[:j+1] + levels[j+2:])

            if(safeone or safetwo):
                skip_total += 1
            else:
                print("Unsafe at:",k)
                print(levels)

    print(total)
    print(skip_total)

