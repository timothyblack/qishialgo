"""
https://www.lintcode.com/problem/window-sum/description?_from=ladder&&fromId=11
https://www.jiuzhang.com/solution/window-sum/#tag-highlight-lang-python
604. Window Sum 
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Have you met this question in a real interview?  
Example
Example 1

Input：array = [1,2,7,8,5], k = 3
Output：[10,17,20]
Explanation：
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
"""
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if not nums or len(nums) < k or k <= 0: 
            return []
        n = len(nums)
       
        # open array of n -k + 1 size 
        win_sum = [0] * (n - k + 1)  
        print( "win sum length" + str(n -k + 1))   
        # calc win_sum[0]  
        for i in range(k):
            win_sum[0] += nums[i]
            
        for i in range(1, n - k + 1):
            print(i + k - 1)
            win_sum[i] = win_sum[i-1] - nums[i-1] + nums[i + k - 1] 
        return win_sum
