class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        
        if num < 1: return False 
        if (num & (num - 1)) != 0: return False 
        while num > 1:
            num = num >> 2  
        if num == 1: return True 
        return False 