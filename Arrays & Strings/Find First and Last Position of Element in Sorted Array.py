# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/interview/card/uber/289/array-and-string/1683/

Created on Mon Oct  5 17:02:17 2020

@author: Glenn
"""

# =============================================================================
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# =============================================================================

# =============================================================================
# start at front of list
# move throughg list until encountering number equal to target
# find next number that is not target
# return indexes
# 
# =============================================================================
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        for start,num in enumerate(nums):
            if num == target:
                for stop in range(start+1,len(nums)):
                    if num != nums[stop]:
                        return [start, stop]
        return [-1,-1]
#%%
solution = Solution()
assert(solution.searchRange([],0)) == [-1,-1]
print(solution.searchRange([1,1],1)) == [0,1]