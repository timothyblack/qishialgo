"""
542. 01 Matrix
Medium 
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""
# BFS 
# 
from collections import deque
class Solution:
    dirs = [(0, 1),(0, -1),(-1, 0), (1, 0)]
    INT_MAX = 2**31 
    def updateMatrix(self, matrix):
        M, N = len(matrix), len(matrix[0])
        if M <= 0 or N <= 0:
            return matrix
        
        que = deque() 
        for i in range(M):
            
            for j in range(N):
                if matrix[i][j] == 0:
                    que.append((i, j))
                else:
                    matrix[i][j] = self.INT_MAX
        
        while que:
            x, y = que.popleft() 
            for dx, dy in self.dirs:
                nx,  ny = x + dx, y + dy 
                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                if  matrix[nx][ny] <= matrix[x][y] + 1: 
                    continue
                
                que.append((nx, ny)) 
                matrix[nx][ny]  = matrix[x][y] + 1 
        return matrix 

"""
https://www.lintcode.com/problem/01-matrix/description  

BFS + distance for extra storage

"""

class Solution:
    """
    @param matrix: a 0-1 matrix
    @return: return a matrix
    """
    def updateMatrix(self, matrix):
        if not matrix: 
            return matrix 
        M = len(matrix)
        if M <= 0:
            return matrix 
        N = len(matrix[0])
        if N <= 0:
            return matrix 
        from collections import deque 
        INT_MAX = 2**31 
        q = deque()
        distance = [[0] * N for _ in range(M)] 
        dirs = [(0, 1),(0, -1),(-1, 0),(1, 0) ]
        #print(distance) 
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    distance[i][j] = INT_MAX 
        while q:
            x, y = q.popleft() 
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
                if distance[nx][ny] <= distance[x][y] + 1: continue
                distance[nx][ny] = distance[x][y] + 1 
                q.append((nx, ny)) 
        return distance
            


if __name__ == "__main__":
   
    A = [[0,0,0],
 [0,1,0],
 [1,1,1]]
    print(Solution().updateMatrix(A))
    A = [[0,0,0],
 [0,1,0],
 [0,0,0]]
    print(Solution().updateMatrix(A))