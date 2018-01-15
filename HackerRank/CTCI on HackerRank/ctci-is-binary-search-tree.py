# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

# Qualities of a Binary Tree
# The value of every node in a node's left subtree is less than the data value of that node.
# The value of every node in a node's right subtree is greater than the data value of that node.
# Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# Left-Middle-Right check

def checkBST(root):

