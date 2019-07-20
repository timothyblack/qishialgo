"""
https://www.lintcode.com/problem/evaluate-division/description
1257. Evaluate Division
中文English
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, 
vector<double>& values, 
vector<pair<string, string>> queries , 
where equations.size() == values.size(), and the values are positive. 
This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

construct adj list from equations  
for query   ["a", "c"] - >  a/b * b/c  
construct map records key = (a, b) : value, (a, b) : 1/ value       
BFS queue start with (start=query[0], val=1.0)  for each adj node of start  new val = val * reords[(start, adj node)]  
check if adj node is the end.   
"""
class Solution:
    """
    @param equations: 
    @param values: 
    @param queries: 
    @return: return a double type array
    """
    def calcEquation(self, equations, values, queries):
        adj_list, records = self.get_adj_records(equations, values)
        ans = []
        for start, end in queries:  
            # [a, e]  -> a/e = a /b * b/c * c/d * d/e 
            if start == end and start in adj_list: # a / a = 1.0 
                ans.append(1.0)
                continue 
            
            queue, res, visited = collections.deque(), -1.0, set()  
            queue.append((start, 1.0))    #  start with 1.0  because product will be calced 
            while queue and res == -1:  
                cur_node, cur_val = queue.popleft() 
                visited.add(cur_node)   
                print("cur node {} cur val {}".format(cur_node, cur_val))
                for adj_node in adj_list[cur_node]:
                    if adj_node in visited: continue   
                    
                    new_val = cur_val * records[(cur_node, adj_node)]
                    print("cur node {} adj_node {} rec value {} new val {}".format(cur_node, adj_node, records[(cur_node, adj_node)], new_val)) 
                    if adj_node == end: 
                        res = new_val 
                        break
                    queue.append((adj_node, new_val))
            ans.append(res)
        return ans
    
    #   equationas [["a","b"],["b","c"]]  values [2.0,3.0]   a/b = 2.0 
    def get_adj_records(self, equations, values):
        adj_list, records = collections.defaultdict(set), collections.defaultdict(float)
        for i in range(len(equations)):  
            u, v = equations[i][0], equations[i][1]
            adj_list[u].add(v)
            adj_list[v].add(u)
            records[(u, v)] = values[i]           #  add both a/b = 2.0 and b/a = 0.5 
            records[(v, u)] = 1 / values[i]  
            
        return adj_list, records 