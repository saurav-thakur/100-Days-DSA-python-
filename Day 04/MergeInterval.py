# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        ans = []
        
        for interval in intervals:
            if ans and ans[-1][1] >= interval[0]:
                ans[-1][1] = max(ans[-1][1],interval[1])
                
            else:
                ans.append(interval)
                
        return ans