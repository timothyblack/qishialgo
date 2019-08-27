"""
https://www.jiuzhang.com/solution/minimum-spanning-tree/#tag-other-lang-python
Kruskal's algorithm  

The core idea of prim's MST algorithm is that as long as we have not spanned all vertices(cities), we keep picking the cheapest edge e = (u, v), u is in X and v is NOT in X.

We can use a union find data structure to simulate this process. If we pick an edge(connection), we would have the following 2 cases.

a. city1 and city2 are already connected: this means this edge does not satisfy the condition that city1 is in X and city2 is NOT in X, this connection should be ignored.

b. city1 and city2 are not connected: this means this edge satisfies the above condition, if it is the cheapst edge out of all those edges that meets the condition, we should

select this connection and add it to the final result.

Based on the above analysis, we have the following algorithm.

sort the connections to make sure smaller cost connections are in front. (Prim MST greedy)

create a mapping between city names and union find index as it is best to use integer as union find's index.

use numbers from 0 to n - 1 for all cities assuming there are n different cities.

As we are creating the mapping, the next available integer index also represents the total number of cities whose mapping are created so far. After all the mapping is done,

this idx variable tells us the total number of nodes(cities). This is important in checking if there is any city that is disconnected with all other cities. 

Based on connected graph theory, if all n cities are connected, there we would include n - 1 different edges that do not introduce any cycle, thus generating the MST.

However, if there is a part of the graph that are disconnected from the rest, then it means we must only included fewer than n - 1 different connections, otherwise all cities 

would be connected. 
Iterate all connections, add to the final result each connection whose ends are not connected in the uf and connect both ends' mapping in the uf.

Check if there are n - 1 connections in the final result. If there aren't return an empty list to indicate there are disconnected cities in the given connections.

Runtime/Space complexity: O(m * logm + 2 * m + n) ~ O(m * logm) runtime; O(n) space

Assuming there are n different cities and m different edges,

sorting: O(m * log m) runtime, O(1) space assuming in place quick sort is used.

mapping: O(m) runtime, O(n) space.

unionfind creation: O(n) runtime, O(n) space.

connections iteration: O(m) runtime, as both the uf find and connect operations take O(1) time on average.

"""
'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        if connections is None or len(connections) == 0:
            return []
        
        connections.sort(key=lambda x: (x.cost, x.city1, x.city2)) 
        self.initialize(connections)
        
        results = []
        for connection in connections: 
            city1 = connection.city1 
            city2 = connection.city2 
            if self.union(city1, city2):
                results.append(connection)  
            
        if self.count != len(self.father) - 1:
            return [] 
        return results 
            
    def initialize(self, connections):
        self.father = {}
        self.count = 0 
        for connection in connections: 
            city1 = connection.city1 
            city2 = connection.city2 
            if city1 not in self.father: 
                self.father[city1] = city1 
            if city2 not in self.father: 
                self.father[city2] = city2 
        print(self.father)
        print(self.count)
    def union(self, city1, city2): 
        root_1 = self.find(city1)
        root_2 = self.find(city2)
        if root_1 != root_2: 
            self.father[root_1] = root_2 
            self.count += 1
            return True 
        return False
    
    def find(self, city):
        path = []
        while self.father[city] != city:
            path.append(city)
            city = self.father[city]
        for p in path:
            self.father[p] = city 
        return city 
        