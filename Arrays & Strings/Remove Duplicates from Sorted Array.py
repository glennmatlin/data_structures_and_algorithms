# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
#%%
"""
Created on Sat Oct  3 14:53:01 2020
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if bool(nums) is False:
            return(0)
        store = nums[0]
        idx = 1
        
        while idx < len(nums):
            if nums[idx] == store:
               nums.pop(idx)
            else:
                store = nums[idx]
                idx += 1
        return(len(nums))
#%%
"""
Forum Solution
"""
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ +=1
        return len_