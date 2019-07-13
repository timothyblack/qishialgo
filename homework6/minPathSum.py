class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0: 
            return 0  
        
        M = len(grid)
        N = len(grid[0])
        dp = [[0] * N for i in range(M)]
        dp[0][0] = grid[0][0]    # starting point  
        
        # first col 
        for i in range(1, M):
            dp[i][0] = dp[i -1][0] + grid[i][0]
        # first row 
        for j in range(1, N):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
            
        for i in range(1, M):
            for j in range(1, N): 
                    dp[i][j] = min(dp[i -1][j], dp[i][j - 1]) + grid[i][j] 
            
        return dp[M - 1][N - 1]