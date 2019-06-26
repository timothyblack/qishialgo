"""
https://leetcode.com/problems/combination-sum-ii/
40. Combination Sum II
Medium 

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]


Notes  
1. sort and dedup and i + 1  Each number in candidates may only be used once in the combination

Time O(N * 2^N)
Space O(2^N)
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        if not candidates:
            return results
        candidates.sort()   
        self.dfs(candidates,  target, 0, [], results)
        return results
    
    def dfs(self, candidates,  target, index, combination, results):
        if target == 0:
            results.append(list(combination))
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]: continue 
            if target < candidates[i]: return 
            
            self.dfs(candidates,  target - candidates[i], i + 1, combination + [candidates[i]], results)