# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:24:15 2020

@author: Glenn

https://www.udemy.com/course/python-for-data-structures-algorithms-and-interviews/learn/lecture/4152026#overview

https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
"""

# =============================================================================
# Example:
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# =============================================================================

#%%
class ListNode():
    def __init__(self, value=0, label='', link=None):
        self.value = value
        self.label = label
        self.link = link
#%%
# Iterative brute solution would be to
# look at node, save value in node
# continue to linked node, and repeat by adding new values to front
# reconstruct node list


# a(1)->b(2)->c(3)->d(4)->e(5)->None
# e(5)->d4->c3->b2->a1->None


# get the order of the linked list
# reverse the order of the data
# modify the link method to next in reversed list
#%%
# =============================================================================
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         reversedNodes = []
#         while head.link != None:
#             reversedNodes.insert(0, head)
#             head = head.link
# 
#         for n in reversedNodes:
#             print(n.label,':',n.value)
#         # [e,d,c,b,a]
#         for i in range(len(reversedNodes)-1):
#             currNode = reversedNodes[i]
#             nextNode = reversedNodes[i+1]
#             currNode.link = nextNode
# =============================================================================
#%%
class Solution:
    def reverseListIteratively(self, head:ListNode)->ListNode:
        currentNode = head
        previousNode = None
        nextNode = None
        
        while currentNode:
            nextNode = currentNode.link #store fast pointer location
            currentNode.link = previousNode #modify node property
            previousNode = currentNode #store current pointer location
            currentNode = nextNode
        return previousNode
    
    def reverseListPythonically(self, head:ListNode)->ListNode:
        prev, cur = None, head
        while cur:
            cur.link, cur, prev = prev, cur.link, cur
        return prev

    def reverseListRecursively(self, head:ListNode)->ListNode:
        
#%%
a = ListNode(1,'a')
b = ListNode(2,'b')
c = ListNode(3,'c')
d = ListNode(4,'d')
e = ListNode(5,'e')

a.link = b
b.link = c
c.link = d
d.link = e
#%%
print(a.label, b.label, c.label, d.label, e.label)
print(a.value, b.value, c.value, d.value, e.value)

print(a.label, b.label, c.label, d.label, e.label)
print(a.link.value, b.link.value, c.link.value, d.link.value)
#%%
solution = Solution()
s = solution.reverseList(a)