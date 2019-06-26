"""
47. Permutations II
Medium

1029

44

Favorite

Share
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 0:
            return [[]]
        results = []
        visited = [False] * len(nums) 
        nums.sort()     #  dont forget to sort    [3,3,0,3] 
        self.dfs(nums, [],  results, visited)  
        return results 
    
    def dfs(self, nums, templist,  results, visited):
        if len(nums) == len(templist):
            results.append(list(templist))
            
        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]): 
                continue 
            visited[i] = True
            self.dfs(nums, templist + [nums[i]], results, visited)
            visited[i] = False