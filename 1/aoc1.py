#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True


if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    one = []
    two = []
    one_lookup = {}
    two_lookup = {}
    for line in lines:
        [a, b] = line.split("   ")
        aaa = int(a)
        one.append(aaa)
        bee = int(b)
        two.append(bee)
        if aaa in one_lookup:
            one_lookup[aaa] += 1
        else:
            one_lookup[aaa] = 1
        if bee in two_lookup:
            two_lookup[bee] += 1
        else:
            two_lookup[bee] = 1
    
    one.sort()
    two.sort()
    total = 0
    for i in range(len(one)):
        total += abs(two[i] - one[i])

    print(total)

    similarity = 0
    for num in one_lookup:
        if(num in two_lookup):
            similarity += num * one_lookup[num] * two_lookup[num]
    
    print(similarity)



