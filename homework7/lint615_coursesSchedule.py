"""
https://www.lintcode.com/problem/course-schedule/description
615. Course Schedule
中文English
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example
Example 1:

Input: n = 2, prerequisites = [[1,0]] 
Output: true
Example 2:

Input: n = 2, prerequisites = [[1,0],[0,1]] 
Output: false


Top sort 
"""
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        degrees = [0 for i in range(numCourses)]  
        edges = {i: [] for i in range(numCourses)}  # dictionary prerequisite: [courses list]   

        for c, pre in prerequisites:
            edges[pre].append(c)  
            degrees[c] += 1     # this is indegrees    
    
        queue, count = collections.deque([]), 0 
        
        # find all courses with 0 indegrees 
        for i in range(numCourses): 
            if degrees[i] == 0:
                queue.append(i) 
        
        while queue:
            node = queue.popleft() 
            count += 1 
            for c in edges[node]:
                degrees[c] -= 1 
                if degrees[c] == 0: # decrease indegrees and add to q if indegrees is 0 
                    queue.append(c) 
        
        return count == numCourses   
            