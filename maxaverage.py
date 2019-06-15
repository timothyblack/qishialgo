"""
https://www.lintcode.com/problem/maximum-average-subarray/description
868. Maximum Average Subarray
中文English
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. You need to output the maximum average value.

Example
Example1

Input:  nums = [1,12,-5,-6,50,3] and k = 4
Output: 12.75
Explanation:
Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Example2

Input:  nums = [4,2,1,3,3] and k = 2
Output: 3.00
Explanation:
Maximum average is (3+3)/2 = 6/2 = 3.00
Notice
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000]


"""
# Time O(n)
# space O(1)
class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    Notes
    sliding window
first calc k sum, then add nums[i] - nums[i -k]
updating max sum
return the max avf
    """
    def findMaxAverage(self, nums, k):
        # 　calc first k sum
        if not nums or len(nums) < k or k < 1:
            return -1
        rollsum = 0
        maxsum = -2 ** 31 + 1
        for i in range(k):
            rollsum += nums[i]

        for i in range(k, len(nums)):
            rollsum += (nums[i] - nums[i - k])
            maxsum = max(maxsum, rollsum)
        return maxsum / k

    # cumulative sum  no good
    def  findMaxAverage2(self, nums, k):
        rollsums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            rollsums[i + 1] = rollsums[i] + nums[i]

        i = 0
        maxsum = -2**31 + 1
        while i + k < len(nums):
            maxsum = max(maxsum, (rollsums[i + k] - rollsums[i]) / (1.0 * k))
            i += 1
        return maxsum


    """
    https://blog.csdn.net/magicbean2/article/details/79142613
    https://www.cnblogs.com/grandyang/p/8021421.html
    617. Maximum Average Subarray II
    Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.

    It's guaranteed that the size of the array is greater or equal to k.
    
    Have you met this question in a real interview?  
    Example
    Example 1:
    
    Input:
    [1,12,-5,-6,50,3]
    3
    Output:
    15.667
    Explanation:
     (-6 + 50 + 3) / 3 = 15.667
    Example 2:
    
    Input:
    [5]
    1
    Output:
    5.000
    """
    # brute force
    # O(n2)
    #  sum of k, and calculate avg of k
    # for k + 1 to len(nums), add new num,  if  res * (i + 1) (pre avg * count + 1)  < new rolling sum,  means get a new max avg
    # from 0, to i -k,  remove nums[j] from the sum.   find max avg in these subarray.

    def findMaxAverageII(self, nums, k):
        # 　calc first k sum
        if not nums or len(nums) < k or k < 1:
            return -1
        presum = 0
        for i in range(k):
            presum += nums[i]
        rollsum = presum
        res = presum / k
        tt = 0
        tc1 = 0

        for i in range(k, len(nums)):
            tc1 += 1
            tc2 = 0
            presum += nums[i]
            rollsum = presum
            if rollsum > res * (i + 1):
                res = rollsum / (i + 1)
                print("sss" + str(res))
            for j in range(i - k + 1):
                tc2 += 1
                rollsum -= nums[j]
                if rollsum > res * (i - j):
                    res = rollsum / (i - j)
            tt += tc1 * tc2
            print(tc1, tc2, tt)
        return res

    # 1e5 = 100000
    # binary search  https://www.jiuzhang.com/solution/maximum-average-subarray-ii/
    def maxAverageII2(self, nums, k):
        if not nums:
            return 0

        start, end = min(nums), max(nums)
        while end - start > 0.00001:
            mid = start + (end - start) // 2
            if self.islarger(nums, k, mid):
                start = mid
            else:
                end = mid
        return start

    def islarger(self, nums, k, average):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)

        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])
        return False

#https://www.lintcode.com/problem/maximum-average-subarray-ii/description
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        if not nums:
            return 0
        if len(nums) < k:
            return 0

        start, end = min(nums), max(nums)
        while end - start > 0.00001:
            #   note   use /  to get decimals  dont use //
            mid = start + (end - start) / 2
            # print(mid)
            min_sum = cum_sum = pre_sum = 0
            check = False
            for i in range(len(nums)):
                cum_sum += nums[i] - mid
                if i >= k:
                    pre_sum += nums[i - k] - mid
                    min_sum = min(min_sum, pre_sum)

                if i >= k - 1 and cum_sum > min_sum:
                    check = True
                    break
            if check:
                start = mid
            else:
                end = mid
                # rounding is needed to pass
        return round(start, 3)


if __name__ == "__main__":
    #print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
    #print(Solution().findMaxAverageII([1,12,-5,-6,50,3], 3))
    print(Solution().findMaxAverageII([1,12,-5,-6,50,3], 3))
    # print(Solution().findMaxAverageII([5], 1))
    print(Solution().maxAverageII2([1, 12, -5, -6, 50, 3], 3))