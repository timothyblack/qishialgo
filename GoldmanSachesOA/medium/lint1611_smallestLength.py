"""
https://www.lintcode.com/problem/shortest-subarray/description
Time O(N^2)   brute force  

"""
class Solution:
    """
    @param nums: 
    @param k: 
    @return: return the length of shortest subarray
    """
    def smallestLength(self, nums, k):
        start, presum = 0, 0 
        minlen = sys.maxsize 
        for i in range(len(nums)):
            presum += nums[i] 
            
            while presum >= k:
                print(i, start,  i - start + 1)
                minlen = min(minlen, i - start + 1)
                presum -= nums[start] 
                start += 1 
        
        return -1 if minlen == sys.maxsize else minlen

"""		
	# https://www.cnblogs.com/grandyang/p/4501934.html	
	这道题给定了我们一个数字，让我们求子数组之和大于等于给定值的最小长度，注意这里是大于等于，不是等于。跟之前那道 Maximum Subarray 有些类似，并且题目中要求我们实现 O(n) 和 O(nlgn) 两种解法，那么我们先来看 O(n) 的解法，我们需要定义两个指针 left 和 right，分别记录子数组的左右的边界位置，然后我们让 right 向右移，直到子数组和大于等于给定值或者 right 达到数组末尾，此时我们更新最短距离，并且将 left 像右移一位，然后再 sum 中减去移去的值，然后重复上面的步骤，直到 right 到达末尾，且 left 到达临界位置，即要么到达边界，要么再往右移动，和就会小于给定值。代码如下：

 
"""
class Solution:
    """
    @param nums: 
    @param k: 
    @return: return the length of shortest subarray
    """
    def smallestLength(self, nums, k):
       
        left, right = 0, 0
        presum = 0
        n = len(nums)
        minlen = n + 1  
        
        while right < n: 
            while presum < k and right < n: 
                presum += nums[right] 
                right += 1 
            
            while presum >= k:
                
                minlen = min(minlen, right - left)
                presum -= nums[left]
                left += 1 
        return -1 if minlen == n + 1 else minlen
        """
        start, presum = 0, 0 
        minlen = sys.maxsize  
        for i in range(len(nums)):
            presum += nums[i] 
            
            while presum >= k:
                print(i, start,  i - start + 1)
                minlen = min(minlen, i - start + 1)
                presum -= nums[start] 
                start += 1 
        
        return -1 if minlen == sys.maxsize else minlen
        """