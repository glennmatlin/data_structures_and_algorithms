# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:45:00 2020

@author: Glenn
"""
class Solution:
    def isPalindrome(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] == t[~i]:
                continue
            else:
                return False
        return True