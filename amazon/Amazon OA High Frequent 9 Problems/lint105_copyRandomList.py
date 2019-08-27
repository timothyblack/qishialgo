"""
https://www.jiuzhang.com/solution/copy-list-with-random-pointer/#tag-highlight-lang-python 
105. Copy List with Random Pointer

Description 
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Have you met this question in a real interview?  
Challenge
Could you solve it with O(1) space?
"""

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
             return head
        
        node_map = {}
        new_head = RandomListNode(head.label) 
        node_map[head] = new_head 
        p = head 
        q = new_head 
        
        while p != None:
            q.random = p.random 
            if p.next != None:
                q.next = RandomListNode(p.next.label) 
                node_map[p.next] = q.next 
            else:
                q.next = None 
            p = p.next 
            q = q.next 
        
        p = new_head 
        while p != None:
            if p.random != None:
                p.random = node_map[p.random] 
            p = p.next 
        return new_head