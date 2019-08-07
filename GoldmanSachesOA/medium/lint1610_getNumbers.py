"""
https://www.jiuzhang.com/solution/find-the-numbers/#tag-highlight-lang-python


"""
class Solution:
    """
    @param n: the integer
    @return: the numbers that larger and smaller than `n` 
    """
    def getNumbers(self, n):
        if n < 0: 
            return []
        if n == 0: 
            return [1] 
        a, b = 0, 1   #  a= f(i-2)   b= f(i-1)
        fib = 0    # fib = f(i) 
        while fib < n: 
            fib = a + b 
            a, b = b, fib    
        
        if fib == n:
            return [a, a + fib] #  a now is b  
        else: 
            return [a, fib]   # fib > n now ,   a = b  
