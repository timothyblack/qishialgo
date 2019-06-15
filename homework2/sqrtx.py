"""
https://leetcode.com/problems/sqrtx/
69. Sqrt(x)
Easy

768

1371

Favorite

Share
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

Note
time O(logn)
space O(1)
right boundary    < x/2 + 1
use  sq = x/ mid  intead of mid * mid to avoid overflow
"""

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x == 0 or x == 1:
            return x
        # sqrt x  < x/2 + 1
        left, right = 1, x // 2 + 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            print(mid)
            if mid * mid <= x:
                left = mid
            else:
                right = mid - 1
        print("left" + str(left))
        print("right" + str(right))
        if right * right <= x:
            return right

        return left


    def sqrt2(self, x):
        if x == 0 or x == 1:
            return x
        # sqrt x  < x/2 + 1
        left, right = 1, x // 2 + 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            print(mid)
            sq = x // mid
            print(sq)
            # mid * mid <= x   answer in range[mid, right]
            if sq >= mid:
                left = mid
            else:
                right = mid - 1
        print("left" + str(left))
        print("right" + str(right))
        if right * right <= x:
            return right
        return left
if __name__ == "__main__":
    import math
    assert Solution().sqrt(100) == 10
    assert Solution().sqrt(34343333) == int(math.sqrt(34343333))
