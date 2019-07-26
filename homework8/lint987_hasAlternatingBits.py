"""
987. Binary Number with Alternating Bits
 
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example
Example 1:

Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:

Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:

Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:

Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
"""
class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """
    def hasAlternatingBits(self, n):
        a = (n ^ (n >> 1))
        return (a &(a + 1)) == 0  
