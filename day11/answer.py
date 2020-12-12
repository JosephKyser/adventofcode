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
from itertools import product
import copy

with open('input','r') as file:
    files = [i.strip() for i in file.readlines() if i != "\n"]

    files  = [i.strip() for i in test.split("\n") if i != "\n"]
    print(files)
    width = len(files[0])
    height = len(files)

    def DoRoundPart1(layout):

        def GetAdjacentPart1(layout, idx, jdx):

            change = {}
            adj = 0

            for i in range(-1,2):
                for j in range(-1,2):
                    if (i,j) != (0,0):

                        if ((0 <= idx + i < height) and (0 <= jdx + j < width)):
                      #      print(idx+i,height,jdx+j,width)
                            if  ('#' == layout[idx+i][jdx+j]):

                                adj += 1

            if (0 == adj and 'L' == layout[idx][jdx]):
                return '#'
            elif (4 <= adj and '#' == layout[idx][jdx]):
                return 'L'
            else:
                return layout[idx][jdx]


        return [[GetAdjacentPart1(layout,i,j) for j in range(0,width)] for i in range(0,height)]

    def DoRoundPart2(layout):

            def GetAdjacentPart2(layout, idx, jdx):

                adj = {(i,j):-1 for i in range(-1,2) for j in range(-1,2) if (i,j) != (0,0)}
                if "." != layout[idx][jdx]:

                    for i in range(0, height - idx):

                        for j in range(0,width - jdx):
                             if (((0 == i or 0 == j) or (abs(i) == abs (j))) and ((i,j) != (0,0))):

                                if 0 == i: cas = (0,j/abs(j))
                                elif 0 == j: cas = (i/abs(i),0)
                                else: cas = (i/abs(i),j/abs(j))

                                if -1 ==  adj[cas]:

                                    if "#" == layout[idx+i][jdx+j]: adj[cas] = 1
                                    elif "." == layout[idx+i][jdx+j]: adj[cas] = 0

                    for i in range(-1 * idx, 0):

                        for j in range(-1 * jdx,0):
                             if (((0 == i or 0 == j) or (abs(i) == abs (j))) and ((i,j) != (0,0))):

                                if 0 == i: cas = (0,j/abs(j))
                                elif 0 == j: cas = (i/abs(i),0)
                                else: cas = (i/abs(i),j/abs(j))

                                if -1 ==  adj[cas]:

                                    if "#" == layout[idx+i][jdx+j]: adj[cas] = 1
                                    elif "." == layout[idx+i][jdx+j]: adj[cas] = 0

                                

                    print(f"({idx},{jdx}):{np.matrix(adj)}")
                adj = sum([i for i in adj.values()])


                if (0 == adj and 'L' == layout[idx][jdx]):
                    return '#'
                elif (5 <= adj and '#' == layout[idx][jdx]):
                    return 'L'
                else:
                    return layout[idx][jdx]


            ret = [[GetAdjacentPart2(layout,i,j) for j in range(0,width)] for i in range(0,height)]
            print(np.matrix(ret))
            return ret



    oldList = files
    newList = DoRoundPart2(oldList)

    while (oldList != newList):

        oldList = newList
        newList = DoRoundPart2(oldList)
    print(sum(i.count("#") for i in newList))
