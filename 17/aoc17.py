#!/usr/bin/env python3

import re

testcase = False
if testcase:
    file = "test2.txt"
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

    for line in lines:
        m = re.search(r'A: (\d+)',line)
        if(m):
            A = int(m.group(1))
        m = re.search(r'B: (\d+)',line)
        if(m):
            B = int(m.group(1))
        m = re.search(r'C: (\d+)',line)
        if(m):
            C = int(m.group(1))
        m = re.search(r'Program: ([\d\,]+)',line)
        if(m):
            P = m.group(1)
            prog = P.split(',')
            prog = [ int(x) for x in prog ]
    

    print(A,B,C,prog)

    # Part 2
    Borig = B
    Corig = C
    i = 12797356586  # skip the slow start
    print(len(prog))
    while(1):
        i += 32768 * 2 * 2 * 2 * 2 * 2
        A = i
        B = Borig
        C = Corig
        ins = 0
        output = []
        while(1):
            op = prog[ins]
            operand = prog[ins+1]

            # handle combo operands
            if(operand >= 1 and operand <= 3):
                combo = operand
            elif(operand == 4):
                combo = A
            elif(operand == 5):
                combo = B
            elif(operand == 6):
                combo = C
            elif(operand == 7):
                print("Invalid Program")
                exit(0)
            
            if op == 0:
                A = int(A / (2 ** combo))
            elif op == 1:
                B = B ^ operand
            elif op == 2:
                B = combo % 8
            elif op == 3:
                if(A != 0):
                    ins = operand
                    continue # do not increase 'ins' by 2
            elif op == 4:
                B = B ^ C
            elif op == 5:
                out = combo % 8
                # quit early if we deviate
                if(out != prog[len(output)]):
                    break
                output.append(out)
                # breaking at lower values of matching length we start to see a pattern
                if(len(output) == 16):
                    print(i)
                    break
            elif op == 6:
                B = int(A / (2 ** combo))
            elif op == 7:
                C = int(A / (2 ** combo))

            ins += 2
            if(ins >= len(prog)):
                break
        if(output == prog):
            break

    print("A:",i)
#    print(','.join(output))


    # Part 1

    exit(1)
    print(A,B,C,prog)
    ins = 0

    output = []
    while(1):
        op = prog[ins]
        operand = prog[ins+1]

        # handle combo operands
        if(operand >= 1 and operand <= 3):
            combo = operand
        elif(operand == 4):
            combo = A
        elif(operand == 5):
            combo = B
        elif(operand == 6):
            combo = C
        elif(operand == 7):
            print("Invalid Program")
            exit(0)
        
        if op == 0:
            A = int(A / (2 ** combo))
        elif op == 1:
            B = B ^ operand
        elif op == 2:
            B = combo % 8
        elif op == 3:
            if(A != 0):
                ins = operand
                continue # do not increase 'ins' by 2
        elif op == 4:
            B = B ^ C
        elif op == 5:
            output.append(str(combo % 8))
        elif op == 6:
            B = int(A / (2 ** combo))
        elif op == 7:
            C = int(A / (2 ** combo))

        ins += 2
        if(ins >= len(prog)):
            break

    print(','.join(output))