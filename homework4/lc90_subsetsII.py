"""
90. Subsets II
Medium 
Share
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Notes subsets II  need to dedup 
TIme  O(N * 2^N)
Space O(2^N)
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums:
            return results 
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results 
    
    def dfs(self,  nums, index, combination, results):
        results.append(list(combination))
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]: continue 
            combination.append(nums[i])  
            self.dfs(nums, i + 1, combination, results)
            combination.pop()  
        