"""
406. Minimum Size Subarray Sum
中文English
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.

Example
Example 1:

Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: [1, 2, 3, 4, 5], s = 100
Output: -1
Challenge
If you have figured out the O(nlog n) solution, try coding another solution of which the time complexity is O(n).


"""

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        if not nums or len(nums) == 0: return -1
        N = len(nums)
        l, r = 0, 0
        csum = 0
        res = float('inf')
        while r < N:
            csum += nums[r]
            while csum >= s:
                res = min(res, r - l + 1)
                csum -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else -1

# Python 3.x
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        if nums is None or len(nums) == 0:
            return -1

        n = len(nums)
        minLength = n + 1
        sum = 0
        j = 0
        for i in range(n):
            while j < n and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                minLength = min(minLength, j - i)

            sum -= nums[i]
            
        if minLength == n + 1:
            return -1
            
        return minLength