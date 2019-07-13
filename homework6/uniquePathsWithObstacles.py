class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0 
        if obstacleGrid[0][0] == 1:  #  start is obstable  [[1,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
            return 0 
        
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        paths = [[0] * N for i in range(M)] 
        paths[0][0] = 1    #  special case
        for i in range(1, M):   #  starting from 1
            paths[i][0] = 0 if obstacleGrid[i][0] else paths[i - 1][0]
        
        for j in range(1, N):
            paths[0][j] = 0 if obstacleGrid[0][j] else paths[0][j - 1]
            
        for i in range(1, M): 
            for j in range(1, N):  
                paths[i][j] = 0 if obstacleGrid[i][j] else paths[i - 1][j] + paths[i][j - 1] 
        return paths[M - 1][N - 1]
        
