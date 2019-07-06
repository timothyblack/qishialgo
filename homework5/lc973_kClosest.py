"""
https://leetcode.com/problems/k-closest-points-to-origin/
973. K Closest Points to Origin
Medium 
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
 
Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000


Analysis  
 point is list  
 use max heap --  add sign to coords because heapq is min heap  
 dist = (a.x - b.x) ** 2 + (a.y - b.y) ** 2 
 Time complexity O(nlogK)   n = number of points  
 Space O(n) 
"""
import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.heap = []  
        origin = [0, 0]
        heapq.heapify(self.heap)
        for point in points:
            dist = (point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2 
            heapq.heappush(self.heap, (-dist, -point[0], -point[1]))
            
            if len(self.heap) > K:
                heapq.heappop(self.heap)
                
        ret = []
        while len(self.heap) > 0:
            dist, x, y = heapq.heappop(self.heap)  
            ret.append([-x, -y])
        
        ret.reverse() 
        return ret 


    