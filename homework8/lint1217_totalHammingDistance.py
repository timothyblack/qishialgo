class Solution:
    """
    @param nums: the gievn integers
    @return: the total Hamming distance between all pairs of the given numbers
    """
    def totalHammingDistance(self, nums):
        total, n = 0, len(nums)
        for j in range(32):
            bit_count = 0 
            for i in range(n):
                bit_count += (nums[i] >> j) & 1 
            total += bit_count * (n - bit_count)
        return total 