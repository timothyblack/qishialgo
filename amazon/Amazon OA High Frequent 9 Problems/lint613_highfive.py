"""
https://www.lintcode.com/problem/high-five/description

13. High Five
There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.

Have you met this question in a real interview?  
Example
Example 1:

Input: 
[[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
Output:
1: 72.40
2: 97.40

Example 2:

Input:
[[1,90],[1,90],[1,90],[1,90],[1,90],[1,90]]
Output: 
1: 90.00


analysis min heap for each id,  and pop when len > 5   

"""
'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq 
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        id_to_scores = {}
        for rec in results:
            if rec.id not in id_to_scores:
                id_to_scores[rec.id] = [rec.score] 
            else:
                heapq.heappush(id_to_scores[rec.id], rec.score)
                if len(id_to_scores[rec.id]) > 5: 
                    heapq.heappop(id_to_scores[rec.id]) 
        
        ret = {}
        for id, scores in id_to_scores.items():
            ret[id] = sum(id_to_scores[id]) / len(id_to_scores[id])  
        return ret
                
                