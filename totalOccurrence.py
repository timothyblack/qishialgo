"""
"""
class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        # array is sorted
        # find first pos and last pos of the target,  lastpos - first + 1
        # [1,1,1,1,1,1,1,1,1,1,1]  1
        if not A:
            return 0
        if target > A[-1] or target < A[0]:
            return 0

        start, end = 0, len(A) - 1
        # first pos
        # dont use None
        firstpos = -1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # print(mid)
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            firstpos = start
        elif A[end] == target:
            firstpos = end
       # print("fff" + str(firstpos))
        lastpos = -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid

        if A[end] == target:
            lastpos = end
        elif A[start] == target:
            lastpos = start
        #print(lastpos)
        if lastpos >= 0 and firstpos >= 0:
            return lastpos - firstpos + 1
        elif firstpos >= 0 or lastpos >= 0:
            return 1
        else:
            return 0

if __name__ == "__main__":

    A, t = [1, 3, 3, 4, 5], 3
    print(Solution().totalOccurrence(A, t))