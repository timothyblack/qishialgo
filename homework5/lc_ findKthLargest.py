"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
215. Kth Largest Element in an Array
Medium  
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Analysis 
Quick sort 
O(n)  
O(1)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k > len(nums): 
            return None 
        
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)
    
    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k]
        
        left, right = start, end
        pivot = nums[(start + end) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot: 
                left += 1
            while left <= right and nums[right] > pivot: 
                right -= 1 
            if left <= right: 
                nums[left], nums[right] = nums[right], nums[left] 
                left += 1 
                right -= 1 
        if k <= right: 
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k) 
        
        return nums[k]