"""
https://www.lintcode.com/problem/cheapest-flights-within-k-stops/description
1029. Cheapest Flights Within K Stops 
There are n cities connected by some flights. Each flight (u, v, w) starts from city u and arrives at v with a price w.

Given n, flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with at most K stops.

If there is no such route, return -1.

Example
Example 1:

Input: 
  n = 3,
  flights = [[0,1,100],[1,2,100],[0,2,500]],
  src = 0, dst = 2, K = 0
Output: 500
Example 2:

Input: 
  n = 3,
  flights = [[0,1,100],[1,2,100],[0,2,500]],
  src = 0, dst = 2, K = 1
Output: 200
Notice
The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be [src, dst, price].
The price of each flight will be in the range [1, 10000].
K is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.  

BFS  

"""

class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)  
        for u, v, e in flights: 
            graph[u][v] = e 
        ans = float('inf')
        queue = collections.deque()
        queue.append((src, 0))
        step = 0 
        while queue:
            size = len(queue) 
            for i in range(size):
                cur, cost = queue.popleft() 
                if cur == dst: 
                    ans = min(ans, cost) 
                for v, w in graph[cur].items():
                    if cost + w > ans:
                        continue
                    queue.append((v, cost + w))
            if step > K: break 
            step += 1 
        return -1 if ans == float('inf') else ans
                    
"""
min heap
"""
import heapq
class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(list)    
        # u - src,  v dest w price 
        for u, v, w in flights: 
            graph[u].append((v, w))
        min_heap = [(0, src, K + 1)]    #  this is upper case K 
  
        while min_heap:
            result, u, k = heapq.heappop(min_heap) 
            if u  == dst:
                return result 
            if k > 0:  
                for v, w in graph[u]:
                    # pushing (new cost, new start(v), k-1
                    heapq.heappush(min_heap, (result + w, v, k - 1))
                    
           
        return -1 
                    
