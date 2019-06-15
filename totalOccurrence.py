"""
https://www.lintcode.com/problem/total-occurrence-of-target/description
462. Total Occurrence of Target
中文English
Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

Example
Example1:

Input: [1, 3, 3, 4, 5] and target = 3,
Output: 2.
Example2:

Input: [2, 2, 3, 4, 6] and target = 4,
Output: 1.
Example3:

Input: [1, 2, 3, 4, 5] and target = 6,
Output: 0.
Challenge
Time complexity in O(logn)

1, find the first position: if mid<target: start = mid
2. find the last position: if mid<=target: start = mid
3. innitialize  pos to -1
相似题:
find the first position
find the last position
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
    assert(Solution().totalOccurrence(A, t)==2), "wrong"
    A, t = [2, 2, 3, 4, 6], 4
    assert(Solution().totalOccurrence(A, t)==1), "wrong"
    A, t = [1, 2, 3, 4, 5], 6
    assert(Solution().totalOccurrence(A, t)==0), "wrong"
    A, t = [1,1,1,1,1,1,1,1,1,1,1], 1
    assert(Solution().totalOccurrence(A, t)==11), "wrong"