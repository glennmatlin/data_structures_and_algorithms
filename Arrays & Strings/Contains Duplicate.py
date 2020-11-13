# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/

Created on Sun Oct  4 20:15:44 2020

@author: Glenn
"""
#%%
# Imports
from typing import List
#%%
# version using set
# O(1) space and time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
#%%
# version by using a dictionary
# O(n) space and time
class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        dict_ = dict()
        for n in nums:
            if n in dict_:
                return True
            else:
                dict_[n] = True
        return False
#%%
# version with pointers?
# O(n^2) time O(1) space
class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] in nums[i+1:]:
                return True
        return False        
#%%
# Testing
solution=Solution()
assert solution.containsDuplicate([1,2,3,1]) == True
assert solution.containsDuplicate([1,2,3,4]) == False
assert solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True