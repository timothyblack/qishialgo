"""
433. Number of Islands
中文English
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Example 1:

Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
Example 2:

Input:
[
  [1,1]
]
Output:
1

"""
# Time O(N * M)  
# Space O(2N * M)  visited can be saved if mark grid directly 
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0 
        
        M = len(grid)
        N = len(grid[0])
        
        visited = [[0 for i in range(N)] for j in range(M) ]
        #print(visited)
        islands = 0 
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and visited[i][j] == 0:
                   
                    self.bfs(grid, i, j, visited)
                    islands += 1 
        return islands
    
    def bfs(self, grid, x, y, visited):
        queue = collections.deque([(x, y)])
        visited[x][y] = 1 
        dirs = [(0, 1), (0, -1),(-1, 0),(1, 0)]
        while queue: 
            x, y = queue.popleft() 
            #print(x, y)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy 
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == 0 or visited[nx][ny] == 1:
                    continue 
                queue.append((nx, ny)) 
                visited[nx][ny] = 1  
       
        