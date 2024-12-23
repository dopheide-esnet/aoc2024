#!/usr/bin/env python3

import copy
import sys
sys.setrecursionlimit(10000)

testcase = False
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
        self.fullpath = []
    def FindPath(self,paths,map,endy,endx,d):
        f = self.facing
        y = self.y  # from the current end...
        x = self.x

        # Limit to a reasonable search depth
#        if(d == 7000):
#            return
        self.fullpath.append((y,x))

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
                    self.ends[(ny,nx,n_f)] = self.score + n_score # ?
                else:
                    self.ends[(ny,nx,n_f)] = self.score + n_score # ?  no difference n_score was already calculated

                if( (ny,nx,n_f) not in paths):
                    new_path = Path(ny,nx,n_f)
                    new_path.score = 0
                    paths[(ny,nx,n_f)] = new_path
                    new_path.FindPath(paths,map,endy,endx,d+1)


def Go(paths,cheapest_paths,p,endy,endx,score,d,cur_cp):
 
    d += 1
#    if(d > 3):
#        exit(1)

    # For Part 2, record the cheapest path we took to get to this spot.
    if paths[p].cheapest_score == 0 or score < paths[p].cheapest_score:
        paths[p].cheapest_score = score

    for next in paths[p].ends:

        cur_score = score
        (ey,ex,f) = next
        e_score = paths[p].ends[next]

        cur_cp = copy.deepcopy(cur_cp)
        cur_cp.append((ey,ex,f))

        cur_score += e_score

#        print("Next:",next, cur_score)

        if ey == endy and ex == endx:
#            print("Found the end",cur_score)
#            print(cur_cp)
            blaa = (ey,ex,f)

#            print("end",f,")",cur_score,blaa)
            if(blaa in cheapest_paths):      
                if(cur_score < cheapest_paths[blaa]):
                    cheapest_paths[blaa] = cur_score
            else:
                cheapest_paths[blaa] = cur_score

        else:
            if(next not in paths):
                continue
            else:
                if(next in cheapest_paths):                      
                    if(cur_score < cheapest_paths[next]):
                        cheapest_paths[next] = cur_score
                    else:
                        continue # if this isn't cheaper skip it.
                else:
                    cheapest_paths[next] = cur_score                
            
                Go(paths,cheapest_paths,next,endy,endx,cur_score,d+1,cur_cp)

def WalkPaths(paths,p,endy,endx,cur_path,score,ARGH,cp,d,too_big):

    if(len(cur_path) > too_big):
        # We assume the shortest path isn't going to be more than half the map
        return

    for next in paths[p].ends:
        (ey,ex,ef) = next
        e_score = paths[p].ends[next]
        cur_score = score + e_score

        new_path = copy.deepcopy(cur_path)
        if(len(cur_path) == 1):
            startp = cur_path[0]
            new_path.extend(paths[startp].fullpath)
            new_path=new_path[1:]  # get rid of the first one that has a facing.
        new_path.extend(paths[p].fullpath)

        if ey == endy and ex == endx:
            if(cur_score == ARGH):
                cp.append(new_path)


        if(next in paths):
            if(cur_score > paths[next].cheapest_score):
            # ignore this one.
                continue
            else:
                WalkPaths(paths,next,endy,endx,copy.deepcopy(new_path),cur_score,ARGH,cp,d,too_big)


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

    too_big = (len(map) * len(map[0])) / 2

    facing = ">"
    my_path = Path(starty,startx,facing)
    paths = {}
    paths[(starty,startx,'>')] = my_path

    my_path.FindPath(paths,map,endy,endx,0)

    # We now have all of our 'paths'

    print("We have all the paths?")

    cheapest_paths = {}
#    for p in [(starty,startx,'>'), (starty,startx,'<'), (starty,startx,'v'), (starty,startx,'^')]:
    for p in [(starty,startx,'>')]:
        if p in paths:
            for end in paths[p].ends:
                Go(paths,cheapest_paths,end,endy,endx,paths[p].ends[end],0,[])

#    print("here")
#    for cp in cheapest_paths:
#        print(cp,"\n",cheapest_paths[cp])

#    print(cheapest_paths)

    blaa = []
    for p in [(endy,endx,'>'), (endy,endx,'<'), (endy,endx,'v'), (endy,endx,'^')]:
        if p in cheapest_paths:
            blaa.append(cheapest_paths[p])

    ARGH = blaa[0]
    print("Part1:",blaa[0])


# (1, 139, '>')
# 102460

## PRINT PATHS
#    for p in paths:
#        (x,y,f) = p
#        print(x,y,f)
#        print("  ",paths[p].fullpath)
#        print("  ",paths[p].cheapest_score)
#        for end in paths[p].ends:
#            print("  ",end,paths[p].ends[end])

    # Finally, figure out the positions that can get you to the end the cheapest way.

    cp = []
    for p in [(starty,startx,'>')]:
        if p in paths:

            for end in paths[p].ends:
                WalkPaths(paths,end,endy,endx,[p],paths[p].ends[end],ARGH,cp,0,too_big)

    all = [(endy,endx)]
#    all = []
    for c in range(len(cp)):
#        print(cp[c],"\n")
        all.extend(cp[c])

    print( len(list(set(all))))


