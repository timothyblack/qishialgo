"""
https://leetcode.com/problems/generate-parentheses/
22. Generate Parentheses
Medium

2857

177

Favorite

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Notes DFS  backtracking 
Time   O(n * 2^n)
Space O(n)
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        if n == 0:
            return results 
        
        self.findParenthesis(n, 0, 0, "", results) 
        return results
    
    # add left prenthesis when left count < n
    # add right parenthesis only when right count < left count
    def findParenthesis(self, n, left, right, combination, results):
        if left == n and right == n: 
            results.append(combination)
			return 
        if left < n:
            self.findParenthesis(n, left + 1, right, combination + "(", results) 
            
        if right < left:
            self.findParenthesis(n, left, right + 1, combination + ")", results) 
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        if n <= 0:
            return results 
        
        self.findParenthesis(n, n, "", results) 
        return results
    
    def findParenthesis(self, left, right, combination, results):
        #  combination　is string
        if left > right: 
            return 
        
        if left == 0 and right == 0: 
            print(combination)
            results.append(combination)
        
        # descrease left/right 
        if left > 0:
            self.findParenthesis(left - 1, right, combination + "(", results) 
            
        if right > 0:
            self.findParenthesis(left, right - 1, combination + ")", results)  
           