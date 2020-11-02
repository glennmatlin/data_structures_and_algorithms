# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:37:30 2020

@author: Glenn
"""
#%%
#v1 using Counter
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs, cd = Counter(s), Counter(t)
        if cs == cd:
            return True
        else:
            return False
        
#%%
#v2 without using Counter
class Solution:
    def letterCounter(self, word: str) -> dict:
        letterCount = {}
        for letter in word:
            if letter in letterCount:
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1
        return letterCount
    def isAnagram(self, s: str, t: str) -> bool:
        cs, cd = self.letterCounter(s), self.letterCounter(t)
        if cs == cd:
            return True
        else:
            return False
