# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/

Created on Sun Oct  4 20:31:09 2020

@author: Glenn
"""

# =============================================================================
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
# 
# Follow up: Could you implement a solution with a linear runtime complexity
# and without using extra memory?
#
# Constraints:
#     1 <= nums.length <= 3 * 104
#     -3 * 104 <= nums[i] <= 3 * 104
#     Each element in the array appears twice except for one element which appears only once.
# =============================================================================
#%%
# Imports
from typing import List
#%%
# Hash map solution
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts=Counter(nums).items()
        return [n[0] for n in counts if n[1]==1].pop()
#%%
# Sort and check with pointer
# O(n) complexity with no space used
class Solution:
    def singleNumber(self, nums:List[int]) -> int:
        nums.sort()
        # print('nums: ', nums)
        for i in range(0,len(nums),2):
            try:
                if nums[i] != nums[i+1]:
                    # print('ret:', nums[i])
                    return nums[i]
            except:
                return nums[i]
#%%
# Sandbox
solution = Solution()
# solution.singleNumber([2,2,1]) == 1
solution.singleNumber([4,1,2,1,2]) == 4
# solution.singleNumber([1]) == 1
#%%
# Testing
solution = Solution()
assert solution.singleNumber([2,2,1]) == 1
assert solution.singleNumber([4,1,2,1,2]) == 4
assert solution.singleNumber([1]) == 1
