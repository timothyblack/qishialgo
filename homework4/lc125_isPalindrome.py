"""
125. Valid Palindrome
Easy   
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Notes  1. case insensitive and only digits and letters counts, 
2. empty string is valid palindrome
two pointer 
Time O(N)
Space O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1 
                continue
            if not s[right].isalnum():
                right -= 1 
                continue
            
            if s[left] != s[right]: return False 
            left += 1
            right -= 1 
        return True 
                