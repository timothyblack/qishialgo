"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
4. Median of Two Sorted Arrays
Hard

4522

635

Favorite

Share
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
   
        # O(N) solution to merge 2 sorted list  
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i]) 
                i += 1 
            else:
                res.append(nums2[j]) 
                j += 1  
            
        while i < len(nums1):
            res.append(nums1[i]) 
            i += 1 
        
        while j < len(nums2):
            res.append(nums2[j]) 
            j += 1 
        
        n = len(res)
        if n % 2 == 0:
            return (res[(n -1) //2] + res[n // 2]) / 2
        else:
            return res[n // 2]  


# divide and conqur 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
   
         # O(NlogN)  
        n = len(nums1) + len(nums2) 
        if n % 2 == 1:
            return self.findKth(nums1, 0, nums2, 0, n // 2 + 1) 
        else:
            smaller = self.findKth(nums1, 0, nums2, 0, n //2) 
            bigger = self.findKth(nums1, 0, nums2, 0, n //2 + 1) 
            return (smaller + bigger) / 2
        
        
    def findKth(self, nums1, index_a, nums2, index_b, k):
        if len(nums1) == index_a:
            return nums2[index_b + k - 1] 
        if len(nums2) == index_b:
            return nums1[index_a + k - 1] 
        
        if k == 1:
            return min(nums1[index_a], nums2[index_b]) 
        a = nums1[index_a + k // 2 - 1] if index_a + k // 2 <= len(nums1) else None 
        b = nums2[index_b + k // 2 - 1] if index_b + k // 2 <= len(nums2) else None 
        
        if b is None or (a is not None and a < b):
            return self.findKth(nums1, index_a + k // 2, nums2, index_b, k - k // 2)
        return self.findKth(nums1, index_a, nums2, index_b + k // 2, k - k // 2)       