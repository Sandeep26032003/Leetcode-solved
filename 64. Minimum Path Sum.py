class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0]*(len(grid[0])) for i in range(len(grid))]
        rsm=0
        csm=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0:
                    dp[i][j]=rsm+grid[i][j]
                    rsm=dp[i][j]
                if j==0 :
                    dp[i][j]=csm+grid[i][j]
                    csm=dp[i][j]
                if i!=0 and j!=0:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
