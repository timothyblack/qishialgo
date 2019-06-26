"""
52. N-Queens II
Hard

283

116

Favorite

Share
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
class Solution:
    def __init__(self):
        self.total = 0 
        self.n = 0
        self.cols = {} 
        
    def totalNQueens(self, n):
        self.n = n 
        self.search(0)
        return self.total 
        
    def search(self, row):
        if row == self.n:
            self.total += 1 
            return 
    
        for col in range(self.n):
            # check if they are in same row 
            if col in self.cols:
                continue
            if not self.issafe(row, col):
                continue
            
            self.cols[col] = row
            self.search(row + 1)
            del self.cols[col] 
    
    
    # check if they are in the same diagonal
    def issafe(self, row, col):  
        for c, r in self.cols.items():
            def issafe(self, row, col):  
        for c, r in self.cols.items():
            #if c + r == row + col or c - r == col - row:    
            if abs(c - col) == abs(r - row):     #
                return False
        return True 