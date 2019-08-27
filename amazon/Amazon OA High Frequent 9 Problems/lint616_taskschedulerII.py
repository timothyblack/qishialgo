"""
https://www.lintcode.com/problem/course-schedule-ii/description
Course Schedule II
Description
中文
English
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Have you met this question in a real interview?  
Example
Example 1:

Input: n = 2, prerequisites = [[1,0]] 
Output: [0,1]
Example 2:

Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
Output: [0,1,2,3] or [0,2,1,3]


Analysis  Top Sort 
"""
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        edges = {i: [] for i in range(numCourses)} 
        degrees = [0 for i in range(numCourses)]
        # prerequisites  [0, 1] 1 is prerequisite
        for i, j in prerequisites: 
            edges[j].append(i) 
            degrees[i] += 1  
        from collections import deque  
        queue = deque()
        
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i) 
                
        order = []
        while queue: 
            node = queue.popleft() 
            order.append(node) 
            for x in edges[node]: 
                degrees[x] -= 1 
                if degrees[x] == 0:
                    queue.append(x) 
        
        if len(order) == numCourses:
            return order 
        return []
"""
题目不难，拓扑排序题目，广度优先搜索完成。主要步骤为：

（1）计算它们的入度，然后把入度为 0 的，顶点依次输出。

（2）从（1）中输出的顶点，要删去从该顶点出发的所有边。

（3）重复（1）（2），直到剩余顶点的没有前驱顶点，或者没有剩余顶点。

（4）在整个过程中，可以依次把入度为 0 的顶点，放到一个队列里面，然后出队入队实现整个过程。
--------------------- 
作者：GorillaNotes 
来源：CSDN 
原文：https://blog.csdn.net/XX_123_1_RJ/article/details/84845711 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
class Solution:
    def findOrder(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for x, y in prerequisites:  # 转换成邻接表的形式
            graph[y].append(x)
            indegree[x] += 1  # 计算每个顶点的入度

        q = []  # 开辟队列，用队列实现bfs

        for i in range(numCourses):  # 初始化队列，把入读为 0 的顶点入队
            if not indegree[i]:
                q.append(i)

        res = []
        while q:  # 队列不为空，bfs, 一层一层地搜索输出
            v = q.pop()  # 出队
            res.append(v)
            for w in graph[v]:  # 广度搜索
                indegree[w] -= 1  # 入度减一
                if not indegree[w]:  # 判断此时 入度是否为0，如果为0，则入队
                    q.append(w)

        return [] if len(res) < numCourses else res  # 判断res 的长度，是否小于顶点数,然后返回结果


if __name__ == '__main__':
    numCourses, prerequisites = 2, [[1, 0]]
    print(Solution().findOrder(numCourses, prerequisites)) 