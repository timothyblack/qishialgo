"""
216. Combination Sum III
Medium

597

30

Favorite

Share
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]


"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []        
        self.dfs(k, n, 0, 0, 0, [], results)  
        
        return results 
    
    def dfs(self, k, n, index, cnt, csum, combination, results):
        if cnt > k or csum > n:
            return 
        if cnt == k and csum == n: 
            print(cnt, csum)
            results.append(list(combination))
            return 
        
        for i in range(index + 1, 10):             
            self.dfs(k, n, i, cnt + 1, csum + i, combination + [i], results)
			
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        ans = []
        def search(start, cnt, sums, nums):
            if cnt > k or sums > n:
                return
            if cnt == k and sums == n:
                ans.append(nums)
                return
            for x in range(start + 1, 10):
                search(x, cnt + 1, sums + x, nums + [x])
        search(0, 0, 0, [])
        return ans
        