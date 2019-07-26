class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        res = [0] * (num + 1) 
        for i in range(1, num + 1):
            res[i] = res[i >> 1] + (i & 1) 
        return res
