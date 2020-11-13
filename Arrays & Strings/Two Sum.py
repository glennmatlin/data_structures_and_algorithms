# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/interview/card/uber/289/array-and-string/1682/


Created on Mon Oct  5 16:17:38 2020

@author: Glenn
"""

# =============================================================================
# nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# Example 2:
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# Example 3:
# 
# Input: nums = [3,3], target = 6
# =============================================================================
#%%
# brute force time O(n^2) space O(1)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return None
#%%
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {value:index for index, value in enumerate(nums)}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in values and i != values[diff]:
                return ([i,values[diff]])
#%%
solution=Solution()
assert solution.twoSum([3,3],6) == [0,1]
assert solution.twoSum([3,2,4],6) == [1,2]
assert solution.twoSum([2,7,11,15],22) == [1,3]