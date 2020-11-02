# -*- coding: utf-8 -*-
"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/880/

Created on Sat Oct  3 17:42:08 2020

@author: Glenn
"""
# =============================================================================
# Examples
# Input: x = 123
# Output: 321
# 
# Input: x = -123
# Output: -321
# 
# Input: x = 120
# Output: 21
# 
# Input: x = 0
# Output: 0
# =============================================================================
#%%
class MySolution:
    def reverse(x: int) -> int:
        #exception handling
        if x==0:
            return x
        #make a string
        s=str(x)
        #store negative symbol
        isNegative=False
        if s[0]=='-':
            isNegative=True
            s=s[1:]
        #reverse string
        s=s[::-1]
        #remove leading zeroes
        idx=0
        for i in range(len(s)):
            if s[i]!='0':
                idx=i
                break                
        s=s[idx:]
        #return negative
        if isNegative:
            s='-'+s
        n=int(s)
        if n < -2**31 or n > 2**31:
            return 0
        return int(n)
#%%
class ForumSolution:
    def reverse(self, x):
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r * (r < 2**31)

#%%
import pytest

@pytest.mark.parametrize("x, x_", [(123,321),(321,123),(-123,-321),(120,12),(0,0),(1534236469,0)])
def test_reverse(x, x_):
    assert Solution.reverse(x)==x_