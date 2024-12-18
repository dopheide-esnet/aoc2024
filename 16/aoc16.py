#!/usr/bin/env python3

import copy
import sys
sys.setrecursionlimit(10000)

testcase = True
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

class Path:
    def __init__(self,y,x,facing):
        # trailhead y,x
        self.heady = y
        self.headx = x
        self.y = y  # current position on path
        self.x = x
        self.ends = {}  # (y,x,facing) = score
        self.facing = facing
#        self.coords = {(y,x): facing}  # y,x = facing
        self.score = 0
        self.cheapest_score = 0
    def FindPath(self,paths,map,endy,endx,d):
        f = self.facing
        y = self.y  # from the current end...
        x = self.x

#        if(d == 9):
#            return

        next = {}
        if(f != "<" and map[y][x+1] == '.'):
            n_score = 0
            if(f == '^' or f == 'v'):
                n_score += 1001
            else:
                n_score += 1
            n_f = '>'            
            next[(y,x+1)] = (n_f,n_score)

        if(f != ">" and map[y][x-1] == '.'):
            n_score = 0
            if(f == '^' or f == 'v'):
                n_score += 1001
            else:
                n_score += 1
            n_f = '<'            
            next[(y,x-1)] = (n_f,n_score)

        if(f != "^" and map[y+1][x] == '.'):
            n_score = 0
            if(f == '<' or f == '>'):
                n_score += 1001
            else:
                n_score += 1
            n_f = 'v'            
            next[(y+1,x)] = (n_f,n_score)

        if(f != "v" and map[y-1][x] == '.'):
            n_score = 0
            if(f == '<' or f == '>'):
                n_score += 1001
            else:
                n_score += 1
            n_f = '^'            
            next[(y-1,x)] = (n_f,n_score)

        if len(next) == 0:
            # populate self.ends
            self.ends[(y,x,f)] = self.score
            return

        # only one way forward means we just stay on this path
        if len(next) == 1:
            for n in next:
                (ny,nx) = n
                (n_f,n_score) = next[n]
                self.score += n_score
                self.facing = n_f
                self.y = ny
                self.x = nx

            if(self.y == endy and self.x == endx):
                self.ends[(ny,nx,n_f)] = self.score
                self.cheapest = 0
                return
            else:
                self.FindPath(paths,map,endy,endx,d+1)
     
        # multiple ways forward means we fork off new paths
        # if those paths don't already exist
        else:
            for n in next:
                (ny,nx) = n
                (n_f,n_score) = next[n]

                # set self.ends
                if(n_f == f):
                    self.ends[(y,x,n_f)] = self.score
                else:
                    self.ends[(y,x,n_f)] = self.score + 1000

                if( (ny,nx,n_f) not in paths):
                    new_path = Path(ny,nx,n_f)
                    new_path.score = 0
                    paths[(ny,nx,n_f)] = new_path
                    new_path.FindPath(paths,map,endy,endx,d+1)


def Go(paths,cheapest_paths,p,endy,endx,score,d,cur_cp,cp):

# cheapest_paths needs to store not just the cur_score
# but the full path to get there.
# 
#


    for next in paths[p].ends:
        cur_score = score
        (ey,ex,f) = next
        e_score = paths[p].ends[next]

        cur_cp = copy.deepcopy(cur_cp)
        cur_cp.append((ey,ex,f))

        if(f == '>'):
            next = (ey,ex+1,f)
        elif(f == '<'):
            next = (ey,ex-1,f)
        elif(f == 'v'):
            next = (ey+1,ex,f)
        else:
            next = (ey-1,ex,f)

        cur_score += 1
        cur_score += e_score

        if ey == endy and ex == endx:
            blaa = (ey,ex,f)
#            print("end",f,")",cur_score,blaa)
            if(blaa in cheapest_paths):
                if(cur_score - 1 == cheapest_paths[blaa]):
                    if(cur_score - 1 == 7036):
                        cp.append(cur_cp)                    
                if(cur_score - 1 < cheapest_paths[blaa]):
                    cheapest_paths[blaa] = cur_score - 1
                    if(cur_score - 1 == 7036):
                        cp.append(cur_cp)
            else:
                cheapest_paths[blaa] = cur_score - 1
                if(cur_score - 1 == 7036):
                    cp.append(cur_cp)
            return e_score # ?
        else:
            if(next not in paths):
                # deadend
                return -1
            else:
                if(next in cheapest_paths):
                    if(cur_score == cheapest_paths[next]):
                        if(cur_score == 7036):
                            cp.append(cur_cp)                        
                    if(cur_score < cheapest_paths[next]):
                        cheapest_paths[next] = cur_score
                        if(cur_score == 7036):
                            cp.append(cur_cp)
                    else:
                        continue # if this isn't cheaper skip it.
                else:
                    cheapest_paths[next] = cur_score
                    if(cur_score == 7036):
                        cp.append(cur_cp)                    
            
                Go(paths,cheapest_paths,next,endy,endx,cur_score,d+1,cur_cp,cp)

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
    y=0
    for line in lines:
        row = list(line)
        if('S' in row):
            starty=y
            startx=row.index('S')
            row[startx] = '.'  # get rid of the confusing 'S'
        if('E' in row):
            endy = y
            endx = row.index('E')
            row[endx] = '.'  # get rid of the confusing 'E
        map.append(row)
        y+=1
    
    facing = ">"
    my_path = Path(starty,startx,facing)
    paths = {}
    paths[(starty,startx,'>')] = my_path

    my_path.FindPath(paths,map,endy,endx,0)

    # We now have all of our 'paths'

#    for p in paths:
#        (x,y,f) = p
#        print(x,y,f)
#        print("  ",paths[p].score)
#        for end in paths[p].ends:
#            print("  ",end,paths[p].ends[end])

    cheapest = -1
    cheapest_paths = {}
    cp = [ [(starty,startx,'^')] ]
    for p in [(starty,startx,'>'), (starty,startx,'<'), (starty,startx,'v'), (starty,startx,'^')]:
        if p in paths:

            for end in paths[p].ends:
                Go(paths,cheapest_paths,p,endy,endx,0,0,[],cp)

    for p in [(endy,endx,'>'), (endy,endx,'<'), (endy,endx,'v'), (endy,endx,'^')]:
        if p in cheapest_paths:
            print("Part 1:",cheapest_paths[p])

    print(len(cp))
    print(cp)


#    print(len(cheapest_paths))
#    for p in cheapest_paths:
#        print(p,cheapest_paths[p])

#    for p in paths:
#        (x,y,f) = p
#        print(x,y,f)
#        for end in paths[p].ends:
#            print("  ",end,paths[p].ends[end])

#    for y in range(len(map)):
#        print(''.join(map[y]))






