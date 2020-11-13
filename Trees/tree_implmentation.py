# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:32:38 2020

@author: Glenn
"""

class BinaryTree(object):
    def __init__(self, rootObj):
        self.rootObj = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else: # when child exists, node is inserted and existing is push down
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.righChild == None:
            self.righChild = BinaryTree(newNode)
        else: # when child exists, node is inserted and existing is push down
            t = BinaryTree(newNode)
            t.righChild = self.righChild
            self.righChild = t

    def setRootObj:
        return 
    def getLeftChild:
        return self.leftChild
    def getRightChild:
        return self.rightChild