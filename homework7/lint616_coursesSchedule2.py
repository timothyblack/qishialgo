"""
https://www.lintcode.com/problem/course-schedule-ii/description
616. Course Schedule II 
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example
Example 1:

Input: n = 2, prerequisites = [[1,0]] 
Output: [0,1]
Example 2:

Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
Output: [0,1,2,3] or [0,2,1,3]


"""
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        indegrees = [0 for i in range(numCourses)]   # initialize degree to 0 
        edges = {i: [] for i in range(numCourses)}  
        
        for crs, pre in prerequisites: 
            edges[pre].append(crs)  
            indegrees[crs] += 1  
        
        print(indegrees)
        print(edges)
        queue = collections.deque([i for i in range(numCourses) if indegrees[i] == 0])  
        order = [] 
        while queue:
            node = queue.popleft()  
            print("q item {}".format(node))
            order.append(node)  
            for crs in edges[node]:
                indegrees[crs] -= 1 
                if indegrees[crs] == 0:
                    queue.append(crs)  
        
        if len(order) == numCourses: 
            return order
        else:
            return []