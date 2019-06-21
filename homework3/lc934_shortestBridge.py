"""
934. Shortest Bridge
Medium

286

21

Favorite

Share
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1

Notes 
DFS to find first island,  
BFS to find first point in second island,  which is the shortest path  
Time O(M*N)
Space O(M*N)
"""
import collections
class Solution:
   
    dirs = [(0, 1),(0, -1),(-1, 0), (1, 0)]
    def shortestBridge(self, A):
        M, N = len(A), len(A[0])
       
        visited = [[0] * N for _ in range(M)] 
        
        que = collections.deque() 
        found = False
        for i in range(M):
            if found: break 
            for j in range(N):
                if A[i][j] == 1:
                    self.dfs(A, i, j, visited, que) 
                    found = True 
                    break 
        
        step = 0
        while que:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                for dx, dy in self.dirs:
                    ni, nj = i + dx, j + dy 
                    if ni >= 0 and ni < M and nj >= 0 and nj < N:
                        visited[ni][nj] = 1
                        if A[ni][nj] == 1:
                            return step 
                        elif A[ni][nj] == 0:
                            A[ni][nj] = 2
                            que.append((ni, nj))
                        else:
                            continue
            step += 1
        return step 
    
    def dfs(self, A, x, y, visited, que):
        if x < 0 or x >= len(A) or y < 0 or y >= len(A[0]):
            return 
        #print(x, y)
        visited[x][y] = 1
               
        if A[x][y] == 1:
            que.append((x, y)) 
            A[x][y] = 2 
            for dx, dy in self.dirs:
                nx, ny = x + dx, y + dy 
              #  print(nx, ny)
                self.dfs(A, nx, ny, visited, que)  


if __name__ == "__main__":
    A = [[0,1],[1,0]]
   # print(Solution().shortestBridge(A))
    A = [[0,1,0],[0,0,0],[0,0,1]]
    print(Solution().shortestBridge(A))
    A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    print(Solution().shortestBridge(A))