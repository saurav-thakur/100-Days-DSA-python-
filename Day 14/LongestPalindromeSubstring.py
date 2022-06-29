# https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1
# https://leetcode.com/problems/longest-palindromic-substring/
# https://www.youtube.com/watch?v=XYQecbcd6_c

class Solution:
        
    def longestPalin(self, S):
        # code here
        
        res = ""
        resLen = 0
        S_length = len(S)
        
        for i in range(len(S)):
            #for odd length
            l,r = i,i
            while l>=0 and r < S_length and S[l] == S[r]:
                if (r-l+1) > resLen:
                    res_l = l
                    res_r = r
                    resLen = (r-l+1)
                
                l-=1
                r+=1
            res = S[res_l:res_r+1]
            
            # for even length
            l,r = i,i+1
            while l>=0 and r < S_length and S[l] == S[r]:
                if (r-l+1) > resLen:
                    res_l = l
                    res_r = r
                    resLen = (r-l+1)
                    
                l-=1
                r+=1
            res = S[res_l:res_r+1]
        return res