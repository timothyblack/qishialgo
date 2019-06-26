"""
https://leetcode.com/problems/word-search/
79. Word Search
Medium

1804

88

Favorite

Share
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Note  
backtracking question to track if there is an answer  
Time each char has 4 choices. s is length of the string. 
1 call of cell would take O(4^s) time. in the worst case all cells take O(m*n*4^s) 
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        if M == 0:
            return False
        N = len(board[0])
        if N == 0:
            return False
        # empty string is 
        if not str: 
            return True 
         
        visited = [[False] * N for _ in range(M)]
         
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, 0, i, j, visited):
                        return True 
        return False 
    
    def dfs(self, board, word, index, x, y, visited):  
        if index == len(word):
            return True  
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        if visited[x][y] or board[x][y] != word[index]:
            return False      
         
        visited[x][y] = True
        res = self.dfs(board, word, index + 1, x, y + 1, visited) or 
			self.dfs(board, word, index + 1, x, y - 1, visited) or 
			self.dfs(board, word, index + 1, x + 1, y, visited) or 
			self.dfs(board, word, index + 1, x - 1, y, visited)   
        visited[x][y] = False      
        return res