# Note that   Manacher's Algorithm can do O(N) 
#TIme O(N^2)
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s: return ""
        
        longest = ""
        for mid in range(len(s)):
            substr = self.find_palindrome(s, mid, mid)
            if len(substr) > len(longest): 
                longest = substr  
            substr = self.find_palindrome(s, mid, mid + 1)
            if len(substr) > len(longest):
                longest = substr
        return longest
    
    def find_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]: 
            left -= 1 
            right += 1 
        print(left, right)  
        return s[left + 1: right]   # note the while loop
# DP 
# TIme O(N^2)	
	
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s: return ""
        
        n = len(s) 
        is_pali = [[False] * n for i in range(n)]  
        
        for i in range(n): 
            is_pali[i][i] = True 
        for i in range(1, n):
            is_pali[i][i - 1] = True 
        
        longest, start, end = 1, 0, 0 
        for length in range(1, n):
            for i in range(n - length):
                j = i + length 
                is_pali[i][j] = s[i] == s[j] and is_pali[i + 1][j - 1] 
                if is_pali[i][j] and length + 1 > longest: 
                    longest = length + 1 
                    start, end = i, j 
        return s[start:end + 1]