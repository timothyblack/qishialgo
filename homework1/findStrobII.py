"""
https://www.lintcode.com/problem/strobogrammatic-number-ii/description
Strobogrammatic Number II
中文English
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.

Example
Example 1:

Input: n = 2,
Output: ["11","69","88","96"]
Example 2:

Input: n = 1,
Output: ["0","1","8"]
input n = 4
["1001","1111","1691","1881","1961","6009","6119","6699","6889","6969","8008","8118","8698","8888","8968","9006","9116","9696","9886","9966"]
"""
# Time  O(N)
# Space O(5N)
class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """

    def __init__(self):
        self.odd_nums = ["0", "1", "8"]
        self.even_nums = ['11', '69', '88', '96', '00']

    def findStrobogrammatic(self, n):
        result = []
        if n <= 0: return [""]
        if n == 1:
            return self.odd_nums
        if n == 2:
            return self.even_nums[:-1]
        # odd number
        if n % 2:
            pre, midnums = self.findStrobogrammatic(n - 1), self.odd_nums
        else:
            pre, midnums = self.findStrobogrammatic(n - 2), self.even_nums

        premid = (n - 1) // 2
        print(premid)
        for p in pre:
            for m in midnums:
                result.append(p[:premid] + m + p[premid:])
        return result
