"""
https://www.jiuzhang.com/solution/maximum-subtree/#tag-highlight-lang-python
https://www.lintcode.com/problem/maximum-subtree/description?_from=ladder&&fromId=11
628. Maximum Subtree
Description
中文
English
Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum sum and the given binary tree is not an empty tree.

Have you met this question in a real interview?  
Example
Example 1:

Input:
{1,-5,2,0,3,-4,-5}
Output:3
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5
The sum of subtree 3 (only one node) is the maximum. So we return 3.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
#  define class var max_sum to track maxsum  
#  define class var result to track root of the max substree,  to return 
#  helper to check left, right tree and   left_sum + right_sum + root.val   
class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    max_sum = 0 
    result = None
    def findSubtree(self, root):
        self.helper(root)
        return self.result 
    
    def helper(self, root):
        if root is None:
            return 0 
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)  
        
        if left_sum + right_sum + root.val >= self.max_sum or self.result is None:
            self.max_sum = left_sum + right_sum + root.val 
            self.result = root 
        
        return left_sum + right_sum + root.val 
    