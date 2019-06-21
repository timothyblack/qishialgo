"""

200. Number of Islands
Medium

2663

97

Favorite

Share
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011


Note input is array  in leetcode,  did list in python
TIme O(M*N) 
Space O(M*N)  
"""

from collections import deque
class Solution:
    dirs = [(0, 1),(0, -1),(-1, 0), (1, 0)]
    
    def  numIslands(self, grid):
        #  []  fail test case if  M, N = len(grid), len(grid[0])
        M = len(grid) 
        if M <= 0:
            return 0
        N = len(grid[0])
        if N <= 0:
            return 0
        
        visited = set()
        islands = 0 
       
        for i in range(M):            
            for j in range(N):  
                #  '1' is required for LC  
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands
               
    def bfs(self, grid, x, y, visited):    
        que = deque([(x, y)]) 
        visited.add((x, y))
        while que:
            x, y = que.popleft() 
            for dx, dy in self.dirs:
                nx,  ny = x + dx, y + dy 
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    continue
                    
                if (nx, ny) in visited or grid[nx][ny] == '0': 
                    continue
                
                que.append((nx, ny)) 
                visited.add((nx, ny)) 
     
#DFS
        
from collections import deque
class Solution:
    dirs = [(0, 1),(0, -1),(-1, 0), (1, 0)]
    
    def  numIslands(self, grid):
        #  []  fail test case if  M, N = len(grid), len(grid[0])
        M = len(grid) 
        if M <= 0:
            return 0
        N = len(grid[0])
        if N <= 0:
            return 0
        
        visited = set()
        islands = 0 
       
        for i in range(M):            
            for j in range(N):  
                #  '1' is required for LC  
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.dfs(grid, i, j, visited)
                    islands += 1
        return islands
               
    def dfs(self, grid, x, y, visited):    
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 
        if (x, y) in visited or grid[x][y] == '0': 
            return 
        visited.add((x, y)) 
        #print((x, y))
        for dx, dy in self.dirs:
            nx,  ny = x + dx, y + dy                   
               
            self.dfs(grid, nx, ny, visited) 
                

if __name__ == "__main__":
   
    A =[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    print(Solution().numIslands(A))
    A = [
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
   # print(Solution().numIslands(A))
    A = [ ]

    #print(Solution().numIslands(A))
  