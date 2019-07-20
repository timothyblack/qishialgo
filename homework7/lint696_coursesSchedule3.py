"""
https://www.lintcode.com/problem/course-schedule-iii/description
696. Course Schedule III
中文English
There are ·n· different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example
Example 1

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation:
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the `101st` day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2

Input: [[100,50]]
Output: 0
Notice
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.
"""
import heapq 
class Solution:
    """
    @param courses: duration and close day of each course
    @return: the maximal number of courses that can be taken
    """
    """
    this is not top sort  
    max heap + greedy    
    为了能够修完最多的课程，贪心的策略如下：
    1. 首先处理课程结束时间最早的课程，因此我们需要对课程按照截止时间进行排序。
    2. 当 修完该课程的时间 > 当前课程的截至时间时，我们应该在已选课程从剔除掉一门占用时长最久的课程。
    因此我们需要使用一个 maxHeap 帮助我们维持这个信息。
    最后队列中有几门课程（持续时间），就说明了我们最多能够修完多少门课程。
    
    时间复杂度：O(nlogn)
    """
    def scheduleCourse(self, courses):
        if not courses or len(courses) == 0: return 0 
        courses.sort(key=lambda x: x[1])
        cur_time = 0 
        heap = [] 
        for duration, deadline in courses:
            cur_time += duration 
            heapq.heappush(heap, -duration)    # map heap keep the max duration   
            if cur_time > deadline:
                 # take the course that takes the longest and emove from schedule
                cur_time -= -heapq.heappop(heap)     
        return len(heap)