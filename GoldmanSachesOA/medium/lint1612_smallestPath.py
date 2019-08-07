"""
https://www.lintcode.com/problem/smallest-path/description
1612. Smallest Path
Description 
Given a two-dimensional matrix, find the smallest path from top to bottom, .Only can move to the bottom left, down, bottom right

1.All elements are positive integer

Have you met this question in a real interview?  
Example
Example 1:

Input:
1 2 3
4 5 6
7 8 9
Output:
12

Explanation:
The smallest path:1->4->7, return 12.
Example 2:

Input:
7 1 12 1
2 3 4 2
1 10 2 6
Output:
4

Explanation:
The smallest path:1->2->1, return 4.
https://www.jiuzhang.com/solution/smallest-path/#tag-other-lang-python 
"""

class Solution:
    """
    @param matrix: 
    @return: Return the smallest path
    """
    def smallestPath(self, matrix):
        if not matrix or len(matrix) == 0:
            return 0 
         # only 1 row
        if len(matrix) == 1: return min(matrix[0])
        m = len(matrix)
        n = len(matrix[0])
        # can only bottom left, down, bottom right 
        distance = [[0 for j in range(n)] for i in range(m)]  
        #  distance[i][j] = min(matrix)
        # first row, set to themselves  
        distance[0][:] = matrix[0][:]
        for i in range(1, m):
            for j in range(n):
                print(max(0, j-1), j+2)  
                #  max(0,j-1):j+2]  deals with out of bounds in python
                distance[i][j] = min(distance[i-1][max(0, j-1):j+2]) + matrix[i][j] 
        return min(distance[-1]) 
        