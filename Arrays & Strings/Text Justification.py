# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:47:18 2020

@author: Glenn
"""
from typing import List

#%%
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        newgroup = []
        while len(' '.join(newgroup)) < maxWidth:
            for element in words:
                if (len(newgroup) + len(element)) < maxWidth:
                    newgroup.append(element)
                    words.remove(element)
                else:
                    print(newgroup)
                    output.append(newgroup)
                    break
            print(newgroup)
        return newgroup
#%%
maxWidth = 16
words = ["This ", "is ", "an ", "example"]
solution = Solution()

solution.fullJustify(words, maxWidth)