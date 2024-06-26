'''
There is a city composed of n x n blocks, where each block contains 
a single building shaped like a vertical square prism. 
You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents 
the height of the building located in the block at row r and column c.

A city's skyline is the outer contour formed by all the building when viewing 
the side of the city from a distance. The skyline from each cardinal direction 
north, east, south, and west may be different.

We are allowed to increase the height of any number of buildings 
by any amount (the amount can be different per building). 
The height of a 0-height building can also be increased. 
However, increasing the height of a building should not affect 
the city's skyline from any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased 
by without changing the city's skyline from any cardinal direction.
'''

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
#Output =  35

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sm=0
        lst=[max(i) for i in zip(*grid)]
        lst1=[max(i) for i in grid]
        for i in range(len(grid)):
            for j in range(len(grid)):
                sm+=min(lst[j],lst1[i])-grid[i][j]
        return sm




grid = [[3,0,8,4],
 [2,4,5,7],
 [9,2,6,3],
 [0,3,1,0]]

h_max = [max(i) for i in grid]
#[8, 7, 9, 3]
v_max = [max(i) for i in zip(*grid)]
#[9, 4, 8, 7]
v_max
res = 0
for i, v in enumerate(h_max):
    for j, h in enumerate(v_max):
        if v>h:
            res += h - grid[i][j] 
        else:
            res+=v-grid[i][j]
res
