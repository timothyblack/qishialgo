class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        s = 0 
        for x in A: 
            s ^= x 
        y = s & (-s) 
        
        ans = [0, 0]
        for x in A:
            if (x & y) != 0:
                ans[0] ^= x 
            else:
                ans[1] ^= x 
        return ans
