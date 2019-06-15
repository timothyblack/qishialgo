"""
 https://leetcode.com/problems/powx-n/description/

题目描述：
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
1
2
Example 2:

Input: 2.10000, 3
Output: 9.26100
1
2
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
1
2
3
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82960833
版权声明：本文为博主原创文章，转载请附上博文链接！

"""
# xn = xn/2 * xn/2 * xn%2
# O(logn)
#O(1)
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1

        if n % 2:
            #  self.myPow(x * x, n/2 )
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n / 2)

    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


    # O(1)
    # O(1)
    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            if n % 2:
                ans *= x
            n >>= 1   #  N = N // 2
            x *= x
        return ans

"""
---------------------
作者：负雪明烛
来源：CSDN
原文：https: // blog.csdn.net / fuxuemingzhu / article / details / 82960833
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
if __name__ == "__main__":

    x, n = 5, 1
    print(Solution().myPow(x, n))
    x, n = 2.1, 3
    print(Solution().myPow2(x, n))