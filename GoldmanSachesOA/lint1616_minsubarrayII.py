"""
https://www.lintcode.com/problem/shortest-subarray-ii/description
1616. Shortest subarray II
中文English
Given an array of integers and a positive integer K , find the length of a smallest contiguous subarray such that the sum of this subarray is ≥ K ,return the length of subarray. if there are no subarrays that match the condition,return -1.

Example
Example 1:

Input： nums = [2,-1,2], k = 3
Output：3
Explanation：2+(-1)+2 = 3
Example 2:

Input：nums = [2,-1,2,-1,4,2], k = 5
Output：2
Explanation：4+2=6
Notice
1.1 <= nuns.length <= 50000
2.-10 ^ 5 <= nums[i] <= 10 ^ 5
3.1 <= K <= 10 ^ 9

https://www.jiuzhang.com/solution/shortest-subarray-ii/#tag-highlight-lang-python
考点：

前缀和
队列
题解：如果队列首的位置至当前位置的连续子数组和>=k时，选择最小结果。如果当前位置前缀和小于等于队列尾部位置的前缀和，删除尾部。


"""
class Solution:
    """
    @param nums: 
    @param k: 
    @return: return the length of subarray
    """
    def smallestLengthII(self, nums, k):
       
        N = len(nums)
        B = [0] * (N + 1)
        for i in range(N): B[i + 1] = B[i] + nums[i]  #构造前缀和
        d = collections.deque()
        res = N + 1
        for i in xrange(N + 1):
            while d and B[i] - B[d[0]] >= k: res = min(res, i - d.popleft()) #如果队列首至当前位置连续子数组和>=k，筛选最小答案
            while d and B[i] <= B[d[-1]]: d.pop()    #如果当前位置前缀和<=队列尾位置的前缀和
            d.append(i)
        return res if res <= N else -1
        