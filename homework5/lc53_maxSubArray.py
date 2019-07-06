"""
https://leetcode.com/problems/maximum-subarray/
53. Maximum Subarray
Easy

4507

159

Favorite

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
# TIme O(n)
#space O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -sys.maxsize
        cur_sum = 0 
        for num in nums:
            # same as cur_sum = 0 if cur_sum  < 0 
            cur_sum = max(cur_sum + num, num) 
            res = max(res, cur_sum)
        return res

# divide and conqur  
# TIme O(nlogn)
#space O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      
        return self.helper(nums, 0, len(nums) - 1)
        
    
    def helper(self, nums, left, right):
        if left > right:
            return -sys.maxsize 
        
        mid = left + (right - left) // 2
        left_max = self.helper(nums, left, mid -1)
        right_max = self.helper(nums, mid + 1, right)
        
        cur_sum = 0 
        left_sum_max = 0
        
        for i in range(mid - 1, left - 1, -1):
            cur_sum += nums[i] 
            left_sum_max = max(left_sum_max, cur_sum)
            
        cur_sum = 0 
        right_sum_max = 0 
        for i in range(mid+1, right+1):
            cur_sum += nums[i]
            right_sum_max = max(right_sum_max, cur_sum) 
        return max(left_max, max(right_max, left_sum_max + right_sum_max + nums[mid])) 