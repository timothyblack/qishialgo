"""
etcode Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

https://stackoverflow.com/questions/26568560/difference-between-subarray-subset-subsequence
subsequence contain elements whose subscripts are increasing in the original sequence.

"""


# dp
# O(N2)
# space O(n)
def lengthLIS(nums):
    if not nums:
        return 0
    n = len(nums)
    # minimum 1 for length
    res = [1] * n
    for i in range(1, n):
        #
        for j in range(i):
            if nums[i] > nums[j]:
                res[i] = max(res[i], res[j] + 1)
    return max(res)

# binary search
# Time O(n * logn)
# space O(n)
def lengthLIS2(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = []

    for i in range(n):
        left, right = 0, len(dp) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if dp[mid] > nums[i]:
                right = mid - 1
            else:
                left = mid + 1

        if left >= len(dp):
            dp.append(nums[i])
        else:
            dp[left] = nums[i]
    return len(dp)

if __name__ == "__main__":
    print(lengthLIS([10, 9, 2, 5, 3, 7, 101, 18]))  #11
    print(lengthLIS2([10, 9, 2, 5, 3, 7, 101, 18]))  # 11




