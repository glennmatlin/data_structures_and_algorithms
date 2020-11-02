# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
Created on Sun Oct  4 15:31:03 2020

@author: Glenn
"""
#%%
test_strs = ["flower","flow","flight",
             "funny", "fubar",
             "foo", "bar"] 
#%%
# =============================================================================
# count characters for str[0] in strs
# 'f' == 6
# 'b' == 1
# 
# fn to count most common letter in group
# 
# count characters for str[1] in strs (f)
# (f)'l' == 3
# (f)'u' == 2
# (f)'o' == 1
# 
# (fl)'o'==2
# (fl)'i'==1
# 
# (flo)'w'==1
# (flo)'w'
# 
# =============================================================================


lcp = ''
for i in range(200):
    p = set()
    try:
        for s in strs:
            p.add(s[i])
        if len(p)==1:
            lcp += p.pop()
        else:
            break
    except IndexError():
        break
return lcp
#%%
# Test Parameters
('strs', 'output'),
[
 (["flower",
   "flow",
   "flight"], "fl"),
 (["dog","racecar","car"], "")
 ]
#%%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        for i in range(200):
            p = set()
            try:
                for s in strs:
                    p.add(s[i])
                if len(p)==1:
                    lcp += p.pop()
                else:
                    break
            except:
                break
        return lcp