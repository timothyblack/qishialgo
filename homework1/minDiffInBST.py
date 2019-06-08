
# LC 783. Minimum Distance Between BST Nodes
# Notes:
# inorder iterative
# data struture queue  +  pre to save prev node val
# TIme O(n)
# SPace O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        mindiff = sys.maxsize
        # inorder
        queue = []
        pre = None
        while queue or root:
            if root:
                queue.append(root)
                root = root.left
            else:
                node = queue.pop()
                if pre:
                    mindiff = min(mindiff, node.val - pre)
                pre = node.val
                root = node.right
        return mindiff