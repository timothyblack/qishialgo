"""
https://leetcode.com/problems/find-bottom-left-tree-value/
513. Find Bottom Left Tree Value
Medium

575

98

Favorite

Share
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note  level order traveral to the last level. first node  

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return None
        result = None
        q = deque([root])
        while q:
            
            size = len(q)
            
            for i in range(size):
                
                node = q.popleft()
                if i == 0: result = node.val 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
       
        return result 
            
    # NRL order,  last node val     
    def findBottomLeftValue(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return None
        result = None
        q = deque([root])
        while q:
            
            size = len(q)
            
            for i in range(size):
                
                node = q.popleft()
                result = node.val 
              
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
       
        return result 
                    
