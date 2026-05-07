# Maximum Path Score in a Grid
# Difficulty : Medium
# Tags       : Array, Dynamic Programming, Matrix
# Language   : python3
# Runtime    : 9961 ms
# Memory     : 37.6 MB
# Link       : https://leetcode.com/problems/maximum-path-score-in-a-grid/

class Solution:
    def recur(self,i,j,grid,cost,dp,k):
        if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1:
            return -1
        s,c=0,0
        if grid[i][j]==1:
            s,c=1,1
        if grid[i][j]==2:
            s,c=2,1
        nc=c+cost
        if nc>k:
            return -1
        if i==len(grid)-1 and j==len(grid[0])-1:
            return s
        if dp[i][j][nc]!=-2:
            return dp[i][j][nc]
        maxi=-1
        sd=self.recur(i+1,j,grid,nc,dp,k)
        if sd!=-1:
            maxi=max(maxi,sd)
        sr=self.recur(i,j+1,grid,nc,dp,k)
        if sr!=-1:
            maxi=max(maxi,sr)
        if maxi==-1:
            result=-1
        else:
            result=s+maxi
        dp[i][j][nc]=result
        return result
    
        
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        dp=[[[-2]*(k+1)  for j in range(len(grid[0]))]for i in range(len(grid))]
        return self.recur(0,0,grid,0,dp,k)
        
        