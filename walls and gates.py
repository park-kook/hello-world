
'''
Walls and Gates,
you are given an nXn grid rooms initalized with these three possible values
    -1 A wall or an obstable
    0 A gate
    inf means an emptry room as you may assume that the distance to a gate is less than the infite
    
fill each emptry room with the distance to its nearst gate. 
If it is impossoble to reach a gate. It should be filled with inf+

BFS -> o(m*n)
'''
rooms=[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1], [2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
output = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]


[2147483647,-1,      0,         2147483647  ]
[2147483647,2147483647,2147483647,-1        ] 
[2147483647,-1        ,2147483647,-1        ]
[0         ,-1        ,2147483647,2147483647]

import collections
import heapq
from collections import deque
from collections import defaultdict
from collections import deque

def wallsAndGates(rooms):
    ROWS, COLS = len(rooms), len(rooms[0])
    visit = set()
    q = deque()
    #helper function while loop below    
    def addRoom(r,c):
        if (r<0 or r==ROWS or c<0 or c ==COLS or (r,c) in visit or rooms[r][c]==-1):
            return
        visit.add((r,c))
        q.append([r,c])
    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c]==0:
                q.append([r,c])
                visit.add((r,c))
    dist = 0
    while q:
        for i in range(len(q)):
            r,c = q.popleft() #[0,2] [3,0] simultaneously needs to be count
            rooms[r][c] = dist
            addRoom(r+1,c) #[1,2] for i=0 , return for i=1
            #adding room in the dequeu again means one distance from above
            addRoom(r-1,c) # return for i=0, [2,0] for i=1
            addRoom(r,c+1) # [0,3] for i=0, return for i=1
            addRoom(r,c-1) # return for i=0, return for i=1 
        dist+=1 # once we are done in the full for loop above, incremental distance +1
wallsAndGates(rooms)
