"""
https://www.lintcode.com/problem/k-closest-points/description
612. K Closest Points 
Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are same in the x-axis, sorted by y-axis.

Have you met this question in a real interview?  
Example
Example 1:

Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3 
Output: [[1,1],[2,5],[4,4]]
Example 2:

Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
Output: [[0,0]]
Related Problems
"""


# max heap  --  turn all number to -  (distance, x, y)
# get distance --  a**2 + b**2  
# pop heap when more than k in heap.   
# convert x, y back by adding - 
# get familar with heapq

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq 
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        self.heap = [] 
        heapq.heapify(self.heap)  
        
        for point in points:  
            dist = self.get_distance(point, origin) 
            heapq.heappush(self.heap, (-dist, -point.x, -point.y))  
            
            if len(self.heap) > k:
                heapq.heappop(self.heap)
    
        ret = []
        while len(self.heap) > 0:
            dist, x, y = heapq.heappop(self.heap)
            ret.append(Point(-x, -y))
            
        ret.reverse()
        return ret
    
    
    
    def get_distance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2  


"""
devide and conqur
https://leetcode.com/articles/k-closest-points-to-origin/
http://massivealgorithms.blogspot.com/2019/01/leetcode-973-k-closest-points-to-origin.html
"""