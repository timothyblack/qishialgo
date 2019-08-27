"""
https://yeqiuquan.blogspot.com/2017/03/lintcode-627-longest-palindrome.html
[LintCode] 627 Longest Palindrome 解题报告
Description
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Notice
Assume the length of given string will not exceed 1010.


Example
Given s = "abccccdd" return 7

One longest palindrome that can be built is "dccaccd", whose length is 7.


思路
这题其实就是找有多少个数出现过2次。
我们维护一个count，并且开一个Set。
遍历所有字符c，如果c没有出现过，那么我们加到Set里。
如果c出现过，我们从Set里把它去掉，并且count += 2。
最后判断是不是还有单个的数。如果没有，那么count就是结果。反之，count要+1。

"""

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        """
        # data structure hashmap
        # count even number of chs,  
        # add 1 only if there are odd number of chs
        if not s or len(s) == 0: return 0
        odd = set()
        res = 0 
        for ch in s: 
            # found a pair 
            if ch in odd: 
                odd.remove(ch) 
                res += 2 
            else:
                odd.add(ch)  
        
        return res + 1 if len(odd) > 0 else res  
        """
        if not s or len(s) == 0: return 0
		
"""
https://www.cnblogs.com/grandyang/p/5931874.html
思路：
這一題如果只要回文長度的話，可以發現回文的組成仰賴於重複的字母，也就是說只要有一組重複的字母就可以構成回文裡面的2個數，比如說我們有 abbcdfghj ，那其中的 bb 就可以在裡面夠成 b_b，我們拆解這個題目就可以發現，我們只要統計每一個字母出現的次數，如果是偶數，比如說4次，那就代表這個字母可以構成4個回文中的字母，回文長度就 +4 ，如果是奇數，那也沒關係，那就代表偶數+1個，而這多出的一個就可以變成放在回文正中間的代表。
再近一步拆解，我們其實也不需要紀錄實際的偶數數量，我們只要紀錄無法成對的字母數量，然後再用原本的字串長度，剪掉這些(字母數量-1)，-1是因為可以留一個在中央。

作者：aammyytt
链接：https://www.jianshu.com/p/7da9943227f0
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
https://www.jiuzhang.com/solution/longest-palindrome/#tag-highlight-lang-python
"""
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        """
        # data structure hashmap
        # count even number of chs,  
        # add 1 only if there are odd number of chs
        if not s or len(s) == 0: return 0
        odd = set()
        res = 0 
        for ch in s: 
            # found a pair 
            if ch in odd: 
                odd.remove(ch) 
                res += 2 
            else:
                odd.add(ch)  
        
        return res + 1 if len(odd) > 0 else res  
        """
        if not s or len(s) == 0: return 0
        
        odd = set()
        for ch in s:
            if ch in odd:
                odd.remove(ch)
            else:
                odd.add(ch)
        
        remove = len(odd)
        # if any odd number can add 1 to res  for aba case 
        if remove > 0:
            remove -= 1 
        
        return len(s) - remove 