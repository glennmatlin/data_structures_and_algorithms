# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/

Created on Sat Oct  3 18:55:42 2020

@author: Glenn
"""
#%%
# =============================================================================
# Solution using a Counter collection
# =============================================================================
from collections import Counter
class MySolution:
    def firstUniqChar(s: str) -> int:
        c = Counter(s)
        singles = [s.index(e[0]) for e in c.items() if e[1]==1]
        if singles:
            return min(singles)
        else:
            return -1
#%%
# =============================================================================
# Solution using a Counter collection
# =============================================================================
from collections import Counter
class MySolution:
    def firstUniqChar(s: str) -> int:
        c = Counter(s)
        singles = [s.index(e[0]) for e in c.items() if e[1]==1]
        if singles:
            return min(singles)
        else:
            return -1
#%%
test="nglenn"
print(MySolution.firstUniqChar(s=test))