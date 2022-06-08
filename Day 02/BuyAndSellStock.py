# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprofit = 0
        minnum = prices[0]
        
        for i in range(len(prices)):
            minnum = min(prices[i],minnum)
            profit = prices[i] - minnum
            maxprofit = max(profit,maxprofit)
            
        return maxprofit
            