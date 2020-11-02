# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

Created on Sun Oct  4 17:47:17 2020

@author: Glenn
"""
#%%
# Solution using built-in functions
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.find(needle)
#%% Solution using list slicing
class Solution:
    def strStr(self, haystack: str, needle:str) -> int:
        H, N = len(haystack), len(needle)
        
        # O((H-N)H) time complexity
        # O(1) space complexity
        
        for i in range(H-N+1):
            if haystack[i:i+N] == needle:
                return i
        return -1

#%%
# Solution without .find()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                print('hay: ', i, haystack[i])
                for j in range(len(needle)):
                    print('pin: ', j, needle[j])
                    if haystack[i] == needle[j]:
                        continue
                    else:
                        break
                    return int(i)
#%%
# Sandbox
solution = Solution()
print(solution.strStr("hello","ll"))
# solution.strStr("aaaaa","bba") == -1
#%%
# Testing
assert solution.strStr("hello","ll") == 2
assert solution.strStr("aaaaa","bba") == -1