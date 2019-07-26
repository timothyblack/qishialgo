"""
1333. Reverse Bits
中文English
Reverse bits of a given 32 bits unsigned integer.

Example
Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: 
The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596
so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: 
The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293
so return 3221225471 which its binary representation is 10101111110010110010011101101001.

Initialize res with 0, and then repeatedly to move the last digit
of original number to the end of res
https://www.jiuzhang.com/solution/reverse-bits/#tag-highlight-lang-python
"""
class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverseBits(self, n):
        m = 32
        res = 0 
        while m > 0:
            res = (res << 1) 
            res += n & 1 
            n = n >> 1 
            m -= 1 
        return res

