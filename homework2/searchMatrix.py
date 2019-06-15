"""
https://leetcode.com/problems/search-a-2d-matrix/
74. Search a 2D Matrix
Medium

839

99

Favorite

Share
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

Note
treat matrix as sorted array.
O(logn)
O(n)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])  # # of columns
        if n == 0:
            return False

        left, right = 0, m * n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            #  mid 5   m = 1, n = 1
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                left = mid
            else:
                right = mid - 1

        if matrix[left // n][left % n] == target:
            return True
        if matrix[right // n][right % n] == target:
            return True
        return False
