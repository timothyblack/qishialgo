"""
620. Maximum Subarray IV
中文English
Given an integer arrays, find a contiguous subarray which has the largest sum and length should be greater or equal to given length k.
Return the largest sum, return 0 if there are fewer than k elements in the array.

Example
Example 1:

Input:
[-2,2,-3,4,-1,2,1,-5,3]
5
Output:
5
Explanation:
[2,-3,4,-1,2,1]
sum=5
Example 2:

Input:
[5,-10,4]
2
Output:
-1
Notice
Ensure that the result is an integer type.
k > 0
"""

public class Solution {
    /**
     * @param nums: an array of integer
     * @param k: an integer
     * @return: the largest sum
     */
    public int maxSubarray4(int[] nums, int k) {
        int n = nums.length;
        if (n < k)
            return 0;

        int result = 0;
        for (int i = 0; i < k; ++i)
            result += nums[i];

        int[] sum = new int[n + 1];
        sum[0] = 0;
        
        int min_prefix = 0;
        for (int i = 1; i <= n; ++i) {
            sum[i] = sum[i - 1] + nums[i - 1];
            if (i >= k && sum[i] - min_prefix > result) {
                result = Math.max(result, sum[i] - min_prefix);
            }
            if (i >= k) {
                min_prefix = Math.min(min_prefix, sum[i - k + 1]);
            }
        }
        return result;
    }
}