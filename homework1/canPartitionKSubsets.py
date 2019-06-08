"""
698. Partition to K Equal Sum Subsets
Medium
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""
# Time O(n**(N-k) * k!)
# SPace O(n)
class Solution:
    def canPartitionKSubsets(self, nums, k):
        if not nums or len(nums) < k: return False
        _sum = sum(nums)
        # must be divisible by k
        if _sum % k != 0: return False
        target = _sum / k
        #print(target)
        nums.sort(reverse=True)
        #print(nums)
        if nums[0] > target: return False
        visited = [False] * len(nums)
        return self.dfs(nums, k, target, 0, 0, visited)

    def dfs(self, nums, k, target, index, cursum, visited):
        if k == 1: return True
        if cursum == target:
            return self.dfs(nums, k - 1, target, 0, 0, visited)
        for i in range(index, len(nums)):
            if visited[i]: continue
            visited[i] = True
            if self.dfs(nums, k, target, i + 1, cursum + nums[i], visited): return True
            visited[i] = False
        return False 

if __name__ == "__main__":
    print(Solution().canPartitionKSubsets([], 4))
    print(Solution().canPartitionKSubsets([4, 3], 4))
    print(Solution().canPartitionKSubsets([4,3,2,3,5,2,1], 4))
    print(Solution().canPartitionKSubsets([4, 3, 2, 6, 3, 5, 2, 1], 4))