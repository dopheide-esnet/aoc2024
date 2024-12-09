#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class Thing:
    def __init__(self,file,id,index,size):
        self.file = file
        self.id = id
        self.index = index
        self.size = size

if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    input = list(lines[0])
    input = [ int(x) for x in input ]

    j = len(input) - 1
    disk = []
    d = 0
    checksum = 0
    j_blocks_rem = 0
    files = []
    spaces = []
    for i in range(len(input)):
        if(i > j):
            while(j_blocks_rem > 0):
                disk.append(j_block_id)
                checksum += j_block_id * d
                d+=1
                j_blocks_rem -= 1 
            break
        if i % 2 == 0:
            # even number, this is a file
            block_id = int(i / 2)
            blocks = input[i]
            for b in range(blocks):
                disk.append(block_id)
                checksum += block_id * d
                d += 1

        else:
            # odd number, free space
            blocks = input[i]

            for b in range(blocks):
                if(j_blocks_rem == 0):
                    j_block_id = int(j/2)
                    j_blocks_rem = input[j]
                    j -= 2
                disk.append(j_block_id)
                checksum += j_block_id * d
                d+=1
                
                j_blocks_rem -= 1                

    print("Part1 Checksum:",checksum)

    # Part 2:
    # Kind of doing the whole thing a different way
    d = 0
    for i in range(len(input)):
        if i % 2 == 0:
            # even number, this is a file
            block_id = int(i / 2)
            blocks = input[i]
            files.append(Thing(True,block_id,d,blocks))
            d += blocks
        else:
            # odd number, free space
            blocks = input[i]
            spaces.append(Thing(False,int(i/2),d,blocks))
            d += blocks

    for f in reversed(range(len(files))):
        # attempt to move each one only once
        for s in range(len(spaces)):
            if(files[f].size <= spaces[s].size):
                # calculate the new space size and index
                if(not files[f].index < spaces[s].index):
                    spaces[s].size = spaces[s].size - files[f].size
                    files[f].index = spaces[s].index
                    spaces[s].index += files[f].size
                    break

    # Print new layout
#    re_ordered = sorted(files,key=lambda x: x.index)
#    files = re_ordered
#    i = 0
#    for f in files:
#        if(i < f.index):
#            for x in range(f.index - i):
#                print('.',end='')
#            i = f.index
#        for x in range(f.size):
#            print(f.id,end='')
#            i+=1
#    print()

#    exit()
    checksum = 0
    for f in files:
        for i in range(f.size):
            checksum += (f.index+i) * f.id
    print("Part2:",checksum)