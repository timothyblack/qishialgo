"""
https://www.lintcode.com/problem/number-of-islands-ii/description
434. Number of Islands II
中文English
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

Example
Example 1:

Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]
Output: [1,1,2,2]
Explanation:
0.  00000
    00000
    00000
    00000
1.  00000
    01000
    00000
    00000
2.  01000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00010
4.  01000
    01000
    00000
    00011
Example 2:

Input: n = 3, m = 3, A = [[0,0],[0,1],[2,2],[2,1]]
Output: [1,1,2,2]
Notice
0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.


# union find  

"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
   
    def union(self,  point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        if root_a != root_b:
            self.father[root_a] = root_b  
            self.size -= 1  
    
    def find(self, point):
        path = []
        while point != self.father[point]:
            path.append(point)
            point = self.father[point]
        
        for p in path:
            self.father[p] = point 
        return point 
        
    def numIslands2(self, n, m, operators):
        results = []
        island = set() 
        self.size = 0 
        self.father = {} 
        for operator in operators:
            x, y = operator.x, operator.y 
            if (x, y) in island:
                results.append(self.size) 
                continue 
            
            island.add((x, y)) 
            self.father[(x, y)] = (x, y)
            self.size += 1  
            dirs = [(0, 1), (0, -1),(-1, 0),(1, 0)]
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) in island:
                    self.union((nx, ny), (x, y))
            results.append(self.size)
        return results 
            
