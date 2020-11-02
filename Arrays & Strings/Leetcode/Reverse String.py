# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/879/

Created on Sat Oct  3 17:16:52 2020

@author: Glenn
"""
#%%
# =============================================================================
# Python3 solution
# =============================================================================
class SolutionPython3:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
#%%
# =============================================================================
# Pythonic solution
# =============================================================================
class SolutionPythonic:
    def reverseString(self, s: List[str]) -> None:
        s=s[::-1]
#%%
# =============================================================================
# Classic Solution
# =============================================================================
class SolutionClassicPythonic(object):
    def reverseString(self, s:List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]
#%%
# =============================================================================
# LeetCode Solutions         
# =============================================================================
class SolutionLeetCodeRecursion:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
        
class SolutionLeetCode2Pointers:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1