"""
https://www.jiuzhang.com/solution/rectangle-overlap/
https://www.lintcode.com/problem/rectangle-overlap/description?_from=ladder&&fromId=11
626. Rectangle Overlap 
Given two rectangles, find if the given two rectangles overlap or not.

l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.

l1 != r1 and l2 != r2

Have you met this question in a real interview?  
Example
Example 1:

Input : l1 = [0, 8], r1 = [8, 0], l2 = [6, 6], r2 = [10, 0]
Output : true
Example 2:

Input : l1 = [0, 8], r1 = [8, 0], l2 = [9, 6], r2 = [10, 0]
Output : false
"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):
        if l1.x > r2.x or l2.x > r1.x: 
            return False
        if l1.y < r2.y or l2.y < r1.y: 
            return False 
        return True 
