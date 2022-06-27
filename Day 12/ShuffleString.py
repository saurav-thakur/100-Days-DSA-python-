# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        new_st = [0 for i in range(len(s))]
        
        for i in range(len(s)):
            new_st[indices[i]] = s[i]
            
        return "".join(new_st)