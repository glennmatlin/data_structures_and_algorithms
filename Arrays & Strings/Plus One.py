# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

Created on Sun Oct  4 20:50:10 2020

@author: Glenn
"""

# =============================================================================
# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# 
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# =============================================================================

#%%
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for d in digits:
            num = num+str(d)
        num = int(num)+1
        out = []
        for n in str(num):
            out.append(int(n))
        return out
#%%        
solution = Solution()
assert solution.plusOne([1,2,3]) == [1,2,4]
assert solution.plusOne([4,3,2,1]) == [4,3,2,2]
assert solution.plusOne([0]) == [1]
