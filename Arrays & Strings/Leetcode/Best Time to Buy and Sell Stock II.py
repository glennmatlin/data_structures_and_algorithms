#%%
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
# =============================================================================
# find maximum possible profit from a given set of stock prices
# 
# one transaction per day buy/sell
# must sell before buy \ must buy before sell
# list min/max & index
# 
# 
# int pointer for first number in list
# bool pointer for owns stock
# int pointer for current profits
# [7,1,5,3,6,4]
# =============================================================================

#%%
"""
Created on Sat Oct  3 14:53:01 2020
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stockProfit,stockOwned,stockPrice=0,False,None
        idx=0
        while idx < len(prices):
            if stockOwned is False:
                    if prices[idx+1] > prices[idx]: #buy (price improves)
                        stockOwned,stockPrice=True, prices[idx]
                        idx += 1
                    else: #dont buy (price declines)
                        idx += 1
                
            else: # stockOwned is True
                    if prices[idx+1] > prices[idx]: #keep (price improving)
                        idx += 1 
                    else: #sell (price declining)
                        stockProfit += prices[idx]-stockPrice
                        stockOwned = False
                        idx += 1 
            return(stockProfit)