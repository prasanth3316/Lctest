# Check if There is a Valid Path in a Grid
# Difficulty : Medium
# Tags       : Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
# Language   : python3
# Runtime    : 115 ms
# Memory     : 40.4 MB
# Link       : https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def dfs(self,grid,i,j):
        z=grid[i][j]
        grid[i][j]=-1
        
        
         
        if z==1:
            q=i
            w=j+1
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [1,3,5]:
                self.dfs(grid,q,w)
            q=i
            w=j-1
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [1,4,6]:
                self.dfs(grid,q,w)
        if z==2:
            
            q=i-1
            w=j
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [2,3,4]:
                self.dfs(grid,q,w)
            q=i+1
            w=j
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [2,5,6]:
                self.dfs(grid,q,w)
        if z==3:
            
            q=i
            w=j-1
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [1,4,6]:
                self.dfs(grid,q,w)
            q=i+1
            w=j
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [2,5,6]:
                self.dfs(grid,q,w)
        if z==4:
            
            q=i
            w=j+1
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [1,3,5]:
                self.dfs(grid,q,w)
            q=i+1
            w=j
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [2,5,6]:
                self.dfs(grid,q,w)
        if z==5:
            
            q=i-1
            w=j
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [2,3,4]:
                self.dfs(grid,q,w)
            q=i
            w=j-1
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [1,4,6]:
                self.dfs(grid,q,w)
        if z==6:
            
            q=i-1
            w=j
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [2,4,3]:
                self.dfs(grid,q,w)
            q=i
            w=j+1
            if q>=0 and w>=0 and q<len(grid) and w<len(grid[0]) and grid[q][w] in [1,5,3]:
                self.dfs(grid,q,w)


            
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.dfs(grid,0,0)
        if grid[-1][-1]==-1:
            return True
        return False

        