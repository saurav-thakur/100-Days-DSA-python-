# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        
        for i in accounts:
            count = 0
            for j in i:
                count += j
            ans = max(count,ans)
            
        return ans