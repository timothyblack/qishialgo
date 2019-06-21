"""

77. Combinations
Medium

784

47

Favorite

Share
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        if n < k:
            return results 
        # note it should start with 1  
        self.dfs(n, k, 1, [], results)  
        return results
    
    
    def dfs(self, n, k, start, combination, results):
        if len(combination) == k:
            results.append(combination[:])
            return 
        # n is included  
        for i in range(start, n + 1):
            combination.append(i)
            self.dfs(n, k, i + 1, combination, results)  
            combination.pop()  
            