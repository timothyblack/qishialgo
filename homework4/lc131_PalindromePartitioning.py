"""
131. Palindrome Partitioning
Medium 
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        if not s:
            return result 
        self.dfs(s, [], result)
        return result 
    
    def dfs(self, s, stringlist, result):
        if len(s) == 0:
            result.append(stringlist[:])
            
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.ispalindrome(prefix):
                stringlist.append(prefix) 
                self.dfs(s[i:], stringlist, result)
                stringlist.pop() 
        
           
            
    def ispalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True
            
        