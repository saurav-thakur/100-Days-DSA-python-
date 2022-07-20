# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        
        def reverse(s,i,j):
            if i >= j:
                return
            s[i],s[j] = s[j],s[i]
            
            reverse(s,i+1,j-1)
            
        i = 0
        j = len(s) - 1
        reverse(s,i,j)  