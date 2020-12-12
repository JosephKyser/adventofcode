test = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

import numpy as np

file = open('input','r')
files = [i.strip() for i in file.readlines() if i != "\n"]
file.close()
#files = [i.strip() for i in test.split("\n") if i != "\n"]
width = len(files[0])
height = len(files)

def DoARound(layout):

    def GetUpOrSit(layout,idx,jdx):
        char = layout[idx][jdx]
        if '.' == char: return char

        adj = {(i,j):0 for i in range(-1,2) for j in range(-1,2) if (i,j) != (0,0)}

        for i in range(-1,-1*(idx+1),-1): #UP
            up = layout[idx+i][jdx]
            if '.' != up:
                if '#' == up:
                    adj[(-1,0)] = 1
                    break
                else:
                    break

        for j in range(-1,-1*(jdx+1),-1): #LEFT
            left = layout[idx][jdx+j]
            if '.' != left:
                if '#' == left:
                    adj[(0,-1)] = 1
                    break
                else:
                    break

        for i in range(1,height-idx): #DOWN
            down = layout[idx+i][jdx]
            if '.' != down:
                if '#' == down:
                    adj[(1,0)] = 1
                    break
                else:
                    break

        for j in range(1,width-jdx): #RIGHT
            right = layout[idx][jdx+j]
            if '.' != right:
                if '#' == right:
                    adj[(0,1)] = 1
                    break
                else:
                    break

        for i,j in [(i,j) for i in range(-1,-1*idx-1,-1) for j in range(-1,-1*jdx-1,-1) if abs(i) == abs(j)]: #UPLEFT
            upleft = layout[idx+i][jdx+j]
            if '.' != upleft:
                if '#' == upleft:
                    adj[(-1,-1)] = 1
                    break
                else:
                    break

        for i,j in [(i,j) for i in range(1,height-idx) for j in range(-1,-1*jdx-1,-1) if abs(i) == abs(j)]: #DOWNLEFT
            downleft = layout[idx+i][jdx+j]
            if '.' != downleft:
                if '#' == downleft:
                    adj[(1,-1)] = 1
                    break
                else:
                    break

        for i,j in [(i,j) for i in range(-1,-1*idx-1,-1) for j in range(1,width-jdx) if abs(i) == abs(j)]: #UPRIGHT
            upright = layout[idx+i][jdx+j]
            if '.' != upright:
                if '#' == upright:
                    adj[(-1,1)] = 1
                    break
                else:
                    break

        for i,j in [(i,j) for i in range(1,height-idx) for j in range(1,width-jdx) if abs(i) == abs(j)]: #DOWNRIGHT
            downright = layout[idx+i][jdx+j]
            if '.' != downright:
                if '#' == downright:
                    adj[(1,1)] = 1
                    break
                else:
                    break

        adj = sum([i for i in adj.values()])

        if "L" == char and 0 == adj: return '#' #if target is an empty seat"
        elif '#' == char and 5 <= adj: return 'L'
        else: return char

    ret = [[GetUpOrSit(layout,i,j) for j in range(0,width)] for i in range(0,height)]
    return ret

oldList = files
newList = DoARound(oldList)

while (oldList != newList):
    oldList = newList
    newList = DoARound(oldList)

print(sum(i.count('#') for i in newList))
